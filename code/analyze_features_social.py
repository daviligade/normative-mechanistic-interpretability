"""Feature activations with the cue 'socially'."""
import argparse, json, math, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import primary_item_set, check_analysis_items

ap = argparse.ArgumentParser()
ap.add_argument("--runs", required=True, help="runs of frames A1 and B (runs/features)"); ap.add_argument("--runs-social", required=True, help="runs of frame A1s (runs/features_social)")
ap.add_argument("--runs-cues", default=None, help="runs of frame A1l (runs/features_cues), optional, descriptive"); ap.add_argument("--items", required=True); ap.add_argument("--located", required=True)
ap.add_argument("--main", default=None, help="summary.json of the main feature analysis, for H6 in A1 and B"); ap.add_argument("--out", required=True)
ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--perm-calib", type=int, default=20000); ap.add_argument("--subsamples", type=int, default=20)
ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--seed", type=int, default=20261028); ap.add_argument("--no-h6", action="store_true", help="skip the permutation counts (software tests)")
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
LOCATED = json.load(open(a.located)); PRIMARY_SET, PRIMARY_WHY = primary_item_set(a.items); MAIN = json.load(open(a.main))["conditions"] if a.main else {}
ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
CATS = ("moral", "norm", "descr"); KINDS = ("prudential", "etiquette", "aesthetic", "epistemic"); MIX = ("prudential", "aesthetic", "epistemic")
EARLY = lambda layer, site: site == "mlp_out" or layer <= 3; SILENT = 1e-6


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def n_sig(X1, X2, P):
    Z = np.concatenate([X1, X2]).astype(np.float32); n1, n = len(X1), len(X1) + len(X2); m = Z.shape[1]; P = max(P, 20 * m)
    if m == 0: return 0
    obs = np.abs(X1.mean(0) - X2.mean(0)); tot = Z.sum(0); hits = np.zeros(m); done = 0
    while done < P:
        k = min(1000, P - done); sel = np.argsort(rng.random((k, n)), axis=1)[:, :n1]; M = np.zeros((k, n), dtype=np.float32); np.put_along_axis(M, sel, 1.0, axis=1); s1 = M @ Z
        hits += (np.abs(s1 / n1 - (tot - s1) / (n - n1)) >= obs - 1e-9).sum(0); done += k
    return int((bh((hits + 1) / (P + 1)) < 0.05).sum())


