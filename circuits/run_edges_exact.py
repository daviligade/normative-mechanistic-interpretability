"""Exact patching of the strongest edges."""
import argparse, json, os, sys, time, glob
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import (FRAMES, READOUT_KEYS, Model, pick_device, token_groups, load_items, head_sets, save_npz, existing_ok, run_config_append, model_tag,
                         readouts, first, equal_length_or_skip, all_present)
from run_edges import GradRun, source_delta_vec

EXACT_KEYS = ("S", "LD", "mass", "S_hist", "LD_gb")


def select_edges(edge_dir, frame, d10, top, model_sha):
    files = sorted(glob.glob(os.path.join(edge_dir, f"{frame}__*.npz"))); tot = None; n = 0; labels = None; L = H = None
    for f in files:
        z = np.load(f, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta.get("items_sha256") != model_sha: sys.exit(f"[run_edges_exact] {f} was made from another item file")
        if labels is None: labels = meta["receiver_inputs"]; L, H = meta["n_layers"], meta["n_heads"]
        e = z["p2r_edges"].astype(np.float64).sum(-1); tot = e if tot is None else tot + e; n += 1
    if n == 0: sys.exit(f"[run_edges_exact] no run_edges.py results for frame {frame} under {edge_dir}; run run_edges.py first")
    mean = tot / n; LH = L * H; d10_names = {f"L{l}H{h}" for (l, h) in d10}
    def src_layer(s): return s // H if s < LH else (s - LH if s < LH + L else -1)
    sel = []
    for j, lab in enumerate(labels):
        if lab != "logits" and lab.split(".")[0] not in d10_names: continue
        lv = L if lab == "logits" else int(lab[1:lab.index("H")])
        allowed = [s for s in range(mean.shape[0]) if src_layer(s) < lv]
        for s in sorted(allowed, key=lambda s: -abs(mean[s, j]))[:top]:
            sel.append({"src": int(s), "recv": int(j), "receiver": lab, "source": (f"L{s // H}H{s % H}" if s < LH else (f"MLP{s - LH}" if s < LH + L else "embed")), "mean_estimate": float(mean[s, j])})
    return sel, labels, n


@torch.no_grad()
def plain_capture(M, ids):
    c = {"z": {}, "mlp": {}}; hooks = []
    hooks.append(M.layers[0].register_forward_pre_hook(lambda m, args, kwargs: c.__setitem__("x0", (args[0] if args else kwargs["hidden_states"]).detach()), with_kwargs=True))
    for l, layer in enumerate(M.layers):
        hooks.append(layer.self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: c["z"].__setitem__(l, a[0].detach())))
        hooks.append(layer.mlp.register_forward_hook(lambda m, a, out, l=l: c["mlp"].__setitem__(l, first(out).detach())))
    try: M.forward_logits([ids])
    finally:
        for h in hooks: h.remove()
    return c


