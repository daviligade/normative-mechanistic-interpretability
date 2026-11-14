"""Removal and exchange of Jacobian-lens directions at the final position."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, load_items, model_tag, run_config_append, save_npz, existing_ok, Model, READOUT_KEYS
from run_category_frame import CATEGORY_WORDS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids, first_token_id

NORM_KINDS = ("prudential", "etiquette", "aesthetic", "epistemic"); SWAP_NAME = {"safety": "prudential", "manners": "etiquette", "taste": "aesthetic", "evidence": "epistemic"}


def unit(v): return v / (v.norm() + 1e-12)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--lens", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/jlens_swap")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"]); ap.add_argument("--layers", nargs="+", type=int, default=None, help="default: quarter, half and three quarters of depth")
    ap.add_argument("--directions", nargs="+", default=["category", "stance"], choices=["category", "stance"]); ap.add_argument("--interventions", nargs="+", default=["project", "flip", "swap"], choices=["project", "flip", "swap"])
    ap.add_argument("--swap-with", default="safety", choices=list(SWAP_NAME)); ap.add_argument("--n-random", type=int, default=10); ap.add_argument("--seed", type=int, default=20261022)
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[jlens_swap] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); dev = pick_device(args.device); rng = np.random.default_rng(args.seed)
    Lz = torch.load(args.lens, map_location="cpu", weights_only=True); J = {int(l): v.float() for l, v in Lz["J"].items()}
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L
    layers = args.layers or sorted({max(0, round(L * q) - 1) for q in (0.25, 0.5, 0.75)}); layers = [l for l in layers if l in J]
    if not layers: sys.exit(f"[jlens_swap] none of the requested layers is in the lens ({sorted(J)[0]}..{sorted(J)[-1]})")

    W = M.W_U.float(); nw = M.norm_w
    u_set = {c: W[[first_token_id(M.tok, w, False) for w in ws]].mean(0) for c, ws in CATEGORY_WORDS.items()}
    u = {"category": u_set["moral"] - torch.stack([u_set[k] for k in NORM_KINDS]).mean(0), "stance": M.u_dir.float(), "swap_other": u_set[SWAP_NAME[args.swap_with]] - torch.stack([u_set[k] for k in ("moral",) + tuple(k2 for k2 in NORM_KINDS if k2 != SWAP_NAME[args.swap_with])]).mean(0)}
    specials = set(getattr(M.tok, "all_special_ids", []) or []); vocab_ok = np.array([i for i in range(W.shape[0]) if i not in specials and i < M.tok.vocab_size])
    rand_pairs = [tuple(rng.choice(vocab_ok, 2, replace=False)) for _ in range(args.n_random)]
    dirs = {}
    for l in layers:
        Jl = J[l].to(M.device); T = lambda vec: unit(Jl.T @ (vec.to(M.device) * nw))
        dirs[(l, "category")] = T(u["category"]); dirs[(l, "stance")] = T(u["stance"]); dirs[(l, "swap_other")] = T(u["swap_other"])
        for r, (w1, w2) in enumerate(rand_pairs): dirs[(l, f"rand{r}")] = T(W[int(w1)] - W[int(w2)])
    print(f"[jlens_swap] model={args.model} device={dev} layers={layers} directions={args.directions} interventions={args.interventions} swap with {args.swap_with}; controls={args.n_random}; items={len(items)}", flush=True)
    run_config_append(out, {"script": "run_jlens_swap.py", "model": args.model, "lens": args.lens, "device": dev, "dtype": args.dtype, "items_file": args.items, "items_sha256": sha, "n_items": len(items), "frames": args.frames, "layers": layers,
                            "directions": args.directions, "interventions": args.interventions, "swap_with": args.swap_with, "n_random": args.n_random, "seed": args.seed, "random_token_pairs": [[int(a_), int(b_)] for a_, b_ in rand_pairs]})
    plan = {}
    def hook(l):
        def f(m, a_, out):
            if l not in plan: return None
            h = out[0] if isinstance(out, tuple) else out; h2 = h.clone(); h2[:, -1, :] = plan[l](h[:, -1, :].float()).to(h.dtype)
            return (h2,) + tuple(out[1:]) if isinstance(out, tuple) else h2
        return f
    handles = [M.layers[l].register_forward_hook(hook(l)) for l in layers]
    B = 1 + args.n_random
    def make(l, name, kind):
        V = torch.stack([dirs[(l, name)]] + [dirs[(l, f"rand{r}")] for r in range(args.n_random)])
        if kind in ("project", "flip"):
            k = 1.0 if kind == "project" else 2.0
            return lambda h: h - k * (h * V).sum(1, keepdim=True) * V

        V2 = torch.stack([dirs[(l, "swap_other")]] + [dirs[(l, f"rand{(r + 1) % args.n_random}")] for r in range(args.n_random)])
        def sw(h):
            outh = h.clone()
            for b in range(h.shape[0]):
                Bm = torch.stack([V[b], V2[b]], 1); c = torch.linalg.pinv(Bm) @ h[b]; outh[b] = h[b] + (c[1] - c[0]) * V[b] + (c[0] - c[1]) * V2[b]
            return outh
        return sw
    try:
        for f in args.frames:
            t0 = time.time()
            for n, it in enumerate(items):
                path = os.path.join(out, f"{f}__{it['id']}.npz")
                if existing_ok(path, sha): continue
                res = {}
                for s in ("perm", "rest"):
                    ids = encode(M.tok, FRAMES[f](it[f"{s}_stem"])); x = torch.tensor([ids] * B, device=M.device)
                    plan.clear()
                    with torch.no_grad(): R0 = readouts(M.model(input_ids=x[:1]).logits[:, -1, :].float(), M.A)
                    for k in READOUT_KEYS: res[f"{s}_clean_{k}"] = float(R0[k][0])
                    for l in layers:
                        for name in args.directions:
                            for kind in args.interventions:
                                if kind == "swap" and name != "category": continue
                                plan.clear(); plan[l] = make(l, name, kind)
                                with torch.no_grad(): R = readouts(M.model(input_ids=x).logits[:, -1, :].float(), M.A)
                                plan.clear()
                                for k in READOUT_KEYS: res[f"{s}_L{l}_{name}_{kind}_{k}"] = R[k].cpu().numpy()
                meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, layers=layers, directions=args.directions, interventions=args.interventions, n_random=args.n_random, swap_with=args.swap_with)
                save_npz(path, meta, res)
                if (n + 1) % 25 == 0: print(f"[jlens_swap] {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in handles: h.remove()
    print("[jlens_swap] finished", flush=True)


if __name__ == "__main__":
    main()
