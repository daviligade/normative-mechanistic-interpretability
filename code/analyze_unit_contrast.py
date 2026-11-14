"""Counts of neurons that separate two groups of pairs."""
import argparse, csv, glob, json, os
import numpy as np

ap = argparse.ArgumentParser(); ap.add_argument("--runs", default="runs/units_contrast"); ap.add_argument("--out", default="results/units_contrast"); ap.add_argument("--corr-bar", type=float, default=0.5)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
summary = {}; report = ["# Neuron contrasts: stance, normative-vs-descriptive, category frame (discovery; exploratory)", ""]
rows = {"mvn": [], "stance": [], "normdescr": [], "catC": []}
fmt = lambda v, d=2: "n/a" if v is None else f"{v:.{d}f}"


def late(vals, L):
    v = [x for l, x in vals if l >= L // 2 and x is not None]; return float(np.median(v)) if v else None


for contrast in ("mvn", "stance", "normdescr", "catC"):
    dirs = sorted(glob.glob(os.path.join(a.runs, contrast, "*")));
    if not dirs: continue
    report += [f"## {contrast}", ""]; summary[contrast] = {}
    for d in dirs:
        model = os.path.basename(d); rec = {}
        for p in sorted(glob.glob(os.path.join(d, "sets__*.json"))):
            S = json.load(open(p)); fr = S["frame"]; L = S["n_layers"]; cnt = {int(l): c for l, c in S["counts"].items()}
            if contrast == "mvn":
                more_sh = sorted(l for l, c in cnt.items() if c.get("more_than_any_split")); more_m = sorted(l for l, c in cnt.items() if c.get("matched_raw_more_than_any_split")); both = sorted(set(more_sh) & set(more_m))
                tot_sh = int(sum(c["full_size"] for c in cnt.values())); tot_raw = int(sum(c["raw_full_size"] for c in cnt.values())); tot_m = int(sum(c["matched_raw_moral_vs_norm"] for c in cnt.values()))
                peak = max(cnt, key=lambda l: cnt[l]["full_size"]); gm = S.get("gap_matching", {})
                nulls = [c for c in cnt.values() if "null_moral_vs_moral_equalised" in c]; more_null = sorted(l for l, c in cnt.items() if c.get("more_than_any_split") and "null_moral_vs_moral_equalised" in c and c["moral_vs_norm_equalised"] > max(c["null_moral_vs_moral_equalised"], c.get("null_theme_vs_other_moral_equalised", 0)))
                r = dict(n_layers=L, total_share=tot_sh, total_raw=tot_raw, total_matched_raw=tot_m, peak_layer_share=peak, layers_share_more_than_any_split=more_sh, layers_matched_raw_more_than_any_split=more_m, layers_both=both, n_layers_both=len(both),
                         gap_matching=gm, total_selA=int(sum(len(v) for v in S["sets"]["selA"].values())), total_selB=int(sum(len(v) for v in S["sets"]["selB"].values())),
                         null_mean_moral_vs_moral=float(np.mean([c["null_moral_vs_moral_equalised"] for c in nulls])) if nulls else None, null_mean_theme_vs_other=float(np.mean([c["null_theme_vs_other_moral_equalised"] for c in nulls if "null_theme_vs_other_moral_equalised" in c])) if any("null_theme_vs_other_moral_equalised" in c for c in nulls) else None,
                         null_theme=next((c["null_theme"] for c in nulls if "null_theme" in c), None), layers_share_more_than_splits_and_nulls=more_null, mean_equalised_moral_vs_norm=float(np.mean([c["moral_vs_norm_equalised"] for c in cnt.values() if "moral_vs_norm_equalised" in c])) if any("moral_vs_norm_equalised" in c for c in cnt.values()) else None)
                eqs = {l: c["equal_size"] for l, c in cnt.items() if "equal_size" in c}
                if eqs:
                    e0 = next(iter(eqs.values())); kinds_ = list(e0["norm_vs_norm"])
                    r["equal_size"] = dict(group_size=sorted({e["group_size"] for e in eqs.values()}), theme=e0.get("theme"), n_layers=len(eqs),
                                           sum_moral_vs_norm=float(sum(e["moral_vs_norm"] for e in eqs.values())), sum_kind_splits={k: float(sum(e["norm_vs_norm"][k] for e in eqs.values())) for k in kinds_},
                                           sum_moral_vs_moral=float(sum(e["moral_vs_moral"] for e in eqs.values())), sum_theme_vs_other_moral=float(sum(e.get("theme_vs_other_moral", 0.0) for e in eqs.values())),
                                           layers_above_both_nulls=sorted(l for l, e in eqs.items() if e["moral_vs_norm"] > max(e["moral_vs_moral"], e.get("theme_vs_other_moral", 0.0))),
                                           layers_above_nulls_and_splits=sorted(l for l, e in eqs.items() if e["moral_vs_norm"] > max([e["moral_vs_moral"], e.get("theme_vs_other_moral", 0.0)] + list(e["norm_vs_norm"].values()))),
                                           layers_splits_above_both_nulls=sorted(l for l, e in eqs.items() if min(e["norm_vs_norm"].values()) > max(e["moral_vs_moral"], e.get("theme_vs_other_moral", 0.0))))
                rec[fr] = r
                for l, c in sorted(cnt.items()):
                    rows[contrast].append(dict(model=model, frame=fr, layer=l, depth=round((l + 1) / L, 4), n_tested=c["n_tested"], share_moral_vs_norm=c["full_size"], share_equalised=c.get("moral_vs_norm_equalised"), share_max_split=max(c["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in c else None,
                                               null_moral_vs_moral=c.get("null_moral_vs_moral_equalised"), null_theme_vs_other=c.get("null_theme_vs_other_moral_equalised"),
                                               share_more_than_any_split=c.get("more_than_any_split"), raw_moral_vs_norm=c["raw_full_size"], matched_raw=c["matched_raw_moral_vs_norm"], matched_raw_max_split=max(c["matched_raw_norm_vs_norm"].values()) if "matched_raw_norm_vs_norm" in c else None,
                                               matched_raw_more_than_any_split=c.get("matched_raw_more_than_any_split"), matched_share=c.get("matched_share_moral_vs_norm"), writing_answer=c.get("share_units_writing_answer"), selA=c.get("selA_size"), selB=c.get("selB_size")))
                report += [f"* {model}, {fr}: shares: {tot_sh} units separate moral from norm over {L} layers (raw responses: {tot_raw}; gap-matched raw: {tot_m}; moral gap {fmt(gm.get('mean_gap_moral_all'), 3)} vs norm {fmt(gm.get('mean_gap_norm_all'), 3)}, matched norm {fmt(gm.get('mean_gap_matched_norm'), 3)}); "
                           f"share count exceeds every split in {len(more_sh)} layers {more_sh}; gap-matched raw count in {len(more_m)} layers {more_m}; both in {len(both)} layers {both}; halves select {r['total_selA']} / {r['total_selB']} (capped)"
                           + (f"; nulls (mean per layer at equal size): moral vs moral {fmt(r['null_mean_moral_vs_moral'], 1)}, {r['null_theme']} vs other moral {fmt(r['null_mean_theme_vs_other'], 1)}, against moral vs norm {fmt(r['mean_equalised_moral_vs_norm'], 1)}; share count exceeds splits AND nulls in {len(more_null)} layers" if nulls else "")]
                if "equal_size" in r:
                    q = r["equal_size"]
                    report += [f"    at one group size (g = {q['group_size']}), summed over {q['n_layers']} layers: moral vs norm {q['sum_moral_vs_norm']:.0f}; kind splits " + ", ".join(f"{v:.0f}" for v in q["sum_kind_splits"].values())
                               + f"; moral vs moral {q['sum_moral_vs_moral']:.0f}; {q['theme']} vs other moral {q['sum_theme_vs_other_moral']:.0f}. Layers where moral vs norm exceeds both nulls: {len(q['layers_above_both_nulls'])}; "
                               + f"both nulls and every split: {len(q['layers_above_nulls_and_splits'])}; where every kind split exceeds both nulls: {len(q['layers_splits_above_both_nulls'])}"]
            elif contrast == "stance":
                cm = [(l, c.get("corr_moral_norm")) for l, c in cnt.items()]; cnd = [(l, c.get("corr_norm_descr")) for l, c in cnt.items()]
                ob = sum(c["overlap_moral_norm"]["observed"] for c in cnt.values()); ex = sum(c["overlap_moral_norm"]["expected"] for c in cnt.values())
                obn = sum(c["overlap_norm_descr"]["observed"] for c in cnt.values()); exn = sum(c["overlap_norm_descr"]["expected"] for c in cnt.values())
                same = [c["shared_moral_norm_same_sign"] for c in cnt.values() if c.get("shared_moral_norm_same_sign") is not None]
                tot = {k: int(sum(c[f"{k}_size"] for c in cnt.values())) for k in ("moral", "norm", "descr", "normative")}
                peak = {k: max(cnt, key=lambda l: cnt[l][f"{k}_size"]) for k in ("moral", "norm", "descr")}
                writing = int(sum(c.get("normative_units_writing_answer", 0) for c in cnt.values()))
                r = dict(n_layers=L, total_units=tot, peak_layer=peak, corr_moral_norm_median=float(np.median([x for _, x in cm if x is not None])) if any(x is not None for _, x in cm) else None, corr_moral_norm_late=late(cm, L),
                         corr_norm_descr_median=float(np.median([x for _, x in cnd if x is not None])) if any(x is not None for _, x in cnd) else None, corr_norm_descr_late=late(cnd, L),
                         overlap_moral_norm=dict(observed=ob, expected=round(ex, 1)), overlap_norm_descr=dict(observed=obn, expected=round(exn, 1)), shared_same_sign_median=float(np.median(same)) if same else None,
                         normative_units_writing_answer=writing, normative_units_writing_answer_share=round(writing / tot["normative"], 3) if tot["normative"] else None)
                r["reading"] = ("shared stance code" if (r["corr_moral_norm_late"] or 0) >= a.corr_bar and ob > ex else "separate codes" if (r["corr_moral_norm_late"] or 0) < 0.2 and ob <= 1.5 * ex else "in between")
                rec[fr] = r
                for l, c in sorted(cnt.items()):
                    rows[contrast].append(dict(model=model, frame=fr, layer=l, depth=round((l + 1) / L, 4), n_tested=c["n_tested"], moral=c["moral_size"], norm=c["norm_size"], descr=c["descr_size"], normative=c["normative_size"],
                                               corr_moral_norm=c.get("corr_moral_norm"), corr_norm_descr=c.get("corr_norm_descr"), overlap_obs=c["overlap_moral_norm"]["observed"], overlap_exp=c["overlap_moral_norm"]["expected"],
                                               shared_same_sign=c.get("shared_moral_norm_same_sign"), writing_answer=c.get("normative_units_writing_answer"), selA=c.get("selA_size"), selB=c.get("selB_size")))
                report += [f"* {model}, {fr}: consistent-direction units (sum over {L} layers) moral {tot['moral']}, norm {tot['norm']}, descr {tot['descr']}, normative {tot['normative']} (peaks at layers {peak['moral']}/{peak['norm']}/{peak['descr']}); "
                           f"corr(moral, norm) median {fmt(r['corr_moral_norm_median'])}, late layers {fmt(r['corr_moral_norm_late'])}; overlap {ob} vs {ex:.1f} expected; shared units same sign {fmt(r['shared_same_sign_median'])}; "
                           f"corr(norm, descr) late {fmt(r['corr_norm_descr_late'])}, overlap {obn} vs {exn:.1f}; normative units in the top decile of answer weight {writing} ({fmt(r['normative_units_writing_answer_share'])}) -> {r['reading']}"]
            elif contrast == "normdescr":
                more = sorted(l for l, c in cnt.items() if c.get("more_than_any_split")); tot = int(sum(c["normative_vs_descr"] for c in cnt.values())); also = int(sum(c["normative_units_also_moral_vs_norm"] for c in cnt.values()))
                eq = {k: float(np.mean([c[k] for c in cnt.values() if k in c])) if any(k in c for c in cnt.values()) else None for k in ("normative_vs_descr_equalised", "moral_vs_descr_equalised", "norm_vs_descr_equalised", "moral_vs_norm_equalised")}
                peak = max(cnt, key=lambda l: cnt[l]["normative_vs_descr"])
                r = dict(n_layers=L, total_normative_vs_descr=tot, peak_layer=peak, layers_more_than_any_split=more, n_layers_more=len(more), mean_equalised_counts=eq, normative_units_also_moral_vs_norm=also, share_also_moral_vs_norm=round(also / tot, 3) if tot else None,
                         total_selA=int(sum(len(v) for v in S["sets"]["selA"].values())), total_selB=int(sum(len(v) for v in S["sets"]["selB"].values())))
                rec[fr] = r
                for l, c in sorted(cnt.items()):
                    rows[contrast].append(dict(model=model, frame=fr, layer=l, depth=round((l + 1) / L, 4), n_tested=c["n_tested"], normative_vs_descr=c["normative_vs_descr"], moral_vs_descr=c["moral_vs_descr"], norm_vs_descr=c["norm_vs_descr"], both_kinds=c["both_kinds_vs_descr"],
                                               moral_vs_norm=c["moral_vs_norm"], also_moral_vs_norm=c["normative_units_also_moral_vs_norm"], eq_normative=c.get("normative_vs_descr_equalised"), eq_moral=c.get("moral_vs_descr_equalised"), eq_norm=c.get("norm_vs_descr_equalised"),
                                               eq_moral_vs_norm=c.get("moral_vs_norm_equalised"), split_max=max(c["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in c else None, normative_at_split_size=c.get("normative_vs_descr_at_split_size"),
                                               more_than_any_split=c.get("more_than_any_split"), selA=c.get("selA_size"), selB=c.get("selB_size")))
                report += [f"* {model}, {fr}: {tot} units respond more to a judged than to a descriptive edit (peak layer {peak}); at equal sizes per layer on average normative {fmt(eq['normative_vs_descr_equalised'], 1)}, moral {fmt(eq['moral_vs_descr_equalised'], 1)}, "
                           f"norm {fmt(eq['norm_vs_descr_equalised'], 1)} vs descriptive, moral vs norm {fmt(eq['moral_vs_norm_equalised'], 1)}; normative vs descriptive exceeds every norm-vs-norm split in {len(more)} layers {more}; "
                           f"of the normative units {also} ({fmt(r['share_also_moral_vs_norm'])}) also separate moral from norm; halves select {r['total_selA']} / {r['total_selB']} (capped)"]
            else:
                more = sorted(l for l, c in cnt.items() if c.get("more_than_any_split")); full = {l: c["full_size"] for l, c in cnt.items()}; writing = int(sum(c.get("moral_vs_norm_writing_category", 0) for c in cnt.values()))
                r = dict(n_layers=L, total_full=int(sum(full.values())), peak_layer=max(full, key=full.get), layers_more_than_any_split=more, n_layers_more=len(more), writing_category=writing, writing_category_share=round(writing / sum(full.values()), 3) if sum(full.values()) else None,
                         total_selA=int(sum(len(v) for v in S["sets"]["selA"].values())), total_selB=int(sum(len(v) for v in S["sets"]["selB"].values())), cat_preset=S.get("cat_preset"))
                rec[fr] = r
                for l, c in sorted(cnt.items()):
                    rows[contrast].append(dict(model=model, frame=fr, layer=l, depth=round((l + 1) / L, 4), n_tested=c["n_tested"], moral_vs_norm_full=c["full_size"], equalised_moral_vs_norm=c.get("moral_vs_norm_equalised"),
                                               max_norm_vs_norm=max(c["norm_vs_norm_equalised"].values()) if "norm_vs_norm_equalised" in c else None, more_than_any_split=c.get("more_than_any_split"), writing_category=c.get("moral_vs_norm_writing_category"), selA=c.get("selA_size"), selB=c.get("selB_size")))
                report += [f"* {model}: C minus B, {r['total_full']} units separate moral from norm pairs over {L} layers (peak at layer {r['peak_layer']}); moral vs norm exceeds every norm-vs-norm split in {len(more)} layers {more}; "
                           f"in the top decile of category weight {writing} ({fmt(r['writing_category_share'])}); halves select {r['total_selA']} / {r['total_selB']} (capped)"]
        summary[contrast][model] = rec
    report += [""]
    with open(os.path.join(a.out, f"depth_{contrast}.csv"), "w", newline="") as f:
        if rows[contrast]: w = csv.DictWriter(f, fieldnames=list(rows[contrast][0])); w.writeheader(); w.writerows(rows[contrast])
if "mvn" in summary:
    if any("equal_size" in r for rec in summary["mvn"].values() for r in rec.values()):
        report += ["## At one group size: moral vs norm, the kind splits and the two within-moral nulls (summed over layers)", ""]
        for fr in sorted({fr for rec in summary["mvn"].values() for fr in rec}):
            E = {m: rec[fr]["equal_size"] for m, rec in summary["mvn"].items() if fr in rec and "equal_size" in rec[fr]}
            if not E: continue
            above_nulls = [m for m, q in E.items() if q["sum_moral_vs_norm"] > max(q["sum_moral_vs_moral"], q["sum_theme_vs_other_moral"])]
            above_all = [m for m, q in E.items() if q["sum_moral_vs_norm"] > max([q["sum_moral_vs_moral"], q["sum_theme_vs_other_moral"]] + list(q["sum_kind_splits"].values()))]
            splits_above = [m for m, q in E.items() if min(q["sum_kind_splits"].values()) > max(q["sum_moral_vs_moral"], q["sum_theme_vs_other_moral"])]
            ratio = [q["sum_moral_vs_norm"] / max(q["sum_theme_vs_other_moral"], 1.0) for q in E.values()]
            report += [f"* frame {fr}: moral vs norm exceeds both within-moral nulls in {len(above_nulls)} of {len(E)} models, and also every kind split in {len(above_all)} ({', '.join(above_all)}); "
                       f"every kind split exceeds both nulls in {len(splits_above)}; moral vs norm over the theme null: median ratio {float(np.median(ratio)):.1f} (range {min(ratio):.1f} to {max(ratio):.1f})"]
        report += [""]
    report += ["## Models with layers where moral vs norm exceeds every norm-vs-norm split on shares and on gap-matched raw responses", ""]
    for fr in sorted({fr for rec in summary["mvn"].values() for fr in rec}):
        n = [m for m, rec in summary["mvn"].items() if fr in rec and rec[fr]["n_layers_both"] > 0]; ns = [m for m, rec in summary["mvn"].items() if fr in rec and rec[fr]["layers_share_more_than_any_split"]]
        report += [f"* frame {fr}: both readings {len(n)} of {sum(1 for rec in summary['mvn'].values() if fr in rec)} models ({', '.join(n)}); shares alone {len(ns)}"]
    report += [""]
if "stance" in summary:
    cnt = {}
    for model, rec in summary["stance"].items():
        for fr, r in rec.items(): cnt.setdefault(fr, []).append(r["reading"])
    report += ["## Count of models by stance reading", ""] + [f"* frame {fr}: " + ", ".join(f"{k} {v}" for k, v in sorted({x: rs.count(x) for x in set(rs)}.items())) for fr, rs in sorted(cnt.items())] + [""]
    summary["stance_count"] = {fr: {x: rs.count(x) for x in set(rs)} for fr, rs in cnt.items()}
if "normdescr" in summary:
    report += ["## Models with layers where normative vs descriptive exceeds every norm-vs-norm split", ""]
    for fr in sorted({fr for rec in summary["normdescr"].values() for fr in rec}):
        n = [m for m, rec in summary["normdescr"].items() if fr in rec and rec[fr]["n_layers_more"] > 0]; report += [f"* frame {fr}: {len(n)} of {sum(1 for rec in summary['normdescr'].values() if fr in rec)} models ({', '.join(n)})"]
    report += [""]
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); open(os.path.join(a.out, "report.md"), "w").write("\n".join(report) + "\n"); print("\n".join(report))
