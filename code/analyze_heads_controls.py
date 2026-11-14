"""The located heads on the descriptive pairs about a person."""
import argparse, json, os, sys, glob, hashlib
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--study-runs", default="runs/heads"); ap.add_argument("--study-items", default="stimuli/items_final.json")
ap.add_argument("--new-runs", nargs="+", default=["runs/heads_followup_person"], help="further run folders (the control pairs; with --no-controls, other frames of the study's pairs)"); ap.add_argument("--new-items", default="stimuli/items_followup_person.json")
ap.add_argument("--new-run-file", default="stimuli/items_followup_person_run.json", help="the file the models were run on: the pairs of --new-items must be the same pairs")
ap.add_argument("--no-controls", action="store_true", help="the study's three groups only (no control pairs): the level of the share and the study's contrasts in other frames, e.g. --study-runs runs/heads_qa --frames QA")
ap.add_argument("--located", default="located/heads.json"); ap.add_argument("--out", default="results/heads_person")
ap.add_argument("--check", default=None, help="folder with per_model.json and summary.json of analyze_heads.py (results/heads)")
ap.add_argument("--frames", nargs="+", default=["A1", "B", "A0"]); ap.add_argument("--subset", default="accepted", choices=["accepted", "all"], help="control pairs: those the screen accepted, or every candidate")
ap.add_argument("--headset", default="located"); ap.add_argument("--condition", default="p2r_all"); ap.add_argument("--readout", default="S")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--min-items", type=int, default=30); ap.add_argument("--min-items-descr", type=int, default=20); ap.add_argument("--min-items-kind", type=int, default=10)
ap.add_argument("--include-on", default="S", choices=["S", "LD"], help="what decides whether a pair is included: the score S with --tau (the study's rule), or the log-odds LD between the positive and the negative answer "
                "words with --tau-ld, for frames in which the answer words get little probability")
ap.add_argument("--tau-ld", type=float, default=0.1); ap.add_argument("--kind", default=None, choices=["prudential", "etiquette", "aesthetic", "epistemic"],
                help="adds two groups (the normative pairs of this kind that the raters confirmed, and the other normative pairs) with the contrasts moral/kind and kind/othernorm")
ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--models", nargs="+", default=None, help="only these model folders (for tests)")
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)

STUDY = [i for i in json.load(open(a.study_items)) if i.get("accepted", True)]
NEW_ALL = [] if a.no_controls else json.load(open(a.new_items)); NEW = [i for i in NEW_ALL if (bool(i.get("accepted", True)) if a.subset == "accepted" else True)]
screened = sorted({s for i in NEW_ALL for s in i.get("accepted_by", [])})
if a.subset == "accepted" and not screened and not a.no_controls: sys.exit(f"{a.new_items} carries no screen (accepted_by is empty): this is a run file, not an acceptance file. Run the screen first, or use --subset all.")
if NEW_ALL and os.path.exists(a.new_run_file):
    RUNF = {i["id"]: (i["perm_stem"], i["rest_stem"]) for i in json.load(open(a.new_run_file))}
    bad = [i["id"] for i in NEW_ALL if RUNF.get(i["id"]) != (i["perm_stem"], i["rest_stem"])]
    if bad: sys.exit(f"{a.new_items} and {a.new_run_file} differ on {bad[:5]}: the models were run on other pairs")
ITEMS = STUDY + NEW; N = len(ITEMS); IDX = {it["id"]: k for k, it in enumerate(ITEMS)}; assert len(IDX) == N, "an id occurs twice"
GNAME = [{"moral": "moral", "norm": "norm", "descr": "thing"}[it["category"]] for it in STUDY] + ["person"] * len(NEW)
GROUPS = ("moral", "norm", "thing", "person"); GROUP = {g: np.array([x == g for x in GNAME]) for g in GROUPS}
MINN = {"moral": a.min_items, "norm": a.min_items, "thing": a.min_items_descr, "person": a.min_items_descr}; EXTRA_C = []
if a.kind:
    GROUP[a.kind] = np.array([g == "norm" and it.get("subtype") == a.kind and bool(it.get("kind_ok", True)) for g, it in zip(GNAME, ITEMS)])
    GROUP["othernorm"] = np.array([g == "norm" and it.get("subtype") != a.kind for g, it in zip(GNAME, ITEMS)])
    GROUPS = GROUPS + (a.kind, "othernorm"); MINN[a.kind] = a.min_items_kind; MINN["othernorm"] = a.min_items; EXTRA_C = [("moral", a.kind), (a.kind, "othernorm"), ("moral", "othernorm")]
