"""Feature activations with the cue 'ethically'."""
import argparse, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import primary_item_set, check_analysis_items

ap = argparse.ArgumentParser()
ap.add_argument("--runs", required=True, help="runs of frames A1 and B (runs/features)"); ap.add_argument("--runs-e", required=True, help="runs of frame A1e (runs/features_ethically)")
ap.add_argument("--items", required=True); ap.add_argument("--located", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--main", default=None, help="summary.json of the main feature analysis, for the H6 results of A1 and B")
ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--perm", type=int, default=20000); ap.add_argument("--perm-calib", type=int, default=20000); ap.add_argument("--subsamples", type=int, default=20)
ap.add_argument("--min-active", type=int, default=5); ap.add_argument("--seed", type=int, default=20261026); ap.add_argument("--no-h6", action="store_true", help="skip H6 (software tests)")
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
LOCATED = json.load(open(a.located)); PRIMARY_SET, PRIMARY_WHY = primary_item_set(a.items); MAIN = json.load(open(a.main))["conditions"] if a.main else {}
ACC = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
CATS = ("moral", "norm", "descr"); FR = ("A1", "A1e", "B"); EARLY = lambda layer, site: site == "mlp_out" or layer <= 3


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def n_sig(X1, X2, P):
    Z = np.concatenate([X1, X2]).astype(np.float32); n1, n = len(X1), len(X1) + len(X2); m = Z.shape[1]; P = max(P, 20 * m)
    obs = np.abs(X1.mean(0) - X2.mean(0)); tot = Z.sum(0); hits = np.zeros(m); done = 0
    while done < P:
        k = min(1000, P - done); sel = np.argsort(rng.random((k, n)), axis=1)[:, :n1]; M = np.zeros((k, n), dtype=np.float32); np.put_along_axis(M, sel, 1.0, axis=1); s1 = M @ Z
        hits += (np.abs(s1 / n1 - (tot - s1) / (n - n1)) >= obs - 1e-9).sum(0); done += k
    return int((bh((hits + 1) / (P + 1)) < 0.05).sum())


SILENT = 1e-6


def ratio_paired(x, y):
    if y.mean() < SILENT: return None, [None, None]
    idx = rng.integers(0, len(x), (a.boot, len(x))); bs = x[idx].mean(1) / np.maximum(y[idx].mean(1), 1e-12)
    return float(x.mean() / y.mean()), [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def ratio_unpaired(x, y):
    if y.mean() < SILENT: return None, [None, None]
    bs = np.array([x[rng.integers(0, len(x), len(x))].mean() / max(y[rng.integers(0, len(y), len(y))].mean(), 1e-12) for _ in range(a.boot)])
    return float(x.mean() / y.mean()), [float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))]


def read_cue(ci): return "not defined (set silent)" if ci[0] is None else ("moral cue in either wording" if ci[0] > 0.5 else ("the word 'morally'" if ci[1] < 0.5 else "inconclusive"))
def read_frame(ci): return "not defined (set silent)" if ci[0] is None else ("follows the frame" if ci[0] > 0.5 else ("follows the content" if ci[1] < 0.5 else "inconclusive"))


