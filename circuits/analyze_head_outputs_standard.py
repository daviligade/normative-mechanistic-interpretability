"""Can the category of a pair be read from what the located heads write?"""
import argparse, json, os, glob
import numpy as np

K_PCA, RIDGE, N_FOLDS, N_REP, N_PERM, SEED = 32, 1.0, 5, 5, 100, 20261114
TASKS = ("moral_vs_norm", "standard5", "norm_vs_descr")


def reduce(X, seed=SEED, dim=256):
    X = (X - X.mean(0)) / (X.std(0) + 1e-6)
    if X.shape[1] <= dim: return X
    return X @ (np.random.default_rng(seed).standard_normal((X.shape[1], dim)) / np.sqrt(dim))


def labels(rows, task):
    out = []
    for r in rows:
        c, s = r["category"], r["subtype"]
        if task == "moral_vs_norm": out.append(None if c == "descr" else ("moral" if c == "moral" else "norm"))
        elif task == "standard5": out.append(None if c == "descr" else ("moral" if c == "moral" else s))
        else: out.append("descr" if c == "descr" else "norm")
    return out


def folds(groups, rng):
    g = np.unique(groups); rng.shuffle(g); f = {x: i % N_FOLDS for i, x in enumerate(g)}
    return np.array([f[x] for x in groups])


def fit_predict(Xtr, ytr, Xte, ncls):
    mu = Xtr.mean(0); sd = Xtr.std(0) + 1e-6; A = (Xtr - mu) / sd; B = (Xte - mu) / sd
    U, S, Vt = np.linalg.svd(A, full_matrices=False); k = min(K_PCA, Vt.shape[0]); V = Vt[:k].T
    P = A @ V; Q = B @ V; ps = P.std(0) + 1e-6; P /= ps; Q /= ps
    P = np.hstack([P, np.ones((len(P), 1))]); Q = np.hstack([Q, np.ones((len(Q), 1))])
    Y = -np.ones((len(ytr), ncls)); Y[np.arange(len(ytr)), ytr] = 1
    W = np.linalg.solve(P.T @ P + RIDGE * np.eye(P.shape[1]), P.T @ Y)
    return (Q @ W).argmax(1)


def bacc(y, p, ncls):
    return float(np.mean([np.mean(p[y == c] == c) for c in range(ncls) if (y == c).any()]))


def cv_score(X, y, groups, ncls, rng, reps=N_REP):
    out = []
    for _ in range(reps):
        fo = folds(groups, rng); pred = np.zeros_like(y)
        for k in range(N_FOLDS):
            tr, te = fo != k, fo == k
            pred[te] = fit_predict(X[tr], y[tr], X[te], ncls)
        out.append(bacc(y, pred, ncls))
    return float(np.mean(out))


