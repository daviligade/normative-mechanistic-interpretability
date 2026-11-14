"""Head patching: the effect of every attention head on the score of every pair."""
import argparse, json, os, sys, time, hashlib, copy
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import FRAMES, answer_ids, encode, readouts, check_run_file, accepted_ids

HIST_DIRS = {"meta-llama/Llama-3.2-1B": "Llama-3.2-1B", "meta-llama/Llama-3.2-1B-Instruct": "Llama-3.2-1B-Instruct",
             "meta-llama/Llama-3.2-3B": "Llama-3.2-3B", "meta-llama/Llama-3.2-3B-Instruct": "Llama-3.2-3B-Instruct",
             "google/gemma-2b": "gemma-2b", "google/gemma-2b-it": "gemma-2b-it", "Qwen/Qwen2.5-3B": "Qwen2.5-3B",
             "Qwen/Qwen2.5-3B-Instruct": "Qwen2.5-3B-Instruct", "Qwen/Qwen2.5-7B": "Qwen2.5-7B", "Qwen/Qwen2.5-7B-Instruct": "Qwen2.5-7B-Instruct",
             "meta-llama/Llama-3.1-8B": "Llama-3.1-8B", "meta-llama/Llama-3.1-8B-Instruct": "Llama-3.1-8B-Instruct",
             "Qwen/Qwen2.5-14B": "Qwen2.5-14B", "Qwen/Qwen2.5-14B-Instruct": "Qwen2.5-14B-Instruct"}


def pick_device(name):
    if name != "auto": return name
    if torch.cuda.is_available(): return "cuda"
    if getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available(): return "mps"
    return "cpu"


class Patcher:
    def __init__(self, model_name, device, dtype, hist_name=None):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.tok = AutoTokenizer.from_pretrained(model_name)
        td = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[dtype]
        try: self.model = AutoModelForCausalLM.from_pretrained(model_name, dtype=td, low_cpu_mem_usage=True)
        except TypeError: self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=td, low_cpu_mem_usage=True)
        self.model.to(device).eval(); self.device = device
        cfg = self.model.config; self.L, self.H = cfg.num_hidden_layers, cfg.num_attention_heads
        self.hd = getattr(cfg, "head_dim", None) or cfg.hidden_size // cfg.num_attention_heads
        self.layers = self.model.model.layers
        assert self.layers[0].self_attn.o_proj.in_features == self.H * self.hd, "unexpected attention layout"
        self.A = answer_ids(self.tok)
        self.A = {k: (torch.tensor(v, device=device) if isinstance(v, list) else v) for k, v in self.A.items()}

    @torch.no_grad()
    def final_logits(self, x):
        h = self.model.model(input_ids=x).last_hidden_state[:, -1, :]
        return self.model.lm_head(h)

    @torch.no_grad()
    def clean(self, ids):
        cache, hooks = {}, []
        for l in range(self.L):
            hooks.append(self.layers[l].self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: cache.__setitem__(l, a[0].detach().clone())))
        x = torch.tensor([ids], device=self.device); lg = self.final_logits(x)
        for h in hooks: h.remove()
        return {k: float(v[0]) for k, v in readouts(lg, self.A).items()}, cache

    @torch.no_grad()
    def patch_all_heads(self, recv_ids, donor_cache, positions, batch, plen=0, only_first_batch=False):
        n = len(recv_ids); out = {k: np.zeros((self.L, self.H), dtype=np.float32) for k in ("S", "LD", "S_hist", "mass", "LD_gb")}
        heads = [(l, h) for l in range(self.L) for h in range(self.H)]; hd = self.hd
        base = self.model.model(input_ids=torch.tensor([recv_ids[:plen]], device=self.device), use_cache=True).past_key_values if plen > 0 else None
        for s in range(0, len(heads), batch):
            assign = heads[s:s + batch]; hooks = []
            for l in sorted({a[0] for a in assign}):
                d = donor_cache[l]; ml = min(n, d.shape[1])
                def pre(m, a, l=l, d=d, ml=ml):
                    z = a[0].clone()
                    for b, (ll, hh) in enumerate(assign):
                        if ll != l: continue
                        if positions == "all": z[b, :ml - plen, hh * hd:(hh + 1) * hd] = d[0, plen:ml, hh * hd:(hh + 1) * hd]
                        else: z[b, -1, hh * hd:(hh + 1) * hd] = d[0, -1, hh * hd:(hh + 1) * hd]
                    return (z,)
                hooks.append(self.layers[l].self_attn.o_proj.register_forward_pre_hook(pre))
            try:
                if base is None: lg = self.final_logits(torch.tensor([recv_ids] * len(assign), device=self.device))
                else:
                    c = copy.deepcopy(base); c.batch_repeat_interleave(len(assign)); x = torch.tensor([recv_ids[plen:]] * len(assign), device=self.device)
                    lg = self.model.lm_head(self.model.model(input_ids=x, past_key_values=c, use_cache=True).last_hidden_state[:, -1, :])
            finally:
                for h in hooks: h.remove()
            r = readouts(lg, self.A)
            for k in out:
                v = r[k].float().cpu().numpy()
                for b, (l, h) in enumerate(assign): out[k][l, h] = v[b]
            if only_first_batch: break
        return out