GROUP = {g: m for g, m in GROUP.items() if m.any()}; MAIN = [g for g in ("moral", "norm", "thing", "person") if g in GROUP]; TAU = a.tau if a.include_on == "S" else a.tau_ld
CONTRASTS = [c for c in [("norm", "person"), ("moral", "person"), ("person", "thing"), ("norm", "thing"), ("moral", "thing"), ("moral", "norm")] + EXTRA_C if c[0] in GROUP and c[1] in GROUP]
TT = np.array([it.get("template_type", "NA") for it in ITEMS]); LOCATED = json.load(open(a.located))


def boot_counts(n, B):
    idx = rng.integers(0, n, size=(B, n)); c = np.zeros((B, n), dtype=np.float32)
    for b in range(B): c[b] = np.bincount(idx[b], minlength=n)
    return c


COUNTS = {g: boot_counts(int(GROUP[g].sum()), a.boot) for g in GROUPS if g in GROUP}


def load_model(model):
    fz = LOCATED[model]; out = {}; key = f"{a.condition}__{a.readout}"
    for folder in [os.path.join(a.study_runs, model)] + [os.path.join(r, model) for r in a.new_runs]:
        for f in sorted(glob.glob(os.path.join(folder, "*__*.npz"))):
            if f.endswith(".tmp.npz"): continue
            frame, iid = os.path.basename(f)[:-4].split("__", 1)
            if iid not in IDX or frame not in a.frames: continue
            try: z = np.load(f, allow_pickle=False)
            except Exception as e: raise SystemExit(f"unreadable result file {f} ({type(e).__name__}): move it away and resume run_heads.py")
            if key not in z.files: continue
            meta = json.loads(str(z["__meta__"])); arr = z[key]
            assert arr.shape == (fz["n_layers"], fz["n_heads"]), f"{f}: array shape {arr.shape} does not match the head table of {model}"
            assert meta["n_tok_perm"] == meta["n_tok_rest"], f"{f}: prompts of unequal token count"
            d = out.setdefault(frame, dict(E=np.full((N, arr.size), np.nan, dtype=np.float32), gap=np.full(N, np.nan), mass=np.full(N, np.nan)))
            d["E"][IDX[iid]] = np.abs(arr).ravel(); d["gap"][IDX[iid]] = meta["base_perm"][a.include_on] - meta["base_rest"][a.include_on]
            d["mass"][IDX[iid]] = (meta["base_perm"]["mass"] + meta["base_rest"]["mass"]) / 2
    return out


def head_index(model):
    fz = LOCATED[model]; H = fz["n_heads"]; return np.array([l * H + h for l, h in fz[a.headset]])


def log_ratio_boot(sh, ok, c1, c2):
    m1, m2 = GROUP[c1], GROUP[c2]; w1, w2 = ok[m1].astype(np.float32), ok[m2].astype(np.float32); s1, s2 = np.nan_to_num(sh[m1]), np.nan_to_num(sh[m2])
    with np.errstate(divide="ignore", invalid="ignore"):
        n1b, n2b = COUNTS[c1] @ w1, COUNTS[c2] @ w2
        b = np.log(((COUNTS[c1] @ (s1 * w1)) / np.where(n1b > 0, n1b, np.nan)) / ((COUNTS[c2] @ (s2 * w2)) / np.where(n2b > 0, n2b, np.nan)))
    b[~np.isfinite(b)] = np.nan; return b