conds = sorted(c for c in os.listdir(a.runs_e) if os.path.exists(os.path.join(a.runs_e, c, "extract__A1e.npz")))
if not conds: sys.exit(f"[analyze_features_ethically] no extract__A1e.npz under {a.runs_e}")
summary = {}
for cond in conds:
    paths = {"A1": os.path.join(a.runs, cond, "extract__A1.npz"), "B": os.path.join(a.runs, cond, "extract__B.npz"), "A1e": os.path.join(a.runs_e, cond, "extract__A1e.npz")}
    missing = [p for p in paths.values() if not os.path.exists(p)]
    if missing: sys.exit(f"[analyze_features_ethically] {cond}: missing {missing}")
    E = {fr: dict(np.load(p)) for fr, p in paths.items()}
    ids = {fr: [str(i) for i in E[fr]["ids"]] for fr in FR}
    assert ids["A1"] == ids["A1e"] == ids["B"], f"{cond}: the item lists differ between the frames"
    assert len({str(E[fr]["items_sha256"]) for fr in FR}) == 1, f"{cond}: the runs come from different item files"
    keep = np.array([i in ACC for i in ids["A1"]]); cat = np.array([str(c) for c in E["A1"]["category"]])[keep]; sub = np.array([str(s) for s in E["A1"]["subtype"]])[keep]
    for fr in FR: assert (np.array([str(c) for c in E[fr]["category"]])[keep] == cat).all(), f"{cond}: categories differ in frame {fr}"
    G = lambda fr, k: E[fr][k][keep]
    cfg = json.load(open(os.path.join(a.runs_e, cond, "run_config.json"))) if os.path.exists(os.path.join(a.runs_e, cond, "run_config.json")) else {}
    out = {"condition": cond, "model": cfg.get("model"), "layer": cfg.get("layer"), "site": cfg.get("site"), "n_items": int(keep.sum()),
           "early": bool(EARLY(int(cfg.get("layer", 99)), cfg.get("site", "resid_post"))) if cfg else None}

    out["behaviour"] = {}; out["capture"] = {}
    for fr in FR:
        mass = (G(fr, "perm_clean_mass") + G(fr, "rest_clean_mass")) / 2; gap = G(fr, "perm_clean_S") - G(fr, "rest_clean_S")
        out["behaviour"][fr] = {c: dict(mass=float(mass[cat == c].mean()), gap=float(gap[cat == c].mean()), n_gap_at_least_0_02=int(((gap >= 0.02) & (cat == c)).sum()), n=int((cat == c).sum())) for c in CATS}
        D, DH = G(fr, "perm_h") - G(fr, "rest_h"), G(fr, "perm_xh") - G(fr, "rest_xh"); r2 = 1 - ((D - DH) ** 2).sum(1) / (D ** 2).sum(1)
        out["capture"][fr] = dict(R2={c: float(r2[cat == c].mean()) for c in CATS}, mean_R2=float(r2.mean()), flagged=bool(r2.mean() < 0.5))

    out["sets"] = {}; sets = LOCATED.get(cond, {})
    for name in ("original_vs_neutral_sig", "original_vs_norm_sig"):
        F = np.array(sets.get(name, []), dtype=int)
        if len(F) == 0: continue
        A = {fr: (G(fr, "perm_f")[:, F].astype(np.float32).mean(1) + G(fr, "rest_f")[:, F].astype(np.float32).mean(1)) / 2 for fr in FR}
        rec = dict(n_features=int(len(F)), mean_activation={f"{fr}/{c}": float(A[fr][cat == c].mean()) for fr in FR for c in CATS})
        for c in CATS:
            r, ci = ratio_paired(A["A1e"][cat == c], A["A1"][cat == c]); rec[f"A1e_over_A1/{c}"] = dict(ratio=r, ci95=ci, reading=read_cue(ci))
            r, ci = ratio_paired(A["B"][cat == c], A["A1"][cat == c]); rec[f"B_over_A1/{c}"] = dict(ratio=r, ci95=ci)
        for other in ("descr", "norm"):
            r, ci = ratio_unpaired(A["A1e"][cat == other], A["A1e"][cat == "moral"]); rec[f"A1e_{other}_over_moral"] = dict(ratio=r, ci95=ci, reading=read_frame(ci))
        out["sets"][name] = rec

    out["H6"] = {}
    for fr in (("A1", "B") if a.no_h6 else ("A1", "A1e", "B")):
        if fr != "A1e":
            m = MAIN.get(cond, {}).get("H6_discovery", {}).get(fr)
            if m and "moral_vs_norm_equalised" in m:
                out["H6"][fr] = dict(source="main analysis", group_size_equalised=m["group_size_equalised"], moral_vs_norm_equalised=m["moral_vs_norm_equalised"],
                                     norm_vs_norm_equalised=m["norm_vs_norm_equalised"], more=bool(m["moral_vs_norm_equalised"] > max(m["norm_vs_norm_equalised"].values())))
            continue
        c, s = cat, sub; mn = np.isin(c, ["moral", "norm"])
        act = ((G(fr, "perm_f")[mn] > 0).sum(0) + (G(fr, "rest_f")[mn] > 0).sum(0)) >= a.min_active
        X = np.abs(G(fr, "perm_f").astype(np.float32) - G(fr, "rest_f").astype(np.float32))[:, act]
        rec = dict(n_features_tested=int(act.sum()), full_size=dict(n_moral=int((c == "moral").sum()), n_norm=int((c == "norm").sum()), n_significant=n_sig(X[c == "moral"], X[c == "norm"], a.perm)))
        kinds = [k for k in ("prudential", "etiquette", "aesthetic", "epistemic") if ((c == "norm") & (s == k)).sum() >= 5]
        if len(kinds) == 4:
            splits = [(("prudential", "etiquette"), ("aesthetic", "epistemic")), (("prudential", "aesthetic"), ("etiquette", "epistemic")), (("prudential", "epistemic"), ("etiquette", "aesthetic"))]
            g = min([int((c == "moral").sum())] + [int(((c == "norm") & np.isin(s, side)).sum()) for sp in splits for side in sp]); mi, ni = np.where(c == "moral")[0], np.where(c == "norm")[0]
            rec["group_size_equalised"] = g
            rec["moral_vs_norm_equalised"] = float(np.mean([n_sig(X[rng.choice(mi, g, replace=False)], X[rng.choice(ni, g, replace=False)], a.perm_calib) for _ in range(a.subsamples)]))
            rec["norm_vs_norm_equalised"] = {"+".join(s1) + " vs " + "+".join(s2): float(np.mean([n_sig(X[rng.choice(np.where((c == "norm") & np.isin(s, s1))[0], g, replace=False)],
                                                                                                     X[rng.choice(np.where((c == "norm") & np.isin(s, s2))[0], g, replace=False)], a.perm_calib) for _ in range(a.subsamples)])) for s1, s2 in splits}
            top = max(rec["norm_vs_norm_equalised"].values()); rec["more"] = bool(rec["moral_vs_norm_equalised"] > top)
            rec["reading"] = ("no feature detected in any comparison: no directional reading" if rec["moral_vs_norm_equalised"] == 0 and top == 0 else
                              ("moral vs norm yields no more features than norm kinds among themselves" if not rec["more"] else "moral vs norm yields more features than any split of the norm kinds"))
        out["H6"][fr] = rec
    summary[cond] = out
    print(f"[analyze_features_ethically] {cond} done", flush=True)


