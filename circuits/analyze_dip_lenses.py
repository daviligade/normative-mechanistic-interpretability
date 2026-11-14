"""The dip of the score through the logit lens and the Jacobian lens."""
import argparse, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/dip_lenses")
ap.add_argument("--lenses", nargs="+", default=["logit_lens=runs/logit_lens", "jacobian=runs/jlens_readout"]); ap.add_argument("--tau", type=float, default=0.02)
ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}; PRIMARY_SET, WHY = primary_item_set(a.items); CATS = ("moral", "norm", "descr"); MIN_DEN = 0.005


def dip_of(tr):
    n = len(tr); half = n // 2; late = tr[half:-1]; m = half + int(np.argmin(late)); peak = tr[:m].max() if m > 0 else tr[0]
    return float(peak - tr[m]), bool(tr[m] < 0 and tr[-1] > 0)


def ratio(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) == 0 or len(y) == 0 or y.mean() < MIN_DEN: return None
    bx = x[rng.integers(0, len(x), (a.boot, len(x)))].mean(1); by = y[rng.integers(0, len(y), (a.boot, len(y)))].mean(1); r = bx / np.maximum(by, 1e-9)
    return dict(ratio=float(x.mean() / y.mean()), ci95=[float(np.percentile(r, 2.5)), float(np.percentile(r, 97.5))])


summary = dict(note="exploratory; the dip measure applied to the logit-lens and the Jacobian-lens trajectories, on the permissive prompt and on the gap", items=WHY, tau=a.tau, lenses={})
report = ["# The dip through two lenses (exploratory)", "", f"Items: {WHY}; inclusion gap >= {a.tau}. 'perm' = the dip measure on the permissive prompt's S; 'gap' = the same on S(perm) - S(rest). Values: mean dip / mean gap.", ""]
models_by_lens = {}
for spec in a.lenses:
    name, root = spec.split("=", 1); summary["lenses"][name] = {}
    for d in sorted(glob.glob(os.path.join(root, "*"))):
        if not os.path.isdir(d): continue
        model = os.path.basename(d); per = {}
        for p in glob.glob(os.path.join(d, "*__*.npz")):
            z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
            if meta["id"] not in ACC or "perm_S" not in z.files: continue
            per.setdefault(meta["frame"], {}).setdefault(meta["category"], []).append((z["perm_S"].astype(float), z["rest_S"].astype(float)))
        if not per: continue
        models_by_lens.setdefault(name, []).append(model); rec = {}
        for fr, bycat in sorted(per.items()):
            rec[fr] = {}; dips = {}
            for c in CATS:
                R = bycat.get(c, [])
                if not R: continue
                g = np.array([pt[-1] - rt[-1] for pt, rt in R]); inc = g >= a.tau
                if inc.sum() == 0: continue
                Dp = [dip_of(pt) for (pt, _), ok in zip(R, inc) if ok]; Dg = [dip_of(pt - rt) for (pt, rt), ok in zip(R, inc) if ok]
                dp = np.array([x for x, _ in Dp]); dg = np.array([x for x, _ in Dg]); dips[c] = (dp, dg)
                rec[fr][c] = dict(n_included=int(inc.sum()), mean_gap=float(g[inc].mean()), perm_dip_mean=float(dp.mean()), perm_dip_over_gap=float(dp.mean() / g[inc].mean()),
                                  gap_dip_mean=float(dg.mean()), gap_dip_over_gap=float(dg.mean() / g[inc].mean()), gap_over_perm_dip=float(dg.mean() / dp.mean()) if dp.mean() > MIN_DEN else None,
                                  perm_sign_reversals=float(np.mean([r for _, r in Dp])), gap_sign_reversals=float(np.mean([r for _, r in Dg])))
            if "moral" in dips and "norm" in dips:
                rec[fr]["moral_over_norm_perm"] = ratio(dips["moral"][0], dips["norm"][0]); rec[fr]["moral_over_norm_gap"] = ratio(dips["moral"][1], dips["norm"][1])
        summary["lenses"][name][model] = rec
fmt = lambda x: "  -  " if x is None else f"{x:5.2f}"
fr_ratio = lambda r: "not reported" if not r else f"{r['ratio']:.2f} [{r['ci95'][0]:.2f}, {r['ci95'][1]:.2f}]"
for model in sorted(set(m for v in models_by_lens.values() for m in v)):
    report += [f"## {model}", ""]
    for name in summary["lenses"]:
        rec = summary["lenses"][name].get(model)
        if not rec: continue
        for fr in sorted(rec):
            cells = "; ".join(f"{c} perm {fmt(rec[fr][c]['perm_dip_over_gap'])} gap {fmt(rec[fr][c]['gap_dip_over_gap'])}" for c in CATS if c in rec[fr])
            report += [f"* {name}, {fr}: {cells}; moral/norm mean dip: perm {fr_ratio(rec[fr].get('moral_over_norm_perm'))}, gap {fr_ratio(rec[fr].get('moral_over_norm_gap'))}"]
    report += [""]
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