def stratified(sh, ok, c1, c2):
    m1, m2 = GROUP[c1], GROUP[c2]; num = den = 0.0; nb = np.zeros(a.boot); db = np.zeros(a.boot); used = []
    for t in sorted(set(TT[m1 & ok]) & set(TT[m2 & ok])):
        k1, k2 = (TT[m1] == t) & ok[m1], (TT[m2] == t) & ok[m2]; w = float(min(k1.sum(), k2.sum())); x1, x2 = np.nan_to_num(sh[m1]) * k1, np.nan_to_num(sh[m2]) * k2
        num += w * x1.sum() / k1.sum(); den += w * x2.sum() / k2.sum(); used.append(f"{t} {int(k1.sum())}/{int(k2.sum())}")
        with np.errstate(divide="ignore", invalid="ignore"):
            n1, n2 = COUNTS[c1] @ k1.astype(np.float32), COUNTS[c2] @ k2.astype(np.float32); valid = (n1 > 0) & (n2 > 0)
            nb += np.where(valid, w * (COUNTS[c1] @ x1.astype(np.float32)) / np.where(n1 > 0, n1, 1), 0.0); db += np.where(valid, w * (COUNTS[c2] @ x2.astype(np.float32)) / np.where(n2 > 0, n2, 1), 0.0)
    if not used or den == 0: return None, None, used
    with np.errstate(divide="ignore", invalid="ignore"): b = np.log(nb / db)
    b[~np.isfinite(b)] = np.nan; return float(num / den), b, used


ci = lambda b: [float(np.exp(np.nanpercentile(b, 2.5))), float(np.exp(np.nanpercentile(b, 97.5)))]
models = sorted(m for m in os.listdir(a.study_runs) if os.path.isdir(os.path.join(a.study_runs, m)) and m in LOCATED and (a.models is None or m in a.models))
if not models: sys.exit(f"no model folder under {a.study_runs}")
behav, per_model, pooled, strat_rows, mult = [], [], [], [], []; SH, OK = {}, {}
for m in models:
    D = load_model(m); hidx = head_index(m)
    for fr in a.frames:
        if fr not in D: continue
        d = D[fr]; have = ~np.isnan(d["gap"]); tot = np.nansum(d["E"], 1); ok = have & (d["gap"] >= TAU) & (tot > 0)
        SH[(m, fr)] = np.where(ok, np.nansum(d["E"][:, hidx], 1) / np.where(tot > 0, tot, 1), np.nan); OK[(m, fr)] = ok; uni = len(hidx) / d["E"].shape[1]
        for g, mk in GROUP.items():
            if not (have & mk).any(): continue
            behav.append(dict(model=m, frame=fr, group=g, n_run=int((have & mk).sum()), n_included=int((ok & mk).sum()), mean_gap=float(np.nanmean(d["gap"][mk])),
                              share_correct_sign=float(np.mean(d["gap"][have & mk] > 0)), mean_mass=float(np.nanmean(d["mass"][mk])),
                              mean_share=float(SH[(m, fr)][mk & ok].mean()) if (ok & mk).any() else None, uniform_share=float(uni),
                              multiple_of_random=float(SH[(m, fr)][mk & ok].mean() / uni) if (ok & mk).any() else None, enough=bool((ok & mk).sum() >= MINN[g])))
    del D
