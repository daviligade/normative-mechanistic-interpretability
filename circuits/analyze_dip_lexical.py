"""Whether the dip follows the valence of the stem's words."""
import argparse, glob, json, os, re, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from run_word_valence import content_words
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--lens", default="runs/logit_lens"); ap.add_argument("--words", default="runs/word_valence"); ap.add_argument("--layers", default="runs/circuits/layers")
ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/dip_lexical"); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=5000)
ap.add_argument("--readout", default="S"); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--any-items", action="store_true"); ap.add_argument("--min-n", type=int, default=10, help="minimum included moral and norm pairs per model and frame")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}; PRIMARY_SET, WHY = primary_item_set(a.items)


def dip_of(tr):
    n = len(tr); half = n // 2; late = tr[half:-1]; m = half + int(np.argmin(late)); peak = tr[:m].max() if m > 0 else tr[0]
    return float(peak - tr[m]), m / (n - 1)


def ols(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None); return beta


def spearman(x, y):
    if len(x) < 5: return None
    rx = np.argsort(np.argsort(x)); ry = np.argsort(np.argsort(y)); return float(np.corrcoef(rx, ry)[0, 1])


def fit(rows, covs):
    y = np.array([r["dip"] for r in rows]); cat = np.array([r["cat"] for r in rows])
    X = np.column_stack([np.ones(len(rows)), cat == "moral", cat == "descr"] + [np.array([r[c] for r in rows]) for c in covs]).astype(float)
    un = y[cat == "moral"].mean() - y[cat == "norm"].mean(); ad = ols(X, y)[1]
    return float(un), float(ad)


def boot_fit(rows, covs):
    cats = {c: [r for r in rows if r["cat"] == c] for c in ("moral", "norm", "descr")}; U, A = [], []
    for _ in range(a.boot):
        s = sum(([cats[c][i] for i in rng.integers(0, len(cats[c]), len(cats[c]))] for c in cats if cats[c]), [])
        u, ad = fit(s, covs); U.append(u); A.append(ad)
    return [float(np.percentile(U, 2.5)), float(np.percentile(U, 97.5))], [float(np.percentile(A, 2.5)), float(np.percentile(A, 97.5))]


