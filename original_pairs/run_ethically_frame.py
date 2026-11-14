"""Head patching on the original moral pairs with "is ethically" in place of "is morally": is the first located head still the head with the largest difference between moral and control pairs?"""
import argparse, os, sys
import numpy as np
from pairs_common import HERE, DATA, pairs, top_head, save
sys.path.insert(0, os.path.join(HERE, "..", "code"))
from run_heads import Patcher, run_pair, pick_device

ap = argparse.ArgumentParser(); ap.add_argument("--model", required=True, help="e.g. meta-llama/Llama-3.2-1B"); ap.add_argument("--device", default="auto"); ap.add_argument("--batch", type=int, default=64); a = ap.parse_args()
tag = a.model.rstrip("/").split("/")[-1]; P = Patcher(a.model, pick_device(a.device), "float32"); P.use_prefix = False
swap = lambda s: s[:-len("is morally")] + "is ethically" if s.endswith("is morally") else s
moral = []
for p in pairs("moral"):
    r = run_pair(P, swap(p["permissive_prompt"]), swap(p["restrictive_prompt"]), ["p2r"], ["all"], a.batch)
    if r["base_perm"]["S_hist"] - r["base_rest"]["S_hist"] > 0: moral.append(np.abs(r["effects"]["p2r_all"]["S_hist"]).ravel())
zc = np.load(os.path.join(DATA, "heads", tag, "control_head_effects.npz")); C = np.stack([np.abs(zc[k]).ravel() for k in zc.files]); M = np.stack(moral)
nh = P.H; diff = M.mean(0) - C.mean(0); order = np.argsort(-diff); l, h = top_head(tag); rank = int(np.where(order == l * nh + h)[0][0]) + 1
out = {"model": tag, "n_moral_pairs": len(M), "first_head_with_is_ethically": f"L{order[0] // nh}H{order[0] % nh}", "first_located_head": f"L{l}H{h}", "rank_of_first_located_head": rank,
       "ratio_of_first_located_head": float(M[:, l * nh + h].mean() / C[:, l * nh + h].mean())}
print(out)
save(f"ethically_frame_{tag}.json", out)