frames = [fr for fr in a.frames if any((m, fr) in SH for m in models)]
for fr in frames:
    for c1, c2 in CONTRASTS:
        logs, slogs, used, left = [], [], [], []
        for m in models:
            if (m, fr) not in SH: continue
            sh, ok = SH[(m, fr)], OK[(m, fr)]; x, y = sh[GROUP[c1] & ok], sh[GROUP[c2] & ok]
            short = [g for g in ("moral", "norm") if g in GROUP and (GROUP[g] & ok).sum() < MINN[g]] + [g for g in (c1, c2) if g not in ("moral", "norm") and (GROUP[g] & ok).sum() < MINN[g]]
            if short: per_model.append(dict(model=m, frame=fr, contrast=f"{c1}/{c2}", n1=len(x), n2=len(y), note="too few included pairs: " + ", ".join(sorted(set(short))))); left.append(m); continue
            b = log_ratio_boot(sh, ok, c1, c2); row = dict(model=m, frame=fr, contrast=f"{c1}/{c2}", n1=len(x), n2=len(y), mean_share_1=float(x.mean()), mean_share_2=float(y.mean()), ratio=float(x.mean() / y.mean()), ci95=ci(b))
            if "person" in (c1, c2) and "thing" not in (c1, c2):
                est, sb, st = stratified(sh, ok, c1, c2)
                if est is not None: row["ratio_within_template_types"] = est; row["template_types"] = st; slogs.append((np.log(est), sb))
            per_model.append(row); logs.append(b); used.append(m)
        if not logs: continue
        est = float(np.mean([np.log(r["ratio"]) for r in per_model if r["frame"] == fr and r["contrast"] == f"{c1}/{c2}" and "ratio" in r]))
        p = dict(frame=fr, contrast=f"{c1}/{c2}", n_models=len(used), models_used=used, models_left_out=left, pooled_ratio=float(np.exp(est)), ci95=ci(np.nanmean(logs, 0)),
                 models_with_interval_above_1=int(sum(1 for r in per_model if r["frame"] == fr and r["contrast"] == f"{c1}/{c2}" and "ratio" in r and r["ci95"][0] > 1)),
                 models_with_interval_below_1=int(sum(1 for r in per_model if r["frame"] == fr and r["contrast"] == f"{c1}/{c2}" and "ratio" in r and r["ci95"][1] < 1)))
        if slogs and len(slogs) == len(logs): p["pooled_ratio_within_template_types"] = float(np.exp(np.mean([s[0] for s in slogs]))); p["ci95_within_template_types"] = ci(np.nanmean([s[1] for s in slogs], 0))
        pooled.append(p)

    full = [m for m in models if (m, fr) in SH and all((GROUP[g] & OK[(m, fr)]).sum() >= MINN[g] for g in MAIN)]
    study3 = [m for m in models if (m, fr) in SH and all((GROUP[g] & OK[(m, fr)]).sum() >= MINN[g] for g in MAIN if g != "person")]
    for label, ms, gs in (("all groups", full, MAIN), ("study groups", study3, [g for g in MAIN if g != "person"])):
        if label == "study groups" and "person" not in GROUP: continue
        if ms: mult.append(dict(frame=fr, models=label, n_models=len(ms), models_used=ms, **{g: float(np.exp(np.mean([np.log(next(b["multiple_of_random"] for b in behav if b["model"] == m and b["frame"] == fr and b["group"] == g)) for m in ms]))) for g in gs}))


def reading(fr):
    P = {p["contrast"]: p for p in pooled if p["frame"] == fr}
    if "norm/person" not in P or "person/thing" not in P: return "not available (a group is missing or has too few included pairs)"
    side = lambda c: "above 1" if P[c]["ci95"][0] > 1 else ("below 1" if P[c]["ci95"][1] < 1 else "includes 1")
    s1, s2 = side("norm/person"), side("person/thing")
    txt = {("above 1", "includes 1"): "the fifth comes with the standard: the located heads carry more when conduct is judged than when something good or bad happens to a person",
           ("includes 1", "above 1"): "the fifth comes from the form of the phrase, not from the standard: on the control pairs the located heads carry what they carry on normative pairs",
           ("above 1", "above 1"): "both contribute: the control pairs lie between the normative pairs and the descriptive pairs about a thing",
           ("includes 1", "includes 1"): "the control pairs do not decide (both intervals include 1)"}.get((s1, s2), "outside the four cases laid down; the two intervals are reported as they are")
    return f"norm/person {P['norm/person']['pooled_ratio']:.2f} [{P['norm/person']['ci95'][0]:.2f}, {P['norm/person']['ci95'][1]:.2f}] ({s1}); person/thing {P['person/thing']['pooled_ratio']:.2f} [{P['person/thing']['ci95'][0]:.2f}, {P['person/thing']['ci95'][1]:.2f}] ({s2}): {txt}"


