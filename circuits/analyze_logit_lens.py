"""The dip of the score in the logit lens."""
import argparse, csv, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/logit_lens"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/logit_lens")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--readout", default="S"); ap.add_argument("--seed", type=int, default=20260920)
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}; PRIMARY_SET, WHY = primary_item_set(a.items)
CATS = ("moral", "norm", "descr")


def dip_of(tr):
    n = len(tr); half = n // 2; late = tr[half:-1]; m = half + int(np.argmin(late)); peak = tr[:m].max() if m > 0 else tr[0]
    return float(peak - tr[m]), bool(tr[m] < 0 and tr[-1] > 0), m / (n - 1)


def ci(vals, f=np.mean):
    v = np.asarray(vals, float); bs = [f(v[rng.integers(0, len(v), len(v))]) for _ in range(a.boot)]
    return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


MIN_DEN = 0.005


def ratio_ci(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    bs = [x[rng.integers(0, len(x), len(x))].mean() / max(y[rng.integers(0, len(y), len(y))].mean(), 1e-9) for _ in range(a.boot)]
    return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def ratio_rec(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if y.mean() < MIN_DEN: return dict(ratio=None, note=f"denominator mean dip {y.mean():.4f} below {MIN_DEN}: ratio not reported")
    return dict(ratio=float(x.mean() / y.mean()), ci95=ratio_ci(x, y))


summary = dict(settings=vars(a), accepted_pairs=PRIMARY_SET, note="exploratory analysis", models={})
report = ["# Pre-commitment dip on the new pairs (exploratory)", "", f"Items: {WHY}; {len(ACC)} accepted pairs; inclusion gap >= {a.tau}; readout {a.readout}; dip on the permissive prompt.", ""]
traj_rows = []
for d in sorted(glob.glob(os.path.join(a.runs, "*"))):
    if not os.path.isdir(d): continue
    model = os.path.basename(d); per = {}
    for p in sorted(glob.glob(os.path.join(d, "*__*.npz"))):
        z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta["id"] not in ACC: continue
        per.setdefault(meta["frame"], []).append((meta, z[f"perm_{a.readout}"].astype(float), z[f"rest_{a.readout}"].astype(float)))
    if not per: continue
    rec = {}
    for fr, rows in sorted(per.items()):
        rec[fr] = {}
        for c in CATS:
            R = [(m, pt, rt) for m, pt, rt in rows if m["category"] == c]; gaps = np.array([pt[-1] - rt[-1] for _, pt, rt in R]); inc = gaps >= a.tau
            if inc.sum() == 0: continue
            D = [dip_of(pt) for (_, pt, _), ok in zip(R, inc) if ok]; dips = np.array([x[0] for x in D]); rev = np.array([x[1] for x in D]); depth = np.array([x[2] for x in D])
            L = len(R[0][1]) - 1; mean_perm = np.mean([pt for (_, pt, _), ok in zip(R, inc) if ok], 0); mean_rest = np.mean([rt for (_, _, rt), ok in zip(R, inc) if ok], 0)
            rec[fr][c] = dict(n_rated=len(R), n_included=int(inc.sum()), mean_gap=float(gaps[inc].mean()), dip_mean=float(dips.mean()), dip_mean_ci95=ci(dips), dip_median=float(np.median(dips)),
                              dip_over_gap=float(dips.mean() / max(gaps[inc].mean(), 1e-9)), dip_over_gap_ci95=ratio_ci(dips, gaps[inc]), sign_reversal_rate=float(rev.mean()),
                              depth_of_late_minimum_median=float(np.median(depth)), n_layers=L, _dips=dips.tolist())
            for l in range(L + 1): traj_rows.append(dict(model=model, frame=fr, category=c, layer=l, depth=round(l / L, 4), mean_perm=round(float(mean_perm[l]), 5), mean_rest=round(float(mean_rest[l]), 5), n=int(inc.sum())))

    comp = {}
    for c in ("moral", "norm"):
        if "A1" in rec and "B" in rec and c in rec["A1"] and c in rec["B"]:
            comp[f"{c}: dip B / dip A1"] = ratio_rec(rec["B"][c]["_dips"], rec["A1"][c]["_dips"])
    for fr in rec:
        if "moral" in rec[fr] and "norm" in rec[fr]:
            comp[f"{fr}: dip moral / dip norm"] = ratio_rec(rec[fr]["moral"]["_dips"], rec[fr]["norm"]["_dips"])
            xg, yg = rec[fr]["moral"]["dip_over_gap"], rec[fr]["norm"]["dip_over_gap"]; comp[f"{fr}: (dip/gap) moral / (dip/gap) norm"] = dict(ratio=float(xg / yg) if yg >= MIN_DEN else None)
    for fr in rec:
        for c in rec[fr]: rec[fr][c].pop("_dips")
    summary["models"][model] = dict(per_frame=rec, comparisons=comp)
    report += [f"## {model}", ""]
    for fr in rec:
        for c, v in rec[fr].items():
            report += [f"* {fr} {c}: {v['n_included']} of {v['n_rated']} included; mean gap {v['mean_gap']:.3f}; dip mean {v['dip_mean']:.3f} [{v['dip_mean_ci95'][0]:.3f}, {v['dip_mean_ci95'][1]:.3f}], median {v['dip_median']:.3f}; "
                       f"dip / gap {v['dip_over_gap']:.2f} [{v['dip_over_gap_ci95'][0]:.2f}, {v['dip_over_gap_ci95'][1]:.2f}]; sign reversals {v['sign_reversal_rate']:.2f}; late minimum at depth {v['depth_of_late_minimum_median']:.2f}"]
    for k, v in comp.items(): report += [f"* {k}: " + (f"{v['ratio']:.2f}" + (f" [{v['ci95'][0]:.2f}, {v['ci95'][1]:.2f}]" if "ci95" in v else "") if v.get("ratio") is not None else "not reported (" + v.get("note", "denominator near zero") + ")")]
    report += [""]

M = summary["models"]
if M:
    report += ["## Over models (medians)", ""]
    for key in ("moral: dip B / dip A1", "norm: dip B / dip A1", "A1: dip moral / dip norm", "B: dip moral / dip norm"):
        v = [m["comparisons"][key]["ratio"] for m in M.values() if key in m["comparisons"] and m["comparisons"][key].get("ratio") is not None]
        if v: report += [f"* {key}: median {np.median(v):.2f} (range {min(v):.2f} to {max(v):.2f}; {len(v)} models)"]; summary.setdefault("over_models", {})[key] = dict(median=float(np.median(v)), min=float(min(v)), max=float(max(v)), n_models=len(v))
    for fr in ("A1", "B"):
        for c in CATS:
            v = [m["per_frame"][fr][c]["dip_over_gap"] for m in M.values() if fr in m["per_frame"] and c in m["per_frame"][fr]]
            if v: report += [f"* {fr} {c}: dip / gap median over models {np.median(v):.2f} (range {min(v):.2f} to {max(v):.2f})"]; summary.setdefault("over_models", {})[f"{fr} {c}: dip/gap"] = dict(median=float(np.median(v)), min=float(min(v)), max=float(max(v)), n_models=len(v))
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n")
with open(os.path.join(a.out, "trajectories_mean.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["model", "frame", "category", "layer", "depth", "mean_perm", "mean_rest", "n"]); w.writeheader(); w.writerows(traj_rows)
print("\n".join(report))