def perm_null(X, y, groups, ncls, rng):
    g = np.unique(groups); lab = {x: y[groups == x][0] for x in g}; null = []
    for _ in range(N_PERM):
        perm = rng.permutation([lab[x] for x in g]); m = dict(zip(g, perm)); yp = np.array([m[x] for x in groups])
        null.append(cv_score(X, yp, groups, ncls, rng, reps=1))
    return float(np.percentile(null, 95)), float(np.mean(null))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/head_outputs_standard"); ap.add_argument("--out", default="results/head_outputs_standard")
    ap.add_argument("--no-perm", action="store_true", help="skip the permutation null (quick look)")
    args = ap.parse_args(); os.makedirs(args.out, exist_ok=True); rows_out = []
    for d in sorted(glob.glob(os.path.join(args.runs, "*"))):
        tag = os.path.basename(d)
        for p in sorted(glob.glob(os.path.join(d, "*.npz"))):
            z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"])); frame = meta["frame"]; rows = meta["rows"]
            groups = np.array([r["id"] for r in rows]); deep = max(l for l, h in meta["located"]) + 1
            F = {"located write": reduce(z["wD10"].astype(np.float64)), "located z": reduce(z["zD10"].reshape(len(rows), -1).astype(np.float64)),
                 "hidden, after": reduce(z["h"][:, deep].astype(np.float64)), "hidden, last": reduce(z["h"][:, -1].astype(np.float64))}
            wR0 = z["wR"]; wR = np.stack([reduce(wR0[:, r].astype(np.float64)) for r in range(wR0.shape[1])], 1); H0 = z["h"]
            H = np.stack([reduce(H0[:, l].astype(np.float64)) for l in range(H0.shape[1])], 1)
            for task in TASKS:
                lab = labels(rows, task); keep = np.array([x is not None for x in lab]); cls = sorted(set(x for x in lab if x is not None))
                y = np.array([cls.index(x) for x in np.array(lab, dtype=object)[keep]]); g = groups[keep]; ncls = len(cls)
                rng = np.random.default_rng(SEED); res = {k: cv_score(v[keep], y, g, ncls, rng) for k, v in F.items()}
                rnd = [cv_score(wR[keep, r], y, g, ncls, rng) for r in range(wR.shape[1])]
                curve = [cv_score(H[keep, l], y, g, ncls, rng, reps=1) for l in range(H.shape[1])]
                row = {"model": tag, "frame": frame, "task": task, "classes": cls, "n_prompts": int(keep.sum()), "chance": 1 / ncls, "deepest_located_layer": deep - 1, **res,
                       "random_write": rnd, "random_median": float(np.median(rnd)), "random_max": float(np.max(rnd)), "random_min": float(np.min(rnd)),
                       "rank_located_write": int(sum(r >= res["located write"] for r in rnd)), "hidden_by_layer": curve}
                if not args.no_perm:
                    row["perm95_located_write"], row["perm_mean_located_write"] = perm_null(F["located write"][keep], y, g, ncls, rng)
                    row["perm95_hidden_after"], _ = perm_null(F["hidden, after"][keep], y, g, ncls, rng)
                rows_out.append(row)
                print(f"[standard] {tag} {frame} {task}: located write {res['located write']:.3f} (random {np.median(rnd):.3f}, {min(rnd):.3f} to {max(rnd):.3f}); "
                      f"hidden after {res['hidden, after']:.3f}, last {res['hidden, last']:.3f}" + ("" if args.no_perm else f"; null 95th {row['perm95_located_write']:.3f}"), flush=True)
    json.dump(rows_out, open(os.path.join(args.out, "rows.json"), "w"))
    summ = {}
    for frame in sorted(set(r["frame"] for r in rows_out)):
        for task in TASKS:
            rr = [r for r in rows_out if r["frame"] == frame and r["task"] == task]
            if not rr: continue
            s = {"models": len(rr), "median_located_write": float(np.median([r["located write"] for r in rr])), "median_located_z": float(np.median([r["located z"] for r in rr])),
                 "median_random_write": float(np.median([r["random_median"] for r in rr])), "median_hidden_after": float(np.median([r["hidden, after"] for r in rr])),
                 "median_hidden_last": float(np.median([r["hidden, last"] for r in rr])),
                 "located_above_every_random": sum(r["rank_located_write"] == 0 for r in rr), "located_below_every_random": sum(r["rank_located_write"] == len(r["random_write"]) for r in rr)}
            if "perm95_located_write" in rr[0]:
                s["located_above_null"] = sum(r["located write"] > r["perm95_located_write"] for r in rr); s["hidden_after_above_null"] = sum(r["hidden, after"] > r["perm95_hidden_after"] for r in rr)
            summ[f"{frame}/{task}"] = s
    json.dump(summ, open(os.path.join(args.out, "summary.json"), "w"), indent=1)
    with open(os.path.join(args.out, "report.md"), "w") as fh:
        fh.write("# Can the standard be read from what the located heads write?\n\nBalanced accuracy, 5 grouped folds x 5 repeats, 32 principal components, ridge 1.0.\n\n## Per frame and task (medians over models)\n\n")
        fh.write("| frame / task | models | located write | located z | random write | hidden after | hidden last | located above null | located above every random | below every random |\n|---|---|---|---|---|---|---|---|---|---|\n")
        for k, s in summ.items():
            fh.write(f"| {k} | {s['models']} | {s['median_located_write']:.3f} | {s['median_located_z']:.3f} | {s['median_random_write']:.3f} | {s['median_hidden_after']:.3f} | {s['median_hidden_last']:.3f} | {s.get('located_above_null', 'n/a')} | {s['located_above_every_random']} | {s['located_below_every_random']} |\n")
        fh.write("\n## Per model\n\n| model | frame | task | chance | located write | null 95th | random median (min to max) | rank | hidden after | hidden last |\n|---|---|---|---|---|---|---|---|---|---|\n")
        for r in rows_out:
            fh.write(f"| {r['model']} | {r['frame']} | {r['task']} | {r['chance']:.2f} | {r['located write']:.3f} | {r.get('perm95_located_write', float('nan')):.3f} | {r['random_median']:.3f} ({r['random_min']:.3f} to {r['random_max']:.3f}) | {r['rank_located_write']} | {r['hidden, after']:.3f} | {r['hidden, last']:.3f} |\n")
    print("[standard] analysis written to", args.out, flush=True)


if __name__ == "__main__":
    main()
