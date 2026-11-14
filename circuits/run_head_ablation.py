"""Removal of a set of heads (mean-ablation) against random sets of heads."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import (FRAMES, READOUT_KEYS, Model, pick_device, load_items, head_sets, random_head_sets, save_npz, existing_ok, run_config_append,
                         model_tag, readouts, encode, equal_length_or_skip, sha, all_present)


def build_sets(tag, M, sets_file, n_random, sizes):
    fs, _ = head_sets(tag, sets_file); names, sets = [], []
    for k in ("located", "topshare10", "located_top5", "located_top1"): names.append(k); sets.append(fs[k])
    union = sorted(set(fs["located"]) | set(fs["topshare10"]))
    if len(union) > len(fs["located"]): names.append("union"); sets.append(union)
    located_heads = set(h for s in sets for h in s)
    rnd = random_head_sets(tag, M.L, M.H, sizes=sizes, n_sets=n_random, exclude=located_heads)
    for size in sizes:
        for r, s in enumerate(rnd[size]): names.append(f"random{size}_{r:02d}"); sets.append(s)
    return names, sets


@torch.no_grad()
def phase1_means(M, items, frame, path, items_sha, reuse=False):
    if os.path.exists(path):
        z = np.load(path, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta.get("items_sha256") != items_sha: sys.exit(f"[run_head_ablation] {path} was made from another item file; move it away or use another --out / --tag")
        if meta.get("n_items") != len(items) and not (reuse and meta.get("n_items", 0) < len(items)):
            sys.exit(f"[run_head_ablation] {path} was made from the first {meta.get('n_items')} items of this run file, this run has {len(items)}; "
                     f"--reuse-means keeps that reference for the added items, otherwise move it away or use another --out / --tag")
        if meta.get("n_items") != len(items): print(f"[phase 1] {frame}: means of the first {meta['n_items']} items kept as the reference for all {len(items)} (--reuse-means)", flush=True)
        else: print(f"[phase 1] {frame}: means exist ({path})", flush=True)
        return torch.tensor(z["mean_all"], device=M.device), torch.tensor(z["mean_final"], device=M.device), int(meta["n_items"])
    s_all = torch.zeros(M.L, M.H * M.hd, dtype=torch.float64); s_fin = torch.zeros_like(s_all); n_all = 0; n_fin = 0; cache = {}
    hooks = [M.layers[l].self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: cache.__setitem__(l, a[0].detach())) for l in range(M.L)]
    t0 = time.time()
    try:
        for k, it in enumerate(items):
            for side in ("perm", "rest"):
                ids = encode(M.tok, FRAMES[frame](it[f"{side}_stem"])); M.forward_logits([ids])
                for l in range(M.L):
                    z = cache[l][0].float().cpu().double(); s_all[l] += z[1:].sum(0); s_fin[l] += z[-1]
                n_all += len(ids) - 1; n_fin += 1
            if (k + 1) % 25 == 0: print(f"[phase 1] {frame} {k + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in hooks: h.remove()
    mean_all = (s_all / n_all).float(); mean_fin = (s_fin / n_fin).float()
    save_npz(path, {"frame": frame, "items_sha256": items_sha, "n_items": len(items), "n_prompts": n_fin, "n_positions_pooled": n_all, "note": "BOS excluded from mean_all"},
             {"mean_all": mean_all.numpy(), "mean_final": mean_fin.numpy()})
    return mean_all.to(M.device), mean_fin.to(M.device), len(items)


@torch.no_grad()
def ablate(M, ids, combos, means, batch):
    out = {k: np.zeros(len(combos), np.float32) for k in READOUT_KEYS}; n = len(ids)
    for s in range(0, len(combos), batch):
        chunk = combos[s:s + batch]; hooks = []
        for l in sorted({l for heads, _ in chunk for (l, _) in heads}):
            def pre(m, a, l=l):
                z = a[0].clone()
                for b, (heads, mode) in enumerate(chunk):
                    for (ll, hh) in heads:
                        if ll != l: continue
                        sl = slice(hh * M.hd, (hh + 1) * M.hd)
                        if mode == "all": z[b, 1:, sl] = means["all"][l, sl].to(z.dtype)
                        else: z[b, -1, sl] = means["final"][l, sl].to(z.dtype)
                return (z,)
            hooks.append(M.layers[l].self_attn.o_proj.register_forward_pre_hook(pre))
        try: lg = M.forward_logits([ids] * len(chunk))
        finally:
            for h in hooks: h.remove()
        R = readouts(lg, M.A)
        for k in out: out[k][s:s + len(chunk)] = R[k].float().cpu().numpy()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/circuits/ablation")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--device", default="auto")
    ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--categories", nargs="+", default=None); ap.add_argument("--tag", default=None)
    ap.add_argument("--n-random", type=int, default=20); ap.add_argument("--sizes", nargs="+", type=int, default=[10, 5, 1], help="sizes of the random control sets")
    ap.add_argument("--reuse-means", action="store_true", help="keep an existing means file made with a shorter --limit on the same run file (reserve round of the 14B models)")
    ap.add_argument("--modes", nargs="+", default=["all", "final"], choices=["all", "final"])
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--allow-unequal", action="store_true", help="the original pairs: skip pairs whose prompts differ in token count")
    ap.add_argument("--sets-file", default=None, help="software tests only: a head-set file with the layout of located/heads.json (default: that file)")
    args = ap.parse_args()
    items, items_sha = load_items(args.items, args.any_items, args.limit, args.categories)
    tag = args.tag or model_tag(args.model)
    if all_present(os.path.join(args.out, tag), args.frames, items, items_sha, extra=[f"means__{f}.npz" for f in args.frames]): print(f"[run_head_ablation] {tag}: every result file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_head_ablation] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    M = Model(args.model, dev, args.dtype); print(f"[run_head_ablation] layers={M.L} heads={M.H} head_dim={M.hd}", flush=True)
    names, sets = build_sets(tag, M, args.sets_file, args.n_random, args.sizes)
    out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); sp = os.path.join(out, "sets.json")
    if os.path.exists(sp):
        old = json.load(open(sp))
        if old["names"] != names or [[list(h) for h in s] for s in sets] != old["sets"]: sys.exit(f"[run_head_ablation] {sp} holds other sets (another --n-random / --sizes?); use another --out / --tag")
    else: json.dump({"names": names, "sets": [[list(h) for h in s] for s in sets], "sets_file": args.sets_file or "located/heads.json", "n_random": args.n_random, "sizes": args.sizes}, open(sp, "w"))
    run_config_append(out, {"script": "run_head_ablation.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": items_sha, "frames": args.frames,
                            "modes": args.modes, "n_items": len(items), "n_sets": len(names), "n_random": args.n_random, "sizes": args.sizes, "sets_file": args.sets_file or "located/heads.json", "n_layers": M.L, "n_heads": M.H})
    means = {}; means_n = {}
    for f in args.frames:
        ma, mf, n_m = phase1_means(M, items, f, os.path.join(out, f"means__{f}.npz"), items_sha, args.reuse_means); means[f] = {"all": ma, "final": mf}; means_n[f] = n_m
    combos = [(s, mode) for s in sets for mode in args.modes]; col = {mode: i for i, mode in enumerate(args.modes)}
    todo = [(f, it) for f in args.frames for it in items]; t0 = time.time(); masses = []
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, items_sha): continue
        if not equal_length_or_skip(M, f, it, args.allow_unequal): continue
        t1 = time.time(); res = {}
        for side in ("perm", "rest"):
            ids = encode(M.tok, FRAMES[f](it[f"{side}_stem"]))
            with torch.no_grad(): base = readouts(M.forward_logits([ids]), M.A)
            for k in READOUT_KEYS: res[f"{side}_base_{k}"] = np.array(float(base[k][0]))
            r = ablate(M, ids, combos, means[f], args.batch)
            for k in READOUT_KEYS:
                arr = np.zeros((len(sets), len(args.modes)), np.float32)
                for j, (_, mode) in enumerate(combos): arr[j // len(args.modes), col[mode]] = r[k][j]
                res[f"{side}_{k}"] = arr
        save_npz(path, dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=items_sha, set_names=names, modes=args.modes,
                            n_layers=M.L, n_heads=M.H, means_n_items=means_n[f], seconds=round(time.time() - t1, 2)), res)
        masses.append(float(res["perm_base_mass"]))
        shown = (f"gap(S)={float(res['perm_base_S']) - float(res['rest_base_S']):+.3f} gap after located ablation (all/final)={float(res['perm_S'][0, 0] - res['rest_S'][0, 0]):+.3f}/"
                 f"{float(res['perm_S'][0, -1] - res['rest_S'][0, -1]):+.3f} " if args.any_items else "")
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} {shown}mean answer-word mass so far={np.mean(masses):.2f} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
    print("[run_head_ablation] finished", flush=True)


if __name__ == "__main__":
    main()
