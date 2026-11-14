"""Removal, roles, layer profiles and edges of the located heads."""
import argparse, json, os, sys, glob, collections, warnings
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); from common import primary_item_set, check_analysis_items
warnings.filterwarnings("ignore", message="Mean of empty slice"); warnings.filterwarnings("ignore", message="invalid value encountered")

ap = argparse.ArgumentParser()
ap.add_argument("--runs", default="runs/circuits"); ap.add_argument("--heads-runs", default="runs/heads", help="the head-patching runs, for the node-score check (optional)")
ap.add_argument("--items", default="stimuli/items_final.json"); ap.add_argument("--located", default="located/heads.json"); ap.add_argument("--out", default="results/circuits")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--subset", default="accepted", choices=["accepted", "strict", "all"])
ap.add_argument("--min-items", type=int, default=30); ap.add_argument("--min-items-descr", type=int, default=20); ap.add_argument("--min-items-kind", type=int, default=10)
ap.add_argument("--boot", type=int, default=2000); ap.add_argument("--seed", type=int, default=20261006); ap.add_argument("--top", type=int, default=10)
ap.add_argument("--stages", nargs="+", default=["ablation", "roles", "layers", "edges"], choices=["ablation", "roles", "layers", "edges"])
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
PRIMARY_SET, PRIMARY_WHY = primary_item_set(a.items)
ITEMS = json.load(open(a.items)); ITEMS = [i for i in ITEMS if (i.get("accepted_strict", True) if a.subset == "strict" else (i.get("accepted", True) if a.subset == "accepted" else True))]
IDX = {it["id"]: k for k, it in enumerate(ITEMS)}; CAT = np.array([it["category"] for it in ITEMS]); N = len(ITEMS); LOCATED = json.load(open(a.located))
KINDS = ("prudential", "etiquette", "aesthetic", "epistemic")
GROUP = {c: CAT == c for c in ("moral", "norm", "descr")}
for k in KINDS: GROUP[k] = np.array([it["category"] == "norm" and it.get("subtype") == k and bool(it.get("kind_ok", True)) for it in ITEMS])
GROUP = {g: m for g, m in GROUP.items() if m.any()}; MAIN = [g for g in ("moral", "norm", "descr") if g in GROUP]
MINN = {g: (a.min_items if g in ("moral", "norm") else (a.min_items_descr if g == "descr" else a.min_items_kind)) for g in GROUP}
COUNTS = {g: rng.multinomial(int(mk.sum()), np.ones(int(mk.sum())) / int(mk.sum()), size=a.boot) for g, mk in GROUP.items()}
FIG = None
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt; FIG = os.path.join(a.out, "figures"); os.makedirs(FIG, exist_ok=True)
except Exception: pass
fmt = lambda x, f="{:.3f}": ("n/a" if x is None or (isinstance(x, float) and not np.isfinite(x)) else f.format(x))
hname = lambda l, h: f"L{l}H{h}"
REPORT = [f"# Circuit-level results", "",
          ("**Run with --any-items (synthetic data): this is not an analysis of the study.**" if a.any_items else
           ("Item set: " + PRIMARY_WHY + (" (the accepted pairs)." if PRIMARY_SET else ". Sensitivity run: not the accepted pairs."))),
          "", f"Items: {N} ({', '.join(f'{g} {int(GROUP[g].sum())}' for g in GROUP)}); inclusion S(perm) - S(rest) >= {a.tau}; subset: {a.subset}; bootstrap {a.boot} item resamples.",
          "These analyses are exploratory.", ""]
SUMMARY = {"items": N, "groups": {g: int(m.sum()) for g, m in GROUP.items()}, "located_set": PRIMARY_SET, "stages": {}}
CSV = {}


def write_csv(name, rows):
    if not rows: return
    keys = list(rows[0].keys()); p = os.path.join(a.out, name)
    with open(p, "w") as f:
        f.write(",".join(keys) + "\n")
        for r in rows: f.write(",".join(("" if r.get(k) is None else (f"{r[k]:.6g}" if isinstance(r[k], float) else str(r[k]).replace(",", ";"))) for k in keys) + "\n")
    CSV[name] = len(rows)


def load_stage(stage):
    out = {}
    for folder in sorted(glob.glob(os.path.join(a.runs, stage, "*/"))):
        model = os.path.basename(folder.rstrip("/")); per = {}
        for f in sorted(glob.glob(os.path.join(folder, "*__*.npz"))):
            if f.endswith(".tmp.npz") or os.path.basename(f).startswith("means__") or os.path.basename(f).startswith("selected_edges__"): continue
            frame, iid = os.path.basename(f)[:-4].split("__", 1)
            if iid not in IDX: continue
            d = per.setdefault(frame, {"ids": [], "files": []}); d["ids"].append(iid); d["files"].append(f)
        if per: out[model] = per
    return out


def arrays(files, keys):
    out = {k: [] for k in keys}; meta0 = None
    for f in files:
        z = np.load(f, allow_pickle=False)
        if meta0 is None: meta0 = json.loads(str(z["__meta__"]))
        for k in keys: out[k].append(np.asarray(z[k], dtype=np.float64) if k in z.files else None)
    missing = [k for k in keys if any(v is None for v in out[k])]
    if missing: raise SystemExit(f"result files under {os.path.dirname(files[0])} lack {missing} (another --frames / --components?)")
    return {k: np.stack(v) for k, v in out.items()}, meta0


