"""Removal of the neuron lists, read on held-out pairs."""
import argparse, csv, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--units", default="runs/units"); ap.add_argument("--runs", default="runs/units_ablation"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/units")
ap.add_argument("--split-meta", default="results/features_h6split/split_meta.json"); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--seed", type=int, default=20260920)
ap.add_argument("--min-effect", type=float, default=0.01, help="a moral-specific call also needs a cross-fitted moral effect of at least this size (readout units)")
ap.add_argument("--min-effect-rel", type=float, default=0.02, help="the same minimum for the relative version (fraction of the pair's gap)")
ap.add_argument("--any-items", action="store_true")
ap.add_argument("--all-held-out", action="store_true", help="follow-up item sets that took no part in the selection: every item is read with both lists (their mean), like the descriptive pairs")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
PRIMARY_SET, WHY = primary_item_set(a.items); ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
CATS = ("moral", "norm", "descr")


def ci(v):
    v = np.asarray(v, float); bs = v[rng.integers(0, len(v), (a.boot, len(v)))].mean(1); return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def ci_diff(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float); bs = x[rng.integers(0, len(x), (a.boot, len(x)))].mean(1) - y[rng.integers(0, len(y), (a.boot, len(y)))].mean(1)
    return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def rec_of(by_cat, min_effect=None):
    me = a.min_effect if min_effect is None else min_effect
    out = {c: dict(n=int(len(v)), set_minus_random=float(np.mean(v)), ci95=ci(v)) for c, v in by_cat.items() if len(v) >= 5}
    if "moral" in out and "norm" in out:
        out["moral_minus_norm"] = dict(value=float(np.mean(by_cat["moral"]) - np.mean(by_cat["norm"])), ci95=ci_diff(by_cat["moral"], by_cat["norm"]))
        out["moral_specific"] = bool(out["moral"]["set_minus_random"] <= -me and out["moral"]["ci95"][1] < 0 and out["moral_minus_norm"]["ci95"][1] < 0)
    return out


summary = dict(settings=vars(a), accepted_pairs=PRIMARY_SET, discovery={}, ablation={}); report = ["# Neurons: discovery by depth and held-out ablation (exploratory)", "", f"Items: {WHY}.", ""]
prof_rows = []