summary = dict(settings=vars(a), accepted_pairs=PRIMARY_SET, models={}); report = ["# The dip and the words (exploratory)", "", f"Items: {WHY}. Inclusion gap >= {a.tau}. Word valence: frame B, run alone.", ""]
readings = {"A1": {}, "B": {}}
for d in sorted(glob.glob(os.path.join(a.lens, "*"))):
    model = os.path.basename(d); wp = os.path.join(a.words, model, "words__B.json")
    if not os.path.isdir(d) or not os.path.exists(wp): continue
    W = {w: v[a.readout] for w, v in json.load(open(wp))["values"].items()}; rec = {}; report += [f"## {model}", ""]
    for fr in ("A1", "B"):
        rows = []
        for p in sorted(glob.glob(os.path.join(d, f"{fr}__*.npz"))):
            z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"])); it = ACC.get(meta["id"])
            if it is None: continue
            pt, rt = z[f"perm_{a.readout}"].astype(float), z[f"rest_{a.readout}"].astype(float); gap = pt[-1] - rt[-1]
            if gap < a.tau: continue
            vals = [W[w[0].upper() + w[1:]] for w in content_words(it["perm_stem"]) if (w[0].upper() + w[1:]) in W]
            if not vals: continue
            dip, depth = dip_of(pt); row = dict(id=meta["id"], cat=meta["category"], dip=dip, dip_depth=depth, gap=float(gap), minS=float(min(vals)), meanS=float(np.mean(vals)), fracneg=float(np.mean(np.array(vals) < 0)), L=len(pt) - 1)
            lp = os.path.join(a.layers, model, f"{fr}__{meta['id']}.npz")
            if os.path.exists(lp):
                y = np.load(lp, allow_pickle=False); g = float(y["perm_S"] - y["rest_S"])
                if g > 0:
                    frac = (y["p2r_resid_final_S"].astype(float) - float(y["rest_S"])) / g; hit = np.where(frac >= 0.5)[0]
                    row["arrival_depth"] = float((hit[0] + 1) / len(frac)) if len(hit) else 1.0
            rows.append(row)
        if sum(r["cat"] == "moral" for r in rows) < a.min_n or sum(r["cat"] == "norm" for r in rows) < a.min_n: continue
        out = dict(n={c: sum(r["cat"] == c for r in rows) for c in ("moral", "norm", "descr")},
                   word_negativity={c: dict(minS_mean=float(np.mean([r["minS"] for r in rows if r["cat"] == c])), meanS_mean=float(np.mean([r["meanS"] for r in rows if r["cat"] == c])), fracneg_mean=float(np.mean([r["fracneg"] for r in rows if r["cat"] == c]))) for c in ("moral", "norm", "descr") if any(r["cat"] == c for r in rows)},
                   dip_mean={c: float(np.mean([r["dip"] for r in rows if r["cat"] == c])) for c in ("moral", "norm", "descr") if any(r["cat"] == c for r in rows)})
        for name, covs in (("minS", ["minS"]), ("minS+meanS", ["minS", "meanS"])):
            un, ad = fit(rows, covs); ciu, cia = boot_fit(rows, covs)
            out[f"adjusted_for_{name}"] = dict(unadjusted_moral_minus_norm=un, unadjusted_ci95=ciu, adjusted_moral_minus_norm=ad, adjusted_ci95=cia)
        out["spearman_dip_vs_minS"] = {c: spearman([r["dip"] for r in rows if r["cat"] == c], [r["minS"] for r in rows if r["cat"] == c]) for c in ("moral", "norm")}
        out["spearman_dip_vs_minS"]["all"] = spearman([r["dip"] for r in rows], [r["minS"] for r in rows])
        m1 = out["adjusted_for_minS"]; un, ad, cia = m1["unadjusted_moral_minus_norm"], m1["adjusted_moral_minus_norm"], m1["adjusted_ci95"]
        reading = "lexical" if (abs(ad) < 0.5 * abs(un) and cia[0] <= 0 <= cia[1]) else ("moral content" if cia[0] > 0 else "mixed")
        if un <= 0: reading = "no moral excess to explain"
        out["reading"] = reading; readings[fr][model] = reading

        T = [r for r in rows if "arrival_depth" in r]
        if T:
            out["timing"] = {}
            for c in ("moral", "norm"):
                Tc = [r for r in T if r["cat"] == c and r["dip"] > 0.01]
                if len(Tc) < 5: continue
                dd = np.array([r["dip_depth"] for r in Tc]); ad_ = np.array([r["arrival_depth"] for r in Tc])
                out["timing"][c] = dict(n=len(Tc), dip_depth_median=float(np.median(dd)), arrival_depth_median=float(np.median(ad_)), frac_minimum_before_arrival=float(np.mean(dd < ad_)),
                                        frac_arrival_at_or_before_half=float(np.mean(ad_ <= 0.5)), spearman_dip_depth_vs_arrival=spearman(dd, ad_))
        rec[fr] = out
        report += [f"* {fr}: dip means moral {out['dip_mean'].get('moral', float('nan')):.3f}, norm {out['dip_mean'].get('norm', float('nan')):.3f}; word negativity (minS) moral {out['word_negativity']['moral']['minS_mean']:+.3f}, norm {out['word_negativity']['norm']['minS_mean']:+.3f}"
                   + (f", descr {out['word_negativity']['descr']['minS_mean']:+.3f}" if "descr" in out["word_negativity"] else ""),
                   f"  moral - norm dip: unadjusted {un:+.3f} [{m1['unadjusted_ci95'][0]:+.3f}, {m1['unadjusted_ci95'][1]:+.3f}]; adjusted for minS {ad:+.3f} [{cia[0]:+.3f}, {cia[1]:+.3f}]; adjusted for minS and meanS {out['adjusted_for_minS+meanS']['adjusted_moral_minus_norm']:+.3f} -> {reading}",
                   "  rank correlation of the dip with minS: " + ", ".join(f"{k} {v:+.2f}" if v is not None else f"{k} --" for k, v in out["spearman_dip_vs_minS"].items())]
        for c, t in out.get("timing", {}).items():
            report += [f"  timing ({c}, n={t['n']}): dip minimum at depth {t['dip_depth_median']:.2f} (median), edit arrives at {t['arrival_depth_median']:.2f}; minimum before arrival in {t['frac_minimum_before_arrival']:.0%} of pairs; arrival at or before half depth in {t['frac_arrival_at_or_before_half']:.0%} (there the dip window starts after the arrival by construction); rank corr. {t['spearman_dip_depth_vs_arrival'] if t['spearman_dip_depth_vs_arrival'] is None else round(t['spearman_dip_depth_vs_arrival'], 2)}"]
    summary["models"][model] = rec; report += [""]
report += ["## Count of models per reading", ""]
for fr in ("A1", "B"):
    cnt = {}
    for v in readings[fr].values(): cnt[v] = cnt.get(v, 0) + 1
    report += [f"* frame {fr}: " + ", ".join(f"{k} {v}" for k, v in sorted(cnt.items()))]
summary["readings"] = readings
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