def count(group):
    cs = [c for c in summary if group is None or summary[c]["early"] == group]; rd = [summary[c]["sets"].get("original_vs_neutral_sig", {}).get("A1e_over_A1/moral", {}).get("reading") for c in cs]
    return dict(n=len(cs), either_wording=sum(r == "moral cue in either wording" for r in rd), word=sum(r == "the word 'morally'" for r in rd), inconclusive=sum(r == "inconclusive" for r in rd), conditions=cs)
counts = dict(layer7_or_deeper=count(False), layer0_to_3=count(True), all=count(None),
              H6_more={fr: sum(1 for c in summary if summary[c]["H6"].get(fr, {}).get("more")) for fr in FR},
              H6_conditions={fr: sum(1 for c in summary if "more" in summary[c]["H6"].get(fr, {})) for fr in FR})
json.dump(dict(settings=vars(a), accepted_pairs=PRIMARY_SET, item_file_note=PRIMARY_WHY, n_items=len(ACC), counts=counts, conditions=summary),
          open(os.path.join(a.out, "summary.json"), "w"), indent=1)


f2 = lambda x: "n/a" if x is None else f"{x:.2f}"
L = ["# The located feature sets with \"is ethically\" (frame A1e), next to \"is morally\" (A1) and no cue (B)", "",
     "Exploratory. " + (f"Items: {PRIMARY_WHY}; {len(ACC)} items." if PRIMARY_SET else f"**Not the accepted item set ({PRIMARY_WHY}).**"), "",
     f"Primary (moral-versus-neutral sets, moral pairs, A1e over A1): at layer 7 or deeper {counts['layer7_or_deeper']['either_wording']} of {counts['layer7_or_deeper']['n']} follow a moral cue in either wording, "
     f"{counts['layer7_or_deeper']['word']} follow the word 'morally', {counts['layer7_or_deeper']['inconclusive']} inconclusive; at layer 0 to 3: {counts['layer0_to_3']['either_wording']} / {counts['layer0_to_3']['word']} / {counts['layer0_to_3']['inconclusive']} of {counts['layer0_to_3']['n']}.",
     f"H6 (moral vs norm yields more features than every split of the norm kinds): A1 {counts['H6_more']['A1']} of {counts['H6_conditions']['A1']}, A1e {counts['H6_more']['A1e']} of {counts['H6_conditions']['A1e']}, B {counts['H6_more']['B']} of {counts['H6_conditions']['B']}.", "",
     "| condition | layer | moral: A1e/A1 [95 % CI] reading | norm: A1e/A1 | descr: A1e/A1 | moral: B/A1 | A1e descr/moral [CI] | H6 A1 / A1e / B (moral vs norm; best split) | answer-word mass A1 / A1e / B | capture R2 A1 / A1e |",
     "|---|---|---|---|---|---|---|---|---|---|"]
