"""The removal test in the further frames, with a chosen score."""
import argparse, csv, glob, json, os, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--runs", required=True, help="folder that holds ablation/<model>/<frame>__<id>.npz"); ap.add_argument("--items", default="stimuli/items_final.json"); ap.add_argument("--out", required=True)
ap.add_argument("--frames", nargs="+", default=None); ap.add_argument("--models", nargs="+", default=None); ap.add_argument("--mode", default="all", choices=["all", "final"])
ap.add_argument("--readout", default="LD", choices=["S", "LD"]); ap.add_argument("--include-on", default="LD", choices=["S", "LD"]); ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--tau-ld", type=float, default=0.1)
ap.add_argument("--min-items", type=int, default=30); ap.add_argument("--min-items-descr", type=int, default=20); ap.add_argument("--boot", type=int, default=2000); ap.add_argument("--seed", type=int, default=20261006)
ap.add_argument("--check", default=None, help="folder with necessity.csv of analyze_circuits.py")
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
ITEMS = [i for i in json.load(open(a.items)) if i.get("accepted", True)]; IDX = {it["id"]: k for k, it in enumerate(ITEMS)}; N = len(ITEMS); CAT = np.array([it["category"] for it in ITEMS])
GROUP = {g: CAT == g for g in ("moral", "norm", "descr")}; GROUP = {g: m for g, m in GROUP.items() if m.any()}
MINN = {"moral": a.min_items, "norm": a.min_items, "descr": a.min_items_descr}; TAU = a.tau if a.include_on == "S" else a.tau_ld
COUNTS = {g: rng.multinomial(int(mk.sum()), np.ones(int(mk.sum())) / int(mk.sum()), size=a.boot) for g, mk in GROUP.items()}
ORDER = ["Llama-3.2-1B", "Llama-3.2-1B-Instruct", "gemma-2b", "gemma-2b-it", "Llama-3.2-3B", "Llama-3.2-3B-Instruct", "Qwen2.5-3B", "Qwen2.5-3B-Instruct", "Qwen2.5-7B", "Qwen2.5-7B-Instruct",
         "Llama-3.1-8B", "Llama-3.1-8B-Instruct", "Qwen2.5-14B", "Qwen2.5-14B-Instruct"]
rows = []
folders = sorted(glob.glob(os.path.join(a.runs, "ablation", "*/")), key=lambda p: (ORDER.index(os.path.basename(p.rstrip("/"))) if os.path.basename(p.rstrip("/")) in ORDER else 99, p))
for folder in folders:
    model = os.path.basename(folder.rstrip("/")); sp = os.path.join(folder, "sets.json")
    if not os.path.exists(sp) or (a.models and model not in a.models): continue
    names = json.load(open(sp))["names"]; d10 = names.index("located"); rnd = [i for i, n in enumerate(names) if n.startswith("random10_")]; per = {}
    for f in sorted(glob.glob(os.path.join(folder, "*__*.npz"))):
        b = os.path.basename(f)
        if b.endswith(".tmp.npz") or b.startswith("means__"): continue
        frame, iid = b[:-4].split("__", 1)
        if iid in IDX and (not a.frames or frame in a.frames): per.setdefault(frame, []).append((iid, f))
    for frame, files in sorted(per.items()):
        g_inc = np.full(N, np.nan); g_clean = np.full(N, np.nan); g_abl = np.full((N, len(names)), np.nan); mi = None
        for iid, f in files:
            z = np.load(f, allow_pickle=False); k = IDX[iid]
            if mi is None:
                modes = json.loads(str(z["__meta__"]))["modes"]
                if a.mode not in modes: sys.exit(f"{f}: mode {a.mode} was not run (modes: {modes})")
                mi = modes.index(a.mode)
            g_inc[k] = float(z[f"perm_base_{a.include_on}"]) - float(z[f"rest_base_{a.include_on}"]); g_clean[k] = float(z[f"perm_base_{a.readout}"]) - float(z[f"rest_base_{a.readout}"])
            g_abl[k] = np.asarray(z[f"perm_{a.readout}"], dtype=np.float64)[:, mi] - np.asarray(z[f"rest_{a.readout}"], dtype=np.float64)[:, mi]
        have = ~np.isnan(g_inc); ok = have & (np.nan_to_num(g_inc, nan=-np.inf) >= TAU)
        for g, mk in GROUP.items():
            w = (ok & mk)[mk].astype(float); n_inc = int(w.sum())
            if n_inc == 0: continue
            y = np.nan_to_num(g_clean[mk]) * w; fr_all = np.array([float((np.nan_to_num(g_clean[mk] - g_abl[mk, s]) * w).sum() / y.sum()) for s in range(len(names))]); r10 = fr_all[rnd]
            x = np.nan_to_num(g_clean[mk] - g_abl[mk, d10]) * w
            with np.errstate(divide="ignore", invalid="ignore"): b = (COUNTS[g] @ x) / (COUNTS[g] @ y)
            b = b[np.isfinite(b)]
            rows.append(dict(model=model, frame=frame, group=g, mode=a.mode, n_run=int((have & mk).sum()), n_included=n_inc, below_minimum=int(n_inc < MINN[g]), mean_clean_gap=float(y.sum() / n_inc), removed_located=float(fr_all[d10]),
                             ci_lo=float(np.percentile(b, 2.5)), ci_hi=float(np.percentile(b, 97.5)), rank_located_among_random10=int((r10[np.isfinite(r10)] >= fr_all[d10]).sum()), n_random10=len(rnd),
                             random10_mean=float(np.nanmean(r10)), random10_max=float(np.nanmax(r10))))
