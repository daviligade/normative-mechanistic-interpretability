"""Check 09: a raw comparison of head effects (moral minus control, pairs of equal length, bootstrap interval) applied to every head."""
import argparse
import numpy as np
from pairs_common import MODELS, pairs, head_effects, top_head, family, token_counter, save

ap = argparse.ArgumentParser(); ap.add_argument("--n-boot", type=int, default=4000); a = ap.parse_args()
ntok = token_counter(); MP = {p["name"]: p for p in pairs("moral")}; CP = {p["name"]: p for p in pairs("control")}; out = {}
for m in MODELS:
    M0, C0, mn, cn, nh = head_effects(m); f = family(m)
    meq = [ntok(f, MP[k]["permissive_prompt"]) == ntok(f, MP[k]["restrictive_prompt"]) for k in mn]; ceq = [ntok(f, CP[k]["permissive_prompt"]) == ntok(f, CP[k]["restrictive_prompt"]) for k in cn]
    M, C = M0[np.array(meq)], C0[np.array(ceq)]; l, h = top_head(m); ti = l * nh + h
    rng = np.random.default_rng(20260919); lo = np.empty((a.n_boot, M.shape[1]), dtype=np.float32)
    for b in range(a.n_boot): lo[b] = M[rng.integers(0, len(M), len(M))].mean(0) - C[rng.integers(0, len(C), len(C))].mean(0)
    ci_lo = np.percentile(lo, 2.5, axis=0); rank = int(np.where(np.argsort(-(M.mean(0) - C.mean(0))) == ti)[0][0]) + 1
    ratio, bg = float(M[:, ti].mean() / C[:, ti].mean()), float(M.mean() / C.mean())
    out[m] = {"n_moral": len(M), "n_control": len(C), "head": f"L{l}H{h}", "ratio_first_located_head": ratio, "ratio_all_heads": bg, "first_located_over_all_heads": ratio / bg,
              "frac_heads_interval_above_zero": float((ci_lo > 0).mean()), "first_located_head_interval_above_zero": bool(ci_lo[ti] > 0), "rank_by_raw_difference": rank}
    print(f"{m:24s} {len(M):3d}/{len(C):<3d} L{l}H{h} | ratio {ratio:5.2f}, all heads {bg:5.2f}, relative {ratio / bg:4.2f} | heads with interval above zero {100 * out[m]['frac_heads_interval_above_zero']:5.1f} % | rank {rank}", flush=True)
save("check_09_raw_test_all_heads.json", out)
