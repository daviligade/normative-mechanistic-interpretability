"""Check 04: overlap of the top five heads across the four construction tiers of the moral pairs, against random four-way splits of the moral and of the control pairs."""
import argparse
import numpy as np
from pairs_common import pairs, head_effects, save

ap = argparse.ArgumentParser(); ap.add_argument("--n-sim", type=int, default=5000); a = ap.parse_args()
tier = {p["name"]: p["tier"] for p in pairs("moral")}; rng = np.random.default_rng(0); top5 = lambda X: set(np.argsort(-X.mean(0))[:5]); out = {}
for m in ["Llama-3.2-1B", "Llama-3.2-3B", "gemma-2b", "Qwen2.5-7B", "Llama-3.1-8B", "Qwen2.5-14B"]:
    M, C, mn, cn, nh = head_effects(m); t = np.array([tier[k] for k in mn])
    obs = len(set.intersection(*[top5(M[t == k]) for k in range(4)])); sizes = [int((t == k).sum()) for k in range(4)]
    ov = np.array([len(set.intersection(*[top5(M[s]) for s in np.split(rng.permutation(len(mn)), np.cumsum(sizes)[:-1])])) for _ in range(a.n_sim)])
    oc = np.array([len(set.intersection(*[top5(C[s]) for s in np.array_split(rng.permutation(len(C)), 4)])) for _ in range(a.n_sim)])
    out[m] = {"tier_overlap": obs, "random_split_mean": float(ov.mean()), "p_random_ge": float((ov >= obs).mean()), "p_random_le": float((ov <= obs).mean()),
              "control_random_split_mean": float(oc.mean()), "control_p_ge_1": float((oc >= 1).mean()), "control_p_ge_2": float((oc >= 2).mean())}
    print(f"{m:14s} tier overlap {obs} | random splits of the moral pairs: mean {ov.mean():.2f}, P(>=) {np.mean(ov >= obs):.2f}, P(<=) {np.mean(ov <= obs):.3f} | "
          f"random splits of the control pairs: mean {oc.mean():.2f}, P(>=1) {np.mean(oc >= 1):.2f}, P(>=2) {np.mean(oc >= 2):.2f}")
save("check_04_tier_splits.json", out)
