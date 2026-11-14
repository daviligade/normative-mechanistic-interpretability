"""Difference-of-means steering at the final position."""
import argparse, copy, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, load_items, model_tag, run_config_append, save_npz, existing_ok, Model, READOUT_KEYS, ROOT
from run_category_frame import PRESETS as CAT_PRESETS, CATEGORY_WORDS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids, first_token_id

NORM_KINDS = ("prudential", "etiquette", "aesthetic", "epistemic")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/steering")
    ap.add_argument("--frames", nargs="+", default=["A1", "B", "C"]); ap.add_argument("--cat-preset", default="fewshot", choices=list(CAT_PRESETS)); ap.add_argument("--layers", nargs="+", type=int, default=None, help="default: quarter, half, three quarters of depth")
    ap.add_argument("--directions", nargs="+", default=["stance", "category"], choices=["stance", "category"]); ap.add_argument("--scales", nargs="+", type=float, default=[-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]); ap.add_argument("--n-random", type=int, default=5)
    ap.add_argument("--split-meta", default=os.path.join(ROOT, "results", "features_h6split", "split_meta.json")); ap.add_argument("--seed", type=int, default=20261022)
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    ap.add_argument("--max-rows", type=int, default=0, help="rows per steered pass, in whole direction blocks (default 72; 36 above 10B parameters)")
    ap.add_argument("--no-prefix-cache", action="store_true", help="rerun the whole prompt for every steered row (the original computation; for checks)")
    ap.add_argument("--check-tol", type=float, default=1e-3, help="largest difference allowed between the unsteered cached row and the full forward pass (probabilities; logit differences x10)")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[steering] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); dev = pick_device(args.device); rng = np.random.default_rng(args.seed)
    if os.path.exists(args.split_meta): meta = json.load(open(args.split_meta)); HA, HB = set(meta["half_A"]), set(meta["half_B"]); split_src = args.split_meta
    else:
        ids = [it["id"] for it in items if it["category"] in ("moral", "norm")]; perm = rng.permutation(len(ids)); HA = {ids[i] for i in perm[: len(ids) // 2]}; HB = set(ids) - HA; split_src = f"drawn here, seed {args.seed}"
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L; d = M.d
    layers = args.layers or sorted({max(0, round(L * q) - 1) for q in (0.25, 0.5, 0.75)})
    cat = np.array([it["category"] for it in items]); idl = [it["id"] for it in items]; inA = np.array([i in HA for i in idl]); inB = np.array([i in HB for i in idl]); mo, no, de = cat == "moral", cat == "norm", cat == "descr"
    cat_ids = {c: [first_token_id(M.tok, w, False) for w in ws] for c, ws in CATEGORY_WORDS.items()}; all_cat = sorted({i for v in cat_ids.values() for i in v})
    def pmoral(lg):
        pr = torch.softmax(lg.float(), -1); return pr[:, cat_ids["moral"]].sum(-1) / pr[:, all_cat].sum(-1)
    prompt_of = lambda f, stem: CAT_PRESETS[args.cat_preset](stem) if f == "C" else FRAMES[f](stem)

    rec = {}; clean = {}
    def hook_rec(l):
        def f(m, a_, o): rec[l] = (o[0] if isinstance(o, tuple) else o)[0, -1, :].detach().float().cpu()
        return f
    H = {}
    hs = [M.layers[l].register_forward_hook(hook_rec(l)) for l in layers]
    try:
        for f in args.frames:
            H[f] = {s: torch.zeros(len(items), len(layers), d) for s in ("perm", "rest")}; t0 = time.time()
            with torch.no_grad():
                for n, it in enumerate(items):
                    for s in ("perm", "rest"):
                        lg = M.model(input_ids=torch.tensor([encode(M.tok, prompt_of(f, it[f"{s}_stem"]))], device=M.device)).logits[:, -1, :].float(); H[f][s][n] = torch.stack([rec[l] for l in layers])
                        R0 = readouts(lg, M.A); clean[(f, it["id"], s)] = {k: float(R0[k][0]) for k in READOUT_KEYS}
                        if f == "C": clean[(f, it["id"], s)]["pmoral"] = float(pmoral(lg)[0])
            print(f"[steering] residuals recorded for frame {f} in {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in hs: h.remove()

    dirs = {}; info = {"frames": {}, "halves_from": split_src, "layers": layers}
    for f in args.frames:
        info["frames"][f] = {}
        for li, l in enumerate(layers):
            P, R = H[f]["perm"][:, li, :], H[f]["rest"][:, li, :]; D = P - R; mean_h = 0.5 * (P + R)
            for half, Hm in (("A", inA), ("B", inB)):
                sel_m, sel_n = torch.tensor(Hm & mo), torch.tensor(Hm & no)
                v_m, v_n = D[sel_m].mean(0), D[sel_n].mean(0); v_norm = D[sel_m | sel_n].mean(0); v_d = D[torch.tensor(de)].mean(0) if de.any() else torch.zeros(d)
                c_vec = mean_h[sel_m].mean(0) - mean_h[sel_n].mean(0)
                dirs[(f, l, half, "stance")] = v_norm; dirs[(f, l, half, "category")] = c_vec
                cos = lambda x, y: float(torch.nn.functional.cosine_similarity(x[None], y[None])[0]) if x.norm() > 0 and y.norm() > 0 else None
                info["frames"][f][f"L{l}_{half}"] = dict(stance_norm=float(v_norm.norm()), category_norm=float(c_vec.norm()), residual_norm_median=float(mean_h.norm(dim=1).median()),
                                                      cos_stance_moral_norm=cos(v_m, v_n), cos_stance_norm_descr=cos(v_n, v_d), cos_stance_moral_descr=cos(v_m, v_d), cos_stance_category=cos(v_norm, c_vec))
    json.dump(info, open(os.path.join(out, "directions_info.json"), "w"), indent=1)
    print("[steering] cosine(moral stance, norm stance) by layer: " + "; ".join(f"{f} L{l}: {info['frames'][f][f'L{l}_A']['cos_stance_moral_norm']:.2f}" for f in args.frames for l in layers), flush=True)
    S = len(args.scales); B = S * (1 + args.n_random); use_cache = not args.no_prefix_cache
    n_par = sum(p.numel() for p in M.model.parameters()); max_rows = args.max_rows or (36 if n_par > 10e9 else 72); per_pass = max(1, max_rows // B)
    run_config_append(out, {"script": "run_steering.py", "model": args.model, "device": dev, "dtype": args.dtype, "items_file": args.items, "items_sha256": sha, "n_items": len(items), "frames": args.frames, "layers": layers, "directions": args.directions,
                            "scales": args.scales, "n_random": args.n_random, "seed": args.seed, "split_meta": split_src, "cat_preset": args.cat_preset,
                            "prefix_cache": use_cache, "direction_blocks_per_pass": per_pass if use_cache else 1, "check_tol": args.check_tol})
    print(f"[steering] steered passes: {'prompt prefix computed once, one token per steered row' if use_cache else 'the whole prompt for every row'}; "
          f"{per_pass if use_cache else 1} block(s) of {B} rows per pass", flush=True)

    plan = {}
    def hook_add(l):
        def f(m, a_, o):
            if l not in plan: return None
            h = o[0] if isinstance(o, tuple) else o; h2 = h.clone(); h2[:, -1, :] = h[:, -1, :] + plan[l].to(h.dtype); return (h2,) + tuple(o[1:]) if isinstance(o, tuple) else h2
        return f

    def steer(ids, blocks, f, cached):
        got = {}; ref = None; k = per_pass if cached else 1; plan.clear()
        if cached:
            with torch.no_grad(): base = M.model(input_ids=torch.tensor([ids[:-1]], device=M.device), use_cache=True).past_key_values
            last = torch.tensor([ids[-1:]], device=M.device)
        for b0 in range(0, len(blocks), k):
            chunk = blocks[b0: b0 + k]; off = 1 if (cached and b0 == 0) else 0; R = off + len(chunk) * B; add = {}
            for j, (l, key, rows) in enumerate(chunk):
                if l not in add: add[l] = torch.zeros(R, d)
                add[l][off + j * B: off + (j + 1) * B] = rows
            plan.clear(); plan.update({l: v.to(M.device) for l, v in add.items()})
            with torch.no_grad():
                if cached:
                    cache = copy.deepcopy(base); cache.batch_repeat_interleave(R)
                    lg = M.model(input_ids=last.repeat(R, 1), past_key_values=cache, use_cache=True).logits[:, -1, :].float(); del cache
                else:
                    lg = M.model(input_ids=torch.tensor([ids] * R, device=M.device)).logits[:, -1, :].float()
            plan.clear(); Rr = readouts(lg, M.A); pm = pmoral(lg) if f == "C" else None
            if off:
                ref = {kk: float(Rr[kk][0]) for kk in READOUT_KEYS}
                if pm is not None: ref["pmoral"] = float(pm[0])
            for j, (l, key, rows) in enumerate(chunk):
                sl = slice(off + j * B, off + (j + 1) * B); got[f"{key}_S"] = Rr["S"][sl].cpu().numpy().reshape(S, 1 + args.n_random)
                if pm is not None: got[f"{key}_pmoral"] = pm[sl].cpu().numpy().reshape(S, 1 + args.n_random)
        return got, ref

    hs = [M.layers[l].register_forward_hook(hook_add(l)) for l in layers]; n_full = 0; worst = 0.0
    try:
        for f in args.frames:
            t0 = time.time()
            for n, it in enumerate(items):
                path = os.path.join(out, f"{f}__{it['id']}.npz")
                if existing_ok(path, sha): continue
                halves = ["A", "B"] if it["category"] == "descr" else (["B"] if it["id"] in HA else ["A"])
                res = {}; check = {}; recomputed = {}
                for s in ("perm", "rest"):
                    ids = encode(M.tok, prompt_of(f, it[f"{s}_stem"])); c0 = clean[(f, it["id"], s)]
                    for k in READOUT_KEYS: res[f"{s}_clean_{k}"] = c0[k]
                    if f == "C": res[f"{s}_clean_pmoral"] = c0["pmoral"]
                    blocks = []
                    for l in layers:
                        for name in args.directions:
                            for half in halves:
                                v = dirs[(f, l, half, name)]; nv = float(v.norm()) + 1e-12
                                rows = []
                                for sc in args.scales:
                                    rows.append(sc * v)
                                    for r in range(args.n_random):
                                        g = torch.tensor(rng.standard_normal(d), dtype=torch.float32); rows.append(sc * g / g.norm() * nv)
                                blocks.append((l, f"{s}_L{l}_{name}_{half}", torch.stack(rows)))
                    got, ref = steer(ids, blocks, f, use_cache)
                    if use_cache:
                        dv = max([abs(ref[k] - c0[k]) for k in ("S", "mass", "S_hist")] + [abs(ref[k] - c0[k]) / 10 for k in ("LD", "LD_gb")] + ([abs(ref["pmoral"] - c0["pmoral"])] if f == "C" else []))
                        check[s] = dv; worst = max(worst, dv) if dv == dv else float("inf")
                        if not dv <= args.check_tol:
                            n_full += 1; recomputed[s] = True; got, _ = steer(ids, blocks, f, False)
                            print(f"[steering] WARNING {f} {it['id']} {s}: the cached prefix differs from the full forward pass by {dv:.2e}; recomputed with the whole prompt per row", flush=True)
                    res.update(got)
                meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, layers=layers, directions=args.directions, scales=args.scales, n_random=args.n_random, halves_used=halves,
                            prefix_cache=use_cache, cache_check=check, recomputed_full=recomputed)
                save_npz(path, meta, res)
                if (n + 1) % 25 == 0: print(f"[steering] {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min" + (f"  (largest cache deviation so far {worst:.1e})" if use_cache else ""), flush=True)
    finally:
        for h in hs: h.remove()
    print(f"[steering] finished" + (f"; largest deviation of the cached prefix from the full forward pass {worst:.1e}; prompts recomputed in full: {n_full}" if use_cache else ""), flush=True)


if __name__ == "__main__":
    main()