def included(ids, gap):
    have = np.zeros(N, bool); g = np.full(N, np.nan)
    for i, iid in enumerate(ids): have[IDX[iid]] = True; g[IDX[iid]] = gap[i]
    return have, have & (np.nan_to_num(g, nan=-np.inf) >= a.tau), g


def to_full(ids, arr):
    full = np.full((N,) + arr.shape[1:], np.nan)
    for i, iid in enumerate(ids): full[IDX[iid]] = arr[i]
    return full


def ratio_of_means_boot(num, den, g, ok):
    mk = GROUP[g]; w = (ok & mk)[mk].astype(float); x = np.nan_to_num(num[mk]) * w; y = np.nan_to_num(den[mk]) * w; n = int(w.sum())
    if n == 0: return float("nan"), float("nan"), float("nan"), 0
    C = COUNTS[g]
    with np.errstate(divide="ignore", invalid="ignore"): b = (C @ x) / (C @ y)
    b = b[np.isfinite(b)]
    return float(x.sum() / y.sum()), float(np.percentile(b, 2.5)) if len(b) else float("nan"), float(np.percentile(b, 97.5)) if len(b) else float("nan"), n


def boot_diff(num1, den1, g1, num2, den2, g2, ok):
    r = []
    for num, den, g in ((num1, den1, g1), (num2, den2, g2)):
        mk = GROUP[g]; w = (ok & mk)[mk].astype(float); C = COUNTS[g]
        with np.errstate(divide="ignore", invalid="ignore"): r.append((C @ (np.nan_to_num(num[mk]) * w)) / (C @ (np.nan_to_num(den[mk]) * w)))
    d = r[0] - r[1]; d = d[np.isfinite(d)]
    return (float(np.percentile(d, 2.5)), float(np.percentile(d, 97.5))) if len(d) else (float("nan"), float("nan"))


def located_sets(model):
    fz = LOCATED.get(model)
    if fz is None: return None
    return {"located": [tuple(x) for x in fz["located"]], "topshare10": [tuple(x) for x in fz["topshare10"]], "located_top5": [tuple(x) for x in fz["located_top5"]], "located_top1": [tuple(x) for x in fz["located_top1"]]}


def spearman(x, y):
    x, y = np.asarray(x, float).ravel(), np.asarray(y, float).ravel(); m = np.isfinite(x) & np.isfinite(y)
    if m.sum() < 3: return float("nan")
    rx, ry = np.argsort(np.argsort(x[m])), np.argsort(np.argsort(y[m]))
    return float(np.corrcoef(rx, ry)[0, 1])


