"""The answers to the category prompt."""
import argparse, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/category_frame"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/category_frame")
ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True)
ITEMS = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}; PRIMARY_SET, WHY = primary_item_set(a.items)
KINDS = ["moral", "prudential", "etiquette", "aesthetic", "epistemic"]


def auc(pos, neg):
    pos, neg = np.asarray(pos), np.asarray(neg)
    if len(pos) == 0 or len(neg) == 0: return None
    return float(((pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean()))


def standard_of(it):
    return "moral" if it["category"] == "moral" else (it.get("subtype", "") if it["category"] == "norm" else None)


summary = dict(accepted_pairs=PRIMARY_SET, models={}); report = ["# Categorisation frame: behaviour (exploratory)", "", f"Items: {WHY}.", ""]
usable = {}
for d in sorted(glob.glob(os.path.join(a.runs, "*"))):
    model = os.path.basename(d); rec = {}
    for p in sorted(glob.glob(os.path.join(d, "cat__*.json"))):
        J = json.load(open(p)); preset = J["preset"]; rows = [r for r in J["rows"] if r["id"] in ITEMS and r["p_norm"] is not None]
        if not rows: continue
        pm = {c: [r["p_norm"]["moral"] for r in rows if r["category"] == c] for c in ("moral", "norm", "descr")}
        res = dict(n_prompts=len(rows), covered_mean=float(np.mean([r["covered"] for r in rows])), p_moral_mean={c: float(np.mean(v)) for c, v in pm.items() if v}, auc_moral_vs_norm=auc(pm["moral"], pm["norm"]))
        five = [r for r in rows if standard_of(ITEMS[r["id"]]) in KINDS and (ITEMS[r["id"]]["category"] == "moral" or ITEMS[r["id"]].get("kind_ok", True))]
        if five:
            conf = {k: {k2: 0 for k2 in KINDS} for k in KINDS}; hits = 0
            for r in five:
                truth = standard_of(ITEMS[r["id"]]); pred = max(KINDS, key=lambda k: r["p_norm"][k]); conf[truth][pred] += 1; hits += (pred == truth)
            res["five_way_accuracy"] = hits / len(five); res["five_way_n"] = len(five); res["confusion"] = conf
            res["own_set_rank_mean"] = float(np.mean([sorted(KINDS, key=lambda k: -r["p_norm"][k]).index(standard_of(ITEMS[r["id"]])) + 1 for r in five]))
        res["usable"] = bool(res["auc_moral_vs_norm"] is not None and res["auc_moral_vs_norm"] >= 0.75 and res.get("five_way_accuracy", 0) > 0.2)
        usable.setdefault(preset, []).append((model, res["usable"])); rec[preset] = res
    if not rec: continue
    summary["models"][model] = rec; report += [f"## {model}", ""]
    for preset, r in rec.items():
        report += [f"* {preset}: category words cover {r['covered_mean']:.1%} of the distribution; P(moral set) moral {r['p_moral_mean'].get('moral', float('nan')):.2f}, norm {r['p_moral_mean'].get('norm', float('nan')):.2f}, descr {r['p_moral_mean'].get('descr', float('nan')):.2f}; "
                   f"AUC moral vs norm {r['auc_moral_vs_norm']:.2f}" + (f"; five-way argmax accuracy {r['five_way_accuracy']:.2f} (n={r['five_way_n']}, chance 0.20; mean rank of the true standard {r['own_set_rank_mean']:.2f})" if "five_way_accuracy" in r else "") + f" -> {'usable' if r['usable'] else 'not usable'}"]
        if "confusion" in r: report += ["  confusion (rows: annotators' standard; columns: model's argmax " + ", ".join(KINDS) + "): " + "; ".join(f"{k}: " + " ".join(str(r['confusion'][k][k2]) for k2 in KINDS) for k in KINDS)]
    report += [""]
report += ["## Usable models per preset", ""] + [f"* {preset}: {sum(u for _, u in v)} of {len(v)} models" for preset, v in usable.items()]
summary["usable"] = {preset: dict(models=[m for m, u in v if u], n_usable=sum(u for _, u in v), n_models=len(v)) for preset, v in usable.items()}
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
