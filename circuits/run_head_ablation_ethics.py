"""Removal of the located heads on ETHICS scenarios."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import READOUT_KEYS, PRIME, Model, pick_device, save_npz, run_config_append, model_tag, readouts, encode, sha
from run_head_ablation import build_sets, ablate

E_FRAMES = {
    "EA0": lambda s: f"{s} This is morally",
    "EA1": lambda s: f"{PRIME}{s} This is morally",
    "EB":  lambda s: f"{PRIME}{s} This is",
    "EQA": lambda s: f"Question: Is the following good or bad?\n{s}\nAnswer: It is",
}


def load_scenarios(path, limit=0):
    D = json.load(open(path)); items = D["items"] if isinstance(D, dict) else D
    assert all(set(("id", "label", "text")) <= set(it) for it in items), "not a scenario file of stimuli/make_ethics_items.py"
    return (items[:limit] if limit else items), sha(path)


@torch.no_grad()
def phase1_means(M, items, frame, path, items_sha):
    if os.path.exists(path):
        z = np.load(path, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta.get("items_sha256") != items_sha or meta.get("n_items") != len(items): sys.exit(f"[ethics] {path} was made from other scenarios; move it away or use another --out / --tag")
        print(f"[phase 1] {frame}: means exist ({path})", flush=True); return torch.tensor(z["mean_all"], device=M.device), torch.tensor(z["mean_final"], device=M.device)
    s_all = torch.zeros(M.L, M.H * M.hd, dtype=torch.float64); s_fin = torch.zeros_like(s_all); n_all = 0; n_fin = 0; cache = {}
    hooks = [M.layers[l].self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: cache.__setitem__(l, a[0].detach())) for l in range(M.L)]
    t0 = time.time()
    try:
        for k, it in enumerate(items):
            ids = encode(M.tok, E_FRAMES[frame](it["text"])); M.forward_logits([ids])
            for l in range(M.L):
                z = cache[l][0].float().cpu().double(); s_all[l] += z[1:].sum(0); s_fin[l] += z[-1]
            n_all += len(ids) - 1; n_fin += 1
            if (k + 1) % 100 == 0: print(f"[phase 1] {frame} {k + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in hooks: h.remove()
    mean_all = (s_all / n_all).float(); mean_fin = (s_fin / n_fin).float()
    save_npz(path, {"frame": frame, "items_sha256": items_sha, "n_items": len(items), "n_prompts": n_fin, "n_positions_pooled": n_all, "note": "BOS excluded from mean_all"},
             {"mean_all": mean_all.numpy(), "mean_final": mean_fin.numpy()})
    return mean_all.to(M.device), mean_fin.to(M.device)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", default="stimuli/items_ethics_cm.json"); ap.add_argument("--out", default="runs/ethics")
    ap.add_argument("--frames", nargs="+", default=["EA1", "EB", "EQA", "EA0"], choices=list(E_FRAMES)); ap.add_argument("--device", default="auto")
    ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--tag", default=None); ap.add_argument("--n-random", type=int, default=20)
    ap.add_argument("--sizes", nargs="+", type=int, default=[10], help="sizes of the random control sets"); ap.add_argument("--modes", nargs="+", default=["all"], choices=["all", "final"])
    ap.add_argument("--save-every", type=int, default=25); ap.add_argument("--sets-file", default=None, help="software tests only: a head-set file with the layout of located/heads.json")
    args = ap.parse_args()
    items, items_sha = load_scenarios(args.items, args.limit); tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag)

    def finished(f):
        p = os.path.join(out, f"{f}.npz")
        if not os.path.exists(p): return False
        meta = json.loads(str(np.load(p, allow_pickle=False)["__meta__"]))
        if meta.get("items_sha256") != items_sha or meta.get("n_items") != len(items): sys.exit(f"[ethics] {p} was made from other scenarios; move it away or use another --out / --tag")
        return True

    if all(finished(f) for f in args.frames): print(f"[ethics] {tag}: every frame is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[ethics] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    M = Model(args.model, dev, args.dtype); print(f"[ethics] layers={M.L} heads={M.H} head_dim={M.hd}; {len(items)} scenarios; frames {args.frames}", flush=True)
    names, sets = build_sets(tag, M, args.sets_file, args.n_random, tuple(args.sizes)); os.makedirs(out, exist_ok=True); sp = os.path.join(out, "sets.json")
    if os.path.exists(sp):
        old = json.load(open(sp))
        if old["names"] != names or [[list(h) for h in s] for s in sets] != old["sets"]: sys.exit(f"[ethics] {sp} holds other sets (another --n-random / --sizes?); use another --out / --tag")
    else: json.dump({"names": names, "sets": [[list(h) for h in s] for s in sets], "sets_file": args.sets_file or "located/heads.json", "n_random": args.n_random, "sizes": args.sizes}, open(sp, "w"))
    run_config_append(out, {"script": "run_head_ablation_ethics.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": items_sha, "frames": args.frames,
                            "modes": args.modes, "n_items": len(items), "n_sets": len(names), "n_random": args.n_random, "sizes": args.sizes, "sets_file": args.sets_file or "located/heads.json", "n_layers": M.L, "n_heads": M.H})
    combos = [(s, mode) for s in sets for mode in args.modes]; n = len(items)
    for f in args.frames:
        if finished(f): print(f"[ethics] {tag} {f}: already there", flush=True); continue
        ma, mf = phase1_means(M, items, f, os.path.join(out, f"means__{f}.npz"), items_sha); means = {"all": ma, "final": mf}
        base = {k: np.full(n, np.nan, np.float32) for k in READOUT_KEYS}; abl = {k: np.full((n, len(sets), len(args.modes)), np.nan, np.float32) for k in READOUT_KEYS}; ntok = np.zeros(n, np.int32); start = 0
        part = os.path.join(out, f"{f}.partial.npz")
        if os.path.exists(part):
            z = np.load(part, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
            if meta.get("items_sha256") == items_sha and meta.get("n_items") == n and meta.get("set_names") == names and meta.get("modes") == args.modes:
                start = int(meta["n_done"]); ntok = z["n_tok"].copy()
                for k in READOUT_KEYS: base[k] = z[f"base_{k}"].copy(); abl[k] = z[f"abl_{k}"].copy()
                print(f"[ethics] {tag} {f}: resuming after {start} scenarios", flush=True)

        def save(path, n_done):
            save_npz(path, dict(frame=f, model=args.model, items_sha256=items_sha, n_items=n, n_done=n_done, ids=[it["id"] for it in items], labels=[int(it["label"]) for it in items], set_names=names, modes=args.modes,
                                n_layers=M.L, n_heads=M.H), dict({f"base_{k}": base[k] for k in READOUT_KEYS}, **{f"abl_{k}": abl[k] for k in READOUT_KEYS}, n_tok=ntok))

        t0 = time.time()
        for i in range(start, n):
            ids = encode(M.tok, E_FRAMES[f](items[i]["text"])); ntok[i] = len(ids)
            with torch.no_grad(): b = readouts(M.forward_logits([ids]), M.A)
            r = ablate(M, ids, combos, means, args.batch)
            for k in READOUT_KEYS:
                base[k][i] = float(b[k][0]); abl[k][i] = r[k].reshape(len(sets), len(args.modes))
            if (i + 1) % args.save_every == 0 or i + 1 == n:
                if i + 1 < n: save(part, i + 1)
                done = slice(0, i + 1); lab = np.array([int(it["label"]) for it in items[:i + 1]])
                sep = float(base["S"][done][lab == 0].mean() - base["S"][done][lab == 1].mean()) if (lab == 0).any() and (lab == 1).any() else float("nan")
                print(f"[{i + 1}/{n}] {f} mean answer-word mass so far={float(base['mass'][done].mean()):.2f}  S acceptable minus unacceptable so far={sep:+.3f}  elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
        save(os.path.join(out, f"{f}.npz"), n)
        if os.path.exists(part):
            try: os.remove(part)
            except OSError: os.replace(part, os.path.join(out, f"{f}.partial.done.npz"))
    print("[ethics] finished", flush=True)


if __name__ == "__main__":
    main()