def analyse_ablation():
    data = load_stage("ablation"); rows, diffs = [], []
    if not data: REPORT.extend(["## Necessity (mean-ablation)", "", "No ablation runs found.", ""]); return
    REPORT.extend(["## Necessity (mean-ablation of head sets against size-matched random sets)", "",
                   "Fraction of the clean gap removed = 1 - mean(gap after ablation) / mean(clean gap) over the included items of a group (ratio of means). "
                   "Rank = number of random sets of the same size that remove at least as much as the located set (0 means the located set beats all of them; with 20 random sets, "
                   "a rank of 0 corresponds to the 95th percentile). Mode `all`: every non-BOS position ablated; `final`: the final position only (the cleaner test).", ""])
    for model, per in sorted(data.items()):
        sets_p = os.path.join(a.runs, "ablation", model, "sets.json")
        if not os.path.exists(sets_p): print(f"[!] {model}: no sets.json, skipped"); continue
        sets = json.load(open(sets_p)); names = sets["names"]; name_idx = {n: i for i, n in enumerate(names)}
        rand = {size: [i for i, n in enumerate(names) if n.startswith(f"random{size}_")] for size in (10, 5, 1)}
        for frame, d in sorted(per.items()):
            A, meta = arrays(d["files"], ["perm_base_S", "rest_base_S", "perm_S", "rest_S"]); modes = meta["modes"]
            gap = A["perm_base_S"] - A["rest_base_S"]; gab = A["perm_S"] - A["rest_S"]
            have, ok, gfull = included(d["ids"], gap); gab_full = to_full(d["ids"], gab)
            for g in GROUP:
                n_inc = int((ok & GROUP[g]).sum())
                if n_inc == 0: continue
                for mi, mode in enumerate(modes):
                    frac = {}
                    for s, name in enumerate(names):
                        est = ratio_of_means_boot(gfull - gab_full[:, s, mi], gfull, g, ok); frac[name] = est[0]
                    def rank(name, size):
                        if name not in frac or not rand[size] or not np.isfinite(frac[name]): return None
                        return int(sum(1 for i in rand[size] if np.isfinite(frac[names[i]]) and frac[names[i]] >= frac[name]))
                    e10 = ratio_of_means_boot(gfull - gab_full[:, name_idx["located"], mi], gfull, g, ok)
                    r10 = [frac[names[i]] for i in rand[10]]
                    row = dict(model=model, frame=frame, group=g, mode=mode, n_included=n_inc, below_minimum=int(n_inc < MINN[g]),
                               frac_located=e10[0], ci_lo=e10[1], ci_hi=e10[2], rank_located_among_random10=rank("located", 10), random10_mean=float(np.nanmean(r10)) if r10 else None, random10_max=float(np.nanmax(r10)) if r10 else None,
                               frac_topshare10=frac.get("topshare10"), rank_topshare10=rank("topshare10", 10), frac_union=frac.get("union"),
                               frac_located_top5=frac.get("located_top5"), rank_located_top5_among_random5=rank("located_top5", 5), frac_located_top1=frac.get("located_top1"), rank_located_top1_among_random1=rank("located_top1", 1),
                               mean_clean_gap=float(np.nanmean(gfull[ok & GROUP[g]])) if n_inc else None)
                    rows.append(row)
                    if g == "norm" and "moral" in GROUP:
                        rm = [r for r in rows if r["model"] == model and r["frame"] == frame and r["group"] == "moral" and r["mode"] == mode]
                        if rm:
                            lo, hi = boot_diff(gfull - gab_full[:, name_idx["located"], mi], gfull, "moral", gfull - gab_full[:, name_idx["located"], mi], gfull, "norm", ok)
                            diffs.append(dict(model=model, frame=frame, mode=mode, frac_located_moral=rm[0]["frac_located"], frac_located_norm=row["frac_located"], difference=rm[0]["frac_located"] - row["frac_located"], ci_lo=lo, ci_hi=hi,
                                              n_moral=rm[0]["n_included"], n_norm=n_inc, below_minimum=int(rm[0]["below_minimum"] or row["below_minimum"])))
            if FIG is not None:
                try:
                    fig, axes = plt.subplots(1, len(modes), figsize=(4.5 * len(modes), 3.4), squeeze=False)
                    for mi, mode in enumerate(modes):
                        ax = axes[0, mi]
                        for gi, g in enumerate(MAIN):
                            rr = [r for r in rows if r["model"] == model and r["frame"] == frame and r["group"] == g and r["mode"] == mode]
                            if not rr: continue
                            fr_rand = [ratio_of_means_boot(gfull - gab_full[:, i, mi], gfull, g, ok)[0] for i in rand[10]]
                            ax.scatter(np.full(len(fr_rand), gi) + rng.uniform(-0.15, 0.15, len(fr_rand)), fr_rand, s=10, color="0.6", label="random size-10 sets" if gi == 0 else None)
                            ax.scatter([gi], [rr[0]["frac_located"]], s=60, color="C3", marker="D", label="located" if gi == 0 else None)
                            if rr[0]["frac_topshare10"] is not None: ax.scatter([gi + 0.25], [rr[0]["frac_topshare10"]], s=40, color="C0", marker="s", label="topshare10" if gi == 0 else None)
                        ax.set_xticks(range(len(MAIN))); ax.set_xticklabels(MAIN); ax.axhline(0, color="k", lw=0.5); ax.set_title(f"{model} {frame}: positions {mode}"); ax.set_ylabel("fraction of clean gap removed")
                        if mi == 0: ax.legend(fontsize=7)
                    fig.tight_layout(); fig.savefig(os.path.join(FIG, f"necessity_{model}_{frame}.png"), dpi=130); plt.close(fig)
                except Exception as e: print(f"[figure] necessity {model} {frame}: {type(e).__name__}: {e}")
    write_csv("necessity.csv", rows); write_csv("necessity_moral_minus_norm.csv", diffs)
    REPORT.extend(["| model | frame | mode | group | n | located removes | 95 % CI | rank among 20 random10 | random10 mean | topshare10 | located_top5 (rank/20) | located_top1 (rank/20) |", "|---|---|---|---|---|---|---|---|---|---|---|---|"])
    for r in rows:
        if r["group"] not in MAIN: continue
        REPORT.append(f"| {r['model']} | {r['frame']} | {r['mode']} | {r['group']} | {r['n_included']}{'*' if r['below_minimum'] else ''} | {fmt(r['frac_located'])} | [{fmt(r['ci_lo'])}, {fmt(r['ci_hi'])}] | {r['rank_located_among_random10']} | {fmt(r['random10_mean'])} | {fmt(r['frac_topshare10'])} ({r['rank_topshare10']}) | {fmt(r['frac_located_top5'])} ({r['rank_located_top5_among_random5']}) | {fmt(r['frac_located_top1'])} ({r['rank_located_top1_among_random1']}) |")
    REPORT.extend(["", "\\* fewer included items than the minimum of the plan; shown, not pooled.", "", "Moral-specificity of the necessity: fraction removed by located on moral items minus on norm items (bootstrap interval, independent resamples).", "",
                   "| model | frame | mode | moral | norm | difference | 95 % CI |", "|---|---|---|---|---|---|---|"])
    for r in diffs: REPORT.append(f"| {r['model']} | {r['frame']} | {r['mode']} | {fmt(r['frac_located_moral'])} | {fmt(r['frac_located_norm'])} | {fmt(r['difference'], '{:+.3f}')} | [{fmt(r['ci_lo'], '{:+.3f}')}, {fmt(r['ci_hi'], '{:+.3f}')}]{' *' if r['below_minimum'] else ''} |")
    pooled = [r for r in rows if r["group"] == "moral" and not r["below_minimum"] and r["rank_located_among_random10"] is not None]
    if pooled:
        for frame in sorted({r["frame"] for r in pooled}):
            for mode in sorted({r["mode"] for r in pooled}):
                rr = [r for r in pooled if r["frame"] == frame and r["mode"] == mode]
                if rr: REPORT.append(f"\nFrame {frame}, mode {mode}: located beats all 20 random size-10 sets on moral items in {sum(1 for r in rr if r['rank_located_among_random10'] == 0)} of {len(rr)} models; median fraction removed {np.median([r['frac_located'] for r in rr]):.3f} (random10 mean, median over models: {np.median([r['random10_mean'] for r in rr]):.3f}).")
    REPORT.append(""); SUMMARY["stages"]["ablation"] = {"models": sorted(data), "rows": len(rows)}


