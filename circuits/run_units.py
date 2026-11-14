"""MLP neurons that separate moral from normative pairs."""
import argparse, json, math, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, pick_device, load_items, model_tag, run_config_append, Model, first
from run_category_frame import PRESETS as CAT_PRESETS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SPLITS = [(("prudential", "etiquette"), ("aesthetic", "epistemic")), (("prudential", "aesthetic"), ("etiquette", "epistemic")), (("prudential", "epistemic"), ("etiquette", "aesthetic"))]


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def betainc_reg(a_, b_, x, iters=300):
    x = np.asarray(x, float); a_ = np.broadcast_to(np.asarray(a_, float), x.shape).copy(); out = np.empty_like(x); lgamma = np.frompyfunc(math.lgamma, 1, 1)
    def cf(A, B, X):
        tiny = 1e-300; qab, qap, qam = A + B, A + 1, A - 1; c = np.ones_like(X); d = 1 - qab * X / qap; d = np.where(np.abs(d) < tiny, tiny, d); d = 1 / d; h = d.copy()
        for m in range(1, iters):
            m2 = 2 * m; aa = m * (B - m) * X / ((qam + m2) * (A + m2)); d = 1 + aa * d; d = np.where(np.abs(d) < tiny, tiny, d); c = 1 + aa / c; c = np.where(np.abs(c) < tiny, tiny, c); d = 1 / d; h *= d * c
            aa = -(A + m) * (qab + m) * X / ((A + m2) * (qap + m2)); d = 1 + aa * d; d = np.where(np.abs(d) < tiny, tiny, d); c = 1 + aa / c; c = np.where(np.abs(c) < tiny, tiny, c); d = 1 / d; h *= d * c
        return h
    lbeta = lgamma(a_).astype(float) + math.lgamma(b_) - lgamma(a_ + b_).astype(float)
    with np.errstate(divide="ignore", invalid="ignore"):
        front = np.exp(a_ * np.log(np.clip(x, 1e-300, 1)) + b_ * np.log(np.clip(1 - x, 1e-300, 1)) - lbeta)
        lo = x < (a_ + 1) / (a_ + b_ + 2)
        out[lo] = front[lo] * cf(a_[lo], b_, x[lo]) / a_[lo]
        out[~lo] = 1 - front[~lo] * cf(b_, a_[~lo], 1 - x[~lo]) / b_
    out[x <= 0] = 0; out[x >= 1] = 1; return out


def t_pvalue_two_sided(t, df):
    t = np.asarray(t, float); df = np.broadcast_to(np.asarray(df, float), t.shape); x = df / (df + t * t); return betainc_reg(df / 2, 0.5, x)


