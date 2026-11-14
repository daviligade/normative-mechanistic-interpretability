"""Feature analysis: capture, H5, H6 and removal of the feature sets."""
import argparse, json, os, sys, itertools, collections
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import primary_item_set, check_analysis_items

ap = argparse.ArgumentParser(); ap.add_argument("--runs", required=True); ap.add_argument("--items", required=True); ap.add_argument("--located", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--perm", type=int, default=20000); ap.add_argument("--perm-calib", type=int, default=20000); ap.add_argument("--subsamples", type=int, default=20)
ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--subset", default="accepted", choices=["accepted", "strict", "all"])
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed); LOCATED = json.load(open(a.located)); PRIMARY_SET, PRIMARY_WHY = primary_item_set(a.items)
ACC = {i["id"]: i for i in json.load(open(a.items)) if (i.get("accepted_strict", True) if a.subset == "strict" else (i.get("accepted", True) if a.subset == "accepted" else True))}


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def n_sig(X1, X2, P, return_mask=False):
    Z = np.concatenate([X1, X2]).astype(np.float32); n1, n = len(X1), len(X1) + len(X2); m = Z.shape[1]; P = max(P, 20 * m)
    obs = np.abs(X1.mean(0) - X2.mean(0)); tot = Z.sum(0); hits = np.zeros(m); done = 0
    while done < P:
        k = min(1000, P - done); sel = np.argsort(rng.random((k, n)), axis=1)[:, :n1]; M = np.zeros((k, n), dtype=np.float32); np.put_along_axis(M, sel, 1.0, axis=1); s1 = M @ Z
        hits += (np.abs(s1 / n1 - (tot - s1) / (n - n1)) >= obs - 1e-9).sum(0); done += k
    sig = bh((hits + 1) / (P + 1)) < 0.05
    return (int(sig.sum()), sig) if return_mask else int(sig.sum())


PRE_SPECIFIED = PRIMARY_SET and (a.subset, a.tau) == ("accepted", 0.02)
report, summary = ["# Feature results", ""] + (["**Run with --any-items (synthetic data): this is not an analysis of the study.**", ""] if a.any_items else []) + [(f"Primary analysis: {PRIMARY_WHY}; {len(ACC)} items." if PRE_SPECIFIED else
                   f"**Sensitivity run ({PRIMARY_WHY if not PRIMARY_SET else 'an option differs from the default'}; items: {a.subset}, {len(ACC)} items): not the primary analysis.**"), f"Runs folder: {a.runs}", ""], {}