def analyse_roles():
    data = load_stage("roles"); att_rows, dla_rows, top_rows = [], [], []
    if not data: REPORT.extend(["## Roles (attention targets and direct logit attribution)", "", "No roles runs found.", ""]); return
    GN = ["bos", "priming", "stem_before_edit", "edit", "stem_after_edit", "cue"]
    REPORT.extend(["## Roles (what the heads attend to, and what they write)", "",
                   "Attention: weight of the final position (the readout position) on each token group, averaged over the two prompts, the included items and the heads of a set; "
                   "`all heads` is the mean over every head of the model. Direct effect: perm-minus-rest difference of the direct logit attribution to the logit difference (positive words minus negative words), "
                   "summed over the heads of a set; the share is its ratio to the total difference (embedding + all heads + all MLPs, which equals the metric difference exactly).", ""])
    for model, per in sorted(data.items()):
        fs = located_sets(model)
        for frame, d in sorted(per.items()):
            keys = [f"{s}_{k}" for s in ("perm", "rest") for k in ("S", "attn_final", "attn_edit", "dla_heads", "dla_mlp", "dla_embed", "dla_attn_bias")]
            A, meta = arrays(d["files"], keys); L, H = A["perm_dla_heads"].shape[1:]
            gap = A["perm_S"] - A["rest_S"]; have, ok, gfull = included(d["ids"], gap)
            att = to_full(d["ids"], (A["perm_attn_final"] + A["rest_attn_final"]) / 2)
            att_edit = to_full(d["ids"], (A["perm_attn_edit"] + A["rest_attn_edit"]) / 2)
            dH = to_full(d["ids"], A["perm_dla_heads"] - A["rest_dla_heads"]); dM = to_full(d["ids"], A["perm_dla_mlp"] - A["rest_dla_mlp"])
            dE = to_full(d["ids"], A["perm_dla_embed"] - A["rest_dla_embed"]); dB = to_full(d["ids"], A["perm_dla_attn_bias"] - A["rest_dla_attn_bias"])
            total = dH.sum((1, 2)) + dM.sum(1) + dE + dB.sum(1)
            sets = dict(fs) if fs else {}; sets["all heads"] = [(l, h) for l in range(L) for h in range(H)]
            for g in MAIN:
                mk = ok & GROUP[g]; n_inc = int(mk.sum())
                if n_inc == 0: continue
                for sname, heads in sets.items():
                    li = np.array([h[0] for h in heads]); hi = np.array([h[1] for h in heads])
                    if li.size == 0: continue
                    shares = np.nanmean(att[mk][:, li, hi, :], axis=(0, 1))
                    att_rows.append(dict(model=model, frame=frame, group=g, set=sname, n_included=n_inc, below_minimum=int(n_inc < MINN[g]),
                                         **{f"attn_{gn}": float(shares[k]) for k, gn in enumerate(GN)}, attn_edit_from_later=float(np.nanmean(att_edit[mk][:, li, hi]))))
                    if sname != "all heads":
                        num = dH[:, li, hi].sum(1); est = ratio_of_means_boot(num, total, g, ok)
                        dla_rows.append(dict(model=model, frame=frame, group=g, set=sname, n_included=n_inc, below_minimum=int(n_inc < MINN[g]), share_of_direct_effect=est[0], ci_lo=est[1], ci_hi=est[2],
                                             mean_direct_effect=float(np.nanmean(num[mk])), mean_total=float(np.nanmean(total[mk]))))
                for sname, num in (("all heads", dH.sum((1, 2))), ("MLPs", dM.sum(1)), ("embedding", dE)):
                    est = ratio_of_means_boot(num, total, g, ok)
                    dla_rows.append(dict(model=model, frame=frame, group=g, set=sname, n_included=n_inc, below_minimum=int(n_inc < MINN[g]), share_of_direct_effect=est[0], ci_lo=est[1], ci_hi=est[2],
                                         mean_direct_effect=float(np.nanmean(num[mk])), mean_total=float(np.nanmean(total[mk]))))
                mean_dh = np.nanmean(dH[mk], 0); order = np.argsort(-np.abs(mean_dh).ravel())[:a.top]
                for rnk, idx in enumerate(order, start=1):
                    l, h = divmod(int(idx), H)
                    top_rows.append(dict(model=model, frame=frame, group=g, rank=rnk, head=hname(l, h), mean_direct_effect=float(mean_dh[l, h]), share=float(mean_dh[l, h] / np.nanmean(total[mk])),
                                         sign_consistency=float(np.mean(np.sign(dH[mk][:, l, h]) == np.sign(mean_dh[l, h]))), in_located=int((l, h) in (fs or {}).get("located", [])), in_topshare10=int((l, h) in (fs or {}).get("topshare10", []))))
    write_csv("roles_attention.csv", att_rows); write_csv("roles_direct_effect.csv", dla_rows); write_csv("roles_top_heads.csv", top_rows)
    REPORT.extend(["### Attention of the located heads at the readout position (share on each token group; `all heads` for comparison)", "",
                   "| model | frame | group | set | n | edit | cue | priming | stem (before / after) | bos | edit attended from later positions |", "|---|---|---|---|---|---|---|---|---|---|---|"])
    for r in att_rows:
        if r["set"] in ("located", "all heads"):
            REPORT.append(f"| {r['model']} | {r['frame']} | {r['group']} | {r['set']} | {r['n_included']}{'*' if r['below_minimum'] else ''} | {fmt(r['attn_edit'])} | {fmt(r['attn_cue'])} | {fmt(r['attn_priming'])} | {fmt(r['attn_stem_before_edit'])} / {fmt(r['attn_stem_after_edit'])} | {fmt(r['attn_bos'])} | {fmt(r['attn_edit_from_later'])} |")
    REPORT.extend(["", "### Share of the direct effect (perm minus rest) carried by each set of components", "", "| model | frame | group | set | share | 95 % CI | mean total difference |", "|---|---|---|---|---|---|---|"])
    for r in dla_rows:
        if r["set"] in ("located", "topshare10", "all heads", "MLPs", "embedding"):
            REPORT.append(f"| {r['model']} | {r['frame']} | {r['group']} | {r['set']} | {fmt(r['share_of_direct_effect'])} | [{fmt(r['ci_lo'])}, {fmt(r['ci_hi'])}]{' *' if r['below_minimum'] else ''} | {fmt(r['mean_total'], '{:+.3f}')} |")
    REPORT.extend(["", f"### The {a.top} heads with the largest direct effect in the held-out data (moral items), with located membership", ""])
    for model in sorted(data):
        for frame in sorted(data[model]):
            rr = [r for r in top_rows if r["model"] == model and r["frame"] == frame and r["group"] == "moral"]
            if rr: REPORT.append(f"* {model} {frame}: " + ", ".join(f"{r['head']} ({r['share']:+.2f}{', located' if r['in_located'] else ''}{', imp10' if r['in_topshare10'] else ''})" for r in rr) + f"; located heads among them: {sum(r['in_located'] for r in rr)}")
    REPORT.append(""); SUMMARY["stages"]["roles"] = {"models": sorted(data), "rows": len(att_rows)}


