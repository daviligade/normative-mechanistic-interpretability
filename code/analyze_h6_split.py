"""Removal of the feature lists, read on the other half of the pairs."""
import argparse, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/features_h6split"); ap.add_argument("--sets", default="results/features_h6split"); ap.add_argument("--items", required=True)
ap.add_argument("--out", default="results/features_h6split"); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--seed", type=int, default=20260920)
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
PRIMARY_SET, WHY = primary_item_set(a.items); ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
META = json.load(open(os.path.join(a.sets, "split_meta.json"))); HA, HB = set(META["half_A"]), set(META["half_B"])
CATS = ("moral", "norm", "descr")


def ci(v):
    v = np.asarray(v, float); bs = [v[rng.integers(0, len(v), len(v))].mean() for _ in range(a.boot)]; return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def ci_diff(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float); bs = [x[rng.integers(0, len(x), len(x))].mean() - y[rng.integers(0, len(y), len(y))].mean() for _ in range(a.boot)]
    return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def rec_of(diff_by_cat):
    out = {c: dict(n=int(len(v)), set_minus_random=float(np.mean(v)), ci95=ci(v)) for c, v in diff_by_cat.items() if len(v) >= 5}
    if "moral" in out and "norm" in out:
        out["moral_minus_norm"] = dict(value=float(np.mean(diff_by_cat["moral"]) - np.mean(diff_by_cat["norm"])), ci95=ci_diff(diff_by_cat["moral"], diff_by_cat["norm"]))
        out["moral_specific"] = bool(out["moral"]["set_minus_random"] < 0 and out["moral"]["ci95"][1] < 0 and out["moral_minus_norm"]["ci95"][1] < 0)
    return out


summary = dict(settings=vars(a), accepted_pairs=PRIMARY_SET, split=dict(seed=META["seed"], n_half_A=META["n_half_A"], n_half_B=META["n_half_B"]), conditions={})
report = ["# Split-half moral-versus-norm features: held-out ablation (exploratory follow-up)", "", f"Items: {WHY}. Halves: A {META['n_half_A']}, B {META['n_half_B']}; descriptive pairs evaluation-only. Inclusion gap >= {a.tau}.",
          "Reading: moral-specific = cross-fitted set-minus-random on moral pairs below zero (interval) and moral-minus-norm difference below zero (interval).", ""]
counts = {"A1": 0, "B": 0}; n_cond = {"A1": 0, "B": 0}
for cond in sorted(os.listdir(a.runs)):
    d = os.path.join(a.runs, cond)
    if not os.path.isdir(d) or not os.path.exists(os.path.join(a.sets, f"sets__{cond}.json")): continue
    sets = json.load(open(os.path.join(a.sets, f"sets__{cond}.json"))); cnt = json.load(open(os.path.join(a.sets, f"counts__{cond}.json"))) if os.path.exists(os.path.join(a.sets, f"counts__{cond}.json")) else {}
    res = {}; report += [f"## {cond}", ""]
    for fr in ("A1", "B"):
        pe, pa = os.path.join(d, f"extract__{fr}.npz"), os.path.join(d, f"ablate__{fr}.npz")
        if not (os.path.exists(pe) and os.path.exists(pa)): continue
        E, Z = np.load(pe), np.load(pa); ids = [str(i) for i in E["ids"]]; assert ids == [str(i) for i in Z["ids"]], f"{pa}: item ids differ from the extraction file"
        cat = np.array([str(c) for c in E["category"]]); gap0 = E["perm_clean_S"] - E["rest_clean_S"]; inc = (gap0 >= a.tau) & np.array([i in ACC for i in ids])
        per_item = {}
        for name in (f"{fr}_selA", f"{fr}_selB"):
            if f"perm_{name}_S" not in Z.files: continue
            gap = Z[f"perm_{name}_S"] - Z[f"rest_{name}_S"]; dg = gap - gap0[:, None]; per_item[name] = dg[:, 0] - dg[:, 1:].mean(1)
        if len(per_item) < 2: continue
        evalA = np.array([i in HB for i in ids]) | (cat == "descr")
        evalB = np.array([i in HA for i in ids]) | (cat == "descr")
        dirs = {}
        for name, ev in ((f"{fr}_selA", evalA), (f"{fr}_selB", evalB)):
            dirs[name] = rec_of({c: per_item[name][ev & inc & (cat == c)] for c in CATS}); dirs[name]["n_features"] = len(sets.get(name, [])); dirs[name]["selection"] = cnt.get(name)
        cross = {}
        for c in ("moral", "norm"):
            cross[c] = np.concatenate([per_item[f"{fr}_selA"][evalA & inc & (cat == c) & ~(cat == "descr")], per_item[f"{fr}_selB"][evalB & inc & (cat == c)]])
        cross["descr"] = 0.5 * (per_item[f"{fr}_selA"] + per_item[f"{fr}_selB"])[inc & (cat == "descr")]
        xf = rec_of(cross)
        res[fr] = dict(directions=dirs, cross_fitted=xf, random_lists=int(Z[f"perm_{fr}_selA_S"].shape[1] - 1))
        n_cond[fr] += 1; counts[fr] += int(xf.get("moral_specific", False))
        for name, r in dirs.items():
            report += [f"* {name} ({r['n_features']} features): " + "; ".join(f"{c}: {r[c]['set_minus_random']:+.3f} [{r[c]['ci95'][0]:+.3f}, {r[c]['ci95'][1]:+.3f}] (n={r[c]['n']})" for c in CATS if c in r)
                       + (f"; moral - norm {r['moral_minus_norm']['value']:+.3f} [{r['moral_minus_norm']['ci95'][0]:+.3f}, {r['moral_minus_norm']['ci95'][1]:+.3f}]" if "moral_minus_norm" in r else "")]
        report += [f"* **{fr} cross-fitted**: " + "; ".join(f"{c}: {xf[c]['set_minus_random']:+.3f} [{xf[c]['ci95'][0]:+.3f}, {xf[c]['ci95'][1]:+.3f}] (n={xf[c]['n']})" for c in CATS if c in xf)
                   + (f"; moral - norm {xf['moral_minus_norm']['value']:+.3f} [{xf['moral_minus_norm']['ci95'][0]:+.3f}, {xf['moral_minus_norm']['ci95'][1]:+.3f}] -> " + ("MORAL-SPECIFIC" if xf.get("moral_specific") else "not moral-specific") if "moral_minus_norm" in xf else "")]
    summary["conditions"][cond] = res; report += [""]
report += ["## Count", ""] + [f"* frame {fr}: moral-specific causal effect (held-out, cross-fitted) in {counts[fr]} of {n_cond[fr]} dictionaries" for fr in ("A1", "B")]
summary["count"] = {fr: dict(moral_specific=counts[fr], dictionaries=n_cond[fr]) for fr in ("A1", "B")}
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
