"""Shares of the located heads by kind of pair (H1 to H4) and sensitivity analyses."""
import argparse, json, os, sys, glob, itertools, collections, warnings
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from common import primary_item_set, check_analysis_items
warnings.filterwarnings("ignore", message="Mean of empty slice"); warnings.filterwarnings("ignore", message="All-NaN slice encountered")

ap = argparse.ArgumentParser()
ap.add_argument("--runs", required=True); ap.add_argument("--items", required=True); ap.add_argument("--located", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--condition", default="p2r_all"); ap.add_argument("--readout", default="S"); ap.add_argument("--headset", default="located")
ap.add_argument("--tau", type=float, default=0.02); ap.add_argument("--min-items", type=int, default=30, help="included moral / norm items a model and frame needs")
ap.add_argument("--min-items-descr", type=int, default=20); ap.add_argument("--min-items-kind", type=int, default=10)
ap.add_argument("--boot", type=int, default=10000); ap.add_argument("--perm", type=int, default=20000); ap.add_argument("--seed", type=int, default=20260920); ap.add_argument("--subset", default="accepted", choices=["accepted", "strict", "all"])
ap.add_argument("--any-items", action="store_true", help="synthetic data only")
a = ap.parse_args(); check_analysis_items(a.any_items); os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
OPTIONS_DEFAULT = (a.headset, a.condition, a.readout, a.tau, a.subset) == ("located", "p2r_all", "S", 0.02, "accepted"); PRIMARY_SET, PRIMARY_WHY = primary_item_set(a.items); IS_DEFAULT = OPTIONS_DEFAULT and PRIMARY_SET
ITEMS = json.load(open(a.items)); ITEMS = [i for i in ITEMS if (i.get("accepted_strict", True) if a.subset == "strict" else (i.get("accepted", True) if a.subset == "accepted" else True))]
IDX = {it["id"]: k for k, it in enumerate(ITEMS)}; CAT = np.array([it["category"] for it in ITEMS]); N = len(ITEMS); LOCATED = json.load(open(a.located))
KINDS = ("prudential", "etiquette", "aesthetic", "epistemic"); HEADSETS = ("located", "located_top5", "located_top1", "topshare10", "topshare_1pct")
GROUP = {c: CAT == c for c in ("moral", "norm", "descr")}
for k in KINDS: GROUP[k] = np.array([it["category"] == "norm" and it.get("subtype") == k and bool(it.get("kind_ok", True)) for it in ITEMS])
GROUP = {g: m for g, m in GROUP.items() if m.any()}; MINN = {g: (a.min_items if g in ("moral", "norm") else (a.min_items_descr if g == "descr" else a.min_items_kind)) for g in GROUP}
CONTRASTS = [c for c in [("moral", "norm"), ("moral", "descr"), ("norm", "descr")] + [("moral", k) for k in KINDS] if c[0] in GROUP and c[1] in GROUP]
PAIRS = [("Llama-3.2-1B", "Llama-3.2-1B-Instruct"), ("Llama-3.2-3B", "Llama-3.2-3B-Instruct"), ("Llama-3.1-8B", "Llama-3.1-8B-Instruct"), ("gemma-2b", "gemma-2b-it"),
         ("Qwen2.5-3B", "Qwen2.5-3B-Instruct"), ("Qwen2.5-7B", "Qwen2.5-7B-Instruct"), ("Qwen2.5-14B", "Qwen2.5-14B-Instruct")]
family = lambda m: "llama" if m.startswith("Llama") else ("gemma" if m.startswith("gemma") else "qwen")


def load_model(folder, model):
    out = {}; fz = LOCATED[model]; nkey = 0
    for f in sorted(glob.glob(os.path.join(folder, "*__*.npz"))):
        if f.endswith(".tmp.npz"): continue
        frame, iid = os.path.basename(f)[:-4].split("__", 1)
        if iid not in IDX: continue
        try: z = np.load(f, allow_pickle=False)
        except Exception as e: raise SystemExit(f"unreadable result file {f} ({type(e).__name__}): delete it and resume run_heads.py")
        key = f"{a.condition}__{a.readout}"
        if key not in z.files: continue
        nkey += 1; meta = json.loads(str(z["__meta__"])); arr = z[key]
        assert arr.shape == (fz["n_layers"], fz["n_heads"]), f"{f}: array shape {arr.shape} does not match the located head table of {model}"
        assert meta["n_tok_perm"] == meta["n_tok_rest"], f"{f}: prompts of unequal token count"
        d = out.setdefault(frame, dict(E=np.full((N, arr.size), np.nan, dtype=np.float32), gap=np.full(N, np.nan), mass=np.full(N, np.nan)))
        d["E"][IDX[iid]] = np.abs(arr).ravel(); d["gap"][IDX[iid]] = meta["base_perm"]["S"] - meta["base_rest"]["S"]
        d["mass"][IDX[iid]] = (meta["base_perm"]["mass"] + meta["base_rest"]["mass"]) / 2
    if nkey == 0: print(f"[!] {model}: no result file contains {a.condition}__{a.readout} (was this condition run?)")
    return out


def head_index(model, name):
    fz = LOCATED[model]; H = fz["n_heads"]; return np.array([l * H + h for l, h in fz[name]])


def boot_counts(n, B):
    idx = rng.integers(0, n, size=(B, n)); c = np.zeros((B, n), dtype=np.float32)
    for b in range(B): c[b] = np.bincount(idx[b], minlength=n)
    return c


def perm_p(x, y, P):
    z = np.concatenate([x, y]); n1 = len(x); obs = np.log(x.mean() / y.mean()); tot = z.sum(); hits = 0; done = 0
    while done < P:
        k = min(2000, P - done); sel = np.argsort(rng.random((k, len(z))), axis=1)[:, :n1]; s1 = z[sel].sum(1); st = np.log((s1 / n1) / ((tot - s1) / (len(z) - n1)))
        hits += int((np.abs(st) >= abs(obs) - 1e-12).sum()); done += k
    return (hits + 1) / (P + 1)


def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; r = np.empty(n); r[o] = np.minimum(q, 1); return r


def reading(ci):
    if ci[0] > 1.5: return "strong moral preference (interval above 1.5)"
    if ci[0] >= 0.8 and ci[1] <= 1.25: return "no meaningful content specificity (interval inside 0.8 to 1.25" + ("; it excludes 1, but the difference is within the margin)" if ci[0] > 1 or ci[1] < 1 else ")")
    if ci[0] > 1: return "weak to moderate moral preference (interval above 1)"
    if ci[1] < 1: return "the published heads carry a SMALLER share for moral than for norm content (interval below 1)"
    return "inconclusive"


fmt = lambda v, f="{:.2f}": "n/a" if v is None or (isinstance(v, float) and not np.isfinite(v)) else f.format(v)
models = sorted(m for m in os.listdir(a.runs) if os.path.isdir(os.path.join(a.runs, m)) and m in LOCATED); skipped = [m for m in os.listdir(a.runs) if os.path.isdir(os.path.join(a.runs, m)) and m not in LOCATED]
if skipped: print("[!] folders without a located head set (ignored):", skipped)
DATA = {m: load_model(os.path.join(a.runs, m), m) for m in models}; frames = sorted({f for m in models for f in DATA[m]})
if not frames: raise SystemExit(f"no result file under {a.runs} contains {a.condition}__{a.readout}: nothing to analyse")
COUNTS = {g: boot_counts(int(mk.sum()), a.boot) for g, mk in GROUP.items()}
behav, per_model, pooled = [], [], []; SHARE = {}; OK = {}
for m in models:
    for fr in frames:
        if fr not in DATA[m]: continue
        d = DATA[m][fr]; have = ~np.isnan(d["gap"]); tot = np.nansum(d["E"], 1); ok = have & (d["gap"] >= a.tau) & (tot > 0); OK[(m, fr)] = ok
        for g in ("moral", "norm", "descr"):
            if g not in GROUP: continue
            mk = GROUP[g]; behav.append(dict(model=m, frame=fr, category=g, n_run=int((have & mk).sum()), n_included=int((ok & mk).sum()), mean_gap=float(np.nanmean(d["gap"][mk])) if (have & mk).any() else float("nan"),
                                             share_correct_sign=float(np.mean(d["gap"][have & mk] > 0)) if (have & mk).any() else float("nan"), mean_mass=float(np.nanmean(d["mass"][mk])) if (have & mk).any() else float("nan")))
        for hs in HEADSETS: SHARE[(m, fr, hs)] = np.where(ok, np.nansum(d["E"][:, head_index(m, hs)], 1) / np.where(tot > 0, tot, 1), np.nan)
for fr, hs, (c1, c2) in itertools.product(frames, HEADSETS, CONTRASTS):
    logs, used, left_out = [], [], []
    for m in models:
        if (m, fr, hs) not in SHARE: continue
        sh, ok = SHARE[(m, fr, hs)], OK[(m, fr)]; m1, m2 = GROUP[c1], GROUP[c2]; x, y = sh[m1 & ok], sh[m2 & ok]
        short = [g for g in ("moral", "norm") if g in GROUP and (GROUP[g] & ok).sum() < MINN[g]] + [g for g in (c1, c2) if g not in ("moral", "norm") and (GROUP[g] & ok).sum() < MINN[g]]
        if short:
            per_model.append(dict(model=m, frame=fr, headset=hs, contrast=f"{c1}/{c2}", n1=len(x), n2=len(y), note="insufficient behavioural contrast: " + ", ".join(sorted(set(short))))); left_out.append(m); continue
        w1, w2 = ok[m1].astype(np.float32), ok[m2].astype(np.float32); s1, s2 = np.nan_to_num(sh[m1]), np.nan_to_num(sh[m2])
        with np.errstate(divide="ignore", invalid="ignore"):
            n1b, n2b = COUNTS[c1] @ w1, COUNTS[c2] @ w2; b = np.log(((COUNTS[c1] @ (s1 * w1)) / np.where(n1b > 0, n1b, np.nan)) / ((COUNTS[c2] @ (s2 * w2)) / np.where(n2b > 0, n2b, np.nan))); b[~np.isfinite(b)] = np.nan
        per_model.append(dict(model=m, frame=fr, headset=hs, contrast=f"{c1}/{c2}", n1=len(x), n2=len(y), mean_share_1=float(x.mean()), mean_share_2=float(y.mean()), uniform_share=float(len(head_index(m, hs)) / DATA[m][fr]["E"].shape[1]),
                              ratio=float(x.mean() / y.mean()), ci95=[float(np.exp(np.nanpercentile(b, 2.5))), float(np.exp(np.nanpercentile(b, 97.5)))], p_perm=perm_p(x, y, a.perm) if hs == a.headset else None))
        logs.append(b); used.append(m)
    if logs:
        B = np.nanmean(logs, 0); est = float(np.mean([np.log(r["ratio"]) for r in per_model if "ratio" in r and r["frame"] == fr and r["headset"] == hs and r["contrast"] == f"{c1}/{c2}"]))
        primary = IS_DEFAULT and hs == "located" and (c1, c2) == ("moral", "norm") and fr in ("A1", "B"); lo, hi = (1.25, 98.75) if primary else (2.5, 97.5)
        ci = [float(np.exp(np.nanpercentile(B, lo))), float(np.exp(np.nanpercentile(B, hi)))]
        pooled.append(dict(frame=fr, headset=hs, contrast=f"{c1}/{c2}", n_models=len(used), models_used=used, models_left_out=left_out, pooled_ratio=float(np.exp(est)), interval=ci, interval_level=0.975 if primary else 0.95,
                           reading=reading(ci) if (c1, c2) == ("moral", "norm") else None, primary=bool(primary)))
for fr, (c1, c2) in itertools.product(frames, CONTRASTS):
    rr = [r for r in per_model if r.get("p_perm") is not None and r["frame"] == fr and r["contrast"] == f"{c1}/{c2}"]
    for r, q in zip(rr, bh([r["p_perm"] for r in rr]) if rr else []): r["q_bh_across_models"] = float(q)


h4 = []
for fr in frames:
    for b_, i_ in PAIRS:
        if b_ not in DATA or i_ not in DATA or fr not in DATA[b_] or fr not in DATA[i_]: continue
        prof = {}
        for m in (b_, i_):
            d = DATA[m][fr]; ok = OK[(m, fr)] & GROUP["moral"]; S_ = d["E"][ok] / d["E"][ok].sum(1, keepdims=True); rel = []
            for _ in range(100):
                p = rng.permutation(len(S_)); h = len(S_) // 2; r = np.corrcoef(S_[p[:h]].mean(0), S_[p[h:]].mean(0))[0, 1]; rel.append(2 * r / (1 + r))
            prof[m] = (S_.mean(0), float(np.mean(rel)), int(ok.sum()))
        if min(prof[b_][2], prof[i_][2]) < a.min_items: continue
        top = head_index(b_, "located_top1")[0]; rank = int(np.where(np.argsort(-prof[i_][0]) == top)[0][0]) + 1; r_ = float(np.corrcoef(prof[b_][0], prof[i_][0])[0, 1])
        h4.append(dict(frame=fr, base=b_, instruct=i_, r_profile=r_, reliability_base=prof[b_][1], reliability_instruct=prof[i_][1], n_base=prof[b_][2], n_instruct=prof[i_][2], rank_of_base_top_head_in_instruct=rank, meets_prediction=bool(r_ >= 0.8 and rank <= 10)))


rob = []
for m in models:
    for fr in frames:
        if (m, fr, a.headset) not in SHARE or "norm" not in GROUP: continue
        sh, ok = SHARE[(m, fr, a.headset)], OK[(m, fr)]; sel = ok & (GROUP["moral"] | GROUP["norm"])
        if (sel & GROUP["moral"]).sum() < a.min_items or (sel & GROUP["norm"]).sum() < a.min_items: continue
        d = DATA[m][fr]; its = [ITEMS[k] for k in np.where(sel)[0]]; v = np.clip(sh[sel], 1e-6, 1 - 1e-6); y = np.log(v / (1 - v)); ismoral = GROUP["moral"][sel].astype(float); nt = f"{family(m)}_ntok"
        tts = sorted({i.get("template_type", "NA") for i in its})
        X = [np.ones(len(its)), ismoral, np.log(d["gap"][sel]), np.array([i.get(nt, i.get("llama_ntok", 0)) for i in its], float), np.array([i.get("llama_after_edit", 0) for i in its], float)]
        X += [np.array([i.get("template_type", "NA") == t for i in its], float) for t in tts[1:]]; X = np.stack(X, 1); X[:, 2:] -= X[:, 2:].mean(0)
        beta = np.linalg.lstsq(X, y, rcond=None)[0]; i1, i0 = np.where(ismoral == 1)[0], np.where(ismoral == 0)[0]; bs = []
        for _ in range(a.boot):
            k = np.concatenate([rng.choice(i1, len(i1)), rng.choice(i0, len(i0))]); bs.append(np.linalg.lstsq(X[k], y[k], rcond=None)[0][1])
        rec = dict(model=m, frame=fr, adj_logit_difference_moral_minus_norm=float(beta[1]), ci95=[float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))], unadjusted=float(y[ismoral == 1].mean() - y[ismoral == 0].mean()))
        def matched(strata):
            num = den = 0.0
            for s_ in np.unique(strata[np.isfinite(strata)]):
                x1, x0 = sh[sel][(strata == s_) & (ismoral == 1)], sh[sel][(strata == s_) & (ismoral == 0)]
                if len(x1) and len(x0): w = min(len(x1), len(x0)); num += w * x1.mean(); den += w * x0.mean()
            return float(num / den) if den else None
        g = np.log(d["gap"][sel]); rec["gap_matched_ratio"] = matched(np.clip(np.digitize(g, np.quantile(g, [.2, .4, .6, .8])), 0, 4).astype(float))
        rec["rated_size_matched_ratio"] = matched(np.array([i.get("median_size", np.nan) if i.get("median_size") is not None else np.nan for i in its], float))
        E = d["E"]; tot = np.nansum(E, 1); Sh = E / np.where(tot > 0, tot, 1)[:, None]; mi, ni = np.where(ok & GROUP["moral"])[0], np.where(ok & GROUP["norm"])[0]; rs, rn = [], []
        for _ in range(200):
            p = rng.permutation(mi); h = len(p) // 2; top = np.argsort(-Sh[p[:h]].mean(0))[:10]; rs.append(Sh[p[h:]][:, top].sum(1).mean() / Sh[ni][:, top].sum(1).mean())
            q = rng.permutation(ni); h = len(q) // 2; top = np.argsort(-Sh[q[:h]].mean(0))[:10]; rn.append(Sh[q[h:]][:, top].sum(1).mean() / Sh[mi][:, top].sum(1).mean())
        sm = lambda r: dict(mean=float(np.mean(r)), p2_5=float(np.percentile(r, 2.5)), p97_5=float(np.percentile(r, 97.5)))
        rec["split_half_moral_selected_moral_over_norm"] = sm(rs); rec["split_half_norm_selected_norm_over_moral"] = sm(rn)
        raw_m, raw_n = E[ok & GROUP["moral"]].mean(0), E[ok & GROUP["norm"]].mean(0); hi_ = head_index(m, a.headset)
        rec["raw_effect_ratio_headset"] = float(raw_m[hi_].mean() / raw_n[hi_].mean()); rec["raw_effect_ratio_all_heads_background"] = float(raw_m.mean() / raw_n.mean()); rob.append(rec)