def analyse_layers():
    data = load_stage("layers"); prof_rows, land_rows = [], []
    if not data: REPORT.extend(["## Layers (activation patching per layer)", "", "No layer runs found.", ""]); return
    REPORT.extend(["## Layers (where the difference is computed and where it travels)", "",
                   "Fraction of the gap recovered = mean(S after patching layer l) - mean(S rest) over mean(clean gap), p2r. `half-layer final`: first layer at which patching the residual stream at the final position "
                   "recovers at least half of the gap; `half-layer edit`: last layer at which patching the residual at the edited tokens still recovers at least half. Both also as a fraction of the depth.", ""])
    for model, per in sorted(data.items()):
        for frame, d in sorted(per.items()):
            z0 = np.load(d["files"][0], allow_pickle=False); meta0 = json.loads(str(z0["__meta__"])); comps = [c for c in meta0["components"]]; dirs = meta0["directions"]
            if "p2r" not in dirs: continue
            A, meta = arrays(d["files"], ["perm_S", "rest_S"] + [f"p2r_{c}_S" for c in comps]); L = A[f"p2r_{comps[0]}_S"].shape[1]
            gap = A["perm_S"] - A["rest_S"]; have, ok, gfull = included(d["ids"], gap)
            for g in MAIN:
                mk = ok & GROUP[g]; n_inc = int(mk.sum())
                if n_inc == 0: continue
                profiles = {}
                for c in comps:
                    rec = to_full(d["ids"], A[f"p2r_{c}_S"] - A["rest_S"][:, None]); prof = np.nanmean(rec[mk], 0) / np.nanmean(gfull[mk]); profiles[c] = prof
                    for l in range(L): prof_rows.append(dict(model=model, frame=frame, group=g, component=c, layer=l, fraction_recovered=float(prof[l]), n_included=n_inc, below_minimum=int(n_inc < MINN[g])))
                land = dict(model=model, frame=frame, group=g, n_included=n_inc, below_minimum=int(n_inc < MINN[g]), n_layers=L)
                if "resid_final" in profiles:
                    hf = next((l for l in range(L) if profiles["resid_final"][l] >= 0.5), None); land["half_layer_final"] = hf; land["half_layer_final_frac"] = None if hf is None else hf / (L - 1)

                    rec = to_full(d["ids"], A["p2r_resid_final_S"] - A["rest_S"][:, None]); w = (ok & GROUP[g])[GROUP[g]].astype(float); C = COUNTS[g]
                    num = np.nan_to_num(rec[GROUP[g]]) * w[:, None]; den = np.nan_to_num(gfull[GROUP[g]]) * w
                    with np.errstate(divide="ignore", invalid="ignore"): pb = (C @ num) / (C @ den)[:, None]
                    hl = [next((l for l in range(L) if p[l] >= 0.5), np.nan) for p in pb if np.all(np.isfinite(p))]
                    land["half_layer_final_ci"] = [float(np.nanpercentile(hl, 2.5)), float(np.nanpercentile(hl, 97.5))] if hl else None
                if "resid_edit" in profiles:
                    he = next((l for l in range(L - 1, -1, -1) if profiles["resid_edit"][l] >= 0.5), None); land["half_layer_edit"] = he; land["half_layer_edit_frac"] = None if he is None else he / (L - 1)
                for c in ("mlp_all", "attn_all", "mlp_final", "attn_final"):
                    if c in profiles: land[f"peak_layer_{c}"] = int(np.nanargmax(profiles[c])); land[f"peak_{c}"] = float(np.nanmax(profiles[c]))
                land_rows.append(land)
            if FIG is not None:
                try:
                    fig, axes = plt.subplots(1, len(comps), figsize=(3.2 * len(comps), 3.0), squeeze=False, sharey=True)
                    for ci, c in enumerate(comps):
                        ax = axes[0, ci]
                        for g in MAIN:
                            rr = [r["fraction_recovered"] for r in prof_rows if r["model"] == model and r["frame"] == frame and r["group"] == g and r["component"] == c]
                            if rr: ax.plot(range(len(rr)), rr, marker="o", ms=2.5, label=g)
                        ax.axhline(0, color="k", lw=0.5); ax.axhline(1, color="k", lw=0.5, ls=":"); ax.set_title(c, fontsize=9); ax.set_xlabel("layer")
                        if ci == 0: ax.set_ylabel("fraction of gap recovered"); ax.legend(fontsize=7)
                    fig.suptitle(f"{model} {frame} (p2r)", fontsize=10); fig.tight_layout(); fig.savefig(os.path.join(FIG, f"layers_{model}_{frame}.png"), dpi=130); plt.close(fig)
                except Exception as e: print(f"[figure] layers {model} {frame}: {type(e).__name__}: {e}")
    write_csv("layers_profiles.csv", prof_rows); write_csv("layers_landmarks.csv", land_rows)
    REPORT.extend(["| model | frame | group | n | layers | half-layer final (95 % CI) | as depth fraction | half-layer edit | as depth fraction | peak MLP (all pos.) | peak attention (all pos.) |", "|---|---|---|---|---|---|---|---|---|---|---|"])
    for r in land_rows:
        ci = r.get("half_layer_final_ci"); cis = f" ({fmt(ci[0], '{:.0f}')}-{fmt(ci[1], '{:.0f}')})" if ci else ""
        REPORT.append(f"| {r['model']} | {r['frame']} | {r['group']} | {r['n_included']}{'*' if r['below_minimum'] else ''} | {r['n_layers']} | {r.get('half_layer_final')}{cis} | {fmt(r.get('half_layer_final_frac'), '{:.2f}')} | {r.get('half_layer_edit')} | {fmt(r.get('half_layer_edit_frac'), '{:.2f}')} | "
                      f"L{r.get('peak_layer_mlp_all')} ({fmt(r.get('peak_mlp_all'), '{:.2f}')}) | L{r.get('peak_layer_attn_all')} ({fmt(r.get('peak_attn_all'), '{:.2f}')}) |")
    REPORT.extend(["", "Full profiles: `layers_profiles.csv`; figures in `figures/layers_*.png`.", ""]); SUMMARY["stages"]["layers"] = {"models": sorted(data), "rows": len(land_rows)}


