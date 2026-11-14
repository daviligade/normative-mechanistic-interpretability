"""The removal test on ETHICS scenarios."""
import argparse, glob, json, os, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--runs", default="runs/ethics"); ap.add_argument("--out", default="results/ethics"); ap.add_argument("--readout", default="S")
ap.add_argument("--min-auc", type=float, default=0.60); ap.add_argument("--boot", type=int, default=2000); ap.add_argument("--seed", type=int, default=20261111)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
ORDER = ["Llama-3.2-1B", "Llama-3.2-1B-Instruct", "gemma-2b", "gemma-2b-it", "Llama-3.2-3B", "Llama-3.2-3B-Instruct", "Qwen2.5-3B", "Qwen2.5-3B-Instruct", "Qwen2.5-7B", "Qwen2.5-7B-Instruct",
         "Llama-3.1-8B", "Llama-3.1-8B-Instruct", "Qwen2.5-14B", "Qwen2.5-14B-Instruct"]
FRAME_ORDER = ["EA1", "EB", "EQA", "EA0"]; FRAME_NAME = {"EA1": "priming and cue", "EB": "priming, no cue", "EQA": "question, no cue, no priming", "EA0": "cue alone"}


def auc(s, y):
    order = np.argsort(s, kind="mergesort"); r = np.empty(len(s)); sv = s[order]; i = 0
    while i < len(sv):
        j = i
        while j + 1 < len(sv) and sv[j + 1] == sv[i]: j += 1
        r[order[i:j + 1]] = (i + j) / 2 + 1; i = j + 1
    n0, n1 = int((y == 0).sum()), int((y == 1).sum()); return float((r[y == 0].sum() - n0 * (n0 + 1) / 2) / (n0 * n1))


sep = lambda s, y: float(s[y == 0].mean() - s[y == 1].mean())
rows, COUNTS = [], {}
models = sorted((os.path.basename(p.rstrip("/")) for p in glob.glob(os.path.join(a.runs, "*/"))), key=lambda m: (ORDER.index(m) if m in ORDER else 99, m))
for model in models:
    sp = os.path.join(a.runs, model, "sets.json")
    if not os.path.exists(sp): continue
    for frame in FRAME_ORDER:
        p = os.path.join(a.runs, model, f"{frame}.npz")
        if not os.path.exists(p): continue
        z = np.load(p, allow_pickle=False); meta = json.loads(str(z["__meta__"])); names = meta["set_names"]; modes = meta["modes"]; y = np.array(meta["labels"]); n = len(y)
        if meta.get("n_done") != meta.get("n_items"): print(f"[!] {p}: only {meta.get('n_done')} of {meta.get('n_items')} scenarios; skipped"); continue
        s0 = z[f"base_{a.readout}"].astype(np.float64); A = z[f"abl_{a.readout}"].astype(np.float64); mass = float(z["base_mass"].mean())
        rnd = [i for i, nm in enumerate(names) if nm.startswith("random10_")]; d10 = names.index("located"); imp = names.index("topshare10") if "topshare10" in names else None
        key = (n, int((y == 0).sum()))
        if key not in COUNTS:
            i0, i1 = np.where(y == 0)[0], np.where(y == 1)[0]; COUNTS[key] = np.concatenate([rng.choice(i0, (a.boot, len(i0))), rng.choice(i1, (a.boot, len(i1)))], 1)
        R = COUNTS[key]; yb = y[R[0]]
        clean_sep, clean_auc = sep(s0, y), auc(s0, y)
        for mi, mode in enumerate(modes):
            frac = {nm: 1 - sep(A[:, i, mi], y) / clean_sep for i, nm in enumerate(names)}; r10 = np.array([frac[names[i]] for i in rnd])
            sb = s0[R]; cb = sb[:, yb == 0].mean(1) - sb[:, yb == 1].mean(1)
            fb = lambda i: 1 - ((A[:, i, mi][R])[:, yb == 0].mean(1) - (A[:, i, mi][R])[:, yb == 1].mean(1)) / cb
            fd = fb(d10); fr_ = np.mean([fb(i) for i in rnd], 0) if rnd else None
            row = dict(model=model, frame=frame, mode=mode, n=n, mean_mass=mass, clean_separation=clean_sep, clean_auc=clean_auc, counts=bool(clean_auc >= a.min_auc),
                       removed_located=frac["located"], removed_located_ci=[float(np.percentile(fd, 2.5)), float(np.percentile(fd, 97.5))], auc_after_located=auc(A[:, d10, mi], y),
                       removed_random10_mean=float(r10.mean()) if len(r10) else None, removed_random10_max=float(r10.max()) if len(r10) else None, n_random10=len(rnd),
                       rank_located_among_random10=int((r10 >= frac["located"]).sum()) if len(r10) else None,
                       located_minus_random10_mean=float(frac["located"] - r10.mean()) if len(r10) else None,
                       located_minus_random10_mean_ci=[float(np.percentile(fd - fr_, 2.5)), float(np.percentile(fd - fr_, 97.5))] if rnd else None,
                       removed_topshare10=frac.get("topshare10"), rank_topshare10=int((r10 >= frac["topshare10"]).sum()) if imp is not None and len(r10) else None,
                       auc_after_random10_mean=float(np.mean([auc(A[:, i, mi], y) for i in rnd])) if rnd else None)
            rows.append(row)
