"""Attention targets and direct effects of every head."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import (FRAMES, GROUPS, READOUT_KEYS, Model, pick_device, token_groups, load_items, head_sets, save_npz, existing_ok,
                         run_config_append, model_tag, readouts, first, equal_length_or_skip, all_present)


class Capture:

    def __init__(self, M):
        self.M = M; self.z, self.attn_w, self.attn_out, self.mlp_out = {}, {}, {}, {}; self.x0 = None; self.h_final = None; self.hooks = []
        for l, layer in enumerate(M.layers):
            self.hooks.append(layer.self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: self.z.__setitem__(l, a[0].detach())))
            self.hooks.append(layer.self_attn.register_forward_hook(lambda m, a, out, l=l: self._attn(l, out)))
            self.hooks.append(layer.mlp.register_forward_hook(lambda m, a, out, l=l: self.mlp_out.__setitem__(l, first(out).detach())))
        self.hooks.append(M.layers[0].register_forward_pre_hook(self._x0, with_kwargs=True))
        self.hooks.append(M.norm.register_forward_pre_hook(lambda m, a: setattr(self, "h_final", a[0].detach())))

    def _attn(self, l, out):
        self.attn_out[l] = out[0].detach()
        w = out[1] if isinstance(out, (tuple, list)) and len(out) > 1 else None
        if w is None: sys.exit("[run_head_roles] the attention weights are not returned; the model must run with the eager attention implementation")
        self.attn_w[l] = w.detach()

    def _x0(self, m, args, kwargs):
        x = args[0] if args else kwargs["hidden_states"]; self.x0 = x.detach()

    def remove(self):
        for h in self.hooks: h.remove()


@torch.no_grad()
def analyse_pair(M, frame, item, set_heads):
    ids, g, (e0, e1) = token_groups(M, frame, item); n = len(ids["perm"])
    cap = Capture(M)
    try: lg = M.forward_logits([ids["perm"], ids["rest"]])
    finally: cap.remove()
    R = readouts(lg, M.A); res = {"groups": g, "edit_span": np.array([e0, e1]), "n_tok": np.array(n)}
    gi = [np.where(g == k)[0] for k in range(len(GROUPS))]; later = np.concatenate([gi[4], gi[5]]); edit = gi[3]
    s = M.norm_scale(cap.h_final[:, -1, :])
    dirs = {"": M.u_dir, "gb_": M.gb_dir}
    recon = cap.x0[:, -1, :].float().clone(); errs = []
    for b, side in enumerate(("perm", "rest")):
        for k in READOUT_KEYS: res[f"{side}_{k}"] = np.array(float(R[k][b]))
        W = torch.stack([cap.attn_w[l][b] for l in range(M.L)])
        fin = W[:, :, -1, :]
        res[f"{side}_attn_final"] = np.stack([fin[:, :, idx].sum(-1).cpu().numpy() if len(idx) else np.zeros((M.L, M.H), np.float32) for idx in gi], -1).astype(np.float32)
        res[f"{side}_attn_edit"] = (W[:, :, later][:, :, :, edit].sum(-1).mean(-1).cpu().numpy().astype(np.float32) if len(edit) and len(later) else np.zeros((M.L, M.H), np.float32))
        res[f"{side}_attn_sets"] = np.stack([fin[l, h].cpu().numpy() for (l, h) in set_heads]).astype(np.float32) if set_heads else np.zeros((0, n), np.float32)
        for pre, dvec in dirs.items():
            u = (dvec * s[b]).to(cap.h_final.dtype)
            dh = np.zeros((M.L, M.H), np.float32); dm = np.zeros(M.L, np.float32); dbias = np.zeros(M.L, np.float32)
            for l in range(M.L):
                ho = M.head_outputs(cap.z[l][b:b + 1, -1:, :], l)[0, 0]
                dh[l] = (ho @ u.float()).cpu().numpy()
                dbias[l] = float((cap.attn_out[l][b, -1].float() - ho.sum(0)) @ u.float())
                dm[l] = float(cap.mlp_out[l][b, -1].float() @ u.float())
            res[f"{side}_dla_{pre}heads"] = dh; res[f"{side}_dla_{pre}mlp"] = dm; res[f"{side}_dla_{pre}attn_bias"] = dbias
            res[f"{side}_dla_{pre}embed"] = np.array(float(cap.x0[b, -1].float() @ u.float()))
            if pre == "":
                total = float(dh.sum() + dm.sum() + dbias.sum()) + float(res[f"{side}_dla_embed"]); metric = float(M.metric(lg[b:b + 1])[0])
                errs.append(float(abs(total - metric) / max(abs(metric), 1e-3)))
        for l in range(M.L): recon[b] += cap.attn_out[l][b, -1].float() + cap.mlp_out[l][b, -1].float()
    rec_err = float((recon - cap.h_final[:, -1, :].float()).abs().max() / cap.h_final[:, -1, :].float().abs().max())
    norm_err = M.check_norm_scale(cap.h_final[:, -1, :])
    return res, {"dla_rel_err": max(errs), "resid_recon_rel_err": rec_err, "norm_scale_rel_err": norm_err}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/circuits/roles")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--device", default="auto")
    ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--categories", nargs="+", default=None); ap.add_argument("--tag", default=None)
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--allow-unequal", action="store_true", help="the original pairs: skip pairs whose prompts differ in token count")
    ap.add_argument("--no-sets", action="store_true", help="do not look up located head sets (tests on models without located sets)")
    ap.add_argument("--sets-file", default=None, help="software tests only: a head-set file with the layout of located/heads.json (default: that file)")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit, args.categories)
    tag = args.tag or model_tag(args.model)
    if all_present(os.path.join(args.out, tag), args.frames, items, sha): print(f"[run_head_roles] {tag}: every result file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_head_roles] model={args.model} device={dev} dtype={args.dtype} (eager attention)", flush=True)
    M = Model(args.model, dev, args.dtype, eager=True)
    print(f"[run_head_roles] layers={M.L} heads={M.H} kv_heads={M.Hkv} head_dim={M.hd}", flush=True)
    sets = {} if args.no_sets else head_sets(tag, args.sets_file)[0]
    set_heads = sorted({h for k in ("located", "topshare10") for h in sets.get(k, [])})
    out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    run_config_append(out, {"script": "run_head_roles.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha,
                            "frames": args.frames, "n_items": len(items), "set_heads": set_heads, "sets_file": args.sets_file or "located/heads.json", "n_layers": M.L, "n_heads": M.H})
    todo = [(f, it) for f in args.frames for it in items]; t0 = time.time(); masses = []; checked = False
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, sha): continue
        if not equal_length_or_skip(M, f, it, args.allow_unequal): continue
        t1 = time.time(); res, chk = analyse_pair(M, f, it, set_heads)
        if not checked:
            print(f"[run_head_roles] exactness on the first item: DLA sum vs metric rel. err = {chk['dla_rel_err']:.2e}; residual reconstruction rel. err = {chk['resid_recon_rel_err']:.2e}; "
                  f"norm scale rel. err = {chk['norm_scale_rel_err']:.2e}", flush=True)
            if max(chk.values()) > 1e-3: sys.exit("[run_head_roles] the attribution does not reproduce the model's own logits; stopping (unexpected architecture?)")
            checked = True
        meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, n_layers=M.L, n_heads=M.H,
                    groups=GROUPS, set_heads=set_heads, seconds=round(time.time() - t1, 2), **{k: round(float(v), 8) for k, v in chk.items()})
        save_npz(path, meta, res); masses.append(float(res["perm_mass"]))
        shown = f"gap(S)={float(res['perm_S']) - float(res['rest_S']):+.3f} " if args.any_items else ""
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} {shown}mean answer-word mass so far={np.mean(masses):.2f} ntok={int(res['n_tok'])} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
    print("[run_head_roles] finished", flush=True)


if __name__ == "__main__":
    main()
