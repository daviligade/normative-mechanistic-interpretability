"""Category prompt and category readout on the twins."""
import argparse, json, os, glob
from math import comb
import numpy as np

K_PCA, RIDGE, DIM, SEED = 32, 1.0, 256, 20261114


def sign_p(k, n):
    return float(sum(comb(n, i) for i in range(k, n + 1)) / 2 ** n) if n else float("nan")


def twin_table(items_path):
    D = json.load(open(items_path)); items = D["items"] if isinstance(D, dict) else D
    tw = {}
    for it in items:
        e = tw.setdefault(it["twin"], {}); role = "moral" if it["category"] == "moral" else "other"
        e[role] = it["id"]; e[role + "_std"] = it["category"] if role == "moral" else it.get("subtype", ""); e[role + "_ok"] = str(it.get("accepted", "")).lower() == "true"
    tw = {k: v for k, v in tw.items() if "moral" in v and "other" in v}
    return tw


def paired(score_by_id, tw, keep):
    ks = [k for k in tw if keep(tw[k]) and tw[k]["moral"] in score_by_id and tw[k]["other"] in score_by_id]
    wins = sum(score_by_id[tw[k]["moral"]] > score_by_id[tw[k]["other"]] for k in ks)
    return len(ks), int(wins), (wins / len(ks) if ks else float("nan")), sign_p(wins, len(ks))


