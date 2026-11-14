"""Check 05: how often the features that separate moral from neutral pairs fire on neutral prompts, and their mean activation on moral, norm and neutral prompts."""
import os
import numpy as np
from pairs_common import DATA, ACTIVATIONS, DICTIONARIES, bh, save

out = {}
print(f"{'dictionary':24s} {'n':>5s} | never on a neutral prompt | on < 5 % of neutral prompts | mean activation: moral / norm / neutral")
for d in DICTIONARIES:
    act = {k: np.load(os.path.join(ACTIVATIONS, d, f"{k}.npz")) for k in ("moral", "neutral", "norm")}
    s = np.load(os.path.join(DATA, "features", d, "vs_neutral.npz")); sig = np.where(bh((s["r_count"] + 1) / (int(s["done"]) + 1)) < 0.05)[0]
    A = {k: np.concatenate([v["perm"], v["rest"]])[:, sig] for k, v in act.items()}
    rec = {"n_moral_vs_neutral_features": int(len(sig)), "frac_never_on_neutral": float(((A["neutral"] > 0).sum(0) == 0).mean()),
           "frac_on_lt_5pct_of_neutral": float(((A["neutral"] > 0).mean(0) < .05).mean()), "mean_activation_moral": float(A["moral"].mean()),
           "mean_activation_norm": float(A["norm"].mean()), "mean_activation_neutral": float(A["neutral"].mean())}
    out[d] = rec
    print(f"{d:24s} {len(sig):5d} | {rec['frac_never_on_neutral']:25.2f} | {rec['frac_on_lt_5pct_of_neutral']:27.2f} | {rec['mean_activation_moral']:.3f} / {rec['mean_activation_norm']:.3f} / {rec['mean_activation_neutral']:.4f}", flush=True)
save("check_05_frame_features.json", out)
