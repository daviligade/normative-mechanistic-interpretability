"""Selects the moral-versus-normative feature lists on one half of the pairs."""
import argparse, json, os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/features"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/features_h6split")
ap.add_argument("--perm", type=int, default=20000); ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--seed", type=int, default=20261020)
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
PRIMARY_SET, WHY = primary_item_set(a.items)
items = [i for i in json.load(open(a.items)) if i.get("accepted", True)]


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def sig_mask(X1, X2, P):
    Z = np.concatenate([X1, X2]).astype(np.float32); n1, n = len(X1), len(X1) + len(X2); m = Z.shape[1]; P = max(P, 20 * m)
    obs = np.abs(X1.mean(0) - X2.mean(0)); tot = Z.sum(0); hits = np.zeros(m); done = 0
    while done < P:
        k = min(1000, P - done); sel = np.argsort(rng.random((k, n)), axis=1)[:, :n1]; M = np.zeros((k, n), dtype=np.float32); np.put_along_axis(M, sel, 1.0, axis=1); s1 = M @ Z
        hits += (np.abs(s1 / n1 - (tot - s1) / (n - n1)) >= obs - 1e-9).sum(0); done += k
    return bh((hits + 1) / (P + 1)) < 0.05


def halve(ids):
    ids = sorted(ids); perm = rng.permutation(len(ids)); h = len(ids) // 2
    return sorted(ids[i] for i in perm[:h]), sorted(ids[i] for i in perm[h:])
moral_ids = [i["id"] for i in items if i["category"] == "moral"]; A, B = halve(moral_ids)
for k in sorted({i.get("subtype", "") for i in items if i["category"] == "norm"}):
    a1, b1 = halve([i["id"] for i in items if i["category"] == "norm" and i.get("subtype", "") == k]); A += a1; B += b1
descr_ids = [i["id"] for i in items if i["category"] == "descr"]
meta = dict(seed=a.seed, items_file=a.items, accepted_pairs=PRIMARY_SET, half_A=sorted(A), half_B=sorted(B), descr_eval_only=sorted(descr_ids),
            n_half_A=dict(moral=sum(1 for i in items if i["id"] in set(A) and i["category"] == "moral"), norm=sum(1 for i in items if i["id"] in set(A) and i["category"] == "norm")),
            n_half_B=dict(moral=sum(1 for i in items if i["id"] in set(B) and i["category"] == "moral"), norm=sum(1 for i in items if i["id"] in set(B) and i["category"] == "norm")),
            rule="features selected on one half (H6 test at BH 0.05, active on >= min_active prompts of that half) are evaluated by code/analyze_h6_split.py on the other half only")
json.dump(meta, open(os.path.join(a.out, "split_meta.json"), "w"), indent=1)
print(f"[h6 split] {WHY}; halves: A {meta['n_half_A']}, B {meta['n_half_B']}; descriptive pairs ({len(descr_ids)}) are evaluation-only", flush=True)
HA, HB = set(A), set(B)

for cond in sorted(os.listdir(a.runs)):
    d = os.path.join(a.runs, cond)
    if not os.path.isdir(d) or not os.path.exists(os.path.join(d, "extract__A1.npz")): continue
    t0 = time.time(); sets = {}; counts = {}
    for fr in ("A1", "B"):
        p = os.path.join(d, f"extract__{fr}.npz")
        if not os.path.exists(p): continue
        E = np.load(p); ids = [str(i) for i in E["ids"]]; cat = np.array([str(c) for c in E["category"]])
        Xall = np.abs(E["perm_f"].astype(np.float32) - E["rest_f"].astype(np.float32)); active = (E["perm_f"] > 0).astype(np.int32) + (E["rest_f"] > 0).astype(np.int32)
        for name, H in (("selA", HA), ("selB", HB)):
            inH = np.array([i in H for i in ids]); mo = inH & (cat == "moral"); no = inH & (cat == "norm")
            act = active[inH].sum(0) >= a.min_active
            mask = sig_mask(Xall[mo][:, act], Xall[no][:, act], a.perm)
            sets[f"{fr}_{name}"] = [int(i) for i in np.where(act)[0][mask]]; counts[f"{fr}_{name}"] = dict(n_moral=int(mo.sum()), n_norm=int(no.sum()), n_tested=int(act.sum()), n_selected=int(mask.sum()))
    json.dump(sets, open(os.path.join(a.out, f"sets__{cond}.json"), "w")); json.dump(counts, open(os.path.join(a.out, f"counts__{cond}.json"), "w"), indent=1)
    print(f"[h6 split] {cond}: " + "; ".join(f"{k}: {v['n_selected']} of {v['n_tested']} tested ({v['n_moral']} moral vs {v['n_norm']} norm)" for k, v in counts.items()) + f"  [{time.time() - t0:.0f} s]", flush=True)
print("[h6 split] done; next: the pass-2 commands of circuits/print_commands_circuits.py --stage h6_split", flush=True)