summary = dict(settings=vars(a), all_options_at_default=OPTIONS_DEFAULT, accepted_pairs=PRIMARY_SET, primary_analysis=IS_DEFAULT, n_items=N, items_by_group={g: int(mk.sum()) for g, mk in GROUP.items()}, models=models, frames=frames, pooled=pooled, base_to_instruct=h4)
json.dump(summary, open(os.path.join(a.out, "summary.json"), "w"), indent=1); json.dump(per_model, open(os.path.join(a.out, "per_model.json"), "w"), indent=1)
json.dump(behav, open(os.path.join(a.out, "behaviour.json"), "w"), indent=1); json.dump(rob, open(os.path.join(a.out, "robustness.json"), "w"), indent=1)
L = [f"# Head results ({a.condition}, readout {a.readout}, head set {a.headset}, items: {a.subset}, inclusion gap >= {a.tau})", ""] + (["**Run with --any-items (synthetic data): this is not an analysis of the study.**", ""] if a.any_items else []) + [
     ("All options are at their defaults and " + PRIMARY_WHY + ": the moral/norm rows for frames A1 and B are the two primary tests (97.5 % intervals)." if IS_DEFAULT else
      "**Sensitivity run (" + ("an option differs from the default" if not OPTIONS_DEFAULT else "") + ("; " if not OPTIONS_DEFAULT and not PRIMARY_SET else "") + (PRIMARY_WHY if not PRIMARY_SET else "") + "): nothing here is a primary test; all intervals are 95 %.**"), "",
     "## Pooled ratios (mean over models of the log ratio; item bootstrap shared across models)", "", "| frame | contrast | models used | left out | pooled ratio | interval | reading |", "|---|---|---|---|---|---|---|"]