def analyse_edges():
    data = load_stage("edges"); top_rows, share_rows, node_rows = [], [], []
    if not data: REPORT.extend(["## Edges (edge attribution patching)", "", "No edge runs found.", ""]); return
    REPORT.extend(["## Edges (which components feed the heads, through which input)", "",
                   "Score of an edge = first-order estimate of the change of the logit difference when that edge alone is patched from the permissive into the restrictive run (p2r), "
                   "mean over the included items of a group; sign kept (positive = pushes the restrictive prompt towards the permissive answer). Sources: every head, every MLP block, the embedding. "
                   "`sign consistency`: share of items whose score has the sign of the mean. The validation of the estimate against exact edge patching on the original pairs is in "
                   "`runs_rehearsal/circuits/edges/*/` (the summary lines of each run's log).", ""])
    SG = ["edit", "stem_after_edit", "cue"]
    for model, per in sorted(data.items()):
        fs = located_sets(model)
        for frame, d in sorted(per.items()):
            z0 = np.load(d["files"][0], allow_pickle=False); meta0 = json.loads(str(z0["__meta__"])); labels = meta0["receiver_inputs"]; L, H = meta0["n_layers"], meta0["n_heads"]
            if "p2r" not in meta0["directions"]: continue
            A, meta = arrays(d["files"], ["perm_S", "rest_S", "p2r_edges", "p2r_node_heads"]); gap = A["perm_S"] - A["rest_S"]; have, ok, gfull = included(d["ids"], gap)
            E = to_full(d["ids"], A["p2r_edges"]); NH = to_full(d["ids"], A["p2r_node_heads"])
            n_src = E.shape[1]; src_label = lambda s: hname(s // H, s % H) if s < L * H else (f"MLP{s - L * H}" if s < L * H + L else "embed")
            for g in MAIN:
                mk = ok & GROUP[g]; n_inc = int(mk.sum())
                if n_inc == 0: continue
                M = np.nanmean(E[mk], 0); tot = M.sum(-1)
                for j, lab in enumerate(labels):
                    order = np.argsort(-np.abs(tot[:, j]))[:a.top]; per_item = E[mk][:, :, j, :].sum(-1)
                    for rnk, s in enumerate(order, start=1):
                        top_rows.append(dict(model=model, frame=frame, group=g, receiver=lab, rank=rnk, source=src_label(int(s)), mean_score=float(tot[s, j]),
                                             score_edit=float(M[s, j, 0]), score_stem_after=float(M[s, j, 1]), score_cue=float(M[s, j, 2]),
                                             sign_consistency=float(np.mean(np.sign(per_item[:, s]) == np.sign(tot[s, j]))), n_included=n_inc, below_minimum=int(n_inc < MINN[g])))
                heads = sorted({lab.split(".")[0] for lab in labels if lab != "logits"})
                for hd in heads + ["logits"]:
                    js = [j for j, lab in enumerate(labels) if (lab == "logits" if hd == "logits" else lab.startswith(hd + "."))]
                    absM = np.abs(M[:, js, :]).sum((0, 1)); total = absM.sum()
                    l_h = None if hd == "logits" else (int(hd[1:hd.index("H")]), int(hd[hd.index("H") + 1:]))
                    share_rows.append(dict(model=model, frame=frame, group=g, receiver=hd, in_located=int(l_h in (fs or {}).get("located", [])) if l_h else None, n_included=n_inc, below_minimum=int(n_inc < MINN[g]),
                                           **{f"share_{SG[k]}": float(absM[k] / total) if total > 0 else None for k in range(3)}, total_abs_score=float(total),
                                           top_source=src_label(int(np.argmax(np.abs(M[:, js, :].sum((1, 2))))))))

            hfolder = os.path.join(a.heads_runs, model)
            if os.path.isdir(hfolder):
                rs_S, rs_LD = [], []; mean_node, mean_exS = [], []
                for i, iid in enumerate(d["ids"]):
                    p = os.path.join(hfolder, f"{frame}__{iid}.npz")
                    if not os.path.exists(p) or not ok[IDX[iid]]: continue
                    z = np.load(p, allow_pickle=False)
                    if "p2r_all__S" not in z.files: continue
                    ex_S = np.asarray(z["p2r_all__S"], float); ex_LD = np.asarray(z["p2r_all__LD"], float) if "p2r_all__LD" in z.files else None; node = A["p2r_node_heads"][i]
                    rs_S.append(spearman(node, ex_S)); mean_node.append(node); mean_exS.append(ex_S)
                    if ex_LD is not None: rs_LD.append(spearman(node, ex_LD))
                if rs_S:
                    node_rows.append(dict(model=model, frame=frame, n_items=len(rs_S), spearman_vs_exact_S_mean=float(np.nanmean(rs_S)), spearman_vs_exact_S_median=float(np.nanmedian(rs_S)),
                                          spearman_vs_exact_LD_mean=float(np.nanmean(rs_LD)) if rs_LD else None, spearman_item_means=spearman(np.mean(mean_node, 0), np.mean(mean_exS, 0)),
                                          top10_overlap_item_means=int(len(set(np.argsort(-np.abs(np.mean(mean_node, 0)).ravel())[:10]) & set(np.argsort(-np.abs(np.mean(mean_exS, 0)).ravel())[:10])))))
    write_csv("edges_top.csv", top_rows); write_csv("edges_position_shares.csv", share_rows); write_csv("edges_node_vs_exact.csv", node_rows)
    REPORT.extend(["### Strongest upstream edges into the located heads and the logits (moral items; three per receiver across its query, key and value inputs; "
                   f"the {a.top} strongest per input, for every receiver and group, are in `edges_top.csv`)", ""])
    for model in sorted(data):
        fs = located_sets(model) or {}
        for frame in sorted(data[model]):
            rr = [r for r in top_rows if r["model"] == model and r["frame"] == frame and r["group"] == "moral"]
            if not rr: continue
            REPORT.append(f"**{model}, {frame}** (n = {rr[0]['n_included']}{'*' if rr[0]['below_minimum'] else ''})"); REPORT.append("")
            heads = [hname(*h) for h in fs.get("located", [])] or sorted({r["receiver"].split(".")[0] for r in rr if r["receiver"] != "logits"})
            for hd in heads + ["logits"]:
                rl = sorted([r for r in rr if (r["receiver"] == "logits" if hd == "logits" else r["receiver"].startswith(hd + "."))], key=lambda r: -abs(r["mean_score"]))[:3]
                if rl: REPORT.append(f"* {hd}: " + ", ".join(f"{r['source']} -> {r['receiver'].split('.')[-1] if hd != 'logits' else 'logits'} ({r['mean_score']:+.3f}, sign {r['sign_consistency']:.2f})" for r in rl))
            REPORT.append("")
    REPORT.extend(["### Where a receiver's incoming score arrives (share of absolute mean score by token group; receivers = the located heads, q/k/v together, and the logits)", "",
                   "| model | frame | group | receiver | located | edit | rest of stem | cue | strongest source |", "|---|---|---|---|---|---|---|---|---|"])
    for r in share_rows:
        if r["group"] in ("moral", "norm"): REPORT.append(f"| {r['model']} | {r['frame']} | {r['group']} | {r['receiver']} | {'yes' if r['in_located'] else ('' if r['in_located'] is None else 'no')} | {fmt(r['share_edit'], '{:.2f}')} | {fmt(r['share_stem_after_edit'], '{:.2f}')} | {fmt(r['share_cue'], '{:.2f}')} | {r['top_source']} |")
    REPORT.extend(["", "### Node-level attribution scores against the exact head-patching effects (p2r, all positions) of the main run", "",
                   "| model | frame | items | Spearman vs exact S (mean / median over items) | vs exact LD (mean) | Spearman of item means | top-10 overlap |", "|---|---|---|---|---|---|---|"])
    for r in node_rows: REPORT.append(f"| {r['model']} | {r['frame']} | {r['n_items']} | {fmt(r['spearman_vs_exact_S_mean'])} / {fmt(r['spearman_vs_exact_S_median'])} | {fmt(r['spearman_vs_exact_LD_mean'])} | {fmt(r['spearman_item_means'])} | {r['top10_overlap_item_means']} / 10 |")
    REPORT.append(""); SUMMARY["stages"]["edges"] = {"models": sorted(data), "rows": len(top_rows)}
    analyse_edges_exact()


def analyse_edges_exact():
    data = load_stage("edges_exact")
    if not data: return
    rows, agree = [], []
    REPORT.extend(["### Exact patching of the strongest estimated edges", "",
                   "For the models listed, the --top edges per receiver input (query, key, value of each located head, and the logits), chosen by their mean "
                   "estimated score over all run items, were patched exactly on every item. `exact` is the mean change of the logit difference over the included "
                   "items of the group, `S` the mean change of the readout S; `r` is the correlation between estimate and exact value over edges and items.", ""])
    for model, per in sorted(data.items()):
        for frame, d in sorted(per.items()):
            selp = os.path.join(a.runs, "edges_exact", model, f"selected_edges__{frame}.json")
            if not os.path.exists(selp): continue
            sel = json.load(open(selp))["edges"]
            A, meta = arrays(d["files"], ["perm_S", "rest_S", "exact_metric", "estimate_metric", "exact_S"]); gap = A["perm_S"] - A["rest_S"]; have, ok, gfull = included(d["ids"], gap)
            EX = to_full(d["ids"], A["exact_metric"]); ES = to_full(d["ids"], A["estimate_metric"]); XS = to_full(d["ids"], A["exact_S"])
            for g in MAIN:
                mk = ok & GROUP[g]; n_inc = int(mk.sum())
                if n_inc == 0: continue
                ex_m = np.nanmean(EX[mk], 0); es_m = np.nanmean(ES[mk], 0); xs_m = np.nanmean(XS[mk], 0)
                x, y = ES[mk].ravel(), EX[mk].ravel(); m_ = np.isfinite(x) & np.isfinite(y)
                r_items = float(np.corrcoef(x[m_], y[m_])[0, 1]) if m_.sum() > 2 and x[m_].std() > 0 else float("nan")
                r_means = float(np.corrcoef(es_m, ex_m)[0, 1]) if len(ex_m) > 2 and es_m.std() > 0 else float("nan")
                agree.append(dict(model=model, frame=frame, group=g, n_included=n_inc, n_edges=len(sel), r_edges_x_items=r_items, r_edge_means=r_means,
                                  sign_agreement_means=float(np.mean(np.sign(es_m) == np.sign(ex_m))), below_minimum=int(n_inc < MINN[g])))
                for k, e in enumerate(sel):
                    rows.append(dict(model=model, frame=frame, group=g, receiver=e["receiver"], source=e["source"], exact_mean=float(ex_m[k]), estimate_mean=float(es_m[k]), exact_S_mean=float(xs_m[k]),
                                     sign_consistency=float(np.mean(np.sign(EX[mk][:, k]) == np.sign(ex_m[k]))), n_included=n_inc, below_minimum=int(n_inc < MINN[g])))
    write_csv("edges_exact.csv", rows); write_csv("edges_exact_agreement.csv", agree)
    REPORT.extend(["| model | frame | group | n | edges | r (edges x items) | r (edge means) | sign agreement of means |", "|---|---|---|---|---|---|---|---|"])
    for r in agree: REPORT.append(f"| {r['model']} | {r['frame']} | {r['group']} | {r['n_included']}{'*' if r['below_minimum'] else ''} | {r['n_edges']} | {fmt(r['r_edges_x_items'])} | {fmt(r['r_edge_means'])} | {fmt(r['sign_agreement_means'], '{:.2f}')} |")
    REPORT.extend(["", "Strongest edges by exact effect (moral items; three per located head and for the logits):", ""])
    for model in sorted(data):
        for frame in sorted(data[model]):
            rr = [r for r in rows if r["model"] == model and r["frame"] == frame and r["group"] == "moral"]
            if not rr: continue
            heads = sorted({r["receiver"].split(".")[0] for r in rr if r["receiver"] != "logits"}) + ["logits"]
            REPORT.append(f"**{model}, {frame}** (n = {rr[0]['n_included']}{'*' if rr[0]['below_minimum'] else ''})"); REPORT.append("")
            for hd in heads:
                rl = sorted([r for r in rr if (r["receiver"] == "logits" if hd == "logits" else r["receiver"].startswith(hd + "."))], key=lambda r: -abs(r["exact_mean"]))[:3]
                if rl: REPORT.append(f"* {hd}: " + ", ".join(f"{r['source']} -> {r['receiver'].split('.')[-1] if hd != 'logits' else 'logits'} (exact {r['exact_mean']:+.3f}, est. {r['estimate_mean']:+.3f}, sign {r['sign_consistency']:.2f})" for r in rl))
            REPORT.append("")
    SUMMARY["stages"]["edges_exact"] = {"models": sorted(data), "rows": len(rows)}


for st in a.stages: {"ablation": analyse_ablation, "roles": analyse_roles, "layers": analyse_layers, "edges": analyse_edges}[st]()
REPORT.extend(["## Files", ""] + [f"* `{k}` ({v} rows)" for k, v in CSV.items()] + ([f"* `figures/` ({len(os.listdir(FIG))} figures)"] if FIG else []))
open(os.path.join(a.out, "circuits_report.md"), "w").write("\n".join(REPORT) + "\n"); json.dump(SUMMARY, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
print(f"[analyze_circuits] report: {os.path.join(a.out, 'circuits_report.md')}; CSV files: {', '.join(CSV)}")
