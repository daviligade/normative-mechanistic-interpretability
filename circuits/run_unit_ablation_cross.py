"""Removal of the neuron lists across frames."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, load_items, model_tag, run_config_append, save_npz, existing_ok, Model, READOUT_KEYS
from run_unit_ablation import build_lists, random_lists
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--units", default="runs/units"); ap.add_argument("--out", default="runs/units_ablation_cross")
    ap.add_argument("--lists-from", default="C", help="the frame whose selected neurons are removed"); ap.add_argument("--frames", nargs="+", default=["A1", "B"]); ap.add_argument("--n-random", type=int, default=10)
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--seed", type=int, default=20261022)
    ap.add_argument("--lists", nargs="+", default=["all", "top"], choices=["all", "top"], help="which lists to remove: the union over layers ('all') and/or the single layer that contributed most ('top')")
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[cross] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); udir = os.path.join(args.units, tag); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); rng = np.random.default_rng(args.seed)
    src = os.path.join(udir, f"sets__{args.lists_from}.json")
    if not os.path.exists(src): print(f"[cross] no unit lists for frame {args.lists_from} in {udir}; nothing to do", flush=True); return
    sets = json.load(open(src)); frames = [f for f in args.frames if os.path.exists(os.path.join(udir, f"stats__{f}.npz"))]
    if not frames: print(f"[cross] no statistics for frames {args.frames} in {udir}; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[cross] model={args.model} device={dev} lists from frame {args.lists_from}, run in {frames}, items={len(items)}", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L
    lists = build_lists(sets, L, tuple(args.lists))
    if not lists: print(f"[cross] frame {args.lists_from} selected no neurons; nothing to ablate", flush=True); return
    run_config_append(out, {"script": "run_unit_ablation_cross.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "n_items": len(items), "frames": frames,
                            "lists_from_frame": args.lists_from, "n_random": args.n_random, "seed": args.seed, "units_dir": udir, "lists": args.lists})
    plan = {}
    def hook(l):
        def pre(m, a_, kw=None):
            if l not in plan: return None
            h = a_[0] if a_ else kw["hidden_states"]; vals, mask = plan[l]; h[:, -1, :] = torch.where(mask, vals.to(h.dtype), h[:, -1, :])
        return pre
    handles = [M.layers[l].mlp.down_proj.register_forward_pre_hook(hook(l)) for l in range(L)]
    try:
        for f in frames:
            st = np.load(os.path.join(udir, f"stats__{f}.npz"), allow_pickle=False); assert str(st["items_sha256"]) == sha, f"{udir}: statistics from another item file"
            mean_act = torch.tensor(st["mean_act"], device=M.device); ctrl = random_lists(lists, st["mean_abs_act"], args.n_random, rng); d = st["mean_act"].shape[1]; Bsz = 1 + args.n_random
            json.dump({"lists_from_frame": args.lists_from, "lists": {k: {str(l): v for l, v in per.items()} for k, per in lists.items()}, "controls": {k: [{str(l): v for l, v in c.items()} for c in cs] for k, cs in ctrl.items()}}, open(os.path.join(out, f"lists__{f}.json"), "w"))
            print(f"[cross] {f}: lists " + ", ".join(f"{k} ({sum(len(v) for v in per.values())} neurons in {len(per)} layer(s))" for k, per in lists.items()), flush=True); t0 = time.time()
            for n, it in enumerate(items):
                path = os.path.join(out, f"{f}__{it['id']}.npz")
                if existing_ok(path, sha): continue
                res = {}; t1 = time.time()
                for s in ("perm", "rest"):
                    ids = encode(M.tok, FRAMES[f](it[f"{s}_stem"])); x = torch.tensor([ids] * Bsz, device=M.device)
                    with torch.no_grad(): lg0 = M.model(input_ids=x[:1]).logits[0, -1, :].float()[None]
                    R0 = readouts(lg0, M.A)
                    for k in READOUT_KEYS: res[f"{s}_clean_{k}"] = float(R0[k][0])
                    for name, per in lists.items():
                        plan.clear()
                        for l in set(per) | {l for c in ctrl[name] for l in c}:
                            mask = torch.zeros(Bsz, d, dtype=torch.bool, device=M.device); vals = mean_act[l][None].expand(Bsz, d)
                            if l in per: mask[0, per[l]] = True
                            for r, c in enumerate(ctrl[name], start=1):
                                if l in c: mask[r, c[l]] = True
                            plan[l] = (vals, mask)
                        with torch.no_grad(): lg = M.model(input_ids=x).logits[:, -1, :].float()
                        plan.clear(); R = readouts(lg, M.A)
                        for k in READOUT_KEYS: res[f"{s}_{name}_{k}"] = R[k].cpu().numpy()
                meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, lists=list(lists), lists_from_frame=args.lists_from, n_random=args.n_random, seconds=round(time.time() - t1, 2))
                save_npz(path, meta, res)
                if (n + 1) % 25 == 0: print(f"[cross] {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in handles: h.remove()
    print("[cross] finished", flush=True)


if __name__ == "__main__":
    main()
