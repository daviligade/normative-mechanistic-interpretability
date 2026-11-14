"""Edges into the located heads (attribution patching)."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import (FRAMES, GROUPS, READOUT_KEYS, Model, pick_device, token_groups, load_items, head_sets, save_npz, existing_ok, run_config_append, model_tag,
                         readouts, first, equal_length_or_skip, all_present)

SCORE_GROUPS = [3, 4, 5]


def keep(store, l):
    def hook(m, a, out):
        t = first(out); t.retain_grad(); store[l] = t
    return hook


class GradRun:

    def __init__(self, M, ids):
        self.M = M; self.z, self.mlp, self.r_in, self.Q, self.K, self.V, self.attn_out, self.mlp_t = {}, {}, {}, {}, {}, {}, {}, {}; hooks = []

        def start(m, args, kwargs):
            x = args[0] if args else kwargs["hidden_states"]; x2 = x.detach().requires_grad_(True); self.x0 = x2
            return ((x2,) + tuple(args[1:]), kwargs) if args else (args, dict(kwargs, hidden_states=x2))
        hooks.append(M.layers[0].register_forward_pre_hook(start, with_kwargs=True))
        for l, layer in enumerate(M.layers):
            hooks.append(layer.register_forward_pre_hook(lambda m, args, kwargs, l=l: self.r_in.__setitem__(l, (args[0] if args else kwargs["hidden_states"]).detach()), with_kwargs=True))
            for name, store in (("q_proj", self.Q), ("k_proj", self.K), ("v_proj", self.V)):
                hooks.append(getattr(layer.self_attn, name).register_forward_hook(keep(store, l)))
            hooks.append(layer.self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: self.z.__setitem__(l, a[0].detach())))
            hooks.append(layer.self_attn.register_forward_hook(keep(self.attn_out, l)))
            hooks.append(layer.mlp.register_forward_hook(keep(self.mlp_t, l)))

        def norm_in(m, a):
            h = a[0].clone(); h.retain_grad(); self.h_final = h; return (h,)
        hooks.append(M.norm.register_forward_pre_hook(norm_in))
        try:
            with torch.enable_grad():
                lg = M.forward_logits([ids]); self.metric = M.metric(lg); self.metric.sum().backward()
        finally:
            for h in hooks: h.remove()
        self.metric = self.metric.detach(); self.logits = lg.detach(); self.readouts = {k: float(v[0]) for k, v in readouts(self.logits, M.A).items()}
        self.mlp = {l: t.detach() for l, t in self.mlp_t.items()}
        self.g_attn = {l: t.grad.detach() for l, t in self.attn_out.items()}; self.g_mlp = {l: t.grad.detach() for l, t in self.mlp_t.items()}
        self.g_x0 = self.x0.grad.detach(); self.g_hfinal = self.h_final.grad.detach()
        self.gQ = {l: t.grad.detach() for l, t in self.Q.items()}; self.gK = {l: t.grad.detach() for l, t in self.K.items()}; self.gV = {l: t.grad.detach() for l, t in self.V.items()}
        self.x0 = self.x0.detach(); self.Q = self.K = self.V = self.attn_out = self.mlp_t = self.h_final = None


def receiver_grads(M, R, recv_heads):
    out = []
    for (l, h) in recv_heads:
        att = M.layers[l].self_attn; g = M.kv_group(h); hd = M.hd
        for name, G, W, idx in (("q", R.gQ[l], att.q_proj.weight, h), ("k", R.gK[l], att.k_proj.weight, g), ("v", R.gV[l], att.v_proj.weight, g)):
            gx = G[0, :, idx * hd:(idx + 1) * hd].float() @ W[idx * hd:(idx + 1) * hd, :].float()
            _, gr = torch.autograd.functional.vjp(lambda r: M.layers[l].input_layernorm(r), R.r_in[l][0].float(), gx)
            out.append((f"L{l}H{h}.{name}", l, gr))
    out.append(("logits", M.L, R.g_hfinal[0].float()))
    return out


def source_deltas(M, R, D):
    dh = [M.head_outputs(D["z"][l], l)[0] - M.head_outputs(R.z[l], l)[0] for l in range(M.L)]
    dm = [D["mlp"][l][0].float() - R.mlp[l][0].float() for l in range(M.L)]
    return dh, dm, D["x0"][0].float() - R.x0[0].float()


def eap_scores(M, R, D, recv_heads, groups):
    n = len(groups); dh, dm, dx = source_deltas(M, R, D); recv = receiver_grads(M, R, recv_heads)
    gmask = torch.tensor(np.stack([(groups == k) for k in SCORE_GROUPS]).astype(np.float32), device=M.device)
    n_src = M.L * M.H + M.L + 1; edges = torch.zeros(n_src, len(recv), 3, device=M.device)
    for j, (label, lv, gr) in enumerate(recv):
        for l in range(min(lv, M.L)):
            ph = torch.einsum("nhd,nd->nh", dh[l], gr)
            edges[l * M.H:(l + 1) * M.H, j] = (gmask @ ph).T
            edges[M.L * M.H + l, j] = gmask @ (dm[l] * gr).sum(-1)
        edges[-1, j] = gmask @ (dx * gr).sum(-1)
    node_heads = torch.stack([torch.einsum("nhd,nd->h", dh[l], R.g_attn[l][0].float()) for l in range(M.L)])
    node_mlp = torch.stack([(dm[l] * R.g_mlp[l][0].float()).sum() for l in range(M.L)])
    node_embed = (dx * R.g_x0[0].float()).sum()
    return edges.cpu().numpy(), node_heads.cpu().numpy(), node_mlp.cpu().numpy(), float(node_embed), [lab for lab, _, _ in recv]


def source_delta_vec(M, R, D, src):
    LH = M.L * M.H
    if src < LH: l, h = divmod(src, M.H); return (M.head_outputs(D["z"][l], l)[0, :, h] - M.head_outputs(R.z[l], l)[0, :, h])
    if src < LH + M.L: l = src - LH; return D["mlp"][l][0].float() - R.mlp[l][0].float()
    return D["x0"][0].float() - R.x0[0].float()


@torch.no_grad()
def true_edge_effects(M, R, D, recv_heads, recv_labels, ids, pairs, batch):
    out = np.zeros(len(pairs), np.float32); clean = float(R.metric[0])
    for s in range(0, len(pairs), batch):
        chunk = pairs[s:s + batch]; hooks = []; by_mod = {}
        for b, (src, j) in enumerate(chunk):
            lab = recv_labels[j]; delta = source_delta_vec(M, R, D, src)
            if lab == "logits": by_mod.setdefault(("norm", None, None), []).append((b, delta, None))
            else:
                head, name = lab.split("."); l = int(head[1:head.index("H")]); h = int(head[head.index("H") + 1:]); idx = h if name == "q" else M.kv_group(h)
                by_mod.setdefault((name, l, idx), []).append((b, delta, idx))
        for (name, l, _), lst in by_mod.items():
            if name == "norm":
                def pre(m, a, lst=lst):
                    hh = a[0].clone()
                    for b, delta, _ in lst: hh[b, -1] += delta[-1].to(hh.dtype)
                    return (hh,)
                hooks.append(M.norm.register_forward_pre_hook(pre))
            else:
                layer = M.layers[l]; proj = getattr(layer.self_attn, f"{name}_proj"); r_clean = R.r_in[l][0].float()
                def hook(m, a, o, lst=lst, layer=layer, proj=proj, r_clean=r_clean):
                    o = o.clone()
                    for b, delta, idx in lst:
                        xb = layer.input_layernorm((r_clean + delta).to(a[0].dtype)); ob = torch.nn.functional.linear(xb, proj.weight, proj.bias)
                        sl = slice(idx * M.hd, (idx + 1) * M.hd); o[b, :, sl] = ob[:, sl]
                    return o
                hooks.append(proj.register_forward_hook(hook))
        try: lg = M.forward_logits([ids] * len(chunk))
        finally:
            for h in hooks: h.remove()
        out[s:s + len(chunk)] = (M.metric(lg) - clean).cpu().numpy()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/circuits/edges")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--directions", nargs="+", default=["p2r"], choices=["p2r", "r2p"])
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"])
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--categories", nargs="+", default=None); ap.add_argument("--tag", default=None)
    ap.add_argument("--receivers-file", default=None, help="JSON list of [layer, head] to use as receivers instead of located | topshare10 (recorded in run_config.json)")
    ap.add_argument("--sets-file", default=None, help="software tests only: a head-set file with the layout of located/heads.json (default: that file)")
    ap.add_argument("--validate", action="store_true", help="software tests only: also patch a sample of edges exactly and compare with the estimate")
    ap.add_argument("--val-top", type=int, default=10); ap.add_argument("--val-random", type=int, default=10); ap.add_argument("--val-batch", type=int, default=32); ap.add_argument("--seed", type=int, default=20261006)
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--allow-unequal", action="store_true", help="the original pairs: skip pairs whose prompts differ in token count")
    args = ap.parse_args()
    if args.validate and not args.any_items: sys.exit("[run_edges] --validate is for software tests only (it prints per-item outcomes); add --any-items with an old-item file")
    items, sha = load_items(args.items, args.any_items, args.limit, args.categories)
    tag = args.tag or model_tag(args.model)
    if not args.validate and all_present(os.path.join(args.out, tag), args.frames, items, sha): print(f"[run_edges] {tag}: every result file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_edges] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    M = Model(args.model, dev, args.dtype); print(f"[run_edges] layers={M.L} heads={M.H} kv_heads={M.Hkv} head_dim={M.hd}", flush=True)
    if args.receivers_file: recv_heads = sorted({(int(a), int(b)) for a, b in json.load(open(args.receivers_file))})
    else: fs, _ = head_sets(tag, args.sets_file); recv_heads = sorted(set(fs["located"]) | set(fs["topshare10"]))
    out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    run_config_append(out, {"script": "run_edges.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "frames": args.frames, "directions": args.directions,
                            "receivers": recv_heads, "receivers_file": args.receivers_file, "sets_file": None if args.receivers_file else (args.sets_file or "located/heads.json"), "validate": args.validate,
                            "n_items": len(items), "n_layers": M.L, "n_heads": M.H})
    rng = np.random.default_rng(args.seed); todo = [(f, it) for f in args.frames for it in items]; t0 = time.time(); masses = []; val_all = []
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, sha): continue
        if not equal_length_or_skip(M, f, it, args.allow_unequal): continue
        t1 = time.time(); ids, groups, span = token_groups(M, f, it); res = {"groups": groups, "edit_span": np.array(span)}; meta = {}
        runs = {side: GradRun(M, ids[side]) for side in ("perm", "rest")}
        for side in ("perm", "rest"):
            for k in READOUT_KEYS: res[f"{side}_{k}"] = np.array(runs[side].readouts[k])
        for d in args.directions:
            recv, donor = ("rest", "perm") if d == "p2r" else ("perm", "rest"); R = runs[recv]
            D = {"z": runs[donor].z, "mlp": runs[donor].mlp, "x0": runs[donor].x0}
            edges, nh, nm, ne, labels = eap_scores(M, R, D, recv_heads, groups)
            res[f"{d}_edges"] = edges.astype(np.float32); res[f"{d}_node_heads"] = nh.astype(np.float32); res[f"{d}_node_mlp"] = nm.astype(np.float32); res[f"{d}_node_embed"] = np.array(ne, np.float32)
            res[f"{d}_metric_receiver"] = np.array(float(R.metric[0])); res[f"{d}_metric_donor"] = np.array(float(runs[donor].metric[0]))
            meta["receiver_inputs"] = labels
            if args.validate:
                tot = edges.sum(-1); pairs = []
                for j, lab in enumerate(labels):
                    lv = M.L if lab == "logits" else int(lab[1:lab.index("H")]); allowed = [s for s in range(edges.shape[0]) if (s // M.H if s < M.L * M.H else (s - M.L * M.H if s < M.L * M.H + M.L else -1)) < lv]
                    top = sorted(allowed, key=lambda s: -abs(tot[s, j]))[:args.val_top]; rest = [s for s in allowed if s not in top]
                    rnd = list(rng.choice(rest, size=min(args.val_random, len(rest)), replace=False)) if rest else []
                    pairs += [(int(s), j) for s in top + rnd]
                true = true_edge_effects(M, R, D, recv_heads, labels, ids[recv], pairs, args.val_batch)
                est = np.array([tot[s, j] for s, j in pairs], np.float32)
                res[f"{d}_val"] = np.stack([np.array([s for s, _ in pairs], np.float32), np.array([j for _, j in pairs], np.float32), est, true], 1)
                kind = np.array([labels[j].split(".")[-1] if labels[j] != "logits" else "logits" for _, j in pairs]); val_all.append((kind, est, true))
                r = np.corrcoef(est, true)[0, 1] if est.std() > 0 and true.std() > 0 else float("nan")
                sign = float(np.mean(np.sign(est) == np.sign(true)))
                print(f"    validation {d}: {len(pairs)} edges, r(estimate, exact) = {r:.3f}, sign agreement = {sign:.2f}, max |exact| = {np.abs(true).max():.3f}, max |estimate| = {np.abs(est).max():.3f}", flush=True)
        save_npz(path, dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, directions=args.directions, receivers=recv_heads,
                            score_groups=[GROUPS[k] for k in SCORE_GROUPS], n_layers=M.L, n_heads=M.H, n_tok=len(ids["perm"]), seconds=round(time.time() - t1, 2), **meta), res)
        masses.append(float(res["perm_mass"]))
        shown = f"gap(S)={float(res['perm_S']) - float(res['rest_S']):+.3f} " if args.any_items else ""
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} {shown}mean answer-word mass so far={np.mean(masses):.2f} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
    if args.validate and val_all:
        kinds = np.concatenate([k for k, _, _ in val_all]); est = np.concatenate([e for _, e, _ in val_all]); true = np.concatenate([t for _, _, t in val_all])
        print("[run_edges] validation summary (all items and frames):")
        for k in ("q", "k", "v", "logits"):
            m = kinds == k
            if m.sum() > 2: print(f"    {k:6s} n={int(m.sum()):5d}  r = {np.corrcoef(est[m], true[m])[0, 1]:.3f}  sign agreement = {np.mean(np.sign(est[m]) == np.sign(true[m])):.2f}  mean |exact| = {np.abs(true[m]).mean():.4f}", flush=True)
        print(f"    all    n={len(est):5d}  r = {np.corrcoef(est, true)[0, 1]:.3f}  sign agreement = {np.mean(np.sign(est) == np.sign(true)):.2f}", flush=True)
    print("[run_edges] finished", flush=True)


if __name__ == "__main__":
    main()