def prefix_len(pi, ri, positions, enabled):
    if not enabled or len(pi) != len(ri): return 0
    if positions == "final": return len(ri) - 1
    k = 0
    while k < len(pi) and pi[k] == ri[k]: k += 1
    return min(k, len(ri) - 1)


def run_pair(P, perm_text, rest_text, directions, positions, batch, only=None):
    pi, ri = encode(P.tok, perm_text), encode(P.tok, rest_text)
    bp, cp = P.clean(pi); br, cr = P.clean(ri)
    res = {"n_tok_perm": len(pi), "n_tok_rest": len(ri), "base_perm": bp, "base_rest": br, "effects": {}}
    if getattr(P, "use_prefix", None) is None:
        P.use_prefix = False; pl = prefix_len(pi, ri, "all", True)
        if pl > 0:
            try:
                worst = {"S": 0.0, "LD": 0.0}
                for pos in ("all", "final"):
                    x0 = P.patch_all_heads(ri, cp, pos, batch, 0, True); x1 = P.patch_all_heads(ri, cp, pos, batch, prefix_len(pi, ri, pos, True), True)
                    for k in worst: worst[k] = max(worst[k], float(np.abs(x0[k] - x1[k]).max()))
                P.use_prefix = worst["S"] < 1e-4 and worst["LD"] < 1e-3
                print(f"[run_heads] prefix cache check (all and final positions): max|dS| = {worst['S']:.2e}, max|dLD| = {worst['LD']:.2e} -> {'ON' if P.use_prefix else 'OFF'}", flush=True)
            except Exception as e: print(f"[run_heads] prefix cache not usable with this transformers version ({type(e).__name__}: {e}) -> OFF", flush=True)
        else: P.use_prefix = None
    for d in directions:
        recv, donor, base = (ri, cp, br) if d == "p2r" else (pi, cr, bp)
        for pos in positions:
            if only is not None and f"{d}_{pos}" not in only: continue
            raw = P.patch_all_heads(recv, donor, pos, batch, prefix_len(pi, ri, pos, bool(P.use_prefix)))
            res["effects"][f"{d}_{pos}"] = {k: raw[k] - np.float32(base[k]) for k in raw}
    res["prefix_cache"] = bool(P.use_prefix)
    return res


def save_pair(path, res, meta, keep=None):
    arrays = dict(keep or {}); arrays.update({f"{c}__{k}": v for c, e in res["effects"].items() for k, v in e.items()})
    info = dict(meta, prefix_cache=res.get("prefix_cache", False), n_tok_perm=res["n_tok_perm"], n_tok_rest=res["n_tok_rest"], base_perm=res["base_perm"], base_rest=res["base_rest"])
    tmp = path + ".tmp.npz"; np.savez_compressed(tmp, __meta__=np.array(json.dumps(info)), **arrays); os.replace(tmp, path)


