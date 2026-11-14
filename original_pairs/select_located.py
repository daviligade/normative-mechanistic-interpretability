"""Selects the located heads and the located features on the original pairs and writes located/heads.json and located/features.json."""
import argparse, json, os
import numpy as np
from pairs_common import HERE, DATA, MODELS, DICTIONARIES, head_effects, shares, bh

ap = argparse.ArgumentParser(); ap.add_argument("--out", default=os.path.join(HERE, "..", "located")); a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
heads = {}
for m in MODELS:
    M, C, mn, cn, nh = head_effects(m); nl = M.shape[1] // nh
    order = np.argsort(-(M.mean(0) - C.mean(0)))
    located = [[int(i // nh), int(i % nh)] for i in order[:10]]
    sh = shares(M).mean(0); top = np.argsort(-sh)
    heads[m] = {"n_layers": int(nl), "n_heads": int(nh), "n_original_moral_pairs": len(mn), "located": located, "located_top5": located[:5], "located_top1": located[:1],
                "topshare10": [[int(i // nh), int(i % nh)] for i in top[:10]], "topshare_1pct": [[int(i // nh), int(i % nh)] for i in top[:max(1, round(0.01 * nl * nh))]],
                "original_share_located": float(sum(sh[l * nh + h] for l, h in located)), "uniform_share_located": 10.0 / (nl * nh)}
    print(f"{m:24s} first located head L{located[0][0]}H{located[0][1]}  share of the ten located heads {heads[m]['original_share_located']:.3f} (uniform {heads[m]['uniform_share_located']:.3f})")
json.dump(heads, open(os.path.join(a.out, "heads.json"), "w"), indent=1)


def significant(path):
    s = np.load(path); return [int(i) for i in np.where(bh((s["r_count"] + 1) / (int(s["done"]) + 1)) < 0.05)[0]]


feats = {}
for d in DICTIONARIES:
    vs_neutral = significant(os.path.join(DATA, "features", d, "vs_neutral.npz")); vs_norm = significant(os.path.join(DATA, "features", d, "vs_norm.npz"))
    ids_file = os.path.join(DATA, "features", d, "vs_norm_ids.json")
    if os.path.exists(ids_file): listed = json.load(open(ids_file)); assert sorted(listed) == vs_norm, d; vs_norm = listed      # the order of the stored list
    feats[d] = {"original_vs_neutral_sig": vs_neutral, "original_vs_norm_sig": vs_norm, "overlap": len(set(vs_norm) & set(vs_neutral))}
    json.dump({"original_vs_neutral_sig": vs_neutral, "original_vs_norm_sig": vs_norm}, open(os.path.join(a.out, f"feature_sets__{d}.json"), "w"))
    print(f"{d:24s} moral vs neutral {len(vs_neutral):4d} | moral vs norm {len(vs_norm):4d} | overlap {feats[d]['overlap']}")
json.dump(feats, open(os.path.join(a.out, "features.json"), "w"), indent=1)