@torch.no_grad()
def exact_effects(M, R, D, labels, ids, pairs, batch):
    out = {"metric": np.zeros(len(pairs), np.float32)}; out.update({k: np.zeros(len(pairs), np.float32) for k in EXACT_KEYS})
    clean_lg = M.forward_logits([ids]); clean_metric = float(M.metric(clean_lg)[0]); clean_R = {k: float(v[0]) for k, v in readouts(clean_lg, M.A).items()}
    for s in range(0, len(pairs), batch):
        chunk = pairs[s:s + batch]; hooks = []; by_mod = {}
        for b, (src, j) in enumerate(chunk):
            lab = labels[j]; delta = source_delta_vec(M, R, D, src)
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
        out["metric"][s:s + len(chunk)] = (M.metric(lg) - clean_metric).cpu().numpy(); R_ = readouts(lg, M.A)
        for k in EXACT_KEYS: out[k][s:s + len(chunk)] = (R_[k].float() - clean_R[k]).cpu().numpy()
    return out, clean_R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/circuits/edges_exact")
    ap.add_argument("--edges", default="runs/circuits/edges", help="output folder of run_edges.py (the estimates to select from)")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--top", type=int, default=5, help="edges per receiver input")
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--categories", nargs="+", default=None); ap.add_argument("--tag", default=None)
    ap.add_argument("--sets-file", default=None, help="software tests only: a head-set file with the layout of located/heads.json (default: that file)")
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--allow-unequal", action="store_true", help="the original pairs: skip pairs whose prompts differ in token count")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit, args.categories)
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); edge_dir = os.path.join(args.edges, tag)
    if all_present(out, args.frames, items, sha, extra=[f"selected_edges__{f}.json" for f in args.frames]): print(f"[run_edges_exact] {tag}: every result file is already there; nothing to do", flush=True); return
    fs, _ = head_sets(tag, args.sets_file); d10 = fs["located"]; os.makedirs(out, exist_ok=True); selected, labels_by_frame = {}, {}
    for f in args.frames:
        p = os.path.join(out, f"selected_edges__{f}.json")
        if os.path.exists(p):
            saved = json.load(open(p)); selected[f] = saved["edges"]; labels_by_frame[f] = saved["receiver_inputs"]
            if saved.get("items_sha256") != sha or saved.get("top") != args.top: sys.exit(f"[run_edges_exact] {p} was made with other settings; use another --out")
        else:
            sel, labels, n_used = select_edges(edge_dir, f, d10, args.top, sha); selected[f] = sel; labels_by_frame[f] = labels
            json.dump({"frame": f, "items_sha256": sha, "top": args.top, "n_items_used_for_selection": n_used, "receiver_inputs": labels, "edges": sel}, open(p, "w"), indent=1)
        print(f"[run_edges_exact] {f}: {len(selected[f])} edges selected ({args.top} per receiver input, located heads and the logits)", flush=True)
    dev = pick_device(args.device); print(f"[run_edges_exact] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    M = Model(args.model, dev, args.dtype); print(f"[run_edges_exact] layers={M.L} heads={M.H} kv_heads={M.Hkv} head_dim={M.hd}", flush=True)
    run_config_append(out, {"script": "run_edges_exact.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "frames": args.frames, "top": args.top,
                            "edges_dir": edge_dir, "n_items": len(items), "n_layers": M.L, "n_heads": M.H, "receivers": [list(h) for h in d10]})
    todo = [(f, it) for f in args.frames for it in items]; t0 = time.time(); masses = []
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, sha): continue
        if not equal_length_or_skip(M, f, it, args.allow_unequal): continue
        t1 = time.time(); ids, groups, span = token_groups(M, f, it); pairs = [(e["src"], e["recv"]) for e in selected[f]]
        R = GradRun(M, ids["rest"]); D = plain_capture(M, ids["perm"])
        ex, clean_R = exact_effects(M, R, D, labels_by_frame[f], ids["rest"], pairs, args.batch)
        est = np.zeros(len(pairs), np.float32); ep = os.path.join(edge_dir, f"{f}__{it['id']}.npz")
        if os.path.exists(ep):
            ze = np.load(ep, allow_pickle=False); tot = ze["p2r_edges"].sum(-1)
            est = np.array([tot[s, j] for s, j in pairs], np.float32)
        res = {"exact_metric": ex["metric"], "estimate_metric": est, **{f"exact_{k}": ex[k] for k in EXACT_KEYS}, **{f"rest_{k}": np.array(clean_R[k]) for k in EXACT_KEYS},
               "perm_S": np.array(float(readouts(M.forward_logits([ids["perm"]]), M.A)["S"][0])), "groups": groups, "edit_span": np.array(span)}
        save_npz(path, dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, direction="p2r", top=args.top, n_edges=len(pairs),
                            n_layers=M.L, n_heads=M.H, seconds=round(time.time() - t1, 2)), res)
        masses.append(float(clean_R["mass"]))
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} mean answer-word mass so far={np.mean(masses):.2f} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
    print("[run_edges_exact] finished", flush=True)


if __name__ == "__main__":
    main()
