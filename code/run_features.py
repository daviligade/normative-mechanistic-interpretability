"""Activations of the located SAE features on every pair."""
import argparse, json, os, sys, time, hashlib
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import FRAMES, answer_ids, encode, readouts, check_run_file
from run_heads import pick_device


class SAEWrap:
    def __init__(self, sae_dir=None, llama_scope=None, device="cpu"):
        from safetensors.torch import load_file
        if sae_dir:
            cfg = json.load(open(os.path.join(sae_dir, "cfg.json"))); sd = load_file(os.path.join(sae_dir, "sae_weights.safetensors"))
            assert cfg["architecture"] == "topk" and cfg.get("normalize_activations", "none") == "none", "unsupported sae_lens configuration"
            self.kind, self.k = "topk", int(cfg["k"]); self.rescale = bool(cfg.get("rescale_acts_by_decoder_norm", False)); self.b_dec_in = bool(cfg.get("apply_b_dec_to_input", True))
            self.W_enc, self.b_enc, self.W_dec, self.b_dec = (sd[k].float().to(device) for k in ("W_enc", "b_enc", "W_dec", "b_dec"))
            self.dn = self.W_dec.norm(dim=-1); self.hook_name = cfg.get("metadata", {}).get("hook_name")
        else:
            hp = json.load(open(os.path.join(llama_scope, "hyperparams.json"))); sd = load_file(os.path.join(llama_scope, "checkpoints", "final.safetensors"))
            s = hp["d_model"] ** 0.5 / hp["dataset_average_activation_norm"]["in"]
            self.kind = "jumprelu"; self.thr = hp["jump_relu_threshold"] * s; self.b_dec_in = bool(hp.get("apply_decoder_bias_to_pre_encoder", False)); self.rescale = False
            self.W_enc = (sd["encoder.weight"].float().T * s).contiguous().to(device); self.b_enc = sd["encoder.bias"].float().to(device)
            self.W_dec = (sd["decoder.weight"].float().T / s).contiguous().to(device); self.b_dec = (sd["decoder.bias"].float() / s).to(device)
            self.dn = self.W_dec.norm(dim=-1); self.hook_name = hp.get("hook_point_in")
        self.d_in, self.d_sae = self.W_enc.shape

    @torch.no_grad()
    def encode(self, x):
        x = x.float(); pre = (x - self.b_dec if self.b_dec_in else x) @ self.W_enc + self.b_enc
        if self.kind == "jumprelu": return pre * (pre > self.thr)
        if self.rescale: pre = pre * self.dn
        v, i = pre.topk(self.k, dim=-1); return torch.zeros_like(pre).scatter_(-1, i, torch.relu(v))

    @torch.no_grad()
    def contributions(self, f, idx):
        a = f[..., idx]
        if self.rescale: a = a / self.dn[idx]
        return a @ self.W_dec[idx]

    @torch.no_grad()
    def decode(self, f):
        a = f / self.dn if self.rescale else f
        return a @ self.W_dec + self.b_dec


class LM:
    def __init__(self, model_name, device, dtype, layer, site):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.tok = AutoTokenizer.from_pretrained(model_name); td = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[dtype]
        try: self.model = AutoModelForCausalLM.from_pretrained(model_name, dtype=td, low_cpu_mem_usage=True)
        except TypeError: self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=td, low_cpu_mem_usage=True)
        self.model.to(device).eval(); self.device = device
        blk = self.model.model.layers[layer]; self.module = blk if site == "resid_post" else blk.mlp
        self.A = {k: (torch.tensor(v, device=device) if isinstance(v, list) else v) for k, v in answer_ids(self.tok).items()}

    @torch.no_grad()
    def run(self, ids, final_override=None):
        B = 1 if final_override is None else final_override.shape[0]; grab = {}
        def hook(m, a, out):
            h = out[0] if isinstance(out, tuple) else out
            grab["h"] = h[0, -1].detach().float().clone()
            if final_override is not None: h[:, -1, :] = final_override.to(h.dtype)
            return out
        hd = self.module.register_forward_hook(hook)
        try:
            x = torch.tensor([ids] * B, device=self.device); hs = self.model.model(input_ids=x).last_hidden_state[:, -1, :]; lg = self.model.lm_head(hs)
        finally: hd.remove()
        return readouts(lg, self.A), grab["h"]


