"""The Jacobian-lens readout by depth."""
import argparse, csv, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import check_analysis_items, primary_item_set

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/jlens_readout"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="results/jlens_readout")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--auc-bar", type=float, default=0.75); ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True)
LOCATED, WHY = primary_item_set(a.items); ITEMS = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
NORM_KINDS = ("prudential", "etiquette", "aesthetic", "epistemic")


def auc(pos, neg):
    pos, neg = np.asarray(pos, float), np.asarray(neg, float)
    if len(pos) == 0 or len(neg) == 0: return None
    return float((np.mean([(p > neg).mean() + 0.5 * (p == neg).mean() for p in pos])))


summary = {}; rows = []; report = ["# Jacobian-lens readout at the final token (exploratory)", "", f"Items: {WHY}.", ""]
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
        L = rows_f[0][0]["n_layers"]; names = rows_f[0][0]["set_names"]; iset = {c: names.index(c) for c in names}

        cat = np.array([m["category"] for m, _ in rows_f]); sub = np.array([ITEMS[m["id"]].get("subtype") or "" for m, _ in rows_f]); conf = np.array([bool(ITEMS[m["id"]].get("kind_ok", False)) for m, _ in rows_f])
        lp = np.stack([0.5 * (z["perm_set_logp"] + z["rest_set_logp"]) for _, z in rows_f])
        moral_score = lp[:, :, iset["moral"]] - np.mean([lp[:, :, iset[k]] for k in NORM_KINDS], 0)
        aucs = [auc(moral_score[cat == "moral", l], moral_score[cat == "norm", l]) for l in range(L)]
        five = [iset[k] for k in ("moral",) + NORM_KINDS]; std_of = {"moral": 0, **{k: i + 1 for i, k in enumerate(NORM_KINDS)}}
        elig = (cat == "moral") | ((cat == "norm") & conf & np.isin(sub, NORM_KINDS)); truth = np.array([std_of["moral"] if c == "moral" else std_of.get(s, -1) for c, s in zip(cat, sub)])
        acc5 = [float(np.mean(np.argmax(lp[elig][:, l, :][:, five], 1) == truth[elig])) if elig.any() else None for l in range(L)]

        gapL = np.stack([z["perm_S"] - z["rest_S"] for _, z in rows_f]); final = gapL[:, -1]; ok = final >= a.tau
        frac = gapL / np.where(np.abs(final[:, None]) > 1e-9, final[:, None], np.nan)
        prof = {c: np.nanmean(frac[(cat == c) & ok], 0) if ((cat == c) & ok).sum() >= 5 else None for c in ("moral", "norm", "descr")}
        def arrival(pr):
            if pr is None: return None
            idx = np.where(pr >= 0.5)[0]; return float((idx[0] + 1) / L) if len(idx) else None
        def dip(pr):
            if pr is None: return None
            idx = np.where(pr >= 0.5)[0]; stop = idx[0] if len(idx) else L; return float(np.min(pr[:stop])) if stop > 0 else None
        best_l = int(np.nanargmax([x if x is not None else np.nan for x in aucs])); first_l = next((l for l, x in enumerate(aucs) if x is not None and x >= a.auc_bar), None)
        best5 = int(np.nanargmax([x if x is not None else np.nan for x in acc5])) if any(x is not None for x in acc5) else None
        rec = dict(n_layers=L, n_moral=int((cat == "moral").sum()), n_norm=int((cat == "norm").sum()), n_descr=int((cat == "descr").sum()), auc_by_layer=aucs, best_auc=aucs[best_l], best_auc_layer=best_l, best_auc_depth=round((best_l + 1) / L, 3),
                   first_layer_auc_at_bar=first_l, first_depth_auc_at_bar=None if first_l is None else round((first_l + 1) / L, 3), auc_final=aucs[-1], acc5_by_layer=acc5, best_acc5=None if best5 is None else acc5[best5], best_acc5_layer=best5, acc5_final=acc5[-1],
                   n_elig_five_way=int(elig.sum()), arrival_depth={c: arrival(prof[c]) for c in prof}, dip_min={c: dip(prof[c]) for c in prof}, gap_fraction_profile={c: (None if prof[c] is None else [round(float(x), 4) for x in prof[c]]) for c in prof})
        summary[model][fr] = rec
        for l in range(L):
            rows.append(dict(model=model, frame=fr, layer=l, depth=round((l + 1) / L, 4), auc_moral_vs_norm=aucs[l], acc_five_way=acc5[l], **{f"gapfrac_{c}": (None if prof[c] is None else float(prof[c][l])) for c in prof}))
        fmt = lambda v: "n/a" if v is None else f"{v:.2f}"
        report += [f"* {fr}: moral readout AUC (moral vs norm) best {fmt(rec['best_auc'])} at layer {best_l} (depth {rec['best_auc_depth']}), first >= {a.auc_bar} at layer {first_l} (depth {rec['first_depth_auc_at_bar']}), at the output {fmt(rec['auc_final'])}; "
                   f"five-way accuracy best {fmt(rec['best_acc5'])} at layer {best5} (n = {rec['n_elig_five_way']}, chance 0.20), at the output {fmt(rec['acc5_final'])}; "
                   f"arrival depth of the judgment moral {fmt(rec['arrival_depth']['moral'])} / norm {fmt(rec['arrival_depth']['norm'])} / descr {fmt(rec['arrival_depth']['descr'])}; dip minimum moral {fmt(rec['dip_min']['moral'])} / norm {fmt(rec['dip_min']['norm'])}"]
    report += [""]
with open(os.path.join(a.out, "by_layer.csv"), "w", newline="") as f:
    if rows: w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
