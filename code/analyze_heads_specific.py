"""Heads selected for specificity on half of the pairs, read on the other half."""
import argparse, glob, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import primary_item_set, check_analysis_items
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "circuits")); from run_units import welch_sig, SPLITS

ap = argparse.ArgumentParser()
ap.add_argument("--runs", default="runs/heads"); ap.add_argument("--items", required=True); ap.add_argument("--located", default="located/heads.json"); ap.add_argument("--out", default="results/heads_specific")
ap.add_argument("--condition", default="p2r_all"); ap.add_argument("--readout", default="S"); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--k", type=int, default=10)
ap.add_argument("--splits", type=int, default=200); ap.add_argument("--subsamples", type=int, default=20); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--models", nargs="+", default=None)
ap.add_argument("--any-items", action="store_true")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
PRIMARY_SET, WHY = primary_item_set(a.items); ITEMS = [i for i in json.load(open(a.items)) if i.get("accepted", True)]; IDX = {it["id"]: k for k, it in enumerate(ITEMS)}; N = len(ITEMS)
CAT = np.array([it["category"] for it in ITEMS]); SUB = np.array([(it.get("subtype") or "") if (it["category"] == "norm" and it.get("kind_ok", True)) else "" for it in ITEMS]); LOCATED = json.load(open(a.located))
KINDS = ("prudential", "etiquette", "aesthetic", "epistemic")


def load_model(folder, model):
    out = {}; fz = LOCATED[model]
    for f in sorted(glob.glob(os.path.join(folder, "*__*.npz"))):
        if f.endswith(".tmp.npz"): continue
        frame, iid = os.path.basename(f)[:-4].split("__", 1)
        if iid not in IDX: continue
        z = np.load(f, allow_pickle=False); key = f"{a.condition}__{a.readout}"
        if key not in z.files: continue
        meta = json.loads(str(z["__meta__"])); arr = z[key]; assert arr.shape == (fz["n_layers"], fz["n_heads"])
        d = out.setdefault(frame, dict(E=np.full((N, arr.size), np.nan, dtype=np.float32), gap=np.full(N, np.nan)))
        d["E"][IDX[iid]] = np.abs(arr).ravel(); d["gap"][IDX[iid]] = meta["base_perm"]["S"] - meta["base_rest"]["S"]
    return out


def held_out_ratio(Sh, g1, g2, k, splits, rng):
    r = []
    for _ in range(splits):
        p1, p2 = rng.permutation(g1), rng.permutation(g2); h1, h2 = len(p1) // 2, len(p2) // 2
        top = np.argsort(-(Sh[p1[:h1]].mean(0) - Sh[p2[:h2]].mean(0)))[:k]
        r.append(float(Sh[p1[h1:]][:, top].sum(1).mean() / max(Sh[p2[h2:]][:, top].sum(1).mean(), 1e-9)))
    r = np.array(r); return dict(mean=float(r.mean()), p2_5=float(np.percentile(r, 2.5)), p97_5=float(np.percentile(r, 97.5)), share_above_1=float((r > 1).mean()))


