"""Check 07: head effects on Llama-3.2-1B for moral, control and same-frame norm pairs (from run 06): raw and share comparisons, the first located head and the head with the largest raw effects."""
import json, os
import numpy as np
from pairs_common import DATA, perm_test, shares, save

b = json.load(open(os.path.join(DATA, "replication", "scores_and_mlp.json")))["baseline"]
zm, zc = np.load(os.path.join(DATA, "heads", "Llama-3.2-1B", "head_effects.npz")), np.load(os.path.join(DATA, "heads", "Llama-3.2-1B", "control_head_effects.npz"))
zn = np.load(os.path.join(DATA, "replication", "heads_norm.npz")); nh = 32
M, C, N = (np.stack([np.abs(z[k]).ravel() for k in z.files]) for z in (zm, zc, zn))
eq = {s: np.array([b[k]["lp"] == b[k]["lr"] for k in z.files]) for s, z in (("M", zm), ("C", zc), ("N", zn))}
gap = {s: np.array([b[k]["sp"] - b[k]["sr"] for k in z.files]) for s, z in (("M", zm), ("C", zc), ("N", zn))}
HEADS = {"first located head": (7, 8), "largest raw effect": (8, 24)}
out = {"n": {"moral": len(M), "control": len(C), "norm": len(N)}, "n_equal_length": {k: int(v.sum()) for k, v in eq.items()},
       "mean_gap": {k: float(v.mean()) for k, v in gap.items()}, "mean_sum_abs_effect": {"moral": float(M.sum(1).mean()), "control": float(C.sum(1).mean()), "norm": float(N.sum(1).mean())}}
print(out)


def report(tag, A, B):
    obs, p, q = perm_test(A, B, 20000, 3); rec = {"ratio_all_heads": float(A.mean() / B.mean()), "frac_heads_a_gt_b": float((A.mean(0) > B.mean(0)).mean()), "n_significant": int((q < .05).sum()), "heads": {}}
    for name, (l, h) in HEADS.items():
        i = l * nh + h; rng = np.random.default_rng(0); bs = [A[rng.integers(0, len(A), len(A)), i].mean() / B[rng.integers(0, len(B), len(B)), i].mean() for _ in range(4000)]
        rec["heads"][f"L{l}H{h}"] = {"name": name, "ratio": float(A[:, i].mean() / B[:, i].mean()), "ci": [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))],
                                    "q": float(q[i]), "rank": int(np.where(np.argsort(-obs) == i)[0][0]) + 1}
    print(tag, json.dumps(rec)); return rec


for kind, f in (("raw", lambda X, s: X), ("shares", lambda X, s: shares(X))):
    out[kind] = {"moral_vs_control": report(f"{kind} moral vs control", f(M, "M"), f(C, "C")), "moral_vs_norm": report(f"{kind} moral vs norm", f(M, "M"), f(N, "N")),
                 "norm_vs_control": report(f"{kind} norm vs control", f(N, "N"), f(C, "C"))}
out["shares_equal_length"] = {"moral_vs_norm": report("shares, equal length, moral vs norm", shares(M[eq["M"]]), shares(N[eq["N"]])),
                              "norm_vs_control": report("shares, equal length, norm vs control", shares(N[eq["N"]]), shares(C[eq["C"]]))}
pm, pn, pc = shares(M).mean(0), shares(N).mean(0), shares(C).mean(0)
top = lambda v: {f"L{i // nh}H{i % nh}" for i in np.argsort(-v)[:10]}
out["profiles"] = {"r_moral_norm": float(np.corrcoef(pm, pn)[0, 1]), "r_moral_control": float(np.corrcoef(pm, pc)[0, 1]), "r_norm_control": float(np.corrcoef(pn, pc)[0, 1]),
                   "top10_moral": sorted(top(pm)), "top10_norm": sorted(top(pn)), "top10_in_common": len(top(pm) & top(pn))}
print(out["profiles"])
save("check_07_norm_pairs_heads.json", out)
