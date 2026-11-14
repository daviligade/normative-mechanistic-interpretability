"""Feature activations under other cue words and positions."""
import argparse, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import primary_item_set, check_analysis_items

ap = argparse.ArgumentParser()
ap.add_argument("--runs", required=True, help="runs of frames A1 and B (runs/features)"); ap.add_argument("--runs-cues", required=True, help="runs of frames A1l and A1p (runs/features_cues)")
ap.add_argument("--runs-e", default=None, help="runs of frame A1e (runs/features_ethically), optional"); ap.add_argument("--items", required=True); ap.add_argument("--located", required=True)
ap.add_argument("--main", default=None, help="summary.json of the main feature analysis, for H6 in A1 and B"); ap.add_argument("--out", required=True)
ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--perm", type=int, default=20000); ap.add_argument("--perm-calib", type=int, default=20000); ap.add_argument("--subsamples", type=int, default=20)
ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--seed", type=int, default=20261027); ap.add_argument("--no-h6", action="store_true", help="skip the permutation counts (software tests)")
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
LOCATED = json.load(open(a.located)); PRIMARY_SET, PRIMARY_WHY = primary_item_set(a.items); MAIN = json.load(open(a.main))["conditions"] if a.main else {}
ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
CATS = ("moral", "norm", "descr"); KINDS = ("prudential", "etiquette", "aesthetic", "epistemic"); REST = ("prudential", "etiquette", "aesthetic")
EARLY = lambda layer, site: site == "mlp_out" or layer <= 3; SILENT = 1e-6


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def n_sig(X1, X2, P):
    Z = np.concatenate([X1, X2]).astype(np.float32); n1, n = len(X1), len(X1) + len(X2); m = Z.shape[1]; P = max(P, 20 * m)
    obs = np.abs(X1.mean(0) - X2.mean(0)); tot = Z.sum(0); hits = np.zeros(m); done = 0
    while done < P:
        k = min(1000, P - done); sel = np.argsort(rng.random((k, n)), axis=1)[:, :n1]; M = np.zeros((k, n), dtype=np.float32); np.put_along_axis(M, sel, 1.0, axis=1); s1 = M @ Z
        hits += (np.abs(s1 / n1 - (tot - s1) / (n - n1)) >= obs - 1e-9).sum(0); done += k
    return int((bh((hits + 1) / (P + 1)) < 0.05).sum())


