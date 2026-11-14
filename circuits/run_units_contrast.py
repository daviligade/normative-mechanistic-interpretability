"""MLP neurons that separate other pairs of groups."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, pick_device, load_items, model_tag, run_config_append, Model, readouts
from run_units import bh, t_pvalue_two_sided, welch_sig, discover, SPLITS, ROOT
from run_category_frame import PRESETS as CAT_PRESETS, CATEGORY_WORDS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids, first_token_id

CATS = ("moral", "norm", "descr")


def welch_t(X1, X2):
    n1, n2 = len(X1), len(X2); se2 = X1.var(0, ddof=1) / n1 + X2.var(0, ddof=1) / n2
    return np.where(se2 > 0, (X1.mean(0) - X2.mean(0)) / np.sqrt(np.where(se2 > 0, se2, 1)), 0.0)


def one_sample(X):
    n = len(X); m = X.mean(0); s = X.std(0, ddof=1); ok = (s > 0) & (n > 1); t = np.where(ok, m / np.where(ok, s, 1) * np.sqrt(n), 0.0)
    p = np.ones_like(t); p[ok] = t_pvalue_two_sided(t[ok], max(n - 1, 1)); return (bh(p) < 0.05) & ok, t


def capped(idx_act, mask, score, cap):
    sig = np.where(mask)[0]; order = sig[np.argsort(-np.abs(score[sig]), kind="stable")][:cap] if cap else sig; return [int(idx_act[i]) for i in order]


def dla_weights(M, u):
    ue = (u.float() * M.norm_w).to(M.layers[0].mlp.down_proj.weight.dtype)
    with torch.no_grad(): return np.stack([(ue @ M.layers[l].mlp.down_proj.weight).float().cpu().numpy() for l in range(M.L)])


def shares(V):
    tot = V.sum(1, keepdims=True); return np.where(tot > 0, V / np.where(tot > 0, tot, 1), 0.0)


def gap_match(ga, gb, rng):
    ia = list(rng.permutation(len(ga))); free = set(range(len(gb))); pa, pb = [], []
    for i in ia:
        if not free: break
        j = min(free, key=lambda k: abs(ga[i] - gb[k])); free.discard(j); pa.append(i); pb.append(j)
    return np.array(pa, int), np.array(pb, int)


def corr(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or x.std() == 0 or y.std() == 0: return None
    return float(np.corrcoef(x, y)[0, 1])


def overlap(a, b, n):
    a, b = set(a), set(b); exp = len(a) * len(b) / n if n else 0.0; return dict(observed=len(a & b), expected=round(exp, 2), jaccard=round(len(a & b) / len(a | b), 3) if (a | b) else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/units_contrast")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], help="frames for the stance and normdescr contrasts (A1 and/or B)")
    ap.add_argument("--contrasts", nargs="+", default=["mvn", "stance", "normdescr", "catC"], choices=["mvn", "stance", "normdescr", "catC"]); ap.add_argument("--cat-preset", default="fewshot", choices=list(CAT_PRESETS))
    ap.add_argument("--cap", type=int, default=25, help="at most this many units per layer in each selected list; 0 = no cap")
    ap.add_argument("--stance-rank", default="t", choices=["t", "dla"], help="order within the stance lists: |t| of the consistent direction, or the shift's weight on the answer direction")
    ap.add_argument("--catc-rank", default="dla", choices=["t", "dla"], help="order within the catC lists: |t| of moral vs norm, or the difference's weight on the category direction")
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--subsamples", type=int, default=10)
    ap.add_argument("--seed", type=int, default=20261022); ap.add_argument("--split-meta", default=os.path.join(ROOT, "results", "features_h6split", "split_meta.json"), help="the halves of F5; if absent, halves are drawn here with --seed")
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    ap.add_argument("--null-size", type=int, default=0, help="mvn: also every comparison at ONE group size (at most this, limited by the largest moral theme and by half the moral pairs): moral vs norm, the three kind splits, moral vs moral (disjoint draws), the largest moral theme vs the other moral pairs; 0 = off")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[contrast] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); rng = np.random.default_rng(args.seed)
    outs = {c: os.path.join(args.out, c, tag) for c in args.contrasts}
    for o in outs.values(): os.makedirs(o, exist_ok=True)

    todo = {c: ([f for f in args.frames if not os.path.exists(os.path.join(outs[c], f"sets__{f}.json"))] if c != "catC" else ([] if os.path.exists(os.path.join(outs[c], "sets__C.json")) else ["C"])) for c in args.contrasts}
    if not any(todo.values()): print(f"[contrast] {tag}: everything is already there; nothing to do", flush=True); return
    need = set(f for fs in todo.values() for f in fs)
    if "C" in need: need.add("B")
    if "catC" in todo and todo["catC"]: need |= set(args.frames)

    if os.path.exists(args.split_meta):
        meta = json.load(open(args.split_meta)); HA, HB = set(meta["half_A"]), set(meta["half_B"]); split_src = args.split_meta
    else:
        ids = [it["id"] for it in items if it["category"] in ("moral", "norm")]; perm = rng.permutation(len(ids)); HA = {ids[i] for i in perm[: len(ids) // 2]}; HB = set(ids) - HA; split_src = f"drawn here, seed {args.seed}"
    dids = [it["id"] for it in items if it["category"] == "descr"]; dp = rng.permutation(len(dids)); DA = {dids[i] for i in dp[: len(dids) // 2]}; DB = set(dids) - DA
    dev = pick_device(args.device); print(f"[contrast] model={args.model} device={dev} contrasts={ {c: f for c, f in todo.items() if f} } passes for frames {sorted(need)} items={len(items)} halves from {split_src}; descriptive halves drawn here ({len(DA)}/{len(DB)})", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L; d_mlp = M.layers[0].mlp.down_proj.in_features
    print(f"[contrast] layers={L} neurons per layer={d_mlp}", flush=True)
    W_ans = dla_weights(M, M.u_dir)
    cat_tok = {c: [first_token_id(M.tok, w, False) for w in ws] for c, ws in CATEGORY_WORDS.items() if c != "descriptive"}
    u_cat = M.W_U[cat_tok["moral"]].float().mean(0) - torch.stack([M.W_U[cat_tok[c]].float().mean(0) for c in cat_tok if c != "moral"]).mean(0); W_cat = dla_weights(M, u_cat)
    for c, o in outs.items():
        if todo[c]: run_config_append(o, {"script": "run_units_contrast.py", "contrast": c, "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "n_items": len(items), "accepted_only": args.accepted_only,
                                           "frames": todo[c], "cat_preset": args.cat_preset, "n_layers": L, "d_mlp": d_mlp, "min_active": args.min_active, "subsamples": args.subsamples, "cap": args.cap, "stance_rank": args.stance_rank, "catc_rank": args.catc_rank,
                                           "category_words": {c: ws for c, ws in CATEGORY_WORDS.items() if c != "descriptive"}, "split_meta": split_src, "seed": args.seed})
    grab = {}
    def hook(l):
        def pre(m, a_, kw=None):
            h = a_[0] if a_ else kw["hidden_states"]; grab[l] = h[0, -1, :].detach().float().cpu().numpy()
        return pre
    handles = [M.layers[l].mlp.down_proj.register_forward_pre_hook(hook(l)) for l in range(L)]
    cat = np.array([it["category"] for it in items]); sub = np.array([it.get("subtype", "") for it in items]); idl = [it["id"] for it in items]
    inA = np.array([i in HA for i in idl]); inB = np.array([i in HB for i in idl]); dA = np.array([i in DA for i in idl]); dB = np.array([i in DB for i in idl])
    mo, no, de = cat == "moral", cat == "norm", cat == "descr"; nm = mo | no
    A = {}; SV = {}
    try:
        for f in sorted(need):
            prompt_of = (lambda stem: CAT_PRESETS[args.cat_preset](stem)) if f == "C" else FRAMES[f]
            t0 = time.time(); A[f] = {s: np.zeros((len(items), L, d_mlp), dtype=np.float32) for s in ("perm", "rest")}; SV[f] = {s: np.zeros(len(items), dtype=np.float64) for s in ("perm", "rest")}
            with torch.no_grad():
                for n, it in enumerate(items):
                    for s in ("perm", "rest"):
                        ids = encode(M.tok, prompt_of(it[f"{s}_stem"])); lg = M.model(input_ids=torch.tensor([ids], device=M.device)).logits[:, -1, :].float(); A[f][s][n] = np.stack([grab[l] for l in range(L)]); SV[f][s][n] = float(readouts(lg, M.A)["S"][0])
                    if (n + 1) % 50 == 0: print(f"[contrast] passes {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    finally:
        for h in handles: h.remove()

    def stats_arrays(f):
        allp = np.concatenate([A[f]["perm"], A[f]["rest"]]); D = A[f]["perm"] - A[f]["rest"]
        absd = np.stack([np.abs(D)[cat == c].mean(0) if (cat == c).any() else np.zeros((L, d_mlp), np.float32) for c in CATS]); sgn = np.stack([D[cat == c].mean(0) if (cat == c).any() else np.zeros((L, d_mlp), np.float32) for c in CATS])
        return dict(items_sha256=np.array(sha), ids=np.array(idl), category=cat, subtype=sub, mean_act=allp.mean(0), mean_abs_act=np.abs(allp).mean(0), mean_absdelta_by_category=absd, mean_signed_delta_by_category=sgn,
                    dla_weight_answer=W_ans, dla_weight_category=W_cat, gap=SV[f]["perm"] - SV[f]["rest"])

    def save(o, f, sets_obj, stats):
        json.dump(sets_obj, open(os.path.join(o, f"sets__{f}.json.tmp"), "w")); os.replace(os.path.join(o, f"sets__{f}.json.tmp"), os.path.join(o, f"sets__{f}.json"))
        np.savez_compressed(os.path.join(o, f"stats__{f}.tmp.npz"), **stats); os.replace(os.path.join(o, f"stats__{f}.tmp.npz"), os.path.join(o, f"stats__{f}.npz"))

    base = dict(n_layers=L, d_mlp=d_mlp, halves_from=split_src, half_A=sorted(HA), half_B=sorted(HB), descr_half_A=sorted(DA), descr_half_B=sorted(DB), items_sha256=sha, cap=args.cap)
    score_stance = lambda t, m, l, ia: t if args.stance_rank == "t" else m * W_ans[l][ia]

    for f in args.frames:
        if f not in A: continue
        allp = np.concatenate([A[f]["perm"], A[f]["rest"]]); D = A[f]["perm"] - A[f]["rest"]; st = stats_arrays(f); gap = st["gap"]; t0 = time.time()
        if "mvn" in todo and f in todo["mvn"]:
            sets = {"full": {}, "selA": {}, "selB": {}}; counts = {}
            mi, ni = np.where(mo)[0], np.where(no)[0]; pm, pn = gap_match(gap[mi], gap[ni], rng); Mm, Mn = mi[pm], ni[pn]
            kinds = [k for k in ("prudential", "etiquette", "aesthetic", "epistemic") if (no & (sub == k)).sum() >= 5]; split_pairs = {}
            if len(kinds) == 4:
                for s1, s2 in SPLITS:
                    i1, i2 = np.where(no & np.isin(sub, s1))[0], np.where(no & np.isin(sub, s2))[0]; q1, q2 = gap_match(gap[i1], gap[i2], rng); split_pairs["+".join(s1) + " vs " + "+".join(s2)] = (i1[q1], i2[q2])
            matched_info = dict(n_matched=int(len(Mm)), mean_gap_moral=float(gap[Mm].mean()), mean_gap_matched_norm=float(gap[Mn].mean()), mean_abs_gap_difference=float(np.abs(gap[Mm] - gap[Mn]).mean()),
                                mean_gap_moral_all=float(gap[mo].mean()), mean_gap_norm_all=float(gap[no].mean()), split_sizes={k: int(len(v[0])) for k, v in split_pairs.items()})
            print(f"[contrast] mvn {f}: gap matching {matched_info['n_matched']} moral pairs (mean gap {matched_info['mean_gap_moral']:.3f}, all moral {matched_info['mean_gap_moral_all']:.3f}) with norm pairs (matched {matched_info['mean_gap_matched_norm']:.3f}, all norm {matched_info['mean_gap_norm_all']:.3f})", flush=True)
            for l in range(L):
                act = ((np.abs(allp[:, l, :]) > 0).sum(0) >= args.min_active); ia = np.where(act)[0]; R = np.abs(D[:, l, :]); Sh = shares(R[:, act])
                rec, full = discover(Sh[nm], cat[nm], sub[nm], np.ones(len(ia), bool), rng, args.subsamples); rec["n_tested"] = int(act.sum()); t = welch_t(Sh[mo], Sh[no])
                if "group_size_equalised" in rec:
                    g = rec["group_size_equalised"]; mi = np.where(mo)[0]
                    if 2 * g <= len(mi): rec["null_moral_vs_moral_equalised"] = float(np.mean([welch_sig(Sh[(q := rng.permutation(mi))[:g]], Sh[q[g:2 * g]]).sum() for _ in range(args.subsamples)]))
                    themes = {k: int((mo & (sub == k)).sum()) for k in set(sub[mo]) if k}
                    if themes:
                        k0 = max(themes, key=themes.get); t_i, o_i = np.where(mo & (sub == k0))[0], np.where(mo & (sub != k0))[0]; gt = min(g, len(t_i), len(o_i))
                        if gt >= 10: rec["null_theme"] = k0; rec["null_theme_group_size"] = int(gt); rec["null_theme_vs_other_moral_equalised"] = float(np.mean([welch_sig(Sh[rng.choice(t_i, gt, replace=False)], Sh[rng.choice(o_i, gt, replace=False)]).sum() for _ in range(args.subsamples)]))
                if args.null_size and "group_size_equalised" in rec:
                    mi0, ni0 = np.where(mo)[0], np.where(no)[0]; th0 = {k: int((mo & (sub == k)).sum()) for k in set(sub[mo]) if k}; k0 = max(th0, key=th0.get) if th0 else None
                    ti0, oi0 = (np.where(mo & (sub == k0))[0], np.where(mo & (sub != k0))[0]) if k0 else (mi0, mi0)
                    g0 = int(min(args.null_size, rec["group_size_equalised"], len(mi0) // 2, len(ti0), len(oi0))); pick0 = lambda idx: rng.choice(idx, g0, replace=False)
                    eq = dict(group_size=g0, theme=k0, subsamples=args.subsamples,
                              moral_vs_norm=float(np.mean([welch_sig(Sh[pick0(mi0)], Sh[pick0(ni0)]).sum() for _ in range(args.subsamples)])),
                              norm_vs_norm={"+".join(s1) + " vs " + "+".join(s2): float(np.mean([welch_sig(Sh[pick0(np.where(no & np.isin(sub, s1))[0])], Sh[pick0(np.where(no & np.isin(sub, s2))[0])]).sum() for _ in range(args.subsamples)])) for s1, s2 in SPLITS},
                              moral_vs_moral=float(np.mean([welch_sig(Sh[(q0 := rng.permutation(mi0))[:g0]], Sh[q0[g0:2 * g0]]).sum() for _ in range(args.subsamples)])))
                    if k0: eq["theme_vs_other_moral"] = float(np.mean([welch_sig(Sh[pick0(ti0)], Sh[pick0(oi0)]).sum() for _ in range(args.subsamples)]))
                    rec["equal_size"] = eq
                    print(f"[contrast] mvn {f} layer {l}: at equal size g={g0}: moral vs norm {eq['moral_vs_norm']:.1f}; kind splits " + ", ".join(f"{v:.1f}" for v in eq["norm_vs_norm"].values())
                          + f"; moral vs moral {eq['moral_vs_moral']:.1f}" + (f"; {k0} vs other moral {eq['theme_vs_other_moral']:.1f}" if k0 else ""), flush=True)
                rec["raw_full_size"] = int(welch_sig(R[mo][:, act], R[no][:, act]).sum())
                rec["matched_raw_moral_vs_norm"] = int(welch_sig(R[Mm][:, act], R[Mn][:, act]).sum()); rec["matched_share_moral_vs_norm"] = int(welch_sig(Sh[Mm], Sh[Mn]).sum())
                if split_pairs:
                    rec["matched_raw_norm_vs_norm"] = {k: int(welch_sig(R[v[0]][:, act], R[v[1]][:, act]).sum()) for k, v in split_pairs.items()}
                    rec["matched_raw_more_than_any_split"] = bool(rec["matched_raw_moral_vs_norm"] > max(rec["matched_raw_norm_vs_norm"].values()))
                rec["share_units_writing_answer"] = int((full & (np.abs(W_ans[l][ia]) > np.percentile(np.abs(W_ans[l]), 90))).sum())
                sets["full"][str(l)] = capped(ia, full, t, args.cap)
                for name, H in (("selA", inA), ("selB", inB)):
                    m = welch_sig(Sh[H & mo], Sh[H & no]); th = welch_t(Sh[H & mo], Sh[H & no]); sets[name][str(l)] = capped(ia, m, th, args.cap); rec[f"{name}_size"] = int(m.sum()); rec[f"{name}_kept"] = len(sets[name][str(l)])
                counts[str(l)] = rec
                print(f"[contrast] mvn {f} layer {l}: tested {rec['n_tested']}; shares: moral vs norm {rec['full_size']}" + (f", equalised {rec['moral_vs_norm_equalised']:.1f} vs splits " + ", ".join(f"{v:.1f}" for v in rec["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in rec else "")
                      + (f", nulls moral/moral {rec['null_moral_vs_moral_equalised']:.1f}" if "null_moral_vs_moral_equalised" in rec else "") + (f", {rec['null_theme']}/other moral {rec['null_theme_vs_other_moral_equalised']:.1f} (g={rec['null_theme_group_size']})" if "null_theme" in rec else "")
                      + f"; raw {rec['raw_full_size']}, gap-matched raw {rec['matched_raw_moral_vs_norm']}" + (f" vs splits " + ", ".join(str(v) for v in rec["matched_raw_norm_vs_norm"].values()) if "matched_raw_norm_vs_norm" in rec else "") + f"; halves {rec['selA_size']} / {rec['selB_size']} (kept {rec['selA_kept']} / {rec['selB_kept']})", flush=True)
            save(outs["mvn"], f, dict(base, frame=f, contrast="mvn", unit_value="share of |a(perm) - a(rest)| within the layer, per pair; lists = moral vs norm on shares", gap_matching=matched_info, counts=counts, sets=sets), st)
        if "stance" in todo and f in todo["stance"]:
            sets = {"full": {}, "selA": {}, "selB": {}}; counts = {}
            for l in range(L):
                act = ((np.abs(allp[:, l, :]) > 0).sum(0) >= args.min_active); ia = np.where(act)[0]; X = D[:, l, act]; rec = dict(n_tested=int(act.sum()))
                masks, ts = {}, {}
                for c in CATS:
                    masks[c], ts[c] = one_sample(X[cat == c]); rec[f"n_{c}"] = int((cat == c).sum()); rec[f"{c}_size"] = int(masks[c].sum())
                mN, tN = one_sample(X[nm]); rec["normative_size"] = int(mN.sum()); rec["full_size"] = rec["normative_size"]
                mean = {c: X[cat == c].mean(0) for c in CATS}
                rec["corr_moral_norm"] = corr(mean["moral"], mean["norm"]); rec["corr_norm_descr"] = corr(mean["norm"], mean["descr"]); rec["corr_moral_descr"] = corr(mean["moral"], mean["descr"])
                both = masks["moral"] & masks["norm"]; rec["overlap_moral_norm"] = overlap(np.where(masks["moral"])[0], np.where(masks["norm"])[0], int(act.sum()))
                rec["overlap_norm_descr"] = overlap(np.where(masks["norm"])[0], np.where(masks["descr"])[0], int(act.sum()))
                rec["shared_moral_norm_same_sign"] = (float(np.mean(np.sign(mean["moral"][both]) == np.sign(mean["norm"][both]))) if both.any() else None)
                rec["shared_moral_norm_corr"] = corr(mean["moral"][both], mean["norm"][both]) if both.sum() >= 3 else None
                rec["normative_units_writing_answer"] = int((mN & (np.abs(W_ans[l][ia]) > np.percentile(np.abs(W_ans[l]), 90))).sum())
                sets["full"][str(l)] = capped(ia, mN, score_stance(tN, X[nm].mean(0), l, ia), args.cap)
                for name, H in (("selA", inA), ("selB", inB)):
                    m, t = one_sample(X[nm & H]); sets[name][str(l)] = capped(ia, m, score_stance(t, X[nm & H].mean(0), l, ia), args.cap); rec[f"{name}_size"] = int(m.sum()); rec[f"{name}_kept"] = len(sets[name][str(l)])
                counts[str(l)] = rec
                print(f"[contrast] stance {f} layer {l}: tested {rec['n_tested']}; consistent-direction units moral {rec['moral_size']}, norm {rec['norm_size']}, descr {rec['descr_size']}, normative {rec['normative_size']}; "
                      f"corr(moral, norm) {rec['corr_moral_norm'] if rec['corr_moral_norm'] is None else round(rec['corr_moral_norm'], 2)}, overlap {rec['overlap_moral_norm']['observed']} vs {rec['overlap_moral_norm']['expected']} expected; halves kept {rec['selA_kept']} / {rec['selB_kept']}", flush=True)
            save(outs["stance"], f, dict(base, frame=f, contrast="stance", unit_value="a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)", counts=counts, sets=sets), st)
        if "normdescr" in todo and f in todo["normdescr"]:
            sets = {"full": {}, "selA": {}, "selB": {}}; counts = {}
            for l in range(L):
                act = ((np.abs(allp[:, l, :]) > 0).sum(0) >= args.min_active); ia = np.where(act)[0]; R = np.abs(D[:, l, act]); V = shares(R); rec = dict(n_tested=int(act.sum()), n_moral=int(mo.sum()), n_norm=int(no.sum()), n_descr=int(de.sum()))
                mND = welch_sig(V[nm], V[de]); tND = welch_t(V[nm], V[de]); mMD = welch_sig(V[mo], V[de]); mnD = welch_sig(V[no], V[de]); mMN = welch_sig(V[mo], V[no])
                rec["full_size"] = rec["normative_vs_descr"] = int(mND.sum()); rec["moral_vs_descr"] = int(mMD.sum()); rec["norm_vs_descr"] = int(mnD.sum()); rec["moral_vs_norm"] = int(mMN.sum()); rec["normative_vs_descr_raw"] = int(welch_sig(R[nm], R[de]).sum())
                rec["both_kinds_vs_descr"] = int((mMD & mnD).sum()); rec["normative_units_also_moral_vs_norm"] = int((mND & mMN).sum())
                rec["normative_units_direction_up"] = int((mND & (tND > 0)).sum())
                g = int(min(mo.sum(), no.sum(), de.sum())); rec["group_size_equalised"] = g
                if g >= 5:
                    pick = lambda m_, k: rng.choice(np.where(m_)[0], k, replace=False)
                    rec["normative_vs_descr_equalised"] = float(np.mean([welch_sig(V[pick(nm, g)], V[pick(de, g)]).sum() for _ in range(args.subsamples)]))
                    rec["moral_vs_descr_equalised"] = float(np.mean([welch_sig(V[pick(mo, g)], V[pick(de, g)]).sum() for _ in range(args.subsamples)]))
                    rec["norm_vs_descr_equalised"] = float(np.mean([welch_sig(V[pick(no, g)], V[pick(de, g)]).sum() for _ in range(args.subsamples)]))
                    rec["moral_vs_norm_equalised"] = float(np.mean([welch_sig(V[pick(mo, g)], V[pick(no, g)]).sum() for _ in range(args.subsamples)]))
                    kinds = [k for k in ("prudential", "etiquette", "aesthetic", "epistemic") if (no & (sub == k)).sum() >= 5]
                    if len(kinds) == 4:
                        gs = min([g] + [int((no & np.isin(sub, side)).sum()) for sp in SPLITS for side in sp]); rec["split_group_size"] = gs
                        rec["norm_vs_norm_equalised"] = {"+".join(s1) + " vs " + "+".join(s2): float(np.mean([welch_sig(V[pick(no & np.isin(sub, s1), gs)], V[pick(no & np.isin(sub, s2), gs)]).sum() for _ in range(args.subsamples)])) for s1, s2 in SPLITS}
                        rec["normative_vs_descr_at_split_size"] = float(np.mean([welch_sig(V[pick(nm, gs)], V[pick(de, gs)]).sum() for _ in range(args.subsamples)]))
                        rec["more_than_any_split"] = bool(rec["normative_vs_descr_at_split_size"] > max(rec["norm_vs_norm_equalised"].values()))
                sets["full"][str(l)] = capped(ia, mND & (tND > 0), tND, args.cap)
                for name, H, Dh in (("selA", inA, dA), ("selB", inB, dB)):
                    m = welch_sig(V[nm & H], V[de & Dh]); t = welch_t(V[nm & H], V[de & Dh]); sets[name][str(l)] = capped(ia, m & (t > 0), t, args.cap); rec[f"{name}_size"] = int((m & (t > 0)).sum()); rec[f"{name}_kept"] = len(sets[name][str(l)])
                counts[str(l)] = rec
                print(f"[contrast] normdescr {f} layer {l}: tested {rec['n_tested']}; shares: normative vs descr {rec['normative_vs_descr']} (up {rec['normative_units_direction_up']}; raw {rec['normative_vs_descr_raw']}), moral vs descr {rec['moral_vs_descr']}, norm vs descr {rec['norm_vs_descr']}, both {rec['both_kinds_vs_descr']}, "
                      f"also moral vs norm {rec['normative_units_also_moral_vs_norm']}" + (f"; equalised (g={g}) normative {rec['normative_vs_descr_equalised']:.1f}, moral {rec['moral_vs_descr_equalised']:.1f}, norm {rec['norm_vs_descr_equalised']:.1f} vs descr, moral vs norm {rec['moral_vs_norm_equalised']:.1f}" if g >= 5 else "")
                      + (f"; splits " + ", ".join(f"{v:.1f}" for v in rec["norm_vs_norm_equalised"].values()) + f" vs normative {rec['normative_vs_descr_at_split_size']:.1f} at size {rec['split_group_size']}" if "norm_vs_norm_equalised" in rec else "") + f"; halves kept {rec['selA_kept']} / {rec['selB_kept']}", flush=True)
            save(outs["normdescr"], f, dict(base, frame=f, contrast="normdescr", unit_value="share of |a(perm) - a(rest)| within the layer, per pair; lists = larger on normative (moral + norm) than on descriptive pairs", counts=counts, sets=sets), st)
        print(f"[contrast] frame {f} contrasts done in {(time.time() - t0) / 60:.1f} min", flush=True)

    if "catC" in todo and todo["catC"]:
        t0 = time.time(); o = outs["catC"]
        for f in args.frames:
            if f in A: np.savez_compressed(os.path.join(o, f"stats__{f}.tmp.npz"), **stats_arrays(f)); os.replace(os.path.join(o, f"stats__{f}.tmp.npz"), os.path.join(o, f"stats__{f}.npz"))
        Vc = 0.5 * ((A["C"]["perm"] - A["B"]["perm"]) + (A["C"]["rest"] - A["B"]["rest"])); aC = 0.5 * (A["C"]["perm"] + A["C"]["rest"]); allC = np.concatenate([A["C"]["perm"], A["C"]["rest"]])
        sets = {"full": {}, "selA": {}, "selB": {}}; counts = {}; absd = np.stack([np.abs(Vc)[cat == c].mean(0) if (cat == c).any() else np.zeros((L, d_mlp), np.float32) for c in CATS])
        for l in range(L):
            act = ((np.abs(allC[:, l, :]) > 0).sum(0) >= args.min_active); ia = np.where(act)[0]; V = Vc[:, l, :]
            score = lambda H: (welch_t(V[H & mo][:, act], V[H & no][:, act]) if args.catc_rank == "t" else (aC[H & mo][:, l, act].mean(0) - aC[H & no][:, l, act].mean(0)) * W_cat[l][ia])
            rec, full = discover(V[nm], cat[nm], sub[nm], act, rng, args.subsamples); sets["full"][str(l)] = capped(ia, full, score(nm), args.cap)
            rec["moral_vs_norm_writing_category"] = int((full & (np.abs(W_cat[l][ia]) > np.percentile(np.abs(W_cat[l]), 90))).sum())
            for name, H in (("selA", inA), ("selB", inB)):
                m = welch_sig(V[H & mo][:, act], V[H & no][:, act]); sets[name][str(l)] = capped(ia, m, score(H), args.cap); rec[f"{name}_size"] = int(m.sum()); rec[f"{name}_kept"] = len(sets[name][str(l)])
            counts[str(l)] = rec
            print(f"[contrast] catC layer {l}: tested {rec['n_tested']}, moral vs norm {rec['full_size']} (writing the category {rec['moral_vs_norm_writing_category']})" + (f", equalised {rec['moral_vs_norm_equalised']:.1f} vs splits " + ", ".join(f"{v:.1f}" for v in rec["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in rec else "") + f"; halves {rec['selA_size']} / {rec['selB_size']} (kept {rec['selA_kept']} / {rec['selB_kept']})", flush=True)
        json.dump(dict(base, frame="C", contrast="catC", unit_value="a_C - a_B per pair (mean over the two versions); lists ordered by " + ("|t|" if args.catc_rank == "t" else "the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction"),
                       cat_preset=args.cat_preset, counts=counts, sets=sets), open(os.path.join(o, "sets__C.json.tmp"), "w")); os.replace(os.path.join(o, "sets__C.json.tmp"), os.path.join(o, "sets__C.json"))
        np.savez_compressed(os.path.join(o, "stats__C.tmp.npz"), items_sha256=np.array(sha), ids=np.array(idl), category=cat, subtype=sub, mean_act=allC.mean(0), mean_abs_act=np.abs(allC).mean(0), mean_absdelta_by_category=absd,
                            dla_weight_answer=W_ans, dla_weight_category=W_cat); os.replace(os.path.join(o, "stats__C.tmp.npz"), os.path.join(o, "stats__C.npz"))
        print(f"[contrast] catC done in {(time.time() - t0) / 60:.1f} min", flush=True)
    print("[contrast] finished", flush=True)


if __name__ == "__main__":
    main()
