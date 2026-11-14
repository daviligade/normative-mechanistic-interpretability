"""Check 03: base against instruction-tuned models on the original pairs, on profiles of shares and on raw effects."""
import json, os
import numpy as np
from scipy.stats import pearsonr, spearmanr
from pairs_common import DATA, BASE_INSTRUCT, top_head, save


def load(m):
    z, zc = np.load(os.path.join(DATA, "heads", m, "head_effects.npz")), np.load(os.path.join(DATA, "heads", m, "control_head_effects.npz"))
    return {k: np.abs(z[k]).ravel() for k in z.files}, {k: np.abs(zc[k]).ravel() for k in zc.files}, z[z.files[0]].shape[1]


out = {}
print(f"{'base model':14s} | profile r / rho | first located head: share ratio base -> instruct (rank in instruct) | raw moral effect, summed over heads, base -> instruct")
for b, i in BASE_INSTRUCT:
    Mb, Cb, nh = load(b); Mi, Ci, _ = load(i); cm = [k for k in Mb if k in Mi]; cc = [k for k in Cb if k in Ci]
    nb, ni = np.stack([Mb[k] / Mb[k].sum() for k in cm]), np.stack([Mi[k] / Mi[k].sum() for k in cm])
    cb, ci = np.stack([Cb[k] / Cb[k].sum() for k in cc]), np.stack([Ci[k] / Ci[k].sum() for k in cc])
    pb, pi = nb.mean(0), ni.mean(0); l, h = top_head(b); ti = l * nh + h
    rb, ri = nb[:, ti].mean() / cb[:, ti].mean(), ni[:, ti].mean() / ci[:, ti].mean(); rank = int(np.where(np.argsort(-(pi - ci.mean(0))) == ti)[0][0]) + 1
    rawb, rawi = np.mean([Mb[k].sum() for k in cm]), np.mean([Mi[k].sum() for k in cm]); rcb, rci = np.mean([Cb[k].sum() for k in cc]), np.mean([Ci[k].sum() for k in cc])
    r, rho = pearsonr(pb, pi)[0], spearmanr(pb, pi)[0]
    out[b] = {"instruct": i, "n_moral_pairs_in_both": len(cm), "n_control_pairs_in_both": len(cc), "profile_pearson": float(r), "profile_spearman": float(rho), "first_located_head": f"L{l}H{h}",
              "share_ratio_base": float(rb), "share_ratio_instruct": float(ri), "rank_in_instruct": rank, "raw_moral_sum_base": float(rawb), "raw_moral_sum_instruct": float(rawi),
              "raw_control_sum_base": float(rcb), "raw_control_sum_instruct": float(rci)}
    print(f"{b:14s} | {r:.3f} / {rho:.3f} | L{l}H{h}: {rb:.2f} -> {ri:.2f} (rank {rank}) | {rawb:.2f} -> {rawi:.2f} ({100 * (rawi / rawb - 1):+.0f} %)")
save("check_03_base_instruct.json", out)
