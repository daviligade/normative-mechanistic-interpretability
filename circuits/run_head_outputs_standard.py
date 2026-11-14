"""What the located heads and random heads write, and the hidden state, at the final position."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from circ_common import FRAMES, Model, pick_device, load_items, save_npz, run_config_append, model_tag, encode, sha
from run_head_ablation import build_sets
try:
    import extra_frames; extra_frames.register()
except Exception as e:
    print(f"[standard] extra frames not registered ({e})", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", default="stimuli/items_run_v1.json"); ap.add_argument("--accepted-only", action="store_true")
    ap.add_argument("--out", default="runs/head_outputs_standard"); ap.add_argument("--frames", nargs="+", default=["A1", "B"])
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"])
    ap.add_argument("--n-random", type=int, default=20); ap.add_argument("--limit", type=int, default=0); ap.add_argument("--tag", default=None)
    ap.add_argument("--sets-file", default=None, help="software tests only: a head-set file with the layout of located/heads.json")
    ap.add_argument("--any-items", action="store_true", help="software tests only")
    args = ap.parse_args()
    for f in args.frames:
        if f not in FRAMES: sys.exit(f"[standard] unknown frame {f}; known: {sorted(FRAMES)}")
    items, items_sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        from common import accepted_ids
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    todo = [f for f in args.frames if not os.path.exists(os.path.join(out, f"{f}.npz"))]
    if not todo: print(f"[standard] {tag}: every frame is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[standard] model={args.model} device={dev} dtype={args.dtype}; {len(items)} pairs; frames {todo}", flush=True)
    M = Model(args.model, dev, args.dtype)
    names, sets = build_sets(tag, M, args.sets_file, args.n_random, (10,))
    located = sets[names.index("located")]; R = [sets[i] for i, n in enumerate(names) if n.startswith("random10_")]
    assert len(located) == 10 and len(R) == args.n_random and all(len(s) == 10 for s in R)
    run_config_append(out, {"script": "run_head_outputs_standard.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": items_sha,
                            "accepted_only": args.accepted_only, "n_pairs": len(items), "frames": todo, "located": [list(h) for h in located], "random10": [[list(h) for h in s] for s in R],
                            "n_layers": M.L, "n_heads": M.H, "head_dim": M.hd, "d_model": M.d})
    cache = {}
    hooks = [M.layers[l].self_attn.o_proj.register_forward_pre_hook(lambda m, a, l=l: cache.__setitem__(l, a[0][0, -1].detach())) for l in range(M.L)]
    WO = {}
    for s in [located] + R:
        for (l, h) in s:
            if l not in WO: WO[l] = M.layers[l].self_attn.o_proj.weight.float().view(M.d, M.H, M.hd)

    def heads_z_and_write(heads):
        z = torch.stack([cache[l].float().view(M.H, M.hd)[h] for (l, h) in heads])
        w = sum(WO[l][:, h, :] @ cache[l].float().view(M.H, M.hd)[h] for (l, h) in heads)
        return z, w
    try:
        for f in todo:
            n = 2 * len(items); zD = np.zeros((n, 10, M.hd), np.float32); wD = np.zeros((n, M.d), np.float32)
            zR = np.zeros((n, len(R), 10, M.hd), np.float16); wR = np.zeros((n, len(R), M.d), np.float16); hs = np.zeros((n, M.L + 1, M.d), np.float16)
            rows = []; t0 = time.time()
            for i, it in enumerate(items):
                for j, side in enumerate(("perm", "rest")):
                    k = 2 * i + j; ids = encode(M.tok, FRAMES[f](it[f"{side}_stem"]))
                    with torch.no_grad():
                        o = M.model.model(input_ids=torch.tensor([ids], device=M.device), output_hidden_states=True)
                        z, w = heads_z_and_write(located); zD[k] = z.cpu().numpy(); wD[k] = w.cpu().numpy()
                        for r, s in enumerate(R):
                            z, w = heads_z_and_write(s); zR[k, r] = z.cpu().numpy().astype(np.float16); wR[k, r] = w.cpu().numpy().astype(np.float16)
                        hs[k] = torch.stack([x[0, -1] for x in o.hidden_states]).float().cpu().numpy().astype(np.float16)
                    rows.append({"id": it["id"], "side": side, "category": it["category"], "subtype": it.get("subtype", ""), "n_tok": len(ids)})
                if (i + 1) % 50 == 0 or i + 1 == len(items): print(f"[standard] {tag} {f} {i + 1}/{len(items)} pairs  {(time.time() - t0) / 60:.1f} min", flush=True)
            if not np.isfinite(wD).all() or not np.isfinite(hs.astype(np.float32)).all(): print(f"[standard] warning: non-finite values in {tag} {f}", flush=True)
            save_npz(os.path.join(out, f"{f}.npz"), {"frame": f, "model": args.model, "items_sha256": items_sha, "rows": rows, "located": [list(h) for h in located],
                                                    "random10": [[list(h) for h in s] for s in R], "note": "final position; h[0] is the embedding output, h[l] the output of layer l"},
                     {"zD10": zD, "wD10": wD, "zR": zR, "wR": wR, "h": hs})
            print(f"[standard] {tag} {f}: saved", flush=True)
    finally:
        for hk in hooks: hk.remove()
    print("[standard] finished", flush=True)


if __name__ == "__main__":
    main()