def selftest(args, lm, sae):
    ref = np.load(args.selftest); byname = {p["name"]: p for p in json.load(open(args.original_pairs))}; names = [str(x) for x in ref["names_moral"]]; n = min(args.selftest_n, len(names)); worst = 1.0
    for j in range(n):
        for side, key in (("permissive_prompt", "perm_moral"), ("restrictive_prompt", "rest_moral")):
            _, h = lm.run(encode(lm.tok, byname[names[j]][side], bos=not args.no_bos)); f = sae.encode(h).cpu().numpy(); r = ref[key][j].astype(np.float32)
            c = float(np.corrcoef(f, r)[0, 1]); worst = min(worst, c)
            print(f"  pair {j:2d} {side[:4]}  corr={c:.5f}  max|diff|={np.abs(f - r).max():.4f}  active mine/stored={int((f > 0).sum())}/{int((r > 0).sum())}  max stored={r.max():.2f}", flush=True)
    ok = worst > 0.99; print(f"SELFTEST {'PASSED' if ok else 'FAILED'}: lowest correlation with the stored features = {worst:.5f} (threshold 0.99)"); return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--sae-dir"); ap.add_argument("--llama-scope"); ap.add_argument("--layer", type=int, required=True)
    ap.add_argument("--site", default="resid_post", choices=["resid_post", "mlp_out"]); ap.add_argument("--items"); ap.add_argument("--out", default="runs/features"); ap.add_argument("--tag", required=True)
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32")
    ap.add_argument("--feature-sets", default=None, help="JSON {set_name: [feature ids]} (the located features) -> enables pass 2")
    ap.add_argument("--n-random", type=int, default=20); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--selftest"); ap.add_argument("--no-bos", action="store_true", help="self-test only: tokenize without the leading BOS-like token (how the stored Qwen features were tokenized)"); ap.add_argument("--original-pairs"); ap.add_argument("--selftest-n", type=int, default=6)
    a = ap.parse_args(); assert bool(a.sae_dir) != bool(a.llama_scope), "give exactly one of --sae-dir / --llama-scope"
    assert not (a.no_bos and not a.selftest), "--no-bos is for the self-test only; the study always uses the leading BOS-like token"
    if a.items and not a.selftest: check_run_file(a.items, hashlib.sha256(open(a.items, "rb").read()).hexdigest(), a.any_items)
    if a.feature_sets and not os.path.exists(a.feature_sets): sys.exit(f"[run_features] feature-set file not found: {a.feature_sets} (located/features.json)")
    dev = pick_device(a.device); print(f"[run_features] model={a.model} device={dev} dtype={a.dtype} site=L{a.layer}.{a.site}", flush=True)
    lm = LM(a.model, dev, a.dtype, a.layer, a.site); sae = SAEWrap(a.sae_dir, a.llama_scope, dev); print(f"[run_features] SAE {sae.kind} d_in={sae.d_in} d_sae={sae.d_sae} trained on {sae.hook_name}", flush=True)
    if a.selftest: sys.exit(0 if selftest(a, lm, sae) else 1)
    if a.feature_sets and not os.path.exists(a.feature_sets): sys.exit(f"[run_features] feature-set file not found: {a.feature_sets} (located/features.json)")
    raw = open(a.items, "rb").read(); items = json.loads(raw); sha = hashlib.sha256(raw).hexdigest(); items = items[:a.limit] if a.limit else items
    out = os.path.join(a.out, a.tag); os.makedirs(out, exist_ok=True); sides = ("perm", "rest"); RK = ("S", "LD", "mass", "S_hist", "LD_gb")
    json.dump({"model": a.model, "sae_dir": a.sae_dir, "llama_scope": a.llama_scope, "layer": a.layer, "site": a.site, "frames": a.frames, "items_sha256": sha, "dtype": a.dtype, "device": dev,
               "n_random": a.n_random, "seed": a.seed, "torch": torch.__version__, "started": time.strftime("%Y-%m-%d %H:%M:%S")}, open(os.path.join(out, "run_config.json"), "w"), indent=1)

    for fr in a.frames:
        path = os.path.join(out, f"extract__{fr}.npz")
        if os.path.exists(path):
            old_sha = str(np.load(path)["items_sha256"]) if "items_sha256" in np.load(path).files else None
            if old_sha != sha: sys.exit(f"[run_features] {path} was made from a different item file ({old_sha}); move it away or use another --out / --tag")
            if len(np.load(path)["ids"]) != len(items): sys.exit(f"[run_features] {path} holds {len(np.load(path)['ids'])} items, this call asks for {len(items)} (another --limit?); move it away or use another --out / --tag")
            print("[pass 1] exists:", path); continue
        R = {f"{s}_{k}": [] for s in sides for k in ("h", "xh", "f", "err2", "norm2") + tuple(f"clean_{r}" for r in RK) + tuple(f"splice_{r}" for r in RK)}; t0 = time.time()
        for n, it in enumerate(items):
            for s in sides:
                ids = encode(lm.tok, FRAMES[fr](it[f"{s}_stem"])); rc, h = lm.run(ids); f = sae.encode(h); xh = sae.decode(f); rs, _ = lm.run(ids, final_override=xh[None])
                R[f"{s}_h"].append(h.cpu().numpy()); R[f"{s}_xh"].append(xh.cpu().numpy()); R[f"{s}_f"].append(f.cpu().numpy().astype(np.float16)); R[f"{s}_err2"].append(float(((h - xh) ** 2).sum())); R[f"{s}_norm2"].append(float((h ** 2).sum()))
                for r in RK: R[f"{s}_clean_{r}"].append(float(rc[r][0])); R[f"{s}_splice_{r}"].append(float(rs[r][0]))
            if (n + 1) % 25 == 0: print(f"[pass 1] {fr} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
        np.savez_compressed(path + ".tmp.npz", items_sha256=np.array(sha), ids=np.array([it["id"] for it in items]), category=np.array([it["category"] for it in items]), subtype=np.array([it.get("subtype", "") for it in items]), **{k: np.array(v) for k, v in R.items()}); os.replace(path + ".tmp.npz", path)
    if not a.feature_sets: print("[run_features] no --feature-sets: pass 2 skipped"); return

    sets = {k: [int(i) for i in v] for k, v in json.load(open(a.feature_sets)).items() if len(v) > 0}
    ctrl = {}; rng = np.random.default_rng(a.seed)
    for fr in a.frames:
        e = np.load(os.path.join(out, f"extract__{fr}.npz")); act = np.concatenate([e[f"{s}_f"].astype(np.float32) for s in sides]).mean(0)
        order = np.argsort(act, kind="stable"); rank = np.empty_like(order); rank[order] = np.arange(len(order)); ctrl[fr] = {}
        for name, F in sets.items():
            inF = set(F); cs = []
            for r in range(a.n_random):
                used = set(inF); chosen = []
                for i in sorted(F, key=lambda j: -act[j]):
                    cand, step = [], 1
                    while len(cand) < 20 and (rank[i] - step >= 0 or rank[i] + step < len(order)):
                        for pos in (rank[i] + step, rank[i] - step):
                            if 0 <= pos < len(order) and int(order[pos]) not in used: cand.append(int(order[pos]))
                        step += 1
                    c = int(rng.choice(cand[:20])); chosen.append(c); used.add(c)
                cs.append(chosen)
            ctrl[fr][name] = cs
            ratio = float(np.mean([act[c].sum() for c in cs]) / max(act[F].sum(), 1e-12)); print(f"[pass 2] {fr} {name}: summed mean activation of the control sets / of the set = {ratio:.2f}", flush=True)
    json.dump({"sets": sets, "controls": ctrl}, open(os.path.join(out, "ablation_sets.json"), "w"))
    for fr in a.frames:
        path = os.path.join(out, f"ablate__{fr}.npz")
        if os.path.exists(path): print("[pass 2] exists:", path); continue
        R = {f"{s}_{name}_{r}": [] for s in sides for name in sets for r in RK}; R.update({f"{s}_{name}_removed_norm": [] for s in sides for name in sets}); t0 = time.time()
        for n, it in enumerate(items):
            for s in sides:
                ids = encode(lm.tok, FRAMES[fr](it[f"{s}_stem"])); _, h = lm.run(ids); f = sae.encode(h)
                for name, F in sets.items():
                    idxs = [F] + ctrl[fr][name]; rem = torch.stack([sae.contributions(f, torch.tensor(ix, device=f.device)) for ix in idxs]); ro, _ = lm.run(ids, final_override=h[None] - rem)
                    for r in RK: R[f"{s}_{name}_{r}"].append(ro[r].float().cpu().numpy())
                    R[f"{s}_{name}_removed_norm"].append(rem.norm(dim=-1).cpu().numpy())
            if (n + 1) % 25 == 0: print(f"[pass 2] {fr} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
        np.savez_compressed(path + ".tmp.npz", items_sha256=np.array(sha), ids=np.array([it["id"] for it in items]), **{k: np.array(v) for k, v in R.items()}); os.replace(path + ".tmp.npz", path)
    print("[run_features] finished", flush=True)


if __name__ == "__main__":
    main()
