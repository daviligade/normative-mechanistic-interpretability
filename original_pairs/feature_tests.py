"""Permutation tests of the SAE features on the original pairs: moral against norm pairs and moral against neutral pairs, and the matched-size effect sizes."""
import argparse, json, os
import numpy as np
from pairs_common import DATA, ACTIVATIONS, DICTIONARIES, bh

SEED = {"vs_norm": 373737, "vs_neutral": 616161}


def diffs(d):
    """Final-token feature change (permissive minus restrictive) per pair, for the moral, neutral and norm pairs kept for this dictionary."""
    z = np.load(os.path.join(ACTIVATIONS, d, "moral.npz")); zc = np.load(os.path.join(ACTIVATIONS, d, "neutral.npz")); zn = np.load(os.path.join(ACTIVATIONS, d, "norm.npz"))
    return ((z["perm"] - z["rest"]).astype(np.float64), (zc["perm"] - zc["rest"]).astype(np.float64), (zn["perm"] - zn["rest"]).astype(np.float64))


def perm_test(A_a, A_b, n_perm, seed, state_path, hi=None):
    """One-sided test of mean |change| on the first set > on the second, label permutations; resumable through state_path."""
    A = np.abs(np.concatenate([A_a, A_b], axis=0)); na, nb = len(A_a), len(A_b); n = na + nb
    obs = A[:na].mean(0) - A[na:].mean(0); tol = 1e-9 * np.maximum(1.0, np.abs(obs))
    if os.path.exists(state_path): st = np.load(state_path); r, done = st["r_count"].copy(), int(st["done"])
    else: r, done = np.zeros(A.shape[1], dtype=np.int64), 0
    target = min(hi or n_perm, n_perm)
    if done < target:
        rng = np.random.default_rng(seed + done); w = np.concatenate([np.full(na, 1.0 / na), np.full(nb, -1.0 / nb)])
        for start in range(done, target, 500):
            c = min(500, target - start); W = np.empty((c, n))
            for i in range(c): W[i] = w[rng.permutation(n)]
            r += ((W @ A) >= obs - tol).sum(0); done = start + c
        np.savez(state_path, r_count=r, done=done)
    p = (r + 1) / (done + 1); return obs, p, bh(p), done


def std_eff(a, b):
    am, ab = np.abs(a), np.abs(b); n1, n2 = len(am), len(ab)
    vp = ((n1 - 1) * am.var(0, ddof=1) + (n2 - 1) * ab.var(0, ddof=1)) / (n1 + n2 - 2); return (am.mean(0) - ab.mean(0)) / np.sqrt(np.maximum(vp, 1e-12))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--dictionary", required=True, choices=DICTIONARIES); ap.add_argument("--n-perm", type=int, default=200000)
    ap.add_argument("--stop-at", type=int, default=None, help="stop after this many permutations (a later call continues)"); a = ap.parse_args()
    d = a.dictionary; ci = DICTIONARIES.index(d); out = os.path.join(DATA, "features", d); os.makedirs(out, exist_ok=True)
    moral, neutral, norm = diffs(d); res = {"dictionary": d, "n_moral": len(moral), "n_neutral": len(neutral), "n_norm": len(norm)}
    for test, other in (("vs_norm", norm), ("vs_neutral", neutral)):
        _, _, q, done = perm_test(moral, other, a.n_perm, SEED[test] + ci * 100, os.path.join(out, f"{test}.npz"), a.stop_at)
        res[test] = {"n_perm": done, "n_significant": int((q < 0.05).sum())}
        print(f"{d}: moral {test.replace('_', ' ')} after {done} permutations: {res[test]['n_significant']} features at q < 0.05", flush=True)
    if all(res[t]["n_perm"] >= a.n_perm for t in SEED):
        n = min(len(neutral), len(norm)); rng = np.random.default_rng(SEED["vs_neutral"] + 7); cn, cm = [], []
        for _ in range(20):
            cn.append(int((std_eff(moral, neutral[rng.choice(len(neutral), n, replace=False)]) >= 0.8).sum()))
            cm.append(int((std_eff(moral, norm[rng.choice(len(norm), n, replace=False)]) >= 0.8).sum()))
        res["effect_size_at_matched_n"] = {"n": n, "d_ge_0.8_vs_neutral": float(np.mean(cn)), "d_ge_0.8_vs_norm": float(np.mean(cm)), "ratio": float(np.mean(cn) / max(np.mean(cm), 1e-9))}
        json.dump(res, open(os.path.join(out, "summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
