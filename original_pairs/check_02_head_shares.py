"""Check 02: raw head effects against shares on the original pairs (moral against control pairs), for every head, on all pairs and on the pairs of equal length."""
import argparse
import numpy as np
from pairs_common import MODELS, pairs, head_effects, shares, perm_test, top_head, family, token_counter, save

ap = argparse.ArgumentParser(); ap.add_argument("--n-perm", type=int, default=50000); a = ap.parse_args()
ntok = token_counter(); MP = {p["name"]: p for p in pairs("moral")}; CP = {p["name"]: p for p in pairs("control")}; out = {}
print(f"{'model':24s} {'raw sig':>7s} {'M/C all':>7s} {'%M>C':>5s} | {'share sig':>9s} {'top head':>8s} {'raw':>6s} {'share':>6s} {'95% CI':>13s} {'q':>7s} {'rank':>4s} | {'equal length n':>14s} {'share':>6s} {'q':>6s}")
for m in MODELS:
    M, C, mn, cn, nh = head_effects(m); l, h = top_head(m); ti = l * nh + h
    _, _, q = perm_test(M, C, a.n_perm, 42)
    Ms, Cs = shares(M), shares(C); o2, _, q2 = perm_test(Ms, Cs, a.n_perm, 42)
    rng = np.random.default_rng(0); bs = [Ms[rng.integers(0, len(Ms), len(Ms)), ti].mean() / Cs[rng.integers(0, len(Cs), len(Cs)), ti].mean() for _ in range(5000)]
    rec = {"raw_n_significant": int((q < .05).sum()), "raw_ratio_all_heads": float(M.mean() / C.mean()), "frac_heads_moral_gt_control": float((M.mean(0) > C.mean(0)).mean()),
           "share_n_significant": int((q2 < .05).sum()), "top_head": f"L{l}H{h}", "top_head_raw_ratio": float(M[:, ti].mean() / C[:, ti].mean()),
           "top_head_share_ratio": float(Ms[:, ti].mean() / Cs[:, ti].mean()), "top_head_share_ratio_ci": [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))],
           "top_head_share_q": float(q2[ti]), "top_head_share_rank": int(np.where(np.argsort(-o2) == ti)[0][0]) + 1}
    meq = np.array([ntok(family(m), MP[k]["permissive_prompt"]) == ntok(family(m), MP[k]["restrictive_prompt"]) for k in mn])
    ceq = np.array([ntok(family(m), CP[k]["permissive_prompt"]) == ntok(family(m), CP[k]["restrictive_prompt"]) for k in cn])
    _, _, q4 = perm_test(Ms[meq], Cs[ceq], a.n_perm, 42)
    rec.update({"equal_length_n_moral": int(meq.sum()), "equal_length_n_control": int(ceq.sum()), "equal_length_share_n_significant": int((q4 < .05).sum()),
                "equal_length_top_head_share_ratio": float(Ms[meq][:, ti].mean() / Cs[ceq][:, ti].mean()), "equal_length_top_head_share_q": float(q4[ti])})
    out[m] = rec
    print(f"{m:24s} {rec['raw_n_significant']:7d} {rec['raw_ratio_all_heads']:7.2f} {100 * rec['frac_heads_moral_gt_control']:5.0f} | {rec['share_n_significant']:9d} {rec['top_head']:>8s} "
          f"{rec['top_head_raw_ratio']:6.2f} {rec['top_head_share_ratio']:6.2f} [{rec['top_head_share_ratio_ci'][0]:5.2f},{rec['top_head_share_ratio_ci'][1]:5.2f}] {rec['top_head_share_q']:7.4f} "
          f"{rec['top_head_share_rank']:4d} | {meq.sum():6d}/{ceq.sum():<7d} {rec['equal_length_top_head_share_ratio']:6.2f} {rec['equal_length_top_head_share_q']:6.3f}", flush=True)
save("check_02_head_shares.json", out)