def ratio_paired(x, y):
    if y.mean() < SILENT: return None, [None, None]
    idx = rng.integers(0, len(x), (a.boot, len(x))); bs = x[idx].mean(1) / np.maximum(y[idx].mean(1), 1e-12)
    return float(x.mean() / y.mean()), [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def ratio_unpaired(x, y):
    if y.mean() < SILENT: return None, [None, None]
    bs = np.array([x[rng.integers(0, len(x), len(x))].mean() / max(y[rng.integers(0, len(y), len(y))].mean(), 1e-12) for _ in range(a.boot)])
    return float(x.mean() / y.mean()), [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def reading(ci, above, below):
    return "not defined (set silent)" if ci[0] is None else (above if ci[0] > 0.5 else (below if ci[1] < 0.5 else "inconclusive"))


ADVERB = ("a non-moral adverb turns it on too", "not turned on by a non-moral adverb"); FRAME = ("follows the frame", "follows the content")
conds = sorted(c for c in os.listdir(a.runs_social) if os.path.exists(os.path.join(a.runs_social, c, "extract__A1s.npz")))
if not conds: sys.exit(f"[analyze_features_social] no condition with extract__A1s.npz under {a.runs_social}")
summary, behaviour_by_model = {}, {}
for cond in conds:
    paths = {"A1": os.path.join(a.runs, cond, "extract__A1.npz"), "B": os.path.join(a.runs, cond, "extract__B.npz"), "A1s": os.path.join(a.runs_social, cond, "extract__A1s.npz")}
    if a.runs_cues and os.path.exists(os.path.join(a.runs_cues, cond, "extract__A1l.npz")): paths["A1l"] = os.path.join(a.runs_cues, cond, "extract__A1l.npz")
    missing = [p for p in paths.values() if not os.path.exists(p)]
    if missing: sys.exit(f"[analyze_features_social] {cond}: missing {missing}")
    E = {fr: dict(np.load(p)) for fr, p in paths.items()}; FR = list(E)
    ids = {fr: [str(i) for i in E[fr]["ids"]] for fr in FR}
    assert all(ids[fr] == ids["A1"] for fr in FR), f"{cond}: the item lists differ between the frames"
    assert len({str(E[fr]["items_sha256"]) for fr in FR}) == 1, f"{cond}: the runs come from different item files"
    keep = np.array([i in ACC for i in ids["A1"]]); cat = np.array([str(c) for c in E["A1"]["category"]])[keep]; sub = np.array([str(s) for s in E["A1"]["subtype"]])[keep]
    for fr in FR:
        assert (np.array([str(c) for c in E[fr]["category"]])[keep] == cat).all(), f"{cond}: categories differ in frame {fr}"
        assert (np.array([str(s) for s in E[fr]["subtype"]])[keep] == sub).all(), f"{cond}: kinds of norm differ in frame {fr}"
    G = lambda fr, k: E[fr][k][keep]
    cfg = json.load(open(os.path.join(a.runs_social, cond, "run_config.json"))) if os.path.exists(os.path.join(a.runs_social, cond, "run_config.json")) else {}
    out = {"condition": cond, "model": cfg.get("model"), "layer": cfg.get("layer"), "site": cfg.get("site"), "frames": FR, "n_items": int(keep.sum()),
           "early": bool(EARLY(int(cfg.get("layer", 99)), cfg.get("site", "resid_post"))) if cfg else None}
    kind = {k: (cat == "norm") & (sub == k) for k in KINDS}; mix = (cat == "norm") & np.isin(sub, MIX)

    out["behaviour"] = {}
    for fr in FR:
        mass = (G(fr, "perm_clean_mass") + G(fr, "rest_clean_mass")) / 2; gap = G(fr, "perm_clean_S") - G(fr, "rest_clean_S")
        groups = {**{c: cat == c for c in CATS}, **kind, "mix_of_three": mix}
        rec = {g: dict(mass=float(mass[m].mean()), gap=float(gap[m].mean()), n=int(m.sum())) for g, m in groups.items() if m.any()}
        rec["moral_fit_ratio"] = rec["moral"]["gap"] / rec["norm"]["gap"] if rec.get("norm", {}).get("gap", 0) > 0 else None
        rec["etiquette_fit_ratio"] = rec["etiquette"]["gap"] / rec["mix_of_three"]["gap"] if ("etiquette" in rec and rec.get("mix_of_three", {}).get("gap", 0) > 0) else None
        out["behaviour"][fr] = rec
    if out["model"] and out["model"] not in behaviour_by_model: behaviour_by_model[out["model"]] = out["behaviour"]

    out["sets"] = {}; sets = LOCATED.get(cond, {})
    for name in ("original_vs_neutral_sig", "original_vs_norm_sig"):
        F = np.array(sets.get(name, []), dtype=int)
        if len(F) == 0: continue
        A = {fr: (G(fr, "perm_f")[:, F].astype(np.float32).mean(1) + G(fr, "rest_f")[:, F].astype(np.float32).mean(1)) / 2 for fr in FR}
        rec = dict(n_features=int(len(F)), mean_activation={f"{fr}/{c}": float(A[fr][cat == c].mean()) for fr in FR for c in CATS})
        for c in CATS:
            r, ci = ratio_paired(A["A1s"][cat == c], A["A1"][cat == c]); rec[f"A1s_over_A1/{c}"] = dict(ratio=r, ci95=ci, reading=reading(ci, *ADVERB))
            r, ci = ratio_paired(A["A1s"][cat == c], A["B"][cat == c]); rec[f"A1s_over_B/{c}"] = dict(ratio=r, ci95=ci)
        for other in ("descr", "norm"):
            r, ci = ratio_unpaired(A["A1s"][cat == other], A["A1s"][cat == "moral"]); rec[f"A1s_{other}_over_moral"] = dict(ratio=r, ci95=ci, reading=reading(ci, *FRAME))
        out["sets"][name] = rec

    out["H6"] = {}; out["fit_test"] = {}
    for fr in ("A1", "B"):
        m = MAIN.get(cond, {}).get("H6_discovery", {}).get(fr)
        if m and "moral_vs_norm_equalised" in m:
            out["H6"][fr] = dict(source="main analysis", moral_vs_norm_equalised=m["moral_vs_norm_equalised"], norm_vs_norm_equalised=m["norm_vs_norm_equalised"],
                                 more=bool(m["moral_vs_norm_equalised"] > max(m["norm_vs_norm_equalised"].values())))
    if not a.no_h6:
        mn = np.isin(cat, ["moral", "norm"])
        for fr in [f for f in ("A1s", "A1", "B", "A1l") if f in FR]:
            act = ((G(fr, "perm_f")[mn] > 0).sum(0) + (G(fr, "rest_f")[mn] > 0).sum(0)) >= a.min_active
            X = np.abs(G(fr, "perm_f").astype(np.float32) - G(fr, "rest_f").astype(np.float32))[:, act]
            draw = lambda mask, g: X[rng.choice(np.where(mask)[0], g, replace=False)]
            if fr == "A1s" and all(kind[k].sum() >= 5 for k in KINDS):
                splits = [(("prudential", "etiquette"), ("aesthetic", "epistemic")), (("prudential", "aesthetic"), ("etiquette", "epistemic")), (("prudential", "epistemic"), ("etiquette", "aesthetic"))]
                g = min([int((cat == "moral").sum())] + [int(((cat == "norm") & np.isin(sub, side)).sum()) for sp in splits for side in sp])
                rec = dict(n_features_tested=int(act.sum()), group_size_equalised=g,
                           moral_vs_norm_equalised=float(np.mean([n_sig(draw(cat == "moral", g), draw(cat == "norm", g), a.perm_calib) for _ in range(a.subsamples)])),
                           norm_vs_norm_equalised={"+".join(s1) + " vs " + "+".join(s2): float(np.mean([n_sig(draw((cat == "norm") & np.isin(sub, s1), g), draw((cat == "norm") & np.isin(sub, s2), g), a.perm_calib)
                                                                                                        for _ in range(a.subsamples)])) for s1, s2 in splits})
                rec["more"] = bool(rec["moral_vs_norm_equalised"] > max(rec["norm_vs_norm_equalised"].values())); out["H6"][fr] = rec
            sizes = [int((cat == "moral").sum())] + [int(kind[k].sum()) for k in KINDS]
            if min(sizes) < 5: continue
            g = min(sizes); others = {k: (cat == "norm") & np.isin(sub, [r for r in MIX if r != k]) for k in MIX}
            cnt = lambda m1, m2: float(np.mean([n_sig(draw(m1, g), draw(m2, g), a.perm_calib) for _ in range(a.subsamples)]))
            rec = dict(group_size=g, n_features_tested=int(act.sum()), moral_vs_mix=cnt(cat == "moral", mix), etiquette_vs_mix=cnt(kind["etiquette"], mix),
                       calibration={f"{k} vs other two": cnt(kind[k], others[k]) for k in MIX})
            top = max(rec["calibration"].values()); rec["largest_calibration"] = top
            rec["moral_apart"] = bool(rec["moral_vs_mix"] > top); rec["etiquette_apart"] = bool(rec["etiquette_vs_mix"] > top)
            rec["margin_moral"] = math.log((rec["moral_vs_mix"] + 1) / (top + 1)); rec["margin_etiquette"] = math.log((rec["etiquette_vs_mix"] + 1) / (top + 1))
            rec["total_count"] = rec["moral_vs_mix"] + rec["etiquette_vs_mix"] + sum(rec["calibration"].values())
            out["fit_test"][fr] = rec
    summary[cond] = out
    print(f"[analyze_features_social] {cond} done", flush=True)


med = lambda v: float(np.median(v)) if len(v) else None
ok = {m: (b["A1s"]["etiquette_fit_ratio"] is not None and b["B"]["etiquette_fit_ratio"] is not None and b["A1s"]["etiquette_fit_ratio"] > b["B"]["etiquette_fit_ratio"])
      for m, b in behaviour_by_model.items() if "A1s" in b}
check = dict(models=ok, n_pass=sum(ok.values()), n=len(ok), passed=sum(ok.values()) >= 5)
ref = {m: bool(b["A1"]["moral_fit_ratio"] > b["B"]["moral_fit_ratio"]) for m, b in behaviour_by_model.items() if b["A1"]["moral_fit_ratio"] is not None and b["B"]["moral_fit_ratio"] is not None}
also_moral = {m: bool(b["A1s"]["moral_fit_ratio"] > b["B"]["moral_fit_ratio"]) for m, b in behaviour_by_model.items() if "A1s" in b and b["A1s"]["moral_fit_ratio"] is not None and b["B"]["moral_fit_ratio"] is not None}
gainE = {m: b["A1s"]["etiquette_fit_ratio"] / b["B"]["etiquette_fit_ratio"] for m, b in behaviour_by_model.items()
         if "A1s" in b and b["A1s"]["etiquette_fit_ratio"] is not None and b["B"]["etiquette_fit_ratio"]}
gainM = {m: b["A1"]["moral_fit_ratio"] / b["B"]["moral_fit_ratio"] for m, b in behaviour_by_model.items() if b["A1"]["moral_fit_ratio"] is not None and b["B"]["moral_fit_ratio"]}
strength = dict(gain_etiquette_A1s_over_B=gainE, gain_moral_A1_over_B=gainM, median_gain_etiquette=med(list(gainE.values())), median_gain_moral=med(list(gainM.values())))
strength["comparable"] = bool(strength["median_gain_etiquette"] is not None and strength["median_gain_moral"] is not None
                              and strength["median_gain_etiquette"] - 1 >= (strength["median_gain_moral"] - 1) / 2)
manip = {"socially_suits_etiquette": check, "reference_morally_suits_moral": dict(models=ref, n_pass=sum(ref.values()), n=len(ref)),
         "socially_also_suits_moral": dict(models=also_moral, n_pass=sum(also_moral.values()), n=len(also_moral)), "strength": strength}

FT_FRAMES = [fr for fr in ("A1", "B", "A1s", "A1l") if any(fr in summary[c]["fit_test"] for c in summary)]
nE = {fr: sum(1 for c in summary if summary[c]["fit_test"].get(fr, {}).get("etiquette_apart")) for fr in FT_FRAMES}
nM = {fr: sum(1 for c in summary if summary[c]["fit_test"].get(fr, {}).get("moral_apart")) for fr in FT_FRAMES}
nC = {fr: sum(1 for c in summary if fr in summary[c]["fit_test"]) for fr in FT_FRAMES}
informative = [c for c in summary if all(fr in summary[c]["fit_test"] for fr in ("A1", "B", "A1s")) and sum(summary[c]["fit_test"][fr]["total_count"] for fr in ("A1", "B", "A1s")) >= 5]
dE = {c: summary[c]["fit_test"]["A1s"]["margin_etiquette"] - summary[c]["fit_test"]["B"]["margin_etiquette"] for c in informative}
dM = {c: summary[c]["fit_test"]["A1"]["margin_moral"] - summary[c]["fit_test"]["B"]["margin_moral"] for c in informative}
margin = dict(informative_conditions=informative, dE=dE, dM=dM, n_dE_positive=sum(v > 0 for v in dE.values()), median_dE=med(list(dE.values())), median_dM=med(list(dM.values())))
if margin["median_dE"] is None: margin_reading = "not defined (no informative condition)"
elif margin["n_dE_positive"] >= 0.75 * len(informative) and margin["median_dM"] > 0 and margin["median_dE"] >= margin["median_dM"] / 2: margin_reading = "fit"
elif margin["n_dE_positive"] <= 0.5 * len(informative): margin_reading = "no fit effect"
else: margin_reading = "in between"
steps = dict(reference_gap=(nM.get("A1", 0) - nM.get("B", 0)) if FT_FRAMES else None)
if a.no_h6 or not FT_FRAMES: fit_reading = "not computed (--no-h6)"
elif not check["passed"]: fit_reading = "not read: 'socially' did not suit the etiquette pairs better than the other kinds (check of the manipulation failed)"
elif nM["A1"] - nM["B"] < 4: fit_reading = "not informative: in this comparison the moral pairs do not stand apart much more with 'morally' than without a cue"
elif nE["B"] >= 11: fit_reading = f"counts leave no room (etiquette apart in {nE['B']} of {nC['B']} without a cue); margin reading: {margin_reading}"
else:
    dn = nE["A1s"] - nE["B"]; T = max(3, math.ceil((nM["A1"] - nM["B"]) / 2)); steps.update(dn=dn, threshold=T)
    fit_reading = "fit" if (dn >= T and nE["A1s"] > nE["A1"]) else ("no fit effect" if dn <= 1 else "in between")
if fit_reading.endswith("no fit effect"):
    fit_reading += (" (the cue suited the etiquette pairs about as well as 'morally' suits the moral pairs: a question that suits a kind of norm does not by itself make it stand apart)"
                    if strength["comparable"] else " (but the cue suited the etiquette pairs less than 'morally' suits the moral pairs, so this is a weaker test)")


def count_sets(group):
    cs = [c for c in summary if (group is None or summary[c]["early"] == group) and "A1s_over_A1/moral" in summary[c]["sets"].get("original_vs_neutral_sig", {})]
    rd = [summary[c]["sets"]["original_vs_neutral_sig"]["A1s_over_A1/moral"]["reading"] for c in cs]
    return dict(n=len(cs), above=sum(r == ADVERB[0] for r in rd), below=sum(r == ADVERB[1] for r in rd), inconclusive=sum(r == "inconclusive" for r in rd),
                above_means=ADVERB[0], below_means=ADVERB[1])
counts = {"sets": {"layer7_or_deeper": count_sets(False), "layer0_to_3": count_sets(True)}, "fit_test": dict(etiquette_apart=nE, moral_apart=nM, n=nC),
          "H6_more": {fr: sum(1 for c in summary if summary[c]["H6"].get(fr, {}).get("more")) for fr in ("A1", "B", "A1s")},
          "H6_conditions": {fr: sum(1 for c in summary if "more" in summary[c]["H6"].get(fr, {})) for fr in ("A1", "B", "A1s")}}
readings = {"fit_test": fit_reading, "margin": margin_reading, "steps": steps}
json.dump(dict(settings=vars(a), accepted_pairs=PRIMARY_SET, item_file_note=PRIMARY_WHY, n_items=len(ACC), manipulation_checks=manip, counts=counts, margin=margin,
               readings=readings, behaviour_by_model=behaviour_by_model, conditions=summary), open(os.path.join(a.out, "summary.json"), "w"), indent=1)


f2 = lambda x: "n/a" if x is None else f"{x:.2f}"
L = ["# A non-moral cue that suits one kind of norm: \"is socially\" (A1s) and the etiquette pairs, next to \"is morally\" (A1), no cue (B) and \"is logically\" (A1l)", "",
     "Exploratory. " + (f"Items: {PRIMARY_WHY}; {len(ACC)} items." if PRIMARY_SET else f"**Not the accepted item set ({PRIMARY_WHY}).**"), "",
     "## Check of the manipulation and strength of the fit (per model; behavioural gap ratios)", "",
     f"* 'socially' suits the etiquette pairs (etiquette fit ratio higher in A1s than in B): {check['n_pass']} of {check['n']} models -> {'passed' if check['passed'] else 'FAILED'}",
     f"* reference, 'morally' suits the moral pairs (moral fit ratio higher in A1 than in B): {manip['reference_morally_suits_moral']['n_pass']} of {manip['reference_morally_suits_moral']['n']} models",
     f"* 'socially' also suits the moral pairs (moral fit ratio higher in A1s than in B): {manip['socially_also_suits_moral']['n_pass']} of {manip['socially_also_suits_moral']['n']} models",
     f"* strength: median etiquette gain (A1s over B) {f2(strength['median_gain_etiquette'])}, median moral gain (A1 over B) {f2(strength['median_gain_moral'])} -> "
     + ("comparable (gain E - 1 at least half of gain M - 1)" if strength["comparable"] else "the etiquette fit is the weaker one"), "",
     "| model | etiquette fit ratio B / A1 / A1s | moral fit ratio B / A1 / A1s | answer-word mass, etiquette pairs, B / A1 / A1s |", "|---|---|---|---|"]
for m, b in behaviour_by_model.items():
    L.append(f"| {m} | " + " / ".join(f2(b[fr]["etiquette_fit_ratio"]) for fr in ("B", "A1", "A1s") if fr in b) + " | " + " / ".join(f2(b[fr]["moral_fit_ratio"]) for fr in ("B", "A1", "A1s") if fr in b)
             + " | " + " / ".join(f2(b[fr]["etiquette"]["mass"]) if "etiquette" in b[fr] else "n/a" for fr in ("B", "A1", "A1s") if fr in b) + " |")
L += ["", "## Readings", ""]
if FT_FRAMES:
    L.append("* Fit test (targets against the mix of prudential, aesthetic and epistemic pairs; " + ", ".join(f"{fr}" for fr in FT_FRAMES) + "): etiquette stands apart in "
             + " / ".join(f"{nE[fr]}" for fr in FT_FRAMES) + f" of {max(nC.values())} conditions, moral in " + " / ".join(f"{nM[fr]}" for fr in FT_FRAMES) + f" -> **{fit_reading}**")
    L.append(f"* Margin ({len(informative)} informative conditions): dE > 0 in {margin['n_dE_positive']}, median dE {f2(margin['median_dE'])}, median dM {f2(margin['median_dM'])} -> {margin_reading}"
             + ("" if fit_reading.startswith("counts leave no room") else " (secondary)"))
L.append(f"* H6 (moral vs norm yields more features than every split of the norm kinds): A1 {counts['H6_more']['A1']} of {counts['H6_conditions']['A1']}, B {counts['H6_more']['B']} of {counts['H6_conditions']['B']}, "
         f"A1s {counts['H6_more']['A1s']} of {counts['H6_conditions']['A1s']} (descriptive)")
for grp, v in counts["sets"].items():
    label = {"layer7_or_deeper": "layer 7 or deeper", "layer0_to_3": "layer 0 to 3"}[grp]
    L.append(f"* located moral-versus-neutral sets, moral pairs, A1s/A1, {label} ({v['n']} conditions): {v['above']} {v['above_means']}; {v['below']} {v['below_means']}; {v['inconclusive']} inconclusive")
L += ["", "## The located sets per condition", "", "| condition | layer | vs-neutral set, moral pairs: A1s/A1 [95 % CI] | B/A1 | A1s descr/moral [CI] | vs-norm set: A1s descr/moral [CI] |", "|---|---|---|---|---|---|"]
for cond, o in summary.items():
    s = o["sets"].get("original_vs_neutral_sig"); t = o["sets"].get("original_vs_norm_sig")
    if not s: continue
    ci = lambda r: f"{f2(r['ratio'])} [{f2(r['ci95'][0])}, {f2(r['ci95'][1])}]"
    ma = s["mean_activation"]; b_over = ma["B/moral"] / ma["A1/moral"] if ma["A1/moral"] >= SILENT else None
    L.append(f"| {cond} | {'MLP0' if o['site'] == 'mlp_out' else 'L' + str(o['layer'])} | {ci(s['A1s_over_A1/moral'])} | {f2(b_over)} | {ci(s['A1s_descr_over_moral'])} | " + (ci(t["A1s_descr_over_moral"]) if t else "-") + " |")
if FT_FRAMES:
    L += ["", f"## Fit test and H6 per condition (mean counts over {a.subsamples} subsamples)", "", "| condition | " + " | ".join(f"{fr}: etiquette, moral; largest calibration" for fr in FT_FRAMES) + " | H6 A1s: moral vs norm; best split |",
          "|---|" + "---|" * len(FT_FRAMES) + "---|"]
    for cond, o in summary.items():
        t = lambda fr: (f"{o['fit_test'][fr]['etiquette_vs_mix']:.1f}, {o['fit_test'][fr]['moral_vs_mix']:.1f}; {o['fit_test'][fr]['largest_calibration']:.1f}" if fr in o["fit_test"] else "-")
        h = (f"{o['H6']['A1s']['moral_vs_norm_equalised']:.1f}; {max(o['H6']['A1s']['norm_vs_norm_equalised'].values()):.1f}" if "A1s" in o["H6"] else "-")
        L.append(f"| {cond} | " + " | ".join(t(fr) for fr in FT_FRAMES) + f" | {h} |")
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
