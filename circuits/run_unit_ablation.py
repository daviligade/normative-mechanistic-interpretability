"""Removal of the neuron lists on held-out pairs."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, load_items, model_tag, run_config_append, save_npz, existing_ok, Model, READOUT_KEYS, ROOT
from run_category_frame import PRESETS as CAT_PRESETS, CATEGORY_WORDS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids, first_token_id, RUN_FILE
import hashlib


def build_lists(sets, L, kinds=("all", "top")):
    out = {}
    for h in ("selA", "selB"):
        per = {int(l): v for l, v in sets["sets"][h].items() if v}
        if not per: continue
        if "all" in kinds: out[f"{h}_all"] = per
        if "top" in kinds: top = max(per, key=lambda l: len(per[l])); out[f"{h}_top"] = {top: per[top]}
    return out


def random_lists(lists, mean_abs, n_random, rng):
    out = {}
    for name, per in lists.items():
        cs = []
        for r in range(n_random):
            chosen = {}
            for l, idx in per.items():
                act = mean_abs[l]; order = np.argsort(act, kind="stable"); rank = np.empty_like(order); rank[order] = np.arange(len(order)); used = set(idx); picks = []
                for i in sorted(idx, key=lambda j: -act[j]):
                    cand, step = [], 1
                    while len(cand) < 20 and (rank[i] - step >= 0 or rank[i] + step < len(order)):
                        for pos in (rank[i] + step, rank[i] - step):
                            if 0 <= pos < len(order) and int(order[pos]) not in used: cand.append(int(order[pos]))
                        step += 1
                    c = int(rng.choice(cand[:20])); picks.append(c); used.add(c)
                chosen[l] = picks
            cs.append(chosen)
        out[name] = cs
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--units", default="runs/units"); ap.add_argument("--out", default="runs/units_ablation")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"]); ap.add_argument("--cat-preset", default="zeroshot", choices=list(CAT_PRESETS)); ap.add_argument("--n-random", type=int, default=10)
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--seed", type=int, default=20261021)
    ap.add_argument("--lists", nargs="+", default=["all", "top"], choices=["all", "top"], help="which lists to ablate: the union over layers ('all') and/or the single layer that contributed most ('top')")
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    ap.add_argument("--lists-from-other-items", action="store_true", help="follow-up item sets: unit lists and mean activations from the statistics of the located run file, read on --items")
    ap.add_argument("--units-items-file", default=None, help="tests only: the item file the unit statistics must come from under --lists-from-other-items (default: the located run file)")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[run_unit_ablation] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); udir = os.path.join(args.units, tag); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); rng = np.random.default_rng(args.seed)
    frames = [f for f in args.frames if os.path.exists(os.path.join(udir, f"sets__{f}.json"))]
    if len(frames) < len(args.frames): print(f"[run_unit_ablation] no unit lists for frames {sorted(set(args.frames) - set(frames))} in {udir}; skipping them", flush=True)
    if not frames: return
    dev = pick_device(args.device); print(f"[run_unit_ablation] model={args.model} device={dev} frames={frames} items={len(items)} random lists={args.n_random}", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L
    cat_ids = {c: [first_token_id(M.tok, w, False) for w in ws] for c, ws in CATEGORY_WORDS.items()}
    run_config_append(out, {"script": "run_unit_ablation.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "n_items": len(items), "frames": frames,
                            "n_random": args.n_random, "seed": args.seed, "cat_preset": args.cat_preset, "units_dir": udir, "lists": args.lists})
    plan = {}
    def hook(l):
        def pre(m, a_, kw=None):
            if l not in plan: return None
            h = a_[0] if a_ else kw["hidden_states"]; vals, mask = plan[l]
            h[:, -1, :] = torch.where(mask, vals.to(h.dtype), h[:, -1, :])
        return pre
    handles = [M.layers[l].mlp.down_proj.register_forward_pre_hook(hook(l)) for l in range(L)]
    try:
        for f in frames:
            sets = json.load(open(os.path.join(udir, f"sets__{f}.json"))); st = np.load(os.path.join(udir, f"stats__{f}.npz"), allow_pickle=False)
            units_sha = str(st["items_sha256"])
            if units_sha != sha:
                if not args.lists_from_other_items: sys.exit(f"[run_unit_ablation] {udir}: the unit statistics were made from another item file (sha256 {units_sha[:16]}...); a follow-up item set needs --lists-from-other-items")
                ref = args.units_items_file or os.path.join(ROOT, RUN_FILE); ref_sha = hashlib.sha256(open(ref, "rb").read()).hexdigest()
                if units_sha != ref_sha: sys.exit(f"[run_unit_ablation] {udir}: the unit statistics come from neither --items nor {ref}; refusing")
                print(f"[run_unit_ablation] {f}: lists and mean activations from the statistics of {os.path.basename(ref)} (sha256 {units_sha[:16]}...), read on {args.items}", flush=True)
            mean_act = torch.tensor(st["mean_act"], device=M.device); lists = build_lists(sets, L, tuple(args.lists))
            if not lists: print(f"[run_unit_ablation] {f}: no selected neurons; nothing to ablate", flush=True); continue
            ctrl = random_lists(lists, st["mean_abs_act"], args.n_random, rng); json.dump({"lists": {k: {str(l): v for l, v in per.items()} for k, per in lists.items()}, "controls": {k: [{str(l): v for l, v in c.items()} for c in cs] for k, cs in ctrl.items()}},
                                                                                           open(os.path.join(out, f"lists__{f}.json"), "w"))
            print(f"[run_unit_ablation] {f}: lists " + ", ".join(f"{k} ({sum(len(v) for v in per.values())} neurons in {len(per)} layer(s))" for k, per in lists.items()), flush=True)
            prompt_of = (lambda stem: CAT_PRESETS[args.cat_preset](stem)) if f == "C" else FRAMES[f]; d = st["mean_act"].shape[1]; Bsz = 1 + args.n_random; t0 = time.time()
            for n, it in enumerate(items):
                path = os.path.join(out, f"{f}__{it['id']}.npz")
                if existing_ok(path, sha): continue
                res = {}; t1 = time.time()
                for s in ("perm", "rest"):
                    ids = encode(M.tok, prompt_of(it[f"{s}_stem"])); x = torch.tensor([ids] * Bsz, device=M.device)
                    with torch.no_grad():
                        lg0 = M.model(input_ids=x[:1]).logits[0, -1, :].float()[None]
                    for name, per in lists.items():
                        plan.clear()
                        for l in set(per) | {l for c in ctrl[name] for l in c}:
                            mask = torch.zeros(Bsz, d, dtype=torch.bool, device=M.device); vals = mean_act[l][None].expand(Bsz, d)
                            if l in per: mask[0, per[l]] = True
                            for r, c in enumerate(ctrl[name], start=1):
                                if l in c: mask[r, c[l]] = True
                            plan[l] = (vals, mask)
                        with torch.no_grad(): lg = M.model(input_ids=x).logits[:, -1, :].float()
                        plan.clear()
                        if f == "C":
                            pr = torch.softmax(lg, -1); ps = {c: pr[:, ids_].sum(-1) for c, ids_ in cat_ids.items()}; tot = sum(ps.values())
                            res[f"{s}_{name}_pmoral"] = (ps["moral"] / tot).cpu().numpy(); res[f"{s}_{name}_covered"] = tot.cpu().numpy()
                        else:
                            R = readouts(lg, M.A)
                            for k in READOUT_KEYS: res[f"{s}_{name}_{k}"] = R[k].cpu().numpy()
                    if f == "C":
                        pr0 = torch.softmax(lg0, -1); ps0 = {c: pr0[:, ids_].sum(-1) for c, ids_ in cat_ids.items()}; tot0 = sum(ps0.values()); res[f"{s}_clean_pmoral"] = float((ps0["moral"] / tot0)[0]); res[f"{s}_clean_covered"] = float(tot0[0])
                    else:
                        R0 = readouts(lg0, M.A)
                        for k in READOUT_KEYS: res[f"{s}_clean_{k}"] = float(R0[k][0])
                meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, units_items_sha256=units_sha, lists=list(lists), n_random=args.n_random, seconds=round(time.time() - t1, 2))
                save_npz(path, meta, res)
                if (n + 1) % 25 == 0: print(f"[run_unit_ablation] {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in handles: h.remove()
    print("[run_unit_ablation] finished", flush=True)


if __name__ == "__main__":
    main()