class Fit:
    def __init__(self, X, y):
        self.mu = X.mean(0); self.sd = X.std(0) + 1e-6; A = (X - self.mu) / self.sd
        self.R = np.random.default_rng(SEED).standard_normal((A.shape[1], DIM)) / np.sqrt(DIM) if A.shape[1] > DIM else None
        if self.R is not None: A = A @ self.R
        self.mu2 = A.mean(0); self.sd2 = A.std(0) + 1e-6; A = (A - self.mu2) / self.sd2
        U, S, Vt = np.linalg.svd(A, full_matrices=False); self.V = Vt[:K_PCA].T; P = A @ self.V; self.ps = P.std(0) + 1e-6; P = P / self.ps
        P = np.hstack([P, np.ones((len(P), 1))]); Y = np.where(y[:, None] == np.arange(2)[None, :], 1.0, -1.0)
        self.W = np.linalg.solve(P.T @ P + RIDGE * np.eye(P.shape[1]), P.T @ Y)

    def moral_score(self, X):
        A = (X - self.mu) / self.sd
        if self.R is not None: A = A @ self.R
        A = (A - self.mu2) / self.sd2; P = (A @ self.V) / self.ps; P = np.hstack([P, np.ones((len(P), 1))]); out = P @ self.W
        return out[:, 1] - out[:, 0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", default="stimuli/items_followup_twins_run.json"); ap.add_argument("--cat", default="runs/category_frame_twins")
    ap.add_argument("--main", default="runs/head_outputs_standard"); ap.add_argument("--twins", default="runs/head_outputs_standard_twins"); ap.add_argument("--out", default="results/twins_standard")
    args = ap.parse_args(); os.makedirs(args.out, exist_ok=True); tw = twin_table(args.items)
    subsets = {"all twins": lambda e: True, "both members passed": lambda e: e["moral_ok"] and e["other_ok"]}
    rows = []

    for d in sorted(glob.glob(os.path.join(args.cat, "*"))):
        p = os.path.join(d, "cat__fewshot.json")
        if not os.path.exists(p): continue
        R = json.load(open(p))["rows"]; tag = os.path.basename(d); moral, own = {}, {}
        std_of = {v["other"]: v["other_std"] for v in tw.values()}
        for r in R:
            if r["p_norm"] is None: continue
            moral.setdefault(r["id"], []).append(r["p_norm"].get("moral", 0.0))
            if r["id"] in std_of: own.setdefault(r["id"], []).append(r["p_norm"].get(std_of[r["id"]], 0.0))
        m = {k: float(np.mean(v)) for k, v in moral.items()}
        o = {}
        for k, v in tw.items():
            if v["other"] in own and v["moral"] in moral:
                mo = [r["p_norm"].get(v["other_std"], 0.0) for r in R if r["id"] == v["moral"] and r["p_norm"]]
                o[v["other"]] = -float(np.mean(own[v["other"]])); o[v["moral"]] = -float(np.mean(mo))
        for sname, keep in subsets.items():
            n, k, acc, pv = paired(m, tw, keep); n2, k2, acc2, pv2 = paired(o, tw, keep)
            rows.append({"part": "category prompt", "model": tag, "subset": sname, "feature": "moral words", "n_twins": n, "wins": k, "paired_accuracy": acc, "p": pv})
            rows.append({"part": "category prompt", "model": tag, "subset": sname, "feature": "words of the other standard", "n_twins": n2, "wins": k2, "paired_accuracy": acc2, "p": pv2})

    for d in sorted(glob.glob(os.path.join(args.twins, "*"))):
        tag = os.path.basename(d)
        for p in sorted(glob.glob(os.path.join(d, "*.npz"))):
            frame = os.path.basename(p)[:-4]; q = os.path.join(args.main, tag, f"{frame}.npz")
            if not os.path.exists(q): continue
            zt = np.load(p, allow_pickle=False); zm = np.load(q, allow_pickle=False)
            mt = json.loads(str(zt["__meta__"])); mm = json.loads(str(zm["__meta__"])); deep = max(l for l, h in mm["located"]) + 1
            keep = np.array([r["category"] != "descr" for r in mm["rows"]]); y = np.array([1 if r["category"] == "moral" else 0 for r in mm["rows"]])[keep]
            ids = [r["id"] for r in mt["rows"]]
            feats = {"located heads write": (zm["wD10"], zt["wD10"]), "hidden, after the located heads": (zm["h"][:, deep], zt["h"][:, deep]), "hidden, last layer": (zm["h"][:, -1], zt["h"][:, -1])}
            for r in range(zm["wR"].shape[1]): feats[f"random set {r:02d} write"] = (zm["wR"][:, r], zt["wR"][:, r])
            for fname, (Xm, Xt) in feats.items():
                f = Fit(Xm[keep].astype(np.float64), y); s = f.moral_score(Xt.astype(np.float64)); sc = {}
                for i, v in zip(ids, s): sc.setdefault(i, []).append(float(v))
                sc = {k: float(np.mean(v)) for k, v in sc.items()}
                for sname, kp in subsets.items():
                    n, k, acc, pv = paired(sc, tw, kp)
                    rows.append({"part": "transfer", "model": tag, "frame": frame, "subset": sname, "feature": fname, "n_twins": n, "wins": k, "paired_accuracy": acc, "p": pv})
    json.dump(rows, open(os.path.join(args.out, "rows.json"), "w"))
    with open(os.path.join(args.out, "report.md"), "w") as fh:
        fh.write("# Standard or topic? The twins\n\nPaired accuracy: share of twins in which the moral member gets the larger moral score (chance 0.5); models at p < 0.05 by a one-sided sign test.\n\n## Summary (medians over models)\n\n")
        fh.write("| part | frame | subset | feature | models | median paired accuracy | models with p < 0.05 |\n|---|---|---|---|---|---|---|\n")
        keys = sorted(set((r["part"], r.get("frame", "-"), r["subset"], r["feature"] if not r["feature"].startswith("random set") else "random sets (median of 20)") for r in rows))
        for part, frame, sub, feat in keys:
            if feat == "random sets (median of 20)":
                by = {}
                for r in rows:
                    if r["part"] == part and r.get("frame", "-") == frame and r["subset"] == sub and r["feature"].startswith("random set"): by.setdefault(r["model"], []).append(r)
                acc = [np.median([x["paired_accuracy"] for x in v]) for v in by.values()]; sig = [np.median([x["p"] < 0.05 for x in v]) >= 0.5 for v in by.values()]
                fh.write(f"| {part} | {frame} | {sub} | {feat} | {len(by)} | {np.median(acc):.3f} | {sum(sig)} (median set) |\n")
            else:
                rr = [r for r in rows if r["part"] == part and r.get("frame", "-") == frame and r["subset"] == sub and r["feature"] == feat]
                fh.write(f"| {part} | {frame} | {sub} | {feat} | {len(rr)} | {np.median([r['paired_accuracy'] for r in rr]):.3f} | {sum(r['p'] < 0.05 for r in rr)} |\n")
        fh.write("\n## Per model (not random sets)\n\n| part | model | frame | subset | feature | twins | wins | paired accuracy | p |\n|---|---|---|---|---|---|---|---|---|\n")
        for r in rows:
            if r["feature"].startswith("random set"): continue
            fh.write(f"| {r['part']} | {r['model']} | {r.get('frame', '-')} | {r['subset']} | {r['feature']} | {r['n_twins']} | {r['wins']} | {r['paired_accuracy']:.3f} | {r['p']:.3f} |\n")
    print("[twins] written to", args.out, flush=True)


if __name__ == "__main__":
    main()