if not rows: sys.exit(f"no finished frame under {a.runs}")
summary = []
for frame in FRAME_ORDER:
    for mode in sorted({r["mode"] for r in rows}):
        rr = [r for r in rows if r["frame"] == frame and r["mode"] == mode]; cc = [r for r in rr if r["counts"]]
        if not rr: continue
        med = lambda k: float(np.median([r[k] for r in cc])) if cc else None
        summary.append(dict(frame=frame, mode=mode, models_run=len(rr), models_that_separate=len(cc), models_left_out=[r["model"] for r in rr if not r["counts"]],
                            located_beats_every_random_set=sum(1 for r in cc if r["rank_located_among_random10"] == 0), located_interval_above_random_mean=sum(1 for r in cc if r["located_minus_random10_mean_ci"][0] > 0),
                            median_removed_located=med("removed_located"), median_removed_random10_mean=med("removed_random10_mean"), median_clean_auc=med("clean_auc"), median_auc_after_located=med("auc_after_located"),
                            median_auc_after_random10=med("auc_after_random10_mean")))
json.dump(dict(settings=vars(a), note="exploratory", summary=summary), open(os.path.join(a.out, "summary.json"), "w"), indent=1)
json.dump(rows, open(os.path.join(a.out, "rows.json"), "w"), indent=1)
f3 = lambda v, f="{:.3f}": "n/a" if v is None else f.format(v)
L = ["# Removal of the located heads on ETHICS scenarios", "",
     f"Readout {a.readout}; a model and frame counts where the clean AUC is at least {a.min_auc}; {a.boot} resamples of the scenarios within their class.", "",
     "## Per frame", "", "| frame | mode | models that separate the classes | located heads remove more than every random set | interval of (located - random mean) above 0 | median removed: located heads | median removed: random sets | median AUC: clean / without located heads / without a random set | left out |", "|---|---|---|---|---|---|---|---|---|"]
for s in summary:
    L.append(f"| {s['frame']} ({FRAME_NAME[s['frame']]}) | {s['mode']} | {s['models_that_separate']} of {s['models_run']} | {s['located_beats_every_random_set']} of {s['models_that_separate']} | {s['located_interval_above_random_mean']} of {s['models_that_separate']} | "
             f"{f3(s['median_removed_located'])} | {f3(s['median_removed_random10_mean'])} | {f3(s['median_clean_auc'])} / {f3(s['median_auc_after_located'])} / {f3(s['median_auc_after_random10'])} | {', '.join(s['models_left_out']) or '-'} |")
L += ["", "## Per model", "", "| model | frame | mode | mass | clean separation | clean AUC | removed by the located heads (95 % interval) | rank among random sets | random sets: mean / largest | located - random mean (95 % interval) | topshare10 (rank) | AUC without located heads |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['model']}{'' if r['counts'] else ' *'} | {r['frame']} | {r['mode']} | {r['mean_mass']:.2f} | {r['clean_separation']:+.3f} | {r['clean_auc']:.3f} | {r['removed_located']:.3f} [{r['removed_located_ci'][0]:.3f}, {r['removed_located_ci'][1]:.3f}] | "
             f"{r['rank_located_among_random10']} of {r['n_random10']} | {f3(r['removed_random10_mean'])} / {f3(r['removed_random10_max'])} | {f3(r['located_minus_random10_mean'], '{:+.3f}')} "
             f"[{f3(r['located_minus_random10_mean_ci'][0], '{:+.3f}')}, {f3(r['located_minus_random10_mean_ci'][1], '{:+.3f}')}] | {f3(r['removed_topshare10'])} ({r['rank_topshare10']}) | {r['auc_after_located']:.3f} |")
L += ["", f"\\* clean AUC below {a.min_auc}: shown, not counted (the share removed is not meaningful where the classes are not separated)."]
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L[:8 + len(summary)]))