def welch_sig(X1, X2):
    n1, n2 = len(X1), len(X2); m1, m2 = X1.mean(0), X2.mean(0); v1, v2 = X1.var(0, ddof=1), X2.var(0, ddof=1)
    se2 = v1 / n1 + v2 / n2; ok = se2 > 0; t = np.where(ok, (m1 - m2) / np.sqrt(np.where(ok, se2, 1)), 0.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        df = np.where(ok, se2 ** 2 / ((v1 / n1) ** 2 / max(n1 - 1, 1) + (v2 / n2) ** 2 / max(n2 - 1, 1)), n1 + n2 - 2); df = np.nan_to_num(df, nan=n1 + n2 - 2, posinf=n1 + n2 - 2)
    p = np.ones_like(t)
    if ok.any(): p[ok] = t_pvalue_two_sided(t[ok], np.maximum(np.round(df[ok]), 1))
    p[~ok] = 1.0
    return bh(p) < 0.05


def discover(V, cat, sub, act, rng, subsamples):
    mo, no = cat == "moral", cat == "norm"; Va = V[:, act]
    full = welch_sig(Va[mo], Va[no]); rec = dict(n_tested=int(act.sum()), n_moral=int(mo.sum()), n_norm=int(no.sum()), full_size=int(full.sum()))
    kinds = [k for k in ("prudential", "etiquette", "aesthetic", "epistemic") if (no & (sub == k)).sum() >= 5]
    if len(kinds) == 4:
        g = min([int(mo.sum())] + [int((no & np.isin(sub, side)).sum()) for sp in SPLITS for side in sp]); mi, ni = np.where(mo)[0], np.where(no)[0]
        rec["group_size_equalised"] = g
        rec["moral_vs_norm_equalised"] = float(np.mean([welch_sig(Va[rng.choice(mi, g, replace=False)], Va[rng.choice(ni, g, replace=False)]).sum() for _ in range(subsamples)]))
        rec["norm_vs_norm_equalised"] = {"+".join(s1) + " vs " + "+".join(s2): float(np.mean([welch_sig(Va[rng.choice(np.where(no & np.isin(sub, s1))[0], g, replace=False)], Va[rng.choice(np.where(no & np.isin(sub, s2))[0], g, replace=False)]).sum() for _ in range(subsamples)])) for s1, s2 in SPLITS}
        top = max(rec["norm_vs_norm_equalised"].values()); rec["more_than_any_split"] = bool(rec["moral_vs_norm_equalised"] > top)
    return rec, full


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/units")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], help="A1, B and/or C (the categorisation frame)"); ap.add_argument("--cat-preset", default="zeroshot", choices=list(CAT_PRESETS))
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--subsamples", type=int, default=20)
    ap.add_argument("--seed", type=int, default=20261021); ap.add_argument("--split-meta", default=os.path.join(ROOT, "results", "features_h6split", "split_meta.json"), help="the halves of F5; if absent, halves are drawn here with --seed")
    ap.add_argument("--save-deltas", action="store_true"); ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[run_units] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); rng = np.random.default_rng(args.seed)
    todo = [f for f in args.frames if not os.path.exists(os.path.join(out, f"sets__{f}.json"))]
    if not todo: print(f"[run_units] {tag}: every frame is already there; nothing to do", flush=True); return

    if os.path.exists(args.split_meta):
        meta = json.load(open(args.split_meta)); HA, HB = set(meta["half_A"]), set(meta["half_B"]); split_src = args.split_meta
    else:
        ids = [it["id"] for it in items if it["category"] in ("moral", "norm")]; perm = rng.permutation(len(ids)); HA = {ids[i] for i in perm[: len(ids) // 2]}; HB = set(ids) - HA; split_src = f"drawn here, seed {args.seed}"
    dev = pick_device(args.device); print(f"[run_units] model={args.model} device={dev} frames={todo} items={len(items)} halves from {split_src}", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L; d_mlp = M.layers[0].mlp.down_proj.in_features
    print(f"[run_units] layers={L} neurons per layer={d_mlp}", flush=True)
    run_config_append(out, {"script": "run_units.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "n_items": len(items), "accepted_only": args.accepted_only,
                            "frames": todo, "cat_preset": args.cat_preset, "n_layers": L, "d_mlp": d_mlp, "min_active": args.min_active, "subsamples": args.subsamples, "split_meta": split_src})
    grab = {}
    def hook(l):
        def pre(m, a_, kw=None):
            h = a_[0] if a_ else kw["hidden_states"]; grab[l] = h[0, -1, :].detach().float().cpu().numpy()
        return pre
    handles = [M.layers[l].mlp.down_proj.register_forward_pre_hook(hook(l)) for l in range(L)]
    try:
        for f in todo:
            prompt_of = (lambda stem: CAT_PRESETS[args.cat_preset](stem)) if f == "C" else FRAMES[f]
            t0 = time.time(); A = {s: np.zeros((len(items), L, d_mlp), dtype=np.float32) for s in ("perm", "rest")}
            with torch.no_grad():
                for n, it in enumerate(items):
                    for s in ("perm", "rest"):
                        ids = encode(M.tok, prompt_of(it[f"{s}_stem"])); M.model(input_ids=torch.tensor([ids], device=M.device)); A[s][n] = np.stack([grab[l] for l in range(L)])
                    if (n + 1) % 25 == 0: print(f"[run_units] {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
            cat = np.array([it["category"] for it in items]); sub = np.array([it.get("subtype", "") for it in items]); idl = [it["id"] for it in items]
            allp = np.concatenate([A["perm"], A["rest"]])
            mean_act = allp.mean(0); mean_abs = np.abs(allp).mean(0)
            if f == "C":
                V_all = allp; cat_r = np.concatenate([cat, cat]); sub_r = np.concatenate([sub, sub]); id_r = idl + idl; kind = "activation (both versions of a pair, as separate prompts)"
            else:
                V_all = A["perm"] - A["rest"]; cat_r, sub_r, id_r = cat, sub, idl; kind = "|a(perm) - a(rest)| per pair"
            inA = np.array([i in HA for i in id_r]); inB = np.array([i in HB for i in id_r])
            sets = {"full": {}, "selA": {}, "selB": {}}; counts = {}; absd = np.zeros((3, L, d_mlp), dtype=np.float32)
            for l in range(L):
                V = np.abs(V_all[:, l, :]) if f != "C" else V_all[:, l, :]; mn = np.isin(cat_r, ["moral", "norm"])
                for ci, c in enumerate(("moral", "norm", "descr")): absd[ci, l] = np.abs(V_all[:, l, :])[cat_r == c].mean(0) if (cat_r == c).any() else 0
                act = ((np.abs(allp[:, l, :]) > 0).sum(0) >= args.min_active)
                rec, full = discover(V[mn], cat_r[mn], sub_r[mn], act, rng, args.subsamples); sets["full"][str(l)] = [int(i) for i in np.where(act)[0][full]]
                for name, H in (("selA", inA), ("selB", inB)):
                    m = welch_sig(V[mn & H & (cat_r == "moral")][:, act], V[mn & H & (cat_r == "norm")][:, act]); sets[name][str(l)] = [int(i) for i in np.where(act)[0][m]]; rec[f"{name}_size"] = int(m.sum())
                counts[str(l)] = rec
                print(f"[run_units] {f} layer {l}: tested {rec['n_tested']}, moral vs norm {rec['full_size']}" + (f", equalised {rec['moral_vs_norm_equalised']:.1f} vs splits " + ", ".join(f"{v:.1f}" for v in rec["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in rec else "") + f"; halves {rec['selA_size']} / {rec['selB_size']}", flush=True)
            json.dump(dict(frame=f, unit_value=kind, cat_preset=args.cat_preset if f == "C" else None, n_layers=L, d_mlp=d_mlp, counts=counts, sets=sets, halves_from=split_src, half_A=sorted(HA), half_B=sorted(HB), items_sha256=sha),
                      open(os.path.join(out, f"sets__{f}.json.tmp"), "w")); os.replace(os.path.join(out, f"sets__{f}.json.tmp"), os.path.join(out, f"sets__{f}.json"))
            np.savez_compressed(os.path.join(out, f"stats__{f}.tmp.npz"), items_sha256=np.array(sha), ids=np.array(idl), category=cat, subtype=sub, mean_act=mean_act, mean_abs_act=mean_abs, mean_absdelta_by_category=absd,
                                **({"delta": V_all.astype(np.float16)} if args.save_deltas else {})); os.replace(os.path.join(out, f"stats__{f}.tmp.npz"), os.path.join(out, f"stats__{f}.npz"))
            print(f"[run_units] {f} done in {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in handles: h.remove()
    print("[run_units] finished", flush=True)


if __name__ == "__main__":
    main()
