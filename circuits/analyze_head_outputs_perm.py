"""Permutation p-values of the decoding analysis, corrected across models and frames."""
import argparse, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analyze_head_outputs_standard import reduce, labels, cv_score, TASKS, SEED


def holm(ps):
    order = np.argsort(ps); m = len(ps); adj = np.empty(m); run = 0.0
    for i, j in enumerate(order):
        run = max(run, min(1.0, (m - i) * ps[j])); adj[j] = run
    return adj


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/head_outputs_standard"); ap.add_argument("--rows", default="results/head_outputs_standard/rows.json")
    ap.add_argument("--out", default="results/head_outputs_perm"); ap.add_argument("--n-perm", type=int, default=600); ap.add_argument("--models", nargs="*", default=None)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    obs = {(r["model"], r["frame"], r["task"]): r for r in json.load(open(a.rows))}; out = []
    for d in sorted(glob.glob(os.path.join(a.runs, "*"))):
        tag = os.path.basename(d)
        if a.models and tag not in a.models: continue
        for p in sorted(glob.glob(os.path.join(d, "*.npz"))):
            z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"])); frame = meta["frame"]; rows = meta["rows"]
            groups = np.array([r["id"] for r in rows]); deep = max(l for l, h in meta["located"]) + 1
            F = {"located write": reduce(z["wD10"].astype(np.float64)), "hidden, after": reduce(z["h"][:, deep].astype(np.float64))}
            for task in TASKS:
                lab = labels(rows, task); keep = np.array([x is not None for x in lab]); cls = sorted(set(x for x in lab if x is not None))
                y = np.array([cls.index(x) for x in np.array(lab, dtype=object)[keep]]); g = groups[keep]; ncls = len(cls)
                ug = np.unique(g); gl = {x: y[g == x][0] for x in ug}; o = obs[(tag, frame, task)]
                for name, key in (("located write", "located write"), ("hidden, after", "hidden, after")):
                    rng = np.random.default_rng(SEED + 1); null = []
                    for _ in range(a.n_perm):
                        perm = rng.permutation([gl[x] for x in ug]); m = dict(zip(ug, perm)); yp = np.array([m[x] for x in g])
                        null.append(cv_score(F[name][keep], yp, g, ncls, rng, reps=1))
                    null = np.array(null); ob = o[key]
                    out.append(dict(model=tag, frame=frame, task=task, feature=name, observed=ob, null_max=float(null.max()), null_95=float(np.percentile(null, 95)),
                                    null_mean=float(null.mean()), n_perm=a.n_perm, p=float((1 + (null >= ob).sum()) / (1 + a.n_perm))))
                    print(f"[perm] {tag} {frame} {task} {name}: observed {ob:.3f}, null max {null.max():.3f}, p {out[-1]['p']:.4f}", flush=True)
    summary = {}
    for name in ("located write", "hidden, after"):
        rr = [r for r in out if r["feature"] == name]
        if not rr: continue
        for task in TASKS:
            t = [r for r in rr if r["task"] == task]
            for r, q in zip(t, holm(np.array([r["p"] for r in t]))): r["holm_task"] = float(q)
            summary[f"{name}/{task}"] = dict(tests=len(t), survive_holm_task=sum(r["holm_task"] < 0.05 for r in t),
                                             lowest_observed=min(r["observed"] for r in t), highest_null_max=max(r["null_max"] for r in t), largest_p=max(r["p"] for r in t))
    json.dump(dict(settings=vars(a), note="exploratory", summary=summary, rows=out), open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    L = ["# Permutation p-values of the decoding analysis, Holm-corrected across models and frames (exploratory)", "", f"{a.n_perm} permutations per test.", "",
         "| feature / task | tests | survive Holm (task) | lowest observed | highest null maximum | largest p |", "|---|---|---|---|---|---|"]
    for k, s in summary.items():
        L.append(f"| {k} | {s['tests']} | {s['survive_holm_task']} | {s['lowest_observed']:.3f} | {s['highest_null_max']:.3f} | {s['largest_p']:.4f} |")
    open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))


if __name__ == "__main__":
    main()