check = None
if a.check:
    _rs = json.load(open(os.path.join(a.check, "summary.json")))["settings"]
    if a.include_on != "S" or _rs["readout"] != a.readout or abs(_rs["tau"] - a.tau) > 1e-12 or _rs["condition"] != a.condition:
        sys.exit(f"[check] {a.check} was made with readout {_rs['readout']}, inclusion on S at {_rs['tau']}, condition {_rs['condition']}: it cannot be compared with these options")
    ref_pm = json.load(open(os.path.join(a.check, "per_model.json"))); ref_sum = json.load(open(os.path.join(a.check, "summary.json"))); mine = {"moral/norm": "moral/norm", "moral/thing": "moral/descr", "norm/thing": "norm/descr"}
    worst = dict(per_model_ratio=0.0, per_model_ci=0.0, pooled_ratio=0.0, pooled_ci=0.0); n_cmp = 0; missing = []
    for r in per_model:
        if r["contrast"] not in mine or "ratio" not in r: continue
        ref = [x for x in ref_pm if x["model"] == r["model"] and x["frame"] == r["frame"] and x["headset"] == a.headset and x["contrast"] == mine[r["contrast"]] and "ratio" in x]
        if not ref: missing.append((r["model"], r["frame"], r["contrast"])); continue
        n_cmp += 1; worst["per_model_ratio"] = max(worst["per_model_ratio"], abs(ref[0]["ratio"] - r["ratio"]))
        if a.boot == ref_sum["settings"]["boot"] and a.seed == ref_sum["settings"]["seed"]: worst["per_model_ci"] = max(worst["per_model_ci"], max(abs(u - v) for u, v in zip(ref[0]["ci95"], r["ci95"])))
    n_pool = 0
    if a.models is None:
        for p in pooled:
            if p["contrast"] not in mine: continue
            ref = [x for x in ref_sum["pooled"] if x["frame"] == p["frame"] and x["headset"] == a.headset and x["contrast"] == mine[p["contrast"]]]
            if not ref: missing.append(("pooled", p["frame"], p["contrast"])); continue
            n_pool += 1; worst["pooled_ratio"] = max(worst["pooled_ratio"], abs(ref[0]["pooled_ratio"] - p["pooled_ratio"]))
            if abs(ref[0]["interval_level"] - 0.95) < 1e-9 and a.boot == ref_sum["settings"]["boot"] and a.seed == ref_sum["settings"]["seed"]: worst["pooled_ci"] = max(worst["pooled_ci"], max(abs(u - v) for u, v in zip(ref[0]["interval"], p["ci95"])))

    okc = n_cmp > 0 and worst["per_model_ratio"] < 1e-5 and worst["pooled_ratio"] < 1e-5 and worst["per_model_ci"] < 0.02 and worst["pooled_ci"] < 0.02
    check = dict(reference=a.check, per_model_rows_compared=n_cmp, pooled_rows_compared=n_pool, largest_difference=worst, not_in_reference=missing, same=bool(okc))
    print(f"[check] against {a.check}: {n_cmp} per-model and {n_pool} pooled ratios of the study recomputed; largest differences {worst} -> {'the same' if okc else 'DIFFERENT'}", flush=True)
    if not okc: json.dump(check, open(os.path.join(a.out, "check_failed.json"), "w"), indent=1); sys.exit("[check] the study's contrasts do not come out as in the reference: nothing written")

summary = dict(settings=vars(a), note="exploratory", n_pairs={g: int(mk.sum()) for g, mk in GROUP.items()},
               control_pairs=dict(candidates=len(NEW_ALL), accepted_by_screen=int(sum(bool(i.get("accepted", True)) for i in NEW_ALL)), screen=screened, used=len(NEW), subset=a.subset,
                                  acceptance_file_sha256=None if a.no_controls else hashlib.sha256(open(a.new_items, "rb").read()).hexdigest()),
               models=models, frames=frames, pooled=pooled, multiple_of_random=mult, reading={fr: reading(fr) for fr in frames}, check=check)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); json.dump(per_model, open(os.path.join(a.out, "per_model.json"), "w"), indent=1); json.dump(behav, open(os.path.join(a.out, "behaviour.json"), "w"), indent=1)
