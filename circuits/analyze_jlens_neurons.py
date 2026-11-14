"""The neuron lists seen through the Jacobian lens."""
import argparse, csv, glob, json, os
import numpy as np

ap = argparse.ArgumentParser(); ap.add_argument("--weights", default="runs/jlens"); ap.add_argument("--units", default="runs/units_contrast"); ap.add_argument("--contrasts", nargs="+", default=["mvn", "stance", "normdescr"])
ap.add_argument("--out", default="results/jlens_neurons"); ap.add_argument("--decile", type=float, default=90.0)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
summary = {}; rows = []; report = ["# Neuron lists and their transported weight on the answer (exploratory)", ""]
for wpath in sorted(glob.glob(os.path.join(a.weights, "*", "neuron_weights.npz"))):
    model = os.path.basename(os.path.dirname(wpath)); Wz = np.load(wpath, allow_pickle=False); L = int(Wz["n_layers"]); summary[model] = {}; report += [f"## {model}", ""]
    thr = {k: np.array([np.percentile(np.abs(Wz[k][l]), a.decile) for l in range(L)]) for k in ("answer_transported", "answer_direct", "category_transported", "category_direct")}
    for contrast in a.contrasts:
        for sp in sorted(glob.glob(os.path.join(a.units, contrast, model, "sets__*.json"))):
            S = json.load(open(sp)); fr = S["frame"]; units = {int(l): sorted(set(S["sets"]["selA"].get(str(l), [])) | set(S["sets"]["selB"].get(str(l), []))) for l in range(L)}
            n_tot = sum(len(v) for v in units.values())
            if n_tot == 0: continue
            agg = {k: 0 for k in thr}; signed = []
            for l, idx in units.items():
                if not idx: continue
                idx = np.array(idx); r = dict(model=model, contrast=contrast, frame=fr, layer=l, depth=round((l + 1) / L, 4), n_units=len(idx))
                for k in thr: hit = int((np.abs(Wz[k][l][idx]) > thr[k][l]).sum()); agg[k] += hit; r[f"top_decile_{k}"] = round(hit / len(idx), 3)
                r["mean_signed_answer_transported"] = float(Wz["answer_transported"][l][idx].mean()); r["mean_abs_answer_transported_vs_layer"] = float(np.abs(Wz["answer_transported"][l][idx]).mean() / (np.abs(Wz["answer_transported"][l]).mean() + 1e-12))
                signed.append(r["mean_signed_answer_transported"]); rows.append(r)
            rec = {f"share_top_decile_{k}": round(agg[k] / n_tot, 3) for k in thr}; rec.update(n_units=n_tot, n_layers_with_units=sum(1 for v in units.values() if v), chance=round(1 - a.decile / 100, 2))
            summary[model][f"{contrast}/{fr}"] = rec
            report += [f"* {contrast}, {fr}: {n_tot} listed units; in the top decile of |weight on the answer|: transported {rec['share_top_decile_answer_transported']:.2f}, direct {rec['share_top_decile_answer_direct']:.2f} (chance 0.10); "
                       f"on the category direction: transported {rec['share_top_decile_category_transported']:.2f}, direct {rec['share_top_decile_category_direct']:.2f}"]
    report += [""]
with open(os.path.join(a.out, "by_layer.csv"), "w", newline="") as f:
    if rows: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
