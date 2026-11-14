"""The steering results."""
import argparse, csv, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/steering"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/steering")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--min-step", type=float, default=0.10); ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
LOCATED, WHY = primary_item_set(a.items); ITEMS = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}; CATS = ("moral", "norm", "descr")


def ci(v):
    v = np.asarray(v, float); bs = v[rng.integers(0, len(v), (a.boot, len(v)))].mean(1); return [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


summary = {}; rows = []; report = ["# Difference-of-means steering at the final token (exploratory)", "", f"Items: {WHY}.", ""]; per_model_flags = {}
for d in sorted(glob.glob(os.path.join(a.runs, "*"))):
    model = os.path.basename(d); files = sorted(glob.glob(os.path.join(d, "*__*.npz")))
    if not files: continue
    info = json.load(open(os.path.join(d, "directions_info.json"))) if os.path.exists(os.path.join(d, "directions_info.json")) else {"frames": {}}
    byframe = {}
    for p in files:
        z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
        if meta["id"] not in ITEMS: continue
        byframe.setdefault(meta["frame"], []).append((meta, {k: z[k] for k in z.files if k != "__meta__"}))
    summary[model] = {}; report += [f"## {model}", ""]
    for fr, rows_f in sorted(byframe.items()):
        m0 = rows_f[0][0]; layers, scales = m0["layers"], m0["scales"]; key_r = "pmoral" if fr == "C" else "S"; summary[model][fr] = {}
        cos_line = "; ".join(f"L{l}: {info['frames'].get(fr, {}).get(f'L{l}_A', {}).get('cos_stance_moral_norm', float('nan')):.2f}" for l in layers)
        report += [f"* {fr}: cosine(moral stance, norm stance) by layer {cos_line}"]
        for l in layers:
            for name in m0["directions"]:
                eff = {c: {s: [] for s in scales} for c in CATS}
                for meta, z in rows_f:
                    gap0 = float(z["perm_clean_S"] - z["rest_clean_S"]); denom = gap0 if fr != "C" else 1.0
                    if fr != "C" and gap0 < a.tau: continue
                    vals = []
                    for half in meta["halves_used"]:
                        kp, kr = f"perm_L{l}_{name}_{half}_{key_r}", f"rest_L{l}_{name}_{half}_{key_r}"
                        if kp not in z: continue
                        P, R = z[kp], z[kr]; c0 = 0.5 * (z[f"perm_clean_{key_r}"] + z[f"rest_clean_{key_r}"])
                        chg = 0.5 * (P + R) - c0
                        vals.append((chg[:, 0] - chg[:, 1:].mean(1)) / denom)
                    if not vals: continue
                    v = np.mean(vals, 0)
                    for si, s in enumerate(scales): eff[meta["category"]][s].append(float(v[si]))
                rec = {}
                for c in CATS:
                    if len(eff[c][scales[0]]) < 5: continue
                    rec[c] = {str(s): dict(effect=float(np.mean(eff[c][s])), ci95=ci(eff[c][s]), n=len(eff[c][s])) for s in scales}
                    up, down = rec[c].get("1.0"), rec[c].get("-1.0")
                    step = 0.5 * (up["effect"] - down["effect"]) if (up and down) else None; rec[c]["step_effect"] = step
                    opposite = bool(up and down and ((up["ci95"][0] > 0 and down["ci95"][1] < 0) or (up["ci95"][1] < 0 and down["ci95"][0] > 0)))
                    rec[c]["steerable"] = bool(opposite and (fr == "C" or abs(step) >= a.min_step)); rec[c]["sign"] = None if step is None else ("expected" if step > 0 else "reversed")
                same_sign = lambda cs: len({rec[c]["sign"] for c in cs}) == 1
                rec["shared"] = bool(all(c in rec and rec[c]["steerable"] for c in CATS) and same_sign(CATS)); rec["normative_shared"] = bool(all(c in rec and rec[c]["steerable"] for c in ("moral", "norm")) and same_sign(("moral", "norm")))
                summary[model][fr][f"L{l}_{name}"] = rec
                per_model_flags.setdefault((fr, name, "shared"), {}).setdefault(model, False); per_model_flags[(fr, name, "shared")][model] |= rec["shared"]
                per_model_flags.setdefault((fr, name, "normative"), {}).setdefault(model, False); per_model_flags[(fr, name, "normative")][model] |= rec["normative_shared"]
                rows.append(dict(model=model, frame=fr, layer=l, direction=name, **{f"step_{c}": rec.get(c, {}).get("step_effect") for c in CATS}, **{f"steerable_{c}": rec.get(c, {}).get("steerable") for c in CATS}, shared=rec["shared"]))
                unit = "of the gap per step" if fr != "C" else "in moral-word probability per step"
                report += [f"  * layer {l}, {name}: " + "; ".join(f"{c} {100 * rec[c]['step_effect']:+.1f}% [{100 * rec[c]['1.0']['ci95'][0]:+.1f}, {100 * rec[c]['1.0']['ci95'][1]:+.1f} at +1]{(' steerable, ' + rec[c]['sign']) if rec[c]['steerable'] else ''}" for c in CATS if c in rec and rec[c]["step_effect"] is not None)
                           + f" ({unit}) -> {'SHARED' if rec['shared'] else ('normative-shared' if rec['normative_shared'] else 'not shared')}"]
    report += [""]
report += ["## Counts of models (any layer counts once per model and frame)", ""] + [f"* frame {fr}, {name}, {kind}: {sum(v.values())} of {len(v)} models ({', '.join(m for m, f in v.items() if f)})" for (fr, name, kind), v in sorted(per_model_flags.items())]
summary["_count"] = {f"{fr}/{name}/{kind}": dict(models_with_effect=sum(v.values()), models=len(v)) for (fr, name, kind), v in per_model_flags.items()}
with open(os.path.join(a.out, "by_layer.csv"), "w", newline="") as f:
    if rows: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