models = a.models or sorted(os.path.basename(d) for d in glob.glob(os.path.join(a.runs, "*")) if os.path.isdir(d) and os.path.basename(d) in LOCATED)
summary = dict(settings=vars(a), accepted_pairs=PRIMARY_SET, models={}); report = ["# Heads selected for specificity on the new pairs, read held out (exploratory)", "", f"Items: {WHY}. k = {a.k} heads, {a.splits} splits.", ""]; counts = {}
for m in models:
    D = load_model(os.path.join(a.runs, m), m); summary["models"][m] = {}
    for fr, d in sorted(D.items()):
        have = ~np.isnan(d["gap"]); tot = np.nansum(d["E"], 1); ok = have & (d["gap"] >= a.tau) & (tot > 0); Sh = d["E"] / np.where(tot > 0, tot, 1)[:, None]
        mi, ni = np.where(ok & (CAT == "moral"))[0], np.where(ok & (CAT == "norm"))[0]
        if len(mi) < 30 or len(ni) < 30: continue
        rec = dict(n_moral=int(len(mi)), n_norm=int(len(ni)), n_heads=int(Sh.shape[1]))
        rec["moral_selected_moral_over_norm"] = held_out_ratio(Sh, mi, ni, a.k, a.splits, rng); rec["norm_selected_norm_over_moral"] = held_out_ratio(Sh, ni, mi, a.k, a.splits, rng)
        rec["kind_splits"] = {}
        for s1, s2 in SPLITS:
            i1, i2 = np.where(ok & np.isin(SUB, s1))[0], np.where(ok & np.isin(SUB, s2))[0]
            if len(i1) >= 20 and len(i2) >= 20: rec["kind_splits"]["+".join(s1) + " vs " + "+".join(s2)] = dict(held_out_ratio(Sh, i1, i2, a.k, a.splits, rng), n1=int(len(i1)), n2=int(len(i2)))

        Va = Sh[ok]; cat_ok = CAT[ok]; sub_ok = SUB[ok]; act = np.ones(Va.shape[1], bool)
        rec["heads_differing_full"] = int(welch_sig(Va[cat_ok == "moral"], Va[cat_ok == "norm"]).sum())
        sides = [np.where(np.isin(sub_ok, side))[0] for sp in SPLITS for side in sp]
        if all(len(s) >= 10 for s in sides):
            g = min([len(mi), len(ni)] + [len(s) for s in sides]); pick = lambda idx: Va[rng.choice(idx, g, replace=False)]
            mo_i, no_i = np.where(cat_ok == "moral")[0], np.where(cat_ok == "norm")[0]
            rec["group_size_equalised"] = int(g); rec["heads_differing_moral_vs_norm_equalised"] = float(np.mean([welch_sig(pick(mo_i), pick(no_i)).sum() for _ in range(a.subsamples)]))
            rec["heads_differing_norm_vs_norm_equalised"] = {"+".join(s1) + " vs " + "+".join(s2): float(np.mean([welch_sig(pick(np.where(np.isin(sub_ok, s1))[0]), pick(np.where(np.isin(sub_ok, s2))[0])).sum() for _ in range(a.subsamples)])) for s1, s2 in SPLITS}
            rec["more_heads_than_any_split"] = bool(rec["heads_differing_moral_vs_norm_equalised"] > max(rec["heads_differing_norm_vs_norm_equalised"].values()))
        ms = rec["moral_selected_moral_over_norm"]; ctrl_hi = max([v["p97_5"] for v in rec["kind_splits"].values()], default=None)
        rec["moral_specific_heads"] = bool(ms["p2_5"] > 1 and (ctrl_hi is None or ms["p2_5"] > ctrl_hi)); counts.setdefault(fr, []).append(rec["moral_specific_heads"])
        summary["models"][m][fr] = rec
        report += [f"* {m}, {fr}: moral-selected (by difference) moral/norm held out {ms['mean']:.2f} [{ms['p2_5']:.2f}, {ms['p97_5']:.2f}]; mirror norm/moral {rec['norm_selected_norm_over_moral']['mean']:.2f} [{rec['norm_selected_norm_over_moral']['p2_5']:.2f}, {rec['norm_selected_norm_over_moral']['p97_5']:.2f}]; "
                   + "kind splits " + ", ".join(f"{v['mean']:.2f} [{v['p2_5']:.2f}, {v['p97_5']:.2f}]" for v in rec["kind_splits"].values())
                   + (f"; heads with a differing share: moral vs norm {rec['heads_differing_moral_vs_norm_equalised']:.1f} vs splits " + ", ".join(f"{v:.1f}" for v in rec["heads_differing_norm_vs_norm_equalised"].values()) + f" (g = {rec['group_size_equalised']})" if "group_size_equalised" in rec else "")
                   + f" -> {'MORAL-SPECIFIC HEADS' if rec['moral_specific_heads'] else 'not specific'}"]
report += ["", "## Count of models with moral-specific heads (held-out ratio above 1 and above every kind-split control)", ""] + [f"* frame {fr}: {sum(v)} of {len(v)} models" for fr, v in sorted(counts.items())]
summary["count"] = {fr: dict(models_with_specific_heads=sum(v), models=len(v)) for fr, v in counts.items()}
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
