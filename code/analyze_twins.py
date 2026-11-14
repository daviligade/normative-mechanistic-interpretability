"""The models' answers on the twins."""
import argparse, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import check_analysis_items

ap = argparse.ArgumentParser(); ap.add_argument("--items", required=True); ap.add_argument("--runs", nargs="*", default=[], help="unit-ablation run folders on the twin items"); ap.add_argument("--heads", default=None, help="head run folder on the twin items")
ap.add_argument("--located", default="located/heads.json"); ap.add_argument("--out", default="results/twins"); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
ITEMS = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True) and "twin" in i}
TW = {}
for i in ITEMS.values(): TW.setdefault(i["twin"], {})["m" if i["category"] == "moral" else "t"] = i["id"]
TW = {k: v for k, v in TW.items() if "m" in v and "t" in v}; print(f"[twins] {len(TW)} complete twins among {len(ITEMS)} items", flush=True)


def ci(v):
    v = np.asarray(v, float); bs = v[rng.integers(0, len(v), (a.boot, len(v)))].mean(1); return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def paired(d):
    d = [x for x in d if x is not None and np.isfinite(x)]
    return dict(n=len(d), mean=float(np.mean(d)), ci95=ci(d)) if len(d) >= 5 else None


summary = {}; report = ["# Twin test: the same scenario and edit, moral member against its prudential/epistemic twin (exploratory)", "", f"{len(TW)} complete twins.", ""]

for rd in a.runs:
    for d in sorted(glob.glob(os.path.join(rd, "*"))):
        model = os.path.basename(d); files = {os.path.basename(p)[:-4]: p for p in glob.glob(os.path.join(d, "*__*.npz"))}
        if not files: continue
        frames = sorted({k.split("__")[0] for k in files}); summary.setdefault(model, {})
        for fr in frames:
            z0 = np.load(next(p for k, p in files.items() if k.startswith(fr + "__")), allow_pickle=False); lists = json.loads(str(z0["__meta__"]))["lists"]
            gaps = {}; eff = {name: {} for name in lists}
            for iid in ITEMS:
                p = files.get(f"{fr}__{iid}")
                if not p: continue
                z = np.load(p, allow_pickle=False); gap0 = float(z["perm_clean_S"] - z["rest_clean_S"]); gaps[iid] = gap0
                if gap0 < a.tau: continue
                for name in lists:
                    g = z[f"perm_{name}_S"] - z[f"rest_{name}_S"]; dg = g - gap0; eff[name][iid] = float((dg[0] - dg[1:].mean()) / gap0)
            rec = dict(n_twins_with_runs=sum(1 for v in TW.values() if v["m"] in gaps and v["t"] in gaps), gap_moral_minus_twin=paired([gaps.get(v["m"]) - gaps.get(v["t"]) if v["m"] in gaps and v["t"] in gaps else None for v in TW.values()]),
                       gap_mean_moral=float(np.mean([gaps[v["m"]] for v in TW.values() if v["m"] in gaps])) if gaps else None, gap_mean_twin=float(np.mean([gaps[v["t"]] for v in TW.values() if v["t"] in gaps])) if gaps else None, lists={})
            for name in lists:
                pr = paired([eff[name].get(v["m"]) - eff[name].get(v["t"]) if v["m"] in eff[name] and v["t"] in eff[name] else None for v in TW.values()])
                if pr: pr["moral_specific"] = bool(pr["ci95"][1] < 0); pr["mean_moral"] = float(np.mean([eff[name][v["m"]] for v in TW.values() if v["m"] in eff[name]])); pr["mean_twin"] = float(np.mean([eff[name][v["t"]] for v in TW.values() if v["t"] in eff[name]]))
                rec["lists"][name] = pr
            summary[model][f"{os.path.basename(rd.rstrip('/'))}/{fr}"] = rec
            g_ = rec["gap_moral_minus_twin"]
            report += [f"* {model}, {os.path.basename(rd.rstrip('/'))}, {fr}: {rec['n_twins_with_runs']} twins; clean gap moral {rec['gap_mean_moral']:.3f} vs twin {rec['gap_mean_twin']:.3f} (paired {g_['mean']:+.3f} [{g_['ci95'][0]:+.3f}, {g_['ci95'][1]:+.3f}])" if g_ else f"* {model}, {fr}: too few twins"]
            for name, pr in rec["lists"].items():
                if pr: report += [f"    {name}: relative fall moral {100 * pr['mean_moral']:+.1f}% vs twin {100 * pr['mean_twin']:+.1f}%; paired {100 * pr['mean']:+.1f}% [{100 * pr['ci95'][0]:+.1f}, {100 * pr['ci95'][1]:+.1f}] -> {'MORAL-SPECIFIC across twins' if pr['moral_specific'] else 'not specific'}"]

if a.heads and os.path.exists(a.located):
    FZ = json.load(open(a.located))
    for d in sorted(glob.glob(os.path.join(a.heads, "*"))):
        model = os.path.basename(d)
        if model not in FZ: continue
        H = FZ[model]["n_heads"]; idx = np.array([l * H + h for l, h in FZ[model]["located"]]); files = {os.path.basename(p)[:-4]: p for p in glob.glob(os.path.join(d, "*__*.npz"))}
        frames = sorted({k.split("__")[0] for k in files}); summary.setdefault(model, {})
        for fr in frames:
            share = {}; gaps = {}
            for iid in ITEMS:
                p = files.get(f"{fr}__{iid}")
                if not p: continue
                z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"])); key = "p2r_all__S"
                if key not in z.files: continue
                E = np.abs(z[key]).ravel(); tot = E.sum(); gap0 = meta["base_perm"]["S"] - meta["base_rest"]["S"]; gaps[iid] = gap0
                if gap0 >= a.tau and tot > 0: share[iid] = float(E[idx].sum() / tot)
            pr = paired([share.get(v["m"]) - share.get(v["t"]) if v["m"] in share and v["t"] in share else None for v in TW.values()])
            if pr:
                pr["moral_specific"] = bool(pr["ci95"][0] > 0); pr["mean_moral"] = float(np.mean([share[v["m"]] for v in TW.values() if v["m"] in share])); pr["mean_twin"] = float(np.mean([share[v["t"]] for v in TW.values() if v["t"] in share]))
                pr["ratio_moral_over_twin"] = pr["mean_moral"] / pr["mean_twin"] if pr["mean_twin"] else None
                summary[model][f"heads_located/{fr}"] = pr
                report += [f"* {model}, located head share, {fr}: moral {pr['mean_moral']:.3f} vs twin {pr['mean_twin']:.3f} (ratio {pr['ratio_moral_over_twin']:.2f}); paired {pr['mean']:+.4f} [{pr['ci95'][0]:+.4f}, {pr['ci95'][1]:+.4f}] -> {'MORAL-SPECIFIC across twins' if pr['moral_specific'] else 'not specific'}"]
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