for d in sorted(glob.glob(os.path.join(a.units, "*"))):
    model = os.path.basename(d); rec = {}
    for p in sorted(glob.glob(os.path.join(d, "sets__*.json"))):
        S = json.load(open(p)); fr = S["frame"]; L = S["n_layers"]; cnt = S["counts"]
        more = [int(l) for l, c in cnt.items() if c.get("more_than_any_split")]; full = {int(l): c["full_size"] for l, c in cnt.items()}
        rec[fr] = dict(n_layers=L, d_mlp=S["d_mlp"], layers_more_than_any_split=sorted(more), n_layers_more=len(more), full_size_by_layer=full, peak_layer=max(full, key=full.get) if full else None,
                       total_full=int(sum(full.values())), total_selA=int(sum(len(v) for v in S["sets"]["selA"].values())), total_selB=int(sum(len(v) for v in S["sets"]["selB"].values())),
                       contrast=S.get("contrast"), unit_value=S.get("unit_value"), cap=S.get("cap"))
        for l, c in cnt.items():
            prof_rows.append(dict(model=model, frame=fr, layer=int(l), depth=round((int(l) + 1) / L, 4), n_tested=c["n_tested"], moral_vs_norm_full=c["full_size"], equalised_moral_vs_norm=c.get("moral_vs_norm_equalised"),
                                  max_norm_vs_norm=max(c["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in c else None, more_than_any_split=c.get("more_than_any_split"), selA=c.get("selA_size"), selB=c.get("selB_size")))
    if rec:
        summary["discovery"][model] = rec; report += [f"## {model}: discovery", ""]
        for fr, r in rec.items():
            if r.get("contrast"): report += [f"* {fr}: lists of the '{r['contrast']}' contrast ({r['unit_value']}); {r['total_full']} units at full size over {r['n_layers']} layers (peak at layer {r['peak_layer']}); halves select {r['total_selA']} / {r['total_selB']} (capped at {r.get('cap')} per layer). Discovery summary: code/analyze_unit_contrast.py"]
            else: report += [f"* {fr}: {r['total_full']} neurons separate moral from norm pairs over {r['n_layers']} layers (peak at layer {r['peak_layer']}); moral vs norm exceeds every norm-vs-norm split in {r['n_layers_more']} layers {r['layers_more_than_any_split']}; halves select {r['total_selA']} / {r['total_selB']}"]
        report += [""]
with open(os.path.join(a.out, "depth_profiles.csv"), "w", newline="") as f:
    if prof_rows: w = csv.DictWriter(f, fieldnames=list(prof_rows[0])); w.writeheader(); w.writerows(prof_rows)

META = json.load(open(a.split_meta)) if os.path.exists(a.split_meta) else None
counts = {}; counts_rel = {}
for d in sorted(glob.glob(os.path.join(a.runs, "*"))):
    model = os.path.basename(d); files = sorted(glob.glob(os.path.join(d, "*__*.npz")))
    if not files: continue
    cfg = json.load(open(os.path.join(d, "run_config.json")))[-1]; units_dir = cfg.get("units_dir", os.path.join(a.units, model))
    HA, HB = (set(META["half_A"]), set(META["half_B"])) if META else (None, None)
    byframe = {}
    for p in files:
        z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta["id"] not in ACC: continue
        byframe.setdefault(meta["frame"], []).append((meta, {k: z[k] for k in z.files if k != "__meta__"}))
    rec = {}; report += [f"## {model}: held-out ablation", ""]
    for fr, rows in sorted(byframe.items()):
        if HA is None:
            sj = os.path.join(units_dir, f"sets__{fr}.json"); S = json.load(open(sj)); HA, HB = set(S["half_A"]), set(S["half_B"]); print(f"[analyze_unit_ablation] halves taken from {sj} ({S.get('halves_from')})", flush=True)
        lists = rows[0][0]["lists"]; per_item = {}; per_rel = {}; cat = {}; inc = {}
        for meta, z in rows:
            i = meta["id"]; cat[i] = meta["category"]
            if fr == "C":
                for name in lists:
                    e = []
                    for s in ("perm", "rest"):
                        dp = z[f"{s}_{name}_pmoral"] - z[f"{s}_clean_pmoral"]; e.append(dp[0] - dp[1:].mean())
                    per_item.setdefault(name, {})[i] = float(np.mean(e))
                inc[i] = True
            else:
                gap0 = float(z["perm_clean_S"] - z["rest_clean_S"]); inc[i] = gap0 >= a.tau
                for name in lists:
                    g = z[f"perm_{name}_S"] - z[f"rest_{name}_S"]; dg = g - gap0; per_item.setdefault(name, {})[i] = float(dg[0] - dg[1:].mean()); per_rel.setdefault(name, {})[i] = float((dg[0] - dg[1:].mean()) / gap0) if gap0 >= a.tau else 0.0
        rec[fr] = {}
        for kind in ("all", "top"):
            la, lb = f"selA_{kind}", f"selB_{kind}"
            if la not in per_item or lb not in per_item: continue
            evA = lambda i: (i in HB or cat[i] == "descr") and inc[i]; evB = lambda i: (i in HA or cat[i] == "descr") and inc[i]
            dirs = {la: rec_of({c: [per_item[la][i] for i in per_item[la] if evA(i) and cat[i] == c] for c in CATS}), lb: rec_of({c: [per_item[lb][i] for i in per_item[lb] if evB(i) and cat[i] == c] for c in CATS})}
            if a.all_held_out:
                cross = {c: [0.5 * (per_item[la][i] + per_item[lb][i]) for i in per_item[la] if cat[i] == c and inc[i]] for c in CATS}
            else:
                cross = {c: [per_item[la][i] for i in per_item[la] if evA(i) and cat[i] == c and c != "descr"] + [per_item[lb][i] for i in per_item[lb] if evB(i) and cat[i] == c and c != "descr"] for c in ("moral", "norm")}
                cross["descr"] = [0.5 * (per_item[la][i] + per_item[lb][i]) for i in per_item[la] if cat[i] == "descr" and inc[i]]
            xf = rec_of(cross); rec[fr][kind] = dict(directions=dirs, cross_fitted=xf)
            counts.setdefault((fr, kind), []).append(bool(xf.get("moral_specific", False)))
            report += [f"* {fr}, {kind} lists: cross-fitted " + "; ".join(f"{c}: {xf[c]['set_minus_random']:+.3f} [{xf[c]['ci95'][0]:+.3f}, {xf[c]['ci95'][1]:+.3f}] (n={xf[c]['n']})" for c in CATS if c in xf)
                       + (f"; moral - norm {xf['moral_minus_norm']['value']:+.3f} [{xf['moral_minus_norm']['ci95'][0]:+.3f}, {xf['moral_minus_norm']['ci95'][1]:+.3f}] -> " + ("MORAL-SPECIFIC" if xf.get("moral_specific") else "not moral-specific") if "moral_minus_norm" in xf else "")]
            if fr != "C" and la in per_rel and lb in per_rel:
                if a.all_held_out: crel = {c: [0.5 * (per_rel[la][i] + per_rel[lb][i]) for i in per_rel[la] if cat[i] == c and inc[i]] for c in CATS}
                else:
                    crel = {c: [per_rel[la][i] for i in per_rel[la] if evA(i) and cat[i] == c] + [per_rel[lb][i] for i in per_rel[lb] if evB(i) and cat[i] == c] for c in ("moral", "norm")}
                    crel["descr"] = [0.5 * (per_rel[la][i] + per_rel[lb][i]) for i in per_rel[la] if cat[i] == "descr" and inc[i]]
                xr = rec_of(crel, a.min_effect_rel); rec[fr][kind]["cross_fitted_relative"] = xr; counts_rel.setdefault((fr, kind), []).append(bool(xr.get("moral_specific", False)))
                report += [f"    relative to the pair's gap: " + "; ".join(f"{c}: {100 * xr[c]['set_minus_random']:+.1f}% [{100 * xr[c]['ci95'][0]:+.1f}, {100 * xr[c]['ci95'][1]:+.1f}]" for c in CATS if c in xr)
                           + (f"; moral - norm {100 * xr['moral_minus_norm']['value']:+.1f}% [{100 * xr['moral_minus_norm']['ci95'][0]:+.1f}, {100 * xr['moral_minus_norm']['ci95'][1]:+.1f}] -> " + ("MORAL-SPECIFIC" if xr.get("moral_specific") else "not moral-specific") if "moral_minus_norm" in xr else "")]
    summary["ablation"][model] = rec; report += [""]
report += ["## Count of models with a moral-specific held-out effect", ""] + [f"* frame {fr}, {kind} lists: {sum(v)} of {len(v)} models (absolute); relative to the pair's gap: {sum(counts_rel.get((fr, kind), []))} of {len(counts_rel.get((fr, kind), []))}" for (fr, kind), v in sorted(counts.items())]
summary["count"] = {f"{fr}/{kind}": dict(moral_specific=sum(v), models=len(v), moral_specific_relative=sum(counts_rel.get((fr, kind), [])), models_relative=len(counts_rel.get((fr, kind), []))) for (fr, kind), v in counts.items()}
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
