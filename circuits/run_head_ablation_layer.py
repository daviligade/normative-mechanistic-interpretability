"""Removal of the located heads against random heads from the same layers."""
import argparse, hashlib, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, READOUT_KEYS, Model, pick_device, load_items, head_sets, save_npz, existing_ok, run_config_append, model_tag, readouts, encode, equal_length_or_skip
from run_head_ablation import ablate, phase1_means

SEED = 20261114


def layer_matched_sets(tag, M, fs, n_random):
    located = fs["located"]; located = set(h for s in fs.values() for h in s)
    rng = np.random.default_rng(SEED + int(hashlib.sha256(tag.encode()).hexdigest(), 16) % 10**6); out = []
    for _ in range(n_random):
        chosen = []
        for (l, _h) in located:
            pool = [(l, h) for h in range(M.H) if (l, h) not in located and (l, h) not in chosen]
            if not pool: pool = [(l, h) for h in range(M.H) if (l, h) not in set(located) and (l, h) not in chosen]
            chosen.append(pool[int(rng.integers(len(pool)))])
        out.append(chosen)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", default="stimuli/items_run_v1.json"); ap.add_argument("--accepted-only", action="store_true")
    ap.add_argument("--means-dir", default="runs/circuits/ablation"); ap.add_argument("--out", default="runs/circuits_layer")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"]); ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32")
    ap.add_argument("--batch", type=int, default=32); ap.add_argument("--n-random", type=int, default=20); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--tag", default=None); ap.add_argument("--sets-file", default=None, help="software tests only"); ap.add_argument("--any-items", action="store_true", help="software tests only")
    args = ap.parse_args()
    items, items_sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import accepted_ids
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, "ablation", tag); os.makedirs(out, exist_ok=True)
    if all(existing_ok(os.path.join(out, f"{f}__{it['id']}.npz"), items_sha) for f in args.frames for it in items): print(f"[layer] {tag}: every result file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); M = Model(args.model, dev, args.dtype); print(f"[layer] model={args.model} device={dev} layers={M.L} heads={M.H}; {len(items)} pairs", flush=True)
    fs, _ = head_sets(tag, args.sets_file); R = layer_matched_sets(tag, M, fs, args.n_random)
    names = ["located"] + [f"random10_{r:02d}" for r in range(len(R))]; sets = [fs["located"]] + R
    assert all(sorted(l for l, _ in s) == sorted(l for l, _ in fs["located"]) for s in R), "a random set does not have the layer profile of the located heads"
    sp = os.path.join(out, "sets.json")
    if os.path.exists(sp) and json.load(open(sp))["sets"] != [[list(h) for h in s] for s in sets]: sys.exit(f"[layer] {sp} holds other sets; use another --out")
    json.dump({"names": names, "sets": [[list(h) for h in s] for s in sets], "sets_file": args.sets_file or "located/heads.json", "n_random": args.n_random, "sizes": [10], "layer_matched": True, "seed": SEED}, open(sp, "w"))
    run_config_append(out, {"script": "run_head_ablation_layer.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": items_sha, "frames": args.frames,
                            "modes": ["all"], "n_items": len(items), "n_random": args.n_random, "means_dir": args.means_dir, "n_layers": M.L, "n_heads": M.H})
    means, means_n = {}, {}
    for f in args.frames:
        p = os.path.join(args.means_dir, tag, f"means__{f}.npz")
        if os.path.exists(p):
            z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
            if meta.get("items_sha256") != items_sha: sys.exit(f"[layer] {p} was made from another item file")
            means[f] = {"all": torch.tensor(z["mean_all"], device=M.device), "final": torch.tensor(z["mean_final"], device=M.device)}; means_n[f] = int(meta["n_items"])
            print(f"[layer] {f}: the study's means ({p}, {meta['n_items']} pairs)", flush=True)
        else:
            ma, mf, n_m = phase1_means(M, items, f, os.path.join(out, f"means__{f}.npz"), items_sha); means[f] = {"all": ma, "final": mf}; means_n[f] = n_m
    combos = [(s, "all") for s in sets]; todo = [(f, it) for f in args.frames for it in items]; t0 = time.time()
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, items_sha): continue
        if not equal_length_or_skip(M, f, it, False): continue
        res = {}
        for side in ("perm", "rest"):
            ids = encode(M.tok, FRAMES[f](it[f"{side}_stem"]))
            with torch.no_grad(): base = readouts(M.forward_logits([ids]), M.A)
            for k in READOUT_KEYS: res[f"{side}_base_{k}"] = np.array(float(base[k][0]))
            r = ablate(M, ids, combos, means[f], args.batch)
            for k in READOUT_KEYS: res[f"{side}_{k}"] = r[k].reshape(len(sets), 1).astype(np.float32)
        save_npz(path, dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=items_sha, set_names=names, modes=["all"],
                            n_layers=M.L, n_heads=M.H, means_n_items=means_n[f], layer_matched=True), res)
        if done % 50 == 0 or done == len(todo): print(f"[layer] {tag} {done}/{len(todo)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    print("[layer] finished", flush=True)


if __name__ == "__main__":
    main()