for cond, o in summary.items():
    s = o["sets"].get("original_vs_neutral_sig")
    if not s: L.append(f"| {cond} | {o['layer']} | no moral-versus-neutral set | | | | | | | |"); continue
    m = s["A1e_over_A1/moral"]; h = lambda fr: (f"{o['H6'][fr]['moral_vs_norm_equalised']:.1f}; {max(o['H6'][fr]['norm_vs_norm_equalised'].values()):.1f}" if "moral_vs_norm_equalised" in o["H6"].get(fr, {}) else "-")
    mass = " / ".join(f2(np.mean([o["behaviour"][fr][c]["mass"] for c in CATS])) for fr in FR if fr in o["behaviour"])
    L.append(f"| {cond} | {'MLP0' if o['site'] == 'mlp_out' else 'L' + str(o['layer'])} | {f2(m['ratio'])} [{f2(m['ci95'][0])}, {f2(m['ci95'][1])}] {m['reading']} | {f2(s['A1e_over_A1/norm']['ratio'])} | {f2(s['A1e_over_A1/descr']['ratio'])} | "
             f"{f2(s['B_over_A1/moral']['ratio'])} | {f2(s['A1e_descr_over_moral']['ratio'])} [{f2(s['A1e_descr_over_moral']['ci95'][0])}, {f2(s['A1e_descr_over_moral']['ci95'][1])}] | {h('A1')} / {h('A1e')} / {h('B')} | {mass} | "
             f"{f2(o['capture']['A1']['mean_R2'])} / {f2(o['capture']['A1e']['mean_R2'])} |")
L += ["", "Moral-versus-norm sets (located; secondary), moral pairs A1e/A1 and the A1e descr/moral ratio:", ""]
for cond, o in summary.items():
    s = o["sets"].get("original_vs_norm_sig")
    if s: L.append(f"* {cond}: moral A1e/A1 {f2(s['A1e_over_A1/moral']['ratio'])} [{f2(s['A1e_over_A1/moral']['ci95'][0])}, {f2(s['A1e_over_A1/moral']['ci95'][1])}] ({s['A1e_over_A1/moral']['reading']}); "
                   f"A1e descr/moral {f2(s['A1e_descr_over_moral']['ratio'])} [{f2(s['A1e_descr_over_moral']['ci95'][0])}, {f2(s['A1e_descr_over_moral']['ci95'][1])}] ({s['A1e_descr_over_moral']['reading']}); "
                   f"A1e norm/moral {f2(s['A1e_norm_over_moral']['ratio'])}")
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
