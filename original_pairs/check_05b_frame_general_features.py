"""Check 05b: features with a large effect (d >= 0.8, matched number of pairs) against neutral and against norm pairs, among all features, the features active in both frames and the features active only with the moral frame."""
import os
import numpy as np
from pairs_common import ACTIVATIONS, DICTIONARIES, save


def std_eff(a, b):
    am, ab = np.abs(a), np.abs(b); n1, n2 = len(am), len(ab)
    vp = ((n1 - 1) * am.var(0, ddof=1) + (n2 - 1) * ab.var(0, ddof=1)) / (n1 + n2 - 2); return (am.mean(0) - ab.mean(0)) / np.sqrt(np.maximum(vp, 1e-12))


out = {}
for d in DICTIONARIES:
    act = {k: np.load(os.path.join(ACTIVATIONS, d, f"{k}.npz")) for k in ("moral", "neutral", "norm")}
    dif = {k: (v["perm"] - v["rest"]).astype(np.float64) for k, v in act.items()}
    fM = (np.concatenate([act["moral"]["perm"], act["moral"]["rest"]]) > 0).mean(0); fC = (np.concatenate([act["neutral"]["perm"], act["neutral"]["rest"]]) > 0).mean(0)
    general, specific = (fM >= .10) & (fC >= .10), (fM >= .10) & (fC < .01)
    n = min(len(dif["neutral"]), len(dif["norm"])); rng = np.random.default_rng(7); cn, cm = [], []
    for _ in range(20):
        cn.append(std_eff(dif["moral"], dif["neutral"][rng.choice(len(dif["neutral"]), n, replace=False)]) >= .8)
        cm.append(std_eff(dif["moral"], dif["norm"][rng.choice(len(dif["norm"]), n, replace=False)]) >= .8)
    cn, cm = np.array(cn), np.array(cm); rec = {}
    for tag, mask in (("all", np.ones_like(general)), ("active_in_both_frames", general), ("active_only_with_moral_frame", specific)):
        x, y = cn[:, mask].sum(1).mean(), cm[:, mask].sum(1).mean(); rec[tag] = {"n_features": int(mask.sum()), "large_vs_neutral": float(x), "large_vs_norm": float(y), "ratio": float(x / max(y, 1e-9))}
    out[d] = rec
    f = lambda r: f"{r['large_vs_neutral']:6.1f} {r['large_vs_norm']:5.1f} {r['ratio']:5.1f}x"
    print(f"{d:24s} | all {f(rec['all'])} | both frames ({rec['active_in_both_frames']['n_features']:4d}) {f(rec['active_in_both_frames'])} | moral frame only ({rec['active_only_with_moral_frame']['n_features']:4d}) {f(rec['active_only_with_moral_frame'])}", flush=True)
save("check_05b_frame_general_features.json", out)