def selftest(args, P):
    root = args.selftest; hist = args.hist_name or HIST_DIRS.get(args.model, os.path.basename(args.model.rstrip("/")))
    ref = np.load(os.path.join(root, "data/heads", hist, "head_effects.npz"))
    pairs = {p["name"]: p for p in json.load(open(os.path.join(root, "../stimuli/original_moral_pairs.json")))}
    names = [n for n in ref.files][:args.selftest_n]; worst = 1.0
    for n in names:
        r = run_pair(P, pairs[n]["permissive_prompt"], pairs[n]["restrictive_prompt"], ["p2r"], ["all"], args.batch)
        mine, theirs = r["effects"]["p2r_all"]["S_hist"], ref[n]
        c = float(np.corrcoef(mine.ravel(), theirs.ravel())[0, 1]); worst = min(worst, c)
        print(f"  {n:45s} corr={c:.4f}  max|diff|={np.abs(mine - theirs).max():.4f}  max|stored|={np.abs(theirs).max():.4f}", flush=True)
    print(f"SELFTEST {'PASSED' if worst > 0.97 else 'FAILED'}: lowest correlation with the stored head effects of the original pairs = {worst:.4f} (threshold 0.97)")
    return worst > 0.97


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items"); ap.add_argument("--out", default="runs/heads")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES))
    ap.add_argument("--directions", nargs="+", default=["p2r", "r2p"], choices=["p2r", "r2p"])
    ap.add_argument("--positions", nargs="+", default=["all", "final"], choices=["all", "final"])
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"])
    ap.add_argument("--batch", type=int, default=64); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--categories", nargs="+", default=None); ap.add_argument("--tag", default=None)
    ap.add_argument("--accepted-only", action="store_true", help="skip the pairs that the annotators did not accept (saves time on the largest models; running again without it adds them)")
    ap.add_argument("--selftest", default=None, help="folder with the stored head effects of the original pairs: reproduce them and exit")
    ap.add_argument("--any-items", action="store_true", help="software tests only")
    ap.add_argument("--allow-unequal", action="store_true", help="accept pairs whose two prompts differ in token count (the original pairs only)")
    ap.add_argument("--no-prefix-cache", action="store_true", help="always run the full sequence (slower; numbers are the same)")
    ap.add_argument("--selftest-n", type=int, default=4); ap.add_argument("--hist-name", default=None, help="folder name of this model among the stored head effects of the original pairs (only needed for local model paths)")
    args = ap.parse_args()
    if args.items and not args.selftest: check_run_file(args.items, hashlib.sha256(open(args.items, "rb").read()).hexdigest(), args.any_items)
    dev = pick_device(args.device); print(f"[run_heads] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    P = Patcher(args.model, dev, args.dtype); P.use_prefix = False if args.no_prefix_cache else None; print(f"[run_heads] layers={P.L} heads={P.H} head_dim={P.hd}", flush=True)
    if args.selftest:
        sys.exit(0 if selftest(args, P) else 1)
    raw = open(args.items, "rb").read(); items = json.loads(raw); sha = hashlib.sha256(raw).hexdigest()
    if args.accepted_only: keep_ids = accepted_ids(); items = [it for it in items if it["id"] in keep_ids]
    if args.categories: items = [it for it in items if it["category"] in args.categories]
    if args.limit: items = items[:args.limit]
    tag = args.tag or args.model.rstrip("/").split("/")[-1]; out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    import transformers; cfgp = os.path.join(out, "run_config.json"); hist = json.load(open(cfgp)) if os.path.exists(cfgp) else []; hist = hist if isinstance(hist, list) else [hist]
    hist.append({"model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "frames": args.frames, "directions": args.directions,
                 "positions": args.positions, "torch": torch.__version__, "transformers": transformers.__version__, "n_layers": P.L, "n_heads": P.H, "started": time.strftime("%Y-%m-%d %H:%M:%S")})
    json.dump(hist, open(cfgp, "w"), indent=1)
    t0 = time.time(); todo = [(f, it) for f in args.frames for it in items]; done = 0; masses = []; want = {f"{d}_{pos}" for d in args.directions for pos in args.positions}
    for f, it in todo:
        path = os.path.join(out, f"{f}__{it['id']}.npz"); keep, only = None, None
        if os.path.exists(path):
            try: z = np.load(path, allow_pickle=False); old_meta = json.loads(str(z["__meta__"])); have = {k.split("__")[0] for k in z.files if k != "__meta__"}
            except Exception as e: print(f"[run_heads] unreadable file, recomputing: {path} ({type(e).__name__})", flush=True); have, old_meta = set(), None
            if old_meta is not None and old_meta.get("items_sha256") != sha: sys.exit(f"[run_heads] {path} was made from a different item file; move it away or use another --out / --tag")
            if want <= have: done += 1; continue
            if have: keep = {k: z[k] for k in z.files if k != "__meta__"}; only = want - have
        perm_text, rest_text = FRAMES[f](it["perm_stem"]), FRAMES[f](it["rest_stem"])
        if not args.allow_unequal and len(encode(P.tok, perm_text)) != len(encode(P.tok, rest_text)): sys.exit(f"[run_heads] item {it['id']} frame {f}: the two prompts differ in token count for this tokenizer; the study items never should (use --allow-unequal for the original pairs)")
        t1 = time.time(); res = run_pair(P, perm_text, rest_text, args.directions, args.positions, args.batch, only)
        save_pair(path, res, {"id": it["id"], "frame": f, "category": it["category"], "subtype": it.get("subtype"), "model": args.model, "items_sha256": sha, "n_layers": P.L, "n_heads": P.H, "seconds": round(time.time() - t1, 2)}, keep)
        done += 1; el = time.time() - t0; masses.append(res["base_perm"]["mass"])


        shown = (f"gap(S)={res['base_perm']['S'] - res['base_rest']['S']:+.3f} mass={res['base_perm']['mass']:.2f}" if args.any_items else f"mean answer-word mass so far={np.mean(masses):.2f}")
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} {shown} ntok={res['n_tok_perm']}/{res['n_tok_rest']}  conditions={sorted(res['effects'])}  elapsed={el/60:.1f} min", flush=True)
    print("[run_heads] finished", flush=True)


if __name__ == "__main__":
    main()