if not rows: sys.exit(f"no removal file under {a.runs}/ablation for these frames")
check = None
if a.check:
    if (a.readout, a.include_on) != ("S", "S") or abs(a.tau - 0.02) > 1e-12: sys.exit("[check] necessity.csv is on the score S with inclusion at 0.02: use --readout S --include-on S")
    ref = {(r["model"], r["frame"], r["group"], r["mode"]): r for r in csv.DictReader(open(os.path.join(a.check, "necessity.csv")))}; worst = dict(removed=0.0, random_mean=0.0, interval=0.0, rank=0); n = 0
    for r in rows:
        q = ref.get((r["model"], r["frame"], r["group"], r["mode"]))
        if q is None: continue
        n += 1; worst["removed"] = max(worst["removed"], abs(float(q["frac_located"]) - r["removed_located"])); worst["random_mean"] = max(worst["random_mean"], abs(float(q["random10_mean"]) - r["random10_mean"]))
        worst["interval"] = max(worst["interval"], abs(float(q["ci_lo"]) - r["ci_lo"]), abs(float(q["ci_hi"]) - r["ci_hi"])); worst["rank"] = max(worst["rank"], abs(int(q["rank_located_among_random10"]) - r["rank_located_among_random10"]))
        assert int(q["n_included"]) == r["n_included"], (r["model"], r["frame"], r["group"], q["n_included"], r["n_included"])
    okc = n > 0 and worst["removed"] < 1e-5 and worst["random_mean"] < 1e-5 and worst["rank"] == 0 and worst["interval"] < 0.02
    check = dict(reference=a.check, rows_compared=n, largest_difference=worst, same=bool(okc)); print(f"[check] against {a.check}/necessity.csv: {n} rows compared; largest differences {worst} -> {'the same' if okc else 'DIFFERENT'}", flush=True)
    if not okc: sys.exit("[check] the removal numbers do not come out as in the reference: nothing written")
summary = []
for frame in sorted({r["frame"] for r in rows}):
    for g in GROUP:
        rr = [r for r in rows if r["frame"] == frame and r["group"] == g]; cc = [r for r in rr if not r["below_minimum"]]
        if rr: summary.append(dict(frame=frame, group=g, models_run=len(rr), models_with_enough_pairs=len(cc), models_left_out=[r["model"] for r in rr if r["below_minimum"]],
                                   median_included=float(np.median([r["n_included"] for r in rr])), located_heads_above_every_random_set=sum(1 for r in cc if r["rank_located_among_random10"] == 0),
                                   median_removed_located=float(np.median([r["removed_located"] for r in cc])) if cc else None, median_random10_mean=float(np.median([r["random10_mean"] for r in cc])) if cc else None))
json.dump(dict(settings=vars(a), note="exploratory", summary=summary, check=check), open(os.path.join(a.out, "summary.json"), "w"), indent=1); json.dump(rows, open(os.path.join(a.out, "rows.json"), "w"), indent=1)
f3 = lambda v: "n/a" if v is None else f"{v:.3f}"
L = [f"# Removal of the located heads, read on {a.readout}", "", f"Runs: {a.runs}/ablation; positions: {a.mode}; a pair is included when its gap in {a.include_on} is at least {TAU}; {a.boot} resamples of the pairs.", "",
     (f"Check against {a.check}/necessity.csv: the same ({check['rows_compared']} rows)." if check else "No check against the study's output was asked for (--check; possible with --readout S --include-on S)."), "",
     "## Per frame and kind of pair", "", "| frame | pairs | models with enough pairs | median pairs included | located heads above every random set | median removed: located heads | median removed: random sets | left out |", "|---|---|---|---|---|---|---|---|"]
for s in summary: L.append(f"| {s['frame']} | {s['group']} | {s['models_with_enough_pairs']} of {s['models_run']} | {s['median_included']:.0f} | {s['located_heads_above_every_random_set']} of {s['models_with_enough_pairs']} | {f3(s['median_removed_located'])} | {f3(s['median_random10_mean'])} | {', '.join(s['models_left_out']) or '-'} |")
L += ["", "## Per model", "", "| model | frame | pairs | included | mean clean gap | removed by the located heads (95 % interval) | rank among random sets | random sets: mean / largest |", "|---|---|---|---|---|---|---|---|"]
for r in rows: L.append(f"| {r['model']} | {r['frame']} | {r['group']} | {r['n_included']} of {r['n_run']}{'*' if r['below_minimum'] else ''} | {r['mean_clean_gap']:+.3f} | {r['removed_located']:.3f} [{r['ci_lo']:.3f}, {r['ci_hi']:.3f}] | {r['rank_located_among_random10']} of {r['n_random10']} | {r['random10_mean']:.3f} / {r['random10_max']:.3f} |")
L += ["", "\\* fewer included pairs than the minimum; shown, not counted."]
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L[:10 + len(summary)]))
