"""The Jacobian-lens interventions."""
import argparse, csv, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/jlens_swap"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/jlens_swap")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--min-effect-rel", type=float, default=0.02); ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
LOCATED, WHY = primary_item_set(a.items); ITEMS = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}; CATS = ("moral", "norm", "descr")


def ci(v):
    v = np.asarray(v, float); bs = v[rng.integers(0, len(v), (a.boot, len(v)))].mean(1); return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def ci_diff(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float); bs = x[rng.integers(0, len(x), (a.boot, len(x)))].mean(1) - y[rng.integers(0, len(y), (a.boot, len(y)))].mean(1); return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def rec_of(by_cat, rel):
    out = {c: dict(n=int(len(v)), effect=float(np.mean(v)), ci95=ci(v)) for c, v in by_cat.items() if len(v) >= 5}
    if "moral" in out and "norm" in out:
        out["moral_minus_norm"] = dict(value=float(np.mean(by_cat["moral"]) - np.mean(by_cat["norm"])), ci95=ci_diff(by_cat["moral"], by_cat["norm"]))
        out["moral_specific"] = bool(out["moral"]["effect"] <= -(a.min_effect_rel if rel else 0.01) and out["moral"]["ci95"][1] < 0 and out["moral_minus_norm"]["ci95"][1] < 0)
        out["general_fall"] = bool(all(c in out and out[c]["ci95"][1] < 0 for c in CATS))
    return out


summary = {}; rows = []; report = ["# Jacobian-lens interventions at the final position (exploratory)", "", f"Items: {WHY}.", ""]; counts = {}
for d in sorted(glob.glob(os.path.join(a.runs, "*"))):
    model = os.path.basename(d); files = sorted(glob.glob(os.path.join(d, "*__*.npz")))
    if not files: continue
    byframe = {}
    for p in files:
        z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta["id"] not in ITEMS: continue
        byframe.setdefault(meta["frame"], []).append((meta, {k: z[k] for k in z.files if k != "__meta__"}))
    summary[model] = {}; report += [f"## {model}", ""]
    for fr, rows_f in sorted(byframe.items()):
        meta0 = rows_f[0][0]; layers = meta0["layers"]; summary[model][fr] = {}
        for l in layers:
            for name in meta0["directions"]:
                for kind in meta0["interventions"]:
                    if kind == "swap" and name != "category": continue
                    key = f"L{l}_{name}_{kind}"; ab = {c: [] for c in CATS}; rl = {c: [] for c in CATS}
                    for meta, z in rows_f:
                        gap0 = float(z["perm_clean_S"] - z["rest_clean_S"])
                        if gap0 < a.tau: continue
                        g = z[f"perm_{key}_S"] - z[f"rest_{key}_S"]; dg = g - gap0; e = float(dg[0] - dg[1:].mean()); ab[meta["category"]].append(e); rl[meta["category"]].append(e / gap0)
                    A_, R_ = rec_of(ab, False), rec_of(rl, True); summary[model][fr][key] = dict(layer=l, direction=name, intervention=kind, absolute=A_, relative=R_)
                    if name == "category" and kind in ("project", "swap"): counts.setdefault((fr, name, kind), []).append(bool(R_.get("moral_specific", False)))
                    if name == "stance" and kind in ("project", "flip"): counts.setdefault((fr, name, kind), []).append(bool(R_.get("general_fall", False)))
                    rows.append(dict(model=model, frame=fr, layer=l, direction=name, intervention=kind, **{f"rel_{c}": R_.get(c, {}).get("effect") for c in CATS}, rel_moral_minus_norm=R_.get("moral_minus_norm", {}).get("value"),
                                     moral_specific=R_.get("moral_specific"), general_fall=R_.get("general_fall"), **{f"abs_{c}": A_.get(c, {}).get("effect") for c in CATS}))
                    if all(c in R_ for c in ("moral", "norm")):
                        verdict = ("MORAL-SPECIFIC" if R_.get("moral_specific") else "not moral-specific") if name == "category" else ("GENERAL FALL" if R_.get("general_fall") else "no general fall")
                        report += [f"* {fr}, layer {l}, {name} / {kind}: relative " + "; ".join(f"{c} {100 * R_[c]['effect']:+.1f}% [{100 * R_[c]['ci95'][0]:+.1f}, {100 * R_[c]['ci95'][1]:+.1f}]" for c in CATS if c in R_)
                                   + f"; moral - norm {100 * R_['moral_minus_norm']['value']:+.1f}% [{100 * R_['moral_minus_norm']['ci95'][0]:+.1f}, {100 * R_['moral_minus_norm']['ci95'][1]:+.1f}] -> {verdict}"]
    report += [""]
report += ["## Counts of models (any layer counts once per model and frame)", ""]
agg = {}
for (fr, name, kind), v in counts.items(): agg.setdefault((fr, name, kind), v)
per_model = {}
for model, rec in summary.items():
    for fr, keys in rec.items():
        for key, r in keys.items():
            flag = r["relative"].get("moral_specific" if r["direction"] == "category" else "general_fall", False)
            per_model.setdefault((fr, r["direction"], r["intervention"]), {}).setdefault(model, False); per_model[(fr, r["direction"], r["intervention"])][model] |= bool(flag)
for (fr, name, kind), d_ in sorted(per_model.items()):
    if kind == "swap" and name != "category": continue
    report += [f"* frame {fr}, {name} / {kind}: {sum(d_.values())} of {len(d_)} models ({', '.join(m for m, v in d_.items() if v)})"]
summary["_count"] = {f"{fr}/{name}/{kind}": dict(models_with_effect=sum(d_.values()), models=len(d_)) for (fr, name, kind), d_ in per_model.items()}
with open(os.path.join(a.out, "by_layer.csv"), "w", newline="") as f:
    if rows: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