for cond in sorted(os.listdir(a.runs)):
    d = os.path.join(a.runs, cond)
    if not os.path.isdir(d) or not os.path.exists(os.path.join(d, "extract__A1.npz")): continue
    out = {"condition": cond}; E = {fr: np.load(os.path.join(d, f"extract__{fr}.npz")) for fr in ("A1", "B", "A0") if os.path.exists(os.path.join(d, f"extract__{fr}.npz"))}
    keep = {fr: np.array([str(i) in ACC for i in e["ids"]]) for fr, e in E.items()}; cat = {fr: np.array([str(c) for c in e["category"]])[keep[fr]] for fr, e in E.items()}; sub = {fr: np.array([str(c) for c in e["subtype"]])[keep[fr]] for fr, e in E.items()}
    G = lambda fr, k: E[fr][k][keep[fr]]

    out["final_token"] = {}
    for fr in E:
        rel = np.concatenate([G(fr, "perm_err2") / G(fr, "perm_norm2"), G(fr, "rest_err2") / G(fr, "rest_norm2")]); dS = np.concatenate([G(fr, "perm_splice_S") - G(fr, "perm_clean_S"), G(fr, "rest_splice_S") - G(fr, "rest_clean_S")])
        D, DH = G(fr, "perm_h") - G(fr, "rest_h"), G(fr, "perm_xh") - G(fr, "rest_xh"); r2 = 1 - ((D - DH) ** 2).sum(1) / (D ** 2).sum(1); cos = (D * DH).sum(1) / (np.linalg.norm(D, axis=1) * np.linalg.norm(DH, axis=1) + 1e-12); proj = (D * DH).sum(1) / (D ** 2).sum(1)
        out["final_token"][fr] = dict(rel_reconstruction_error=float(rel.mean()), splice_mean_abs_dS=float(np.abs(dS).mean()), splice_max_abs_dS=float(np.abs(dS).max()),
                                      capture={c: dict(R2=float(r2[cat[fr] == c].mean()), cosine=float(cos[cat[fr] == c].mean()), projection=float(proj[cat[fr] == c].mean())) for c in ("moral", "norm", "descr") if (cat[fr] == c).any()},
                                      flagged_uninformative=bool(r2.mean() < 0.5))

    sets = LOCATED.get(cond, {}); out["H5_frame_following"] = {}
    for name in ("original_vs_neutral_sig", "original_vs_norm_sig"):
        F = np.array(sets.get(name, []), dtype=int)
        if len(F) == 0: continue
        A = {fr: (G(fr, "perm_f")[:, F].astype(np.float32).mean(1) + G(fr, "rest_f")[:, F].astype(np.float32).mean(1)) / 2 for fr in E}; cell = {f"{fr}/{c}": float(A[fr][cat[fr] == c].mean()) for fr in E for c in ("moral", "norm", "descr") if (cat[fr] == c).any()}
        rec = dict(n_features=int(len(F)), mean_activation=cell)
        if "A1" in E and (cat["A1"] == "moral").any():
            for other in ("descr", "norm"):
                if not (cat["A1"] == other).any(): continue
                x, y = A["A1"][cat["A1"] == other], A["A1"][cat["A1"] == "moral"]; bs = np.array([x[rng.integers(0, len(x), len(x))].mean() / max(y[rng.integers(0, len(y), len(y))].mean(), 1e-12) for _ in range(a.boot)])
                ci = [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]; rec[f"ratio_A1_{other}_over_moral"] = dict(ratio=float(x.mean() / y.mean()), ci95=ci, reading="frame-driven" if ci[0] > 0.5 else ("content-driven" if ci[1] < 0.5 else "inconclusive"))
        out["H5_frame_following"][name] = rec

    out["H6_discovery"] = {}; h6_sets = {}
    for fr in E:
        c, s = cat[fr], sub[fr]
        if not ((c == "moral").any() and (c == "norm").any()): continue
        mn = np.isin(c, ["moral", "norm"]); act = ((G(fr, "perm_f")[mn] > 0).sum(0) + (G(fr, "rest_f")[mn] > 0).sum(0)) >= a.min_active
        X = np.abs(G(fr, "perm_f").astype(np.float32) - G(fr, "rest_f").astype(np.float32))[:, act]
        n_full, sig_mask = n_sig(X[c == "moral"], X[c == "norm"], a.perm, return_mask=True)
        h6_sets[f"h6_moral_vs_norm_{fr}"] = [int(i) for i in np.where(act)[0][sig_mask]]
        rec = dict(n_features_tested=int(act.sum()), full_size=dict(n_moral=int((c == "moral").sum()), n_norm=int((c == "norm").sum()), n_significant=n_full))
        kinds = [k for k in ("prudential", "etiquette", "aesthetic", "epistemic") if ((c == "norm") & (s == k)).sum() >= 5]
        if len(kinds) == 4:
            splits = [(("prudential", "etiquette"), ("aesthetic", "epistemic")), (("prudential", "aesthetic"), ("etiquette", "epistemic")), (("prudential", "epistemic"), ("etiquette", "aesthetic"))]
            g = min([int((c == "moral").sum())] + [int(((c == "norm") & np.isin(s, side)).sum()) for sp in splits for side in sp]); mi, ni = np.where(c == "moral")[0], np.where(c == "norm")[0]
            rec["group_size_equalised"] = g; rec["moral_vs_norm_equalised"] = float(np.mean([n_sig(X[rng.choice(mi, g, replace=False)], X[rng.choice(ni, g, replace=False)], a.perm_calib) for _ in range(a.subsamples)]))
            rec["norm_vs_norm_equalised"] = {"+".join(s1) + " vs " + "+".join(s2): float(np.mean([n_sig(X[rng.choice(np.where((c == "norm") & np.isin(s, s1))[0], g, replace=False)], X[rng.choice(np.where((c == "norm") & np.isin(s, s2))[0], g, replace=False)], a.perm_calib) for _ in range(a.subsamples)])) for s1, s2 in splits}
            top = max(rec["norm_vs_norm_equalised"].values())
            rec["reading"] = ("no feature detected in any comparison: no directional reading" if rec["moral_vs_norm_equalised"] == 0 and top == 0 else
                              ("moral vs norm yields no more features than norm kinds among themselves" if rec["moral_vs_norm_equalised"] <= top else "moral vs norm yields more features than any split of the norm kinds"))
        out["H6_discovery"][fr] = rec

    out["ablation"] = {}
    for fr in E:
        p = os.path.join(d, f"ablate__{fr}.npz")
        if not os.path.exists(p): continue
        Z = np.load(p); assert [str(i) for i in Z["ids"]] == [str(i) for i in E[fr]["ids"]], f"{p}: item ids differ from the extraction file"
        kp = keep[fr]; gap0 = G(fr, "perm_clean_S") - G(fr, "rest_clean_S"); inc = gap0 >= a.tau
        for name in [k[len("perm_"):-len("_S")] for k in Z.files if k.startswith("perm_") and k.endswith("_S") and not k.endswith("_hist_S")]:
            gap = Z[f"perm_{name}_S"][kp] - Z[f"rest_{name}_S"][kp]; dg = gap - gap0[:, None]; diff = dg[:, 0] - dg[:, 1:].mean(1); rec = {}
            for cc in ("moral", "norm", "descr"):
                m = (cat[fr] == cc) & inc
                if m.sum() < 5: continue
                bs = [diff[m][rng.integers(0, m.sum(), m.sum())].mean() for _ in range(a.boot)]
                rec[cc] = dict(n=int(m.sum()), gap_change_set=float(dg[m, 0].mean()), gap_change_random=float(dg[m, 1:].mean()), set_minus_random=float(diff[m].mean()), ci95=[float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))],
                               removed_norm_set=float(Z[f"rest_{name}_removed_norm"][kp][m, 0].mean()), removed_norm_random=float(Z[f"rest_{name}_removed_norm"][kp][m, 1:].mean()))
            out["ablation"][f"{fr}/{name}"] = rec
    summary[cond] = out; json.dump(h6_sets, open(os.path.join(a.out, f"h6_sets__{cond}.json"), "w"))
    report += [f"## {cond}", ""]
    for fr, ft in out["final_token"].items():
        report += [f"Final token (frame {fr}): relative reconstruction error {ft['rel_reconstruction_error']:.3f}; splice mean |dS| {ft['splice_mean_abs_dS']:.3f}; pair difference captured R2 "
                   + ", ".join(f"{c} {v['R2']:.2f} (cos {v['cosine']:.2f})" for c, v in ft["capture"].items()) + ("  **flagged: feature-level nulls are uninformative in this frame**" if ft["flagged_uninformative"] else "")]
    report += [""]
    for name, rec in out["H5_frame_following"].items():
        report += [f"H5 {name} ({rec['n_features']} features): mean activation " + ", ".join(f"{k} {v:.4f}" for k, v in rec["mean_activation"].items())]
        for k in ("ratio_A1_descr_over_moral", "ratio_A1_norm_over_moral"):
            if k in rec: report += [f"  {k}: {rec[k]['ratio']:.2f} ({rec[k]['ci95'][0]:.2f} to {rec[k]['ci95'][1]:.2f}) -> {rec[k]['reading']}"]
    for fr, rec in out["H6_discovery"].items():
        report += [f"H6 frame {fr}: {rec['n_features_tested']} features tested; moral vs norm at full size: {rec['full_size']['n_significant']} significant" + (f"; equalised group size {rec['group_size_equalised']}: moral vs norm {rec['moral_vs_norm_equalised']:.1f}, norm vs norm " + ", ".join(f"{v:.1f}" for v in rec["norm_vs_norm_equalised"].values()) + f" -> {rec['reading']}" if "reading" in rec else "")]
    for k, rec in out["ablation"].items():
        report += [f"Ablation {k} (change of the behavioural gap): " + "; ".join(f"{c}: set {v['gap_change_set']:+.3f}, random {v['gap_change_random']:+.3f}, difference {v['set_minus_random']:+.3f} ({v['ci95'][0]:+.3f} to {v['ci95'][1]:+.3f}), removed norm set / random {v['removed_norm_set']:.2f} / {v['removed_norm_random']:.2f}" for c, v in rec.items())]
    report += [""]
summary = dict(settings=vars(a), accepted_pairs=PRIMARY_SET, pre_specified_analysis=PRE_SPECIFIED, n_items=len(ACC), conditions=summary)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