f2 = lambda v: "n/a" if v is None else f"{v:.2f}"
L = ["# The located heads on the control pairs about a person" if not a.no_controls else f"# The located heads' share by kind of pair, frames {', '.join(frames)}", "",
     f"Pairs: {', '.join(f'{g} {int(mk.sum())}' for g, mk in GROUP.items())}. " + ("No control pairs in this run (--no-controls)" if a.no_controls else f"Control pairs: {len(NEW_ALL)} candidates" + (f", {summary['control_pairs']['accepted_by_screen']} accepted by the screen ({', '.join(screened)})" if screened else ", no screen in this file") +
     f"; used here: {len(NEW)} ({a.subset})") + f". Runs: {', '.join([a.study_runs] + ([] if (a.no_controls and a.new_runs == ['runs/heads_followup_person']) else a.new_runs))}. Head set {a.headset}, condition {a.condition}, effects read on {a.readout}, a pair is included when its gap in {a.include_on} is at least {TAU}, {a.boot} bootstrap resamples.", "",
     (f"Check against {a.check}: the study's contrasts recomputed here are the same ({check['per_model_rows_compared']} per-model and {check['pooled_rows_compared']} pooled ratios; largest difference {max(check['largest_difference'].values()):.1e})." if check else "No check against the study's output was asked for (--check)."), "",
     ] + ([] if a.no_controls else ["## Reading", ""] + [f"- Frame {fr}: {summary['reading'][fr]}" for fr in frames] + [""]) + [
     "## Pooled ratios of the located heads' share (geometric mean over models; 95 % interval from the item bootstrap)", "", "| frame | contrast | models | ratio | 95 % interval | within template types | models with interval above 1 / below 1 | left out |", "|---|---|---|---|---|---|---|---|"]
for p in pooled:
    w = f"{p['pooled_ratio_within_template_types']:.2f} [{p['ci95_within_template_types'][0]:.2f}, {p['ci95_within_template_types'][1]:.2f}]" if "pooled_ratio_within_template_types" in p else ""
    L.append(f"| {p['frame']} | {p['contrast']} | {p['n_models']} | {p['pooled_ratio']:.2f} | [{p['ci95'][0]:.2f}, {p['ci95'][1]:.2f}] | {w} | {p['models_with_interval_above_1']} / {p['models_with_interval_below_1']} | {', '.join(p['models_left_out']) or '-'} |")
L += ["", "## The share as a multiple of the share of ten heads chosen at random (geometric mean over models)", "", "| frame | models | moral | norm | person | thing |", "|---|---|---|---|---|---|"]
for r in mult: L.append(f"| {r['frame']} | {r['n_models']} ({r['models']}) | {f2(r.get('moral'))} | {f2(r.get('norm'))} | {f2(r.get('person'))} | {f2(r.get('thing'))} |")
for c in ["norm/person", "person/thing", "moral/person"] + [f"{x}/{y}" for x, y in EXTRA_C]:
    rr = [r for r in per_model if r["contrast"] == c]
    if not rr: continue
    L += ["", f"## Per model, {c}", "", "| model | frame | n | n | share | share | ratio | 95 % interval | within template types |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rr: L.append(f"| {r['model']} | {r['frame']} | {r['n1']} | {r['n2']} | " + (f"{r['mean_share_1']:.3f} | {r['mean_share_2']:.3f} | {r['ratio']:.2f} | [{r['ci95'][0]:.2f}, {r['ci95'][1]:.2f}] | {f2(r.get('ratio_within_template_types'))} |" if "ratio" in r else f"{r['note']} | | | | |"))
L += ["", "## Behaviour", "", "| model | frame | group | run | included | mean gap | better version preferred | mean mass | multiple of random |", "|---|---|---|---|---|---|---|---|---|"]
for b in behav: L.append(f"| {b['model']} | {b['frame']} | {b['group']} | {b['n_run']} | {b['n_included']}{'' if b['enough'] else '*'} | {b['mean_gap']:+.3f} | {b['share_correct_sign']:.2f} | {b['mean_mass']:.2f} | {f2(b['multiple_of_random'])} |")
L += ["", "\\* fewer included pairs than the minimum; shown, not pooled."]
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L[:14 + 2 * len(frames) + len(pooled) + len(mult)]))
