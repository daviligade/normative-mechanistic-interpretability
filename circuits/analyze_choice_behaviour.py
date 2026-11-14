"""The models' answers in the choice frame and its control."""
import argparse, glob, json, os, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--runs", nargs="+", default=["runs/circuits_choice", "runs/circuits_choice_word"]); ap.add_argument("--items", default="stimuli/items_final.json")
ap.add_argument("--out", default="results/choice_behaviour"); ap.add_argument("--tau-ld", type=float, default=0.1); ap.add_argument("--all-ids", action="store_true", help="software tests: take every file, whatever its id")
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
ITEMS = {i["id"]: i for i in json.load(open(a.items)) if i.get("accepted", True)}
ORDER = ["Llama-3.2-1B", "Llama-3.2-1B-Instruct", "gemma-2b", "gemma-2b-it", "Llama-3.2-3B", "Llama-3.2-3B-Instruct", "Qwen2.5-3B", "Qwen2.5-3B-Instruct", "Qwen2.5-7B", "Qwen2.5-7B-Instruct",
         "Llama-3.1-8B", "Llama-3.1-8B-Instruct", "Qwen2.5-14B", "Qwen2.5-14B-Instruct"]
NAME = {"CH": "choice", "CW": "control (word)"}; GROUPS = ("all", "moral", "norm", "descr"); rows = []
for runs in a.runs:
    folders = sorted(glob.glob(os.path.join(runs, "ablation", "*/")), key=lambda p: (ORDER.index(os.path.basename(p.rstrip("/"))) if os.path.basename(p.rstrip("/")) in ORDER else 99, p))
    for folder in folders:
        model = os.path.basename(folder.rstrip("/")); per = {}
        for f in sorted(glob.glob(os.path.join(folder, "*__*.npz"))):
            b = os.path.basename(f)
            if b.endswith(".tmp.npz") or b.startswith("means__"): continue
            frame, iid = b[:-4].split("__", 1)
            if not (iid in ITEMS or a.all_ids): continue
            z = np.load(f, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
            per.setdefault(frame, []).append((meta.get("category"), float(z["perm_base_LD"]), float(z["rest_base_LD"]), float(z["perm_base_mass"]), float(z["rest_base_mass"])))
        for frame, v in sorted(per.items()):
            cat = np.array([x[0] for x in v]); p, r, mp, mr = (np.array([x[k] for x in v]) for k in (1, 2, 3, 4)); gap = p - r
            for g in GROUPS:
                mk = np.ones(len(v), bool) if g == "all" else cat == g
                if not mk.any(): continue
                rows.append(dict(model=model, frame=frame, group=g, n=int(mk.sum()), mass=float(np.mean(np.r_[mp[mk], mr[mk]])), answers_A=float(np.mean(np.r_[p[mk] > 0, r[mk] > 0])),
                                 gap_positive=float(np.mean(gap[mk] > 0)), gap_included=float(np.mean(gap[mk] >= a.tau_ld)), expected_in_both_orders=float(np.mean((p[mk] > 0) & (r[mk] < 0))),
                                 median_gap=float(np.median(gap[mk])), mean_gap=float(np.mean(gap[mk]))))
if not rows: sys.exit(f"no removal file of the choice frame under {a.runs}")
json.dump(dict(settings=vars(a), note="exploratory", rows=rows), open(os.path.join(a.out, "summary.json"), "w"), indent=1)
L = ["# The choice frame: what the models answer", "",
     "LD = logit(A) - logit(B). Gap of a pair = LD(prompt whose expected answer is A) - LD(prompt whose expected answer is B).",
     f"Choice (CH): the expected answer is the better version. Control (CW): the expected answer is the option that holds the word, which is the worse version. A pair is included in the removal analysis when its gap is at least {a.tau_ld}.", ""]
for frame in sorted({r["frame"] for r in rows}):
    L += [f"## {frame}: {NAME.get(frame, frame)}", "", "### All pairs", "", "| model | pairs | probability on A and B | answers A | gap above 0 | gap at least %.1f | expected label in both orders | median gap |" % a.tau_ld, "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["frame"] == frame and r["group"] == "all": L.append(f"| {r['model']} | {r['n']} | {r['mass']:.2f} | {100 * r['answers_A']:.0f} % | {100 * r['gap_positive']:.0f} % | {100 * r['gap_included']:.0f} % | {100 * r['expected_in_both_orders']:.0f} % | {r['median_gap']:+.2f} |")
    rr = [r for r in rows if r["frame"] == frame and r["group"] == "all"]
    L += ["", f"Median over the {len(rr)} models: gap above 0 in {100 * np.median([r['gap_positive'] for r in rr]):.0f} % of the pairs, expected label in both orders in {100 * np.median([r['expected_in_both_orders'] for r in rr]):.0f} %, "
              f"probability on the two labels {np.median([r['mass'] for r in rr]):.2f}; gap above 0 in more than half of the pairs in {sum(r['gap_positive'] > 0.5 for r in rr)} of {len(rr)} models.", "",
          "### By kind of pair (share of pairs with a gap above 0; median gap)", "", "| model | moral | normative | descriptive |", "|---|---|---|---|"]
    for m in dict.fromkeys(r["model"] for r in rr):
        c = {r["group"]: r for r in rows if r["frame"] == frame and r["model"] == m}
        L.append(f"| {m} | " + " | ".join(f"{100 * c[g]['gap_positive']:.0f} % ({c[g]['median_gap']:+.2f}; n = {c[g]['n']})" if g in c else "-" for g in ("moral", "norm", "descr")) + " |")
    L.append("")
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))