for p in pooled:
    if p["headset"] == a.headset: L.append(f"| {p['frame']} | {p['contrast']}{' (primary)' if p['primary'] else ''} | {p['n_models']} | {', '.join(p['models_left_out']) or '-'} | {p['pooled_ratio']:.2f} | {p['interval'][0]:.2f} to {p['interval'][1]:.2f} ({100 * p['interval_level']:.1f} %) | {p['reading'] or ''} |")
L += ["", "Other head sets, moral / norm: " + "; ".join(f"{p['frame']} {p['headset']} {p['pooled_ratio']:.2f} ({p['interval'][0]:.2f} to {p['interval'][1]:.2f})" for p in pooled if p["headset"] != a.headset and p["contrast"] == "moral/norm")]
for c1, c2 in CONTRASTS[:3]:
    L += ["", f"## Per model, {c1} / {c2}", "", f"| model | frame | n {c1} | n {c2} | share {c1} | share {c2} | uniform | ratio | 95 % CI | p | q (BH over models) |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in per_model:
        if r["headset"] == a.headset and r["contrast"] == f"{c1}/{c2}":
            L.append(f"| {r['model']} | {r['frame']} | {r['n1']} | {r['n2']} | " + (f"{r['mean_share_1']:.3f} | {r['mean_share_2']:.3f} | {r['uniform_share']:.3f} | {r['ratio']:.2f} | {r['ci95'][0]:.2f} to {r['ci95'][1]:.2f} | {fmt(r['p_perm'], '{:.4f}')} | {fmt(r.get('q_bh_across_models'), '{:.4f}')} |" if "ratio" in r else f"{r['note']} | | | | | | |"))
L += ["", "## Base to instruct (moral items)", "", "| frame | pair | r | reliability base / instruct | rank of base top head | prediction met |", "|---|---|---|---|---|---|"]
for h in h4: L.append(f"| {h['frame']} | {h['base']} | {h['r_profile']:.3f} | {h['reliability_base']:.3f} / {h['reliability_instruct']:.3f} | {h['rank_of_base_top_head_in_instruct']} | {h['meets_prediction']} |")
L += ["", "## Robustness (moral vs norm)", "", "The last two columns select ten heads on half of the NEW items and test on the other half. If heads chosen on norm items show the same ratio in the other direction, a ratio above 1 only says that the two profiles differ.", "",
      "| model | frame | adjusted logit difference (95 % CI) | unadjusted | gap-matched | rated-size-matched | raw ratio: head set / all heads | moral-selected: moral / norm | norm-selected: norm / moral |", "|---|---|---|---|---|---|---|---|---|"]
for r in rob:
    s1, s2 = r["split_half_moral_selected_moral_over_norm"], r["split_half_norm_selected_norm_over_moral"]
    L.append(f"| {r['model']} | {r['frame']} | {r['adj_logit_difference_moral_minus_norm']:+.3f} ({r['ci95'][0]:+.3f} to {r['ci95'][1]:+.3f}) | {r['unadjusted']:+.3f} | {fmt(r['gap_matched_ratio'])} | {fmt(r['rated_size_matched_ratio'])} | {r['raw_effect_ratio_headset']:.2f} / {r['raw_effect_ratio_all_heads_background']:.2f} | {s1['mean']:.2f} ({s1['p2_5']:.2f} to {s1['p97_5']:.2f}) | {s2['mean']:.2f} ({s2['p2_5']:.2f} to {s2['p97_5']:.2f}) |")
L += ["", "## Behaviour", "", "| model | frame | category | run | included | mean gap | correct sign | mean mass |", "|---|---|---|---|---|---|---|---|"]
for b in behav: L.append(f"| {b['model']} | {b['frame']} | {b['category']} | {b['n_run']} | {b['n_included']} | {fmt(b['mean_gap'], '{:+.3f}')} | {fmt(b['share_correct_sign'])} | {fmt(b['mean_mass'])} |")
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L[:16]))
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    fs = [f for f in frames if f in ("A1", "B")] or frames[:1]; fig, axes = plt.subplots(1, len(fs), figsize=(4.6 * len(fs), 0.35 * len(models) + 1.8), sharey=True, squeeze=False)
    for ax, fr in zip(axes[0], fs):
        rr = [r for r in per_model if r["headset"] == a.headset and r["contrast"] == "moral/norm" and r["frame"] == fr and "ratio" in r]
        for k, r in enumerate(rr): ax.plot(r["ci95"], [k, k], color="#444"); ax.plot(r["ratio"], k, "o", color="#1f5fa8")
        ax.axvline(1, color="k", lw=.8); ax.axvspan(0.8, 1.25, color="#ddd", alpha=.5); ax.set_yticks(range(len(rr))); ax.set_yticklabels([r["model"] for r in rr]); ax.set_xscale("log"); ax.set_title(f"frame {fr}: share ratio moral / norm"); ax.set_xlabel("ratio (log scale)")
        lo_, hi_ = ax.get_xlim(); tk = [t for t in (0.25, 0.5, 0.8, 1, 1.25, 1.5, 2, 3, 4, 6, 8) if lo_ <= t <= hi_]; ax.set_xticks(tk); ax.set_xticklabels([str(t) for t in tk]); ax.minorticks_off()
    fig.tight_layout(); fig.savefig(os.path.join(a.out, "forest_moral_vs_norm.pdf")); fig.savefig(os.path.join(a.out, "forest_moral_vs_norm.png"), dpi=150)
except Exception as e: print("[figure skipped]", e)