def ratio_paired(x, y):
    if y.mean() < SILENT: return None, [None, None]
    idx = rng.integers(0, len(x), (a.boot, len(x))); bs = x[idx].mean(1) / np.maximum(y[idx].mean(1), 1e-12)
    return float(x.mean() / y.mean()), [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def reading(ci, above, below):
    return "not defined (set silent)" if ci[0] is None else (above if ci[0] > 0.5 else (below if ci[1] < 0.5 else "inconclusive"))


READ = {"A1e": ("moral cue in either wording", "the word 'morally'"), "A1l": ("a non-moral adverb turns it on too", "not turned on by a non-moral adverb"),
        "A1p": ("the moral question in context", "tied to the word at the final position")}

conds = sorted(c for c in os.listdir(a.runs_cues) if all(os.path.exists(os.path.join(a.runs_cues, c, f"extract__{f}.npz")) for f in ("A1l", "A1p")))
if not conds: sys.exit(f"[analyze_features_cues] no condition with extract__A1l.npz and extract__A1p.npz under {a.runs_cues}")
summary, behaviour_by_model = {}, {}
for cond in conds:
    paths = {"A1": os.path.join(a.runs, cond, "extract__A1.npz"), "B": os.path.join(a.runs, cond, "extract__B.npz"),
             "A1l": os.path.join(a.runs_cues, cond, "extract__A1l.npz"), "A1p": os.path.join(a.runs_cues, cond, "extract__A1p.npz")}
    if a.runs_e and os.path.exists(os.path.join(a.runs_e, cond, "extract__A1e.npz")): paths["A1e"] = os.path.join(a.runs_e, cond, "extract__A1e.npz")
    missing = [p for p in paths.values() if not os.path.exists(p)]
    if missing: sys.exit(f"[analyze_features_cues] {cond}: missing {missing}")
    E = {fr: dict(np.load(p)) for fr, p in paths.items()}; FR = list(E)
    ids = {fr: [str(i) for i in E[fr]["ids"]] for fr in FR}
    assert all(ids[fr] == ids["A1"] for fr in FR), f"{cond}: the item lists differ between the frames"
    assert len({str(E[fr]["items_sha256"]) for fr in FR}) == 1, f"{cond}: the runs come from different item files"
    keep = np.array([i in ACC for i in ids["A1"]]); cat = np.array([str(c) for c in E["A1"]["category"]])[keep]; sub = np.array([str(s) for s in E["A1"]["subtype"]])[keep]
    for fr in FR: assert (np.array([str(c) for c in E[fr]["category"]])[keep] == cat).all(), f"{cond}: categories differ in frame {fr}"
    G = lambda fr, k: E[fr][k][keep]
    cfg = json.load(open(os.path.join(a.runs_cues, cond, "run_config.json"))) if os.path.exists(os.path.join(a.runs_cues, cond, "run_config.json")) else {}
    out = {"condition": cond, "model": cfg.get("model"), "layer": cfg.get("layer"), "site": cfg.get("site"), "frames": FR, "n_items": int(keep.sum()),
           "early": bool(EARLY(int(cfg.get("layer", 99)), cfg.get("site", "resid_post"))) if cfg else None}
    norm_kind = {k: (cat == "norm") & (sub == k) for k in KINDS}; rest = (cat == "norm") & np.isin(sub, REST)

    out["behaviour"] = {}
    for fr in FR:
        mass = (G(fr, "perm_clean_mass") + G(fr, "rest_clean_mass")) / 2; gap = G(fr, "perm_clean_S") - G(fr, "rest_clean_S")
        groups = {**{c: cat == c for c in CATS}, **norm_kind, "rest_of_norms": rest}
        rec = {g: dict(mass=float(mass[m].mean()), gap=float(gap[m].mean()), n=int(m.sum())) for g, m in groups.items() if m.any()}
        rec["moral_fit_ratio"] = rec["moral"]["gap"] / rec["norm"]["gap"] if rec["norm"]["gap"] > 0 else None
        rec["epistemic_fit_ratio"] = rec["epistemic"]["gap"] / rec["rest_of_norms"]["gap"] if rec.get("rest_of_norms", {}).get("gap", 0) > 0 else None
        out["behaviour"][fr] = rec
    if out["model"] and out["model"] not in behaviour_by_model: behaviour_by_model[out["model"]] = out["behaviour"]

    out["sets"] = {}; sets = LOCATED.get(cond, {})
    for name in ("original_vs_neutral_sig", "original_vs_norm_sig"):
        F = np.array(sets.get(name, []), dtype=int)
        if len(F) == 0: continue
        A = {fr: (G(fr, "perm_f")[:, F].astype(np.float32).mean(1) + G(fr, "rest_f")[:, F].astype(np.float32).mean(1)) / 2 for fr in FR}
        rec = dict(n_features=int(len(F)), mean_activation={f"{fr}/{c}": float(A[fr][cat == c].mean()) for fr in FR for c in CATS})
        for fr in [f for f in ("A1e", "A1l", "A1p") if f in FR]:
            for c in CATS:
                r, ci = ratio_paired(A[fr][cat == c], A["A1"][cat == c]); rec[f"{fr}_over_A1/{c}"] = dict(ratio=r, ci95=ci, reading=reading(ci, *READ[fr]))
                r, ci = ratio_paired(A[fr][cat == c], A["B"][cat == c]); rec[f"{fr}_over_B/{c}"] = dict(ratio=r, ci95=ci)
        out["sets"][name] = rec

    out["H6"] = {}; out["fit_test"] = {}
    for fr in ("A1", "B"):
        m = MAIN.get(cond, {}).get("H6_discovery", {}).get(fr)
        if m and "moral_vs_norm_equalised" in m:
            out["H6"][fr] = dict(source="main analysis", moral_vs_norm_equalised=m["moral_vs_norm_equalised"], norm_vs_norm_equalised=m["norm_vs_norm_equalised"],
                                 more=bool(m["moral_vs_norm_equalised"] > max(m["norm_vs_norm_equalised"].values())))
    if not a.no_h6:
        mn = np.isin(cat, ["moral", "norm"])
        for fr in ("A1l", "A1p", "A1", "B"):
            act = ((G(fr, "perm_f")[mn] > 0).sum(0) + (G(fr, "rest_f")[mn] > 0).sum(0)) >= a.min_active
            X = np.abs(G(fr, "perm_f").astype(np.float32) - G(fr, "rest_f").astype(np.float32))[:, act]
            draw = lambda mask, g: X[rng.choice(np.where(mask)[0], g, replace=False)]
            if fr in ("A1l", "A1p") and all(((cat == "norm") & (sub == k)).sum() >= 5 for k in KINDS):
                splits = [(("prudential", "etiquette"), ("aesthetic", "epistemic")), (("prudential", "aesthetic"), ("etiquette", "epistemic")), (("prudential", "epistemic"), ("etiquette", "aesthetic"))]
                g = min([int((cat == "moral").sum())] + [int(((cat == "norm") & np.isin(sub, side)).sum()) for sp in splits for side in sp])
                rec = dict(n_features_tested=int(act.sum()), group_size_equalised=g,
                           moral_vs_norm_equalised=float(np.mean([n_sig(draw(cat == "moral", g), draw(cat == "norm", g), a.perm_calib) for _ in range(a.subsamples)])),
                           norm_vs_norm_equalised={"+".join(s1) + " vs " + "+".join(s2): float(np.mean([n_sig(draw((cat == "norm") & np.isin(sub, s1), g), draw((cat == "norm") & np.isin(sub, s2), g), a.perm_calib)
                                                                                                        for _ in range(a.subsamples)])) for s1, s2 in splits})
                rec["more"] = bool(rec["moral_vs_norm_equalised"] > max(rec["norm_vs_norm_equalised"].values())); out["H6"][fr] = rec
            if fr in ("A1", "B", "A1l"):
                sizes = [int((cat == "moral").sum())] + [int(norm_kind[k].sum()) for k in KINDS]
                if min(sizes) < 5: continue
                g = min(sizes); others = {k: (cat == "norm") & np.isin(sub, [r for r in REST if r != k]) for k in REST}
                cnt = lambda m1, m2: float(np.mean([n_sig(draw(m1, g), draw(m2, g), a.perm_calib) for _ in range(a.subsamples)]))
                rec = dict(group_size=g, moral_vs_rest=cnt(cat == "moral", rest), epistemic_vs_rest=cnt(norm_kind["epistemic"], rest),
                           calibration={f"{k} vs other two": cnt(norm_kind[k], others[k]) for k in REST})
                top = max(rec["calibration"].values()); rec["moral_apart"] = bool(rec["moral_vs_rest"] > top); rec["epistemic_apart"] = bool(rec["epistemic_vs_rest"] > top)
                out["fit_test"][fr] = rec
    summary[cond] = out
    print(f"[analyze_features_cues] {cond} done", flush=True)


def check(ratio_key, frame):
    ok = {m: (b[frame][ratio_key] is not None and b["B"][ratio_key] is not None and b[frame][ratio_key] > b["B"][ratio_key]) for m, b in behaviour_by_model.items() if frame in b}
    return dict(models=ok, n_pass=sum(ok.values()), n=len(ok), passed=sum(ok.values()) >= 5)
manip = {"logically_fits_epistemic": check("epistemic_fit_ratio", "A1l"), "morally_speaking_is_a_moral_question": check("moral_fit_ratio", "A1p"),
         "reference_morally": check("moral_fit_ratio", "A1")}

def count_sets(frame, group):
    cs = [c for c in summary if (group is None or summary[c]["early"] == group) and f"{frame}_over_A1/moral" in summary[c]["sets"].get("original_vs_neutral_sig", {})]
    rd = [summary[c]["sets"]["original_vs_neutral_sig"][f"{frame}_over_A1/moral"]["reading"] for c in cs]; hi, lo = READ[frame]
    return dict(n=len(cs), above=sum(r == hi for r in rd), below=sum(r == lo for r in rd), inconclusive=sum(r == "inconclusive" for r in rd), above_means=hi, below_means=lo)
counts = {"sets": {fr: {"layer7_or_deeper": count_sets(fr, False), "layer0_to_3": count_sets(fr, True)} for fr in ("A1e", "A1l", "A1p") if any(fr in s["frames"] for s in summary.values())},
          "H6_more": {fr: sum(1 for c in summary if summary[c]["H6"].get(fr, {}).get("more")) for fr in ("A1", "B", "A1l", "A1p")},
          "H6_conditions": {fr: sum(1 for c in summary if "more" in summary[c]["H6"].get(fr, {})) for fr in ("A1", "B", "A1l", "A1p")},
          "fit_test": {fr: dict(moral_apart=sum(1 for c in summary if summary[c]["fit_test"].get(fr, {}).get("moral_apart")),
                                epistemic_apart=sum(1 for c in summary if summary[c]["fit_test"].get(fr, {}).get("epistemic_apart")),
                                n=sum(1 for c in summary if fr in summary[c]["fit_test"])) for fr in ("A1", "B", "A1l")}}
ft = counts["fit_test"]
if not manip["logically_fits_epistemic"]["passed"]: fit_reading = "not read: 'logically' did not fit the epistemic pairs better than the other kinds (check of the manipulation failed)"
elif ft["A1l"]["epistemic_apart"] > ft["A1"]["epistemic_apart"] and ft["A1l"]["epistemic_apart"] > ft["B"]["epistemic_apart"] and ft["A1l"]["moral_apart"] < ft["A1"]["moral_apart"]: fit_reading = "fit"
elif ft["A1l"]["moral_apart"] >= ft["A1"]["moral_apart"] - 2 and ft["A1l"]["epistemic_apart"] <= ft["B"]["epistemic_apart"]: fit_reading = "moral content"
else: fit_reading = "mixed"
n_p = counts["H6_more"]["A1p"]
a1p_reading = ("not read: 'Morally speaking' did not work as a moral question (check of the manipulation failed)" if not manip["morally_speaking_is_a_moral_question"]["passed"] else
               ("the separation follows the moral question in context" if n_p >= 9 else ("the separation needs the cue word at the final position" if n_p <= 5 else "in between")))
readings = {"fit_test": fit_reading, "H6_A1p": a1p_reading}
json.dump(dict(settings=vars(a), accepted_pairs=PRIMARY_SET, item_file_note=PRIMARY_WHY, n_items=len(ACC), manipulation_checks=manip, counts=counts, readings=readings,
               behaviour_by_model=behaviour_by_model, conditions=summary), open(os.path.join(a.out, "summary.json"), "w"), indent=1)


f2 = lambda x: "n/a" if x is None else f"{x:.2f}"
L = ["# Cue frames for the features: \"is logically\" (A1l) and \"Morally speaking, ... is\" (A1p), next to \"is morally\" (A1), no cue (B) and \"is ethically\" (A1e)", "",
     "Exploratory. " + (f"Items: {PRIMARY_WHY}; {len(ACC)} items." if PRIMARY_SET else f"**Not the accepted item set ({PRIMARY_WHY}).**"), "",
     "## Checks of the manipulation (per model; behavioural gap ratios)", "",
     f"* 'logically' fits the epistemic pairs (epistemic fit ratio higher in A1l than in B): {manip['logically_fits_epistemic']['n_pass']} of {manip['logically_fits_epistemic']['n']} models -> {'passed' if manip['logically_fits_epistemic']['passed'] else 'FAILED'}",
     f"* 'Morally speaking' works as a moral question (moral fit ratio higher in A1p than in B): {manip['morally_speaking_is_a_moral_question']['n_pass']} of {manip['morally_speaking_is_a_moral_question']['n']} models -> {'passed' if manip['morally_speaking_is_a_moral_question']['passed'] else 'FAILED'}",
     f"* reference, 'morally' (moral fit ratio higher in A1 than in B): {manip['reference_morally']['n_pass']} of {manip['reference_morally']['n']} models", "",
     "| model | moral fit ratio B / A1 / A1p / A1l | epistemic fit ratio B / A1 / A1l | answer-word mass, moral pairs, B / A1 / A1p / A1l |", "|---|---|---|---|"]
for m, b in behaviour_by_model.items():
    L.append(f"| {m} | " + " / ".join(f2(b[fr]["moral_fit_ratio"]) for fr in ("B", "A1", "A1p", "A1l") if fr in b) + " | " + " / ".join(f2(b[fr]["epistemic_fit_ratio"]) for fr in ("B", "A1", "A1l") if fr in b)
             + " | " + " / ".join(f2(b[fr]["moral"]["mass"]) for fr in ("B", "A1", "A1p", "A1l") if fr in b) + " |")
L += ["", "## Readings", "", f"* Fit test (moral and epistemic pairs against the other norms, A1 / B / A1l): moral stands apart in {ft['A1']['moral_apart']} / {ft['B']['moral_apart']} / {ft['A1l']['moral_apart']} of {ft['A1l']['n']} conditions, "
      f"epistemic in {ft['A1']['epistemic_apart']} / {ft['B']['epistemic_apart']} / {ft['A1l']['epistemic_apart']} -> **{fit_reading}**",
      f"* H6 (moral vs norm yields more features than every split of the norm kinds): A1 {counts['H6_more']['A1']} of {counts['H6_conditions']['A1']}, B {counts['H6_more']['B']} of {counts['H6_conditions']['B']}, "
      f"A1l {counts['H6_more']['A1l']} of {counts['H6_conditions']['A1l']}, A1p {counts['H6_more']['A1p']} of {counts['H6_conditions']['A1p']} -> A1p: **{a1p_reading}**"]
for fr, c in counts["sets"].items():
    for grp, v in c.items():
        label = {"layer7_or_deeper": "layer 7 or deeper", "layer0_to_3": "layer 0 to 3"}[grp]
        L.append(f"* located moral-versus-neutral sets, moral pairs, {fr}/A1, {label} ({v['n']} conditions): {v['above']} {v['above_means']}; {v['below']} {v['below_means']}; {v['inconclusive']} inconclusive")
L += ["", "## The located moral-versus-neutral sets per condition (moral pairs)", "", "| condition | layer | " + " | ".join(f"{fr}/A1 [95 % CI]" for fr in ("A1e", "A1l", "A1p")) + " | B/A1 | descr in A1l / A1p (over moral) |", "|---|---|---|---|---|---|---|"]
for cond, o in summary.items():
    s = o["sets"].get("original_vs_neutral_sig")
    if not s: continue
    cell = lambda fr: (f"{f2(s[f'{fr}_over_A1/moral']['ratio'])} [{f2(s[f'{fr}_over_A1/moral']['ci95'][0])}, {f2(s[f'{fr}_over_A1/moral']['ci95'][1])}]" if f"{fr}_over_A1/moral" in s else "-")
    ma = s["mean_activation"]; b_over = ma["B/moral"] / ma["A1/moral"] if ma["A1/moral"] >= SILENT else None
    dm = lambda fr: (ma[f"{fr}/descr"] / ma[f"{fr}/moral"] if ma.get(f"{fr}/moral", 0) >= SILENT else None)
    L.append(f"| {cond} | {'MLP0' if o['site'] == 'mlp_out' else 'L' + str(o['layer'])} | {cell('A1e')} | {cell('A1l')} | {cell('A1p')} | {f2(b_over)} | {f2(dm('A1l'))} / {f2(dm('A1p'))} |")
L += ["", "## H6 and the fit test per condition", "", "| condition | H6 moral vs norm; best split: A1 / B / A1l / A1p | fit test A1: moral, epistemic; best calibration | B | A1l |", "|---|---|---|---|---|"]
for cond, o in summary.items():
    h = lambda fr: (f"{o['H6'][fr]['moral_vs_norm_equalised']:.1f}; {max(o['H6'][fr]['norm_vs_norm_equalised'].values()):.1f}" if fr in o["H6"] else "-")
    t = lambda fr: (f"{o['fit_test'][fr]['moral_vs_rest']:.1f}, {o['fit_test'][fr]['epistemic_vs_rest']:.1f}; {max(o['fit_test'][fr]['calibration'].values()):.1f}" if fr in o["fit_test"] else "-")
    L.append(f"| {cond} | {h('A1')} / {h('B')} / {h('A1l')} / {h('A1p')} | {t('A1')} | {t('B')} | {t('A1l')} |")
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
