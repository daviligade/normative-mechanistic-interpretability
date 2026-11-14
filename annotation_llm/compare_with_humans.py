"""Compares the language models with the annotators (alternative annotator test)."""
import argparse, collections, csv, hashlib, itertools, json, math, os, statistics as st
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--llm", required=True, help="output folder of llm_annotate.py run on stimuli/items_calibration_242.json")
ap.add_argument("--items", default="stimuli/items_calibration_242.json")
ap.add_argument("--human-long", nargs="+", default=["ratings/ratings_long.csv", "ratings/ratings_long_round2.csv"])
ap.add_argument("--human-items", nargs="+", default=["ratings/ratings_items.csv", "ratings/ratings_items_round2.csv"])
ap.add_argument("--out", default="results/llm_calibration")
ap.add_argument("--eps", type=float, default=0.1); ap.add_argument("--q", type=float, default=0.05)
ap.add_argument("--boot", type=int, default=5000); ap.add_argument("--seed", type=int, default=20261025)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)

KINDS = ["moral", "prudential", "etiquette", "aesthetic", "epistemic"]; LETTERS = "MPEAK"; NONMORAL = set("PEAK")
ITEMS = {i["id"]: i for i in json.load(open(a.items))}; IDS = list(ITEMS)
INTENDED_CLASS = {"moral": "M", "norm": "norm", "descr": "N"}


def cls4_of(std, tie):
    if std is None: return None
    if std in ("M", "N"): return std
    if std in NONMORAL or (std == "T" and tie and set(tie) <= NONMORAL): return "norm"
    return "mixed"


def finish(better, judged, std, tie, grades, unclear):
    return dict(better=better, judged=judged, std=std, tie=tie, cls4=cls4_of(std, tie), moral=grades["M"], grades=grades, unclear=bool(unclear))


H, HA = collections.defaultdict(dict), collections.defaultdict(dict)
for path in a.human_long:
    for r in csv.DictReader(open(path)):
        if r["item_id"] not in ITEMS: raise SystemExit(f"{path}: item {r['item_id']} is not in {a.items}")
        if r.get("scored", "1") != "1": continue
        HA[r["rater"]][r["item_id"]] = dict(better=r["better"] or None, std=r["standard"] or None, moral=int(r["gM"]) if r["gM"] not in ("", None) else None)
        if r["complete"] != "True": H[r["rater"]][r["item_id"]] = None; continue
        g = {L: int(r["g" + L]) for L in LETTERS}
        H[r["rater"]][r["item_id"]] = finish(r["better"], r["judged"], r["standard"], r["tie"], g, r["unclear"] == "True")
RATERS = sorted(H); assert len(RATERS) >= 3 and all(set(H[h]) == set(ITEMS) for h in RATERS), "every rater must have rated every pair"
OFFICIAL = {}
for path in a.human_items:
    for r in csv.DictReader(open(path)): OFFICIAL[r["id"]] = r["accepted"] == "True"
assert set(OFFICIAL) == set(ITEMS), "the panel's decisions do not cover the 242 pairs"


def num(v):
    if isinstance(v, bool) or v is None: return 0
    if isinstance(v, (int, float)): return v
    try: return float(str(v).strip())
    except ValueError: return 0

MODELS, M_ANS, M_NAMES = [], {}, {}
for r in ("anthropic", "openai", "google"):
    p = os.path.join(a.llm, f"answers_{r}.json")
    if not os.path.exists(p): continue
    MODELS.append(r); d = json.load(open(p)); M_ANS[r] = {}
    for i in IDS:
        x = d.get(i)
        if not x or not x.get("parsed"): M_ANS[r][i] = None; continue
        q, side = x["parsed"], int(x["side"]); M_NAMES[r] = x.get("model", r)
        better = "none" if q["q1"] == 0 else ("perm" if q["q1"] == side else "rest")
        if q["q3"] == "N": g = {L: 0 for L in LETTERS}; std, tie = "N", ""
        else:
            g = {LETTERS[k]: num(q.get(kind)) for k, kind in enumerate(KINDS)}; mx = max(g.values()); tops = [L for L in LETTERS if g[L] == mx]
            std = "N" if mx == 0 else (tops[0] if len(tops) == 1 else "T"); tie = "".join(tops) if std == "T" else ""
        M_ANS[r][i] = finish(better, q["q3"], std, tie, g, q.get("unclear", False))
assert len(MODELS) >= 1, f"no answers_*.json in {a.llm}"


def class_ok(it, x): return x["cls4"] == INTENDED_CLASS[it["category"]]


def accept(it, recs):
    R = len(recs); need = math.ceil(2 * R / 3)
    if any(x is None for x in recs): return False
    med = st.median([x["moral"] for x in recs]); moral_ok = med >= 2 if it["category"] == "moral" else med <= 1
    return (sum(x["better"] == "perm" for x in recs) >= need and sum(class_ok(it, x) for x in recs) >= need and moral_ok
            and sum(x["unclear"] for x in recs) < math.ceil(R / 2))


def verdict(it, x):
    if x is None: return None
    moral_ok = x["moral"] >= 2 if it["category"] == "moral" else x["moral"] <= 1
    return int(x["better"] == "perm" and class_ok(it, x) and moral_ok and not x["unclear"])


mism = [i for i in IDS if accept(ITEMS[i], [H[h][i] for h in RATERS]) != OFFICIAL[i]]
assert not mism, f"the rule as written here does not reproduce the panel's decisions for {mism}"
AI_DEC = {i: accept(ITEMS[i], [M_ANS[m][i] for m in MODELS]) for i in IDS}
llm_items = os.path.join(a.llm, "items_llm.json"); script_check = "not available"
if os.path.exists(llm_items) and len(MODELS) == 3:
    S = {x["id"]: bool(x["accepted"]) for x in json.load(open(llm_items))}; bad = [i for i in IDS if S.get(i) != AI_DEC[i]]
    assert not bad, f"the rule as written here disagrees with llm_annotate.py on {bad}"; script_check = "identical on all pairs"


def betacf(p, q, x):
    tiny = 1e-300; qab, qap, qam = p + q, p + 1, p - 1; c = 1.0; d = 1 - qab * x / qap; d = tiny if abs(d) < tiny else d; d = 1 / d; h = d
    for m in range(1, 400):
        m2 = 2 * m; aa = m * (q - m) * x / ((qam + m2) * (p + m2))
        d = 1 + aa * d; d = tiny if abs(d) < tiny else d; c = 1 + aa / c; c = tiny if abs(c) < tiny else c; d = 1 / d; h *= d * c
        aa = -(p + m) * (qab + m) * x / ((p + m2) * (qap + m2))
        d = 1 + aa * d; d = tiny if abs(d) < tiny else d; c = 1 + aa / c; c = tiny if abs(c) < tiny else c; d = 1 / d; de = d * c; h *= de
        if abs(de - 1) < 1e-15: break
    return h


def betai(p, q, x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    bt = math.exp(math.lgamma(p + q) - math.lgamma(p) - math.lgamma(q) + p * math.log(x) + q * math.log(1 - x))
    return bt * betacf(p, q, x) / p if x < (p + 1) / (p + q + 2) else 1 - bt * betacf(q, p, 1 - x) / q


def t_cdf(t, df):
    tail = 0.5 * betai(df / 2, 0.5, df / (df + t * t)); return tail if t < 0 else 1 - tail


def by_reject(pvals, q):
    m = len(pvals); c = sum(1 / k for k in range(1, m + 1)); order = sorted(range(m), key=lambda k: pvals[k]); kmax = 0
    for rank, k in enumerate(order, 1):
        if pvals[k] <= rank * q / (m * c): kmax = rank
    rej = [False] * m
    for rank, k in enumerate(order, 1): rej[k] = rank <= kmax
    return rej


def alt_test(cand, humans, ordinal=False):
    per = {}
    for j in humans:
        others = [h for h in humans if h != j]; Wf, Wh = [], []
        for i in IDS:
            f, hj = cand.get(i), humans[j].get(i); os_ = [humans[h][i] for h in others if humans[h].get(i) is not None]
            if f is None or hj is None or not os_: continue
            if ordinal: sf, sj = -sum(abs(f - o) for o in os_), -sum(abs(hj - o) for o in os_)
            else: sf, sj = sum(f == o for o in os_), sum(hj == o for o in os_)
            Wf.append(int(sf >= sj)); Wh.append(int(sj >= sf))
        d = np.array(Wh, float) - np.array(Wf, float); n = len(d); md = float(d.mean()); sd = float(d.std(ddof=1)) if n > 1 else 0.0
        p = (0.0 if md < a.eps else 1.0) if sd == 0 else t_cdf((md - a.eps) / (sd / math.sqrt(n)), n - 1)
        per[j] = dict(n=n, rho_f=round(float(np.mean(Wf)), 4), rho_h=round(float(np.mean(Wh)), 4), p=p)
    rej = by_reject([per[j]["p"] for j in humans], a.q)
    for j, r_ in zip(humans, rej): per[j]["rejected"] = bool(r_)
    omega = sum(rej) / len(humans)
    return dict(omega=omega, passed=omega >= 0.5, AP=round(float(np.mean([per[j]["rho_f"] for j in humans])), 4), per_rater=per)


LABELS = {"class": (lambda it, x: None if x is None else x["cls4"], False), "better": (lambda it, x: None if x is None else x["better"], False),
          "class_fine": (lambda it, x: None if x is None else x["std"], False), "moral_rating": (lambda it, x: None if x is None else x["moral"], True),
          "verdict": (lambda it, x: verdict(it, x), False)}
PRIMARY = ("class", "better", "verdict")
lab = lambda name, src: {i: LABELS[name][0](ITEMS[i], src[i]) for i in IDS}
ALT = {m: {name: alt_test(lab(name, M_ANS[m]), {h: lab(name, H[h]) for h in RATERS}, LABELS[name][1]) for name in LABELS} for m in MODELS}
ALT_H = {c: {name: alt_test(lab(name, H[c]), {h: lab(name, H[h]) for h in RATERS if h != c}, LABELS[name][1]) for name in LABELS} for c in RATERS}
all_pass = len(MODELS) == 3 and all(ALT[m][name]["passed"] for m in MODELS for name in PRIMARY)


def agree_kappa(x, y):
    x, y = np.array(x, float), np.array(y, float); po = float((x == y).mean()); pe = float(x.mean() * y.mean() + (1 - x.mean()) * (1 - y.mean()))
    return po, (po - pe) / (1 - pe) if pe < 1 else float("nan")


off = [OFFICIAL[i] for i in IDS]; ai = [AI_DEC[i] for i in IDS]
conf = collections.Counter((OFFICIAL[i], AI_DEC[i]) for i in IDS); po_ai, k_ai = agree_kappa(ai, off)
panels3 = []
for S3 in itertools.combinations(RATERS, 3):
    dec = [accept(ITEMS[i], [H[h][i] for h in S3]) for i in IDS]; po, k = agree_kappa(dec, off)
    panels3.append(dict(raters="".join(h[-1] for h in S3), agree=po, kappa=k, accepted=sum(dec), kept_of_dropped=sum(d_ and not o for d_, o in zip(dec, off)),
                        dropped_of_kept=sum(o and not d_ for d_, o in zip(dec, off))))
A_s, H_s, splits = [], [], []
for S3 in itertools.combinations(RATERS, 3):
    ref2 = [h for h in RATERS if h not in S3]
    ref = np.array([accept(ITEMS[i], [H[h][i] for h in ref2]) for i in IDS]); h3 = np.array([accept(ITEMS[i], [H[h][i] for h in S3]) for i in IDS])
    A_s.append((np.array(ai) == ref).astype(float)); H_s.append((h3 == ref).astype(float))
    splits.append(dict(panel="".join(h[-1] for h in S3), reference="".join(h[-1] for h in ref2), ref_accepts=int(ref.sum()), models_agree=float(A_s[-1].mean()), raters_agree=float(H_s[-1].mean())))
dif_i = (np.array(A_s) - np.array(H_s)).mean(0); rng = np.random.default_rng(a.seed)
boot = np.array([dif_i[rng.integers(0, len(IDS), len(IDS))].mean() for _ in range(a.boot)])
split_cmp = dict(models=float(np.mean([s["models_agree"] for s in splits])), raters=float(np.mean([s["raters_agree"] for s in splits])),
                 diff=float(dif_i.mean()), ci95=[float(np.percentile(boot, 2.5)), float(np.percentile(boot, 97.5))])


def kripp_alpha(units, metric):
    units = [u for u in units if len(u) >= 2]; vals = sorted({v for u in units for v in u}); idx = {v: i for i, v in enumerate(vals)}; K = len(vals)
    if K < 2: return float("nan")
    o = [[0.0] * K for _ in range(K)]
    for u in units:
        m = len(u)
        for x in range(m):
            for y in range(m):
                if x != y: o[idx[u[x]]][idx[u[y]]] += 1.0 / (m - 1)
    n_c = [sum(o[c]) for c in range(K)]; n = sum(n_c)
    def d2(c, k):
        if c == k: return 0.0
        if metric == "nominal": return 1.0
        lo, hi = min(c, k), max(c, k); return (sum(n_c[lo:hi + 1]) - (n_c[lo] + n_c[hi]) / 2.0) ** 2
    Do = sum(o[c][k] * d2(c, k) for c in range(K) for k in range(K)); De = sum(n_c[c] * n_c[k] * d2(c, k) for c in range(K) for k in range(K)) / (n - 1)
    return 1.0 - Do / De if De > 0 else float("nan")


flip = {i: int(hashlib.sha256(i.encode()).hexdigest(), 16) % 2 for i in IDS}
ALPHA_DEF = {"better option (nominal)": (lambda i, x: None if x is None or x.get("better") is None else (0 if x["better"] == "none" else (1 if (x["better"] == "perm") ^ bool(flip[i]) else 2)), "nominal"),
             "class of standard, all letters incl. ties (nominal)": (lambda i, x: None if x is None else x.get("std"), "nominal"),
             "class M / non-moral norm / N, ties left out (nominal)": (lambda i, x: None if x is None or x.get("std") in (None, "T") else ("norm" if x["std"] in NONMORAL else x["std"]), "nominal"),
             "class as the rule reads it (M / norm / N / mixed; nominal)": (lambda i, x: None if x is None else cls4_of(x.get("std"), x.get("tie")), "nominal"),
             "moral rating (ordinal 0-3)": (lambda i, x: None if x is None else x.get("moral"), "ordinal")}
for h in RATERS:
    for i in IDS: HA[h][i]["tie"] = H[h][i]["tie"] if H[h][i] else ""
def alpha_for(sources, ids=IDS):
    return {name: kripp_alpha([[v for v in (f(i, s[i]) for s in sources) if v is not None] for i in ids], metric) for name, (f, metric) in ALPHA_DEF.items()}
alphas = {"the five raters": alpha_for([HA[h] for h in RATERS])}
for m in MODELS: alphas[f"the five raters + {m}"] = alpha_for([HA[h] for h in RATERS] + [M_ANS[m]])
if len(MODELS) > 1: alphas["the five raters + all models"] = alpha_for([HA[h] for h in RATERS] + [M_ANS[m] for m in MODELS])
alphas["the models only"] = alpha_for([M_ANS[m] for m in MODELS]) if len(MODELS) > 1 else {}
main_ids = [i for i in IDS if i in {r["item_id"] for r in csv.DictReader(open(a.human_long[0]))}]
alpha_main_check = alpha_for([HA[h] for h in RATERS], main_ids)


maj = lambda labels: (lambda c: c[0][0] if c and c[0][1] >= 3 else None)(collections.Counter(v for v in labels if v is not None).most_common(1))
rows = []
for i in IDS:
    it = ITEMS[i]; hc = maj([H[h][i]["cls4"] if H[h][i] else None for h in RATERS])
    rows.append(dict(id=i, category=it["category"], subtype=it.get("subtype"), panel_accepted=OFFICIAL[i], models_accepted=AI_DEC[i], raters_class_majority=hc,
                     raters_classes="".join(sorted((H[h][i]["std"] if H[h][i] else "-") for h in RATERS)),
                     **{f"{m}_class": (M_ANS[m][i]["cls4"] if M_ANS[m][i] else None) for m in MODELS}, **{f"{m}_better": (M_ANS[m][i]["better"] if M_ANS[m][i] else None) for m in MODELS}))
with open(os.path.join(a.out, "pairs.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
n_better = collections.Counter(x["better"] for h in RATERS for x in HA[h].values() if x["better"])


fmt = lambda v: "n/a" if v is None or (isinstance(v, float) and math.isnan(v)) else f"{v:.3f}"
L = ["# AI annotators checked against the human panel (242 pairs of the main study)", "",
     f"Models: {', '.join(f'{m} ({M_NAMES.get(m, m)})' for m in MODELS)}; raters: {', '.join(RATERS)}. Pairs: {len(IDS)} "
     f"({sum(1 for i in IDS if ITEMS[i]['category'] == 'moral')} moral, {sum(1 for i in IDS if ITEMS[i]['category'] == 'norm')} norm, {sum(1 for i in IDS if ITEMS[i]['category'] == 'descr')} descriptive). "
     f"Answers parsed: " + ", ".join(f"{m} {sum(1 for i in IDS if M_ANS[m][i])}" for m in MODELS) + ".", "",
     f"Checks: the rule as written here reproduces the panel's decisions on all {len(IDS)} pairs, and llm_annotate.py's decisions for the models: {script_check}. "
     f"Agreement of the raters on the main round, recomputed here (must equal the main rating report): " + ", ".join(f"{k} {fmt(v)}" for k, v in alpha_main_check.items()) + ".", "",
     "## Primary: the alternative annotator test", "",
     f"eps = {a.eps}, one-sided paired t-tests, Benjamini-Yekutieli over the {len(RATERS)} raters at q = {a.q}; a model passes a label when it wins against at least half of the raters (omega >= 0.5).", "",
     "| model | label | omega (raters won) | passed | average advantage probability | per rater: rho_model / rho_rater (won?) |", "|---|---|---|---|---|---|"]
for m in MODELS:
    for name in LABELS:
        r_ = ALT[m][name]
        L.append(f"| {m} | {name}{' (primary)' if name in PRIMARY else ''} | {r_['omega']:.1f} | {'yes' if r_['passed'] else 'no'} | {r_['AP']:.3f} | "
                 + "; ".join(f"{h} {v['rho_f']:.2f}/{v['rho_h']:.2f} ({'won' if v['rejected'] else 'not won'})" for h, v in r_["per_rater"].items()) + " |")
L += ["", ("**Outcome: all three models pass all three primary labels.** The follow-up sets are reported as annotated by the three models, checked against "
           "the human panel by this test." if all_pass else
           "**Outcome: not every model passes all three primary labels.** The follow-up results are reported only with the outcome of this check next to them, "
           "and none of them enters the abstract, the introduction or the conclusion."), "",
      "How one of our raters fares in the same test against the other four (context; omega with four raters):", "",
      "| rater | " + " | ".join(LABELS) + " |", "|---|" + "---|" * len(LABELS)]
for c in RATERS: L.append(f"| {c} | " + " | ".join(f"omega {ALT_H[c][n]['omega']:.2f}, AP {ALT_H[c][n]['AP']:.3f}" for n in LABELS) + " |")
L += ["", "## Keep-or-drop decisions", "",
      f"The three models as a panel (two of three, the study's rule) against the five raters' decisions: agreement {po_ai:.3f}, Cohen's kappa {fmt(k_ai)}. "
      f"Both keep {conf[(True, True)]}, only the raters keep {conf[(True, False)]}, only the models keep {conf[(False, True)]}, both drop {conf[(False, False)]} "
      f"(the raters drop {sum(not v for v in off)} of {len(IDS)}).", "",
      "Three of the five raters as a panel, same rule, against the five raters' decisions (they are part of that panel, so this favours them):", "",
      f"| panel | agreement | kappa | keeps, of the {sum(not v for v in off)} the five dropped | drops, of the {sum(off)} the five kept |", "|---|---|---|---|---|"]
L += [f"| raters {p['raters']} | {p['agree']:.3f} | {fmt(p['kappa'])} | {p['kept_of_dropped']} | {p['dropped_of_kept']} |" for p in panels3]
L += [f"| the three models | {po_ai:.3f} | {fmt(k_ai)} | {conf[(False, True)]} | {conf[(True, False)]} |", "",
      f"Models and raters judged against the same reference (each of the ten splits of the raters into three and two; the reference is the other two "
      f"raters under the study's rule for two raters, i.e. both): mean agreement of the models {split_cmp['models']:.3f}, of the three raters "
      f"{split_cmp['raters']:.3f}; difference {split_cmp['diff']:+.3f} (95 % bootstrap interval over pairs {split_cmp['ci95'][0]:+.3f} to {split_cmp['ci95'][1]:+.3f}).", "",
      "| split: panel / reference | reference keeps | models agree | three raters agree |", "|---|---|---|---|"]
L += [f"| {s['panel']} / {s['reference']} | {s['ref_accepts']} | {s['models_agree']:.3f} | {s['raters_agree']:.3f} |" for s in splits]
L += ["", "By category (kept by the raters / by the models): " + "; ".join(
    f"{c} {sum(1 for i in IDS if ITEMS[i]['category'] == c and OFFICIAL[i])} / {sum(1 for i in IDS if ITEMS[i]['category'] == c and AI_DEC[i])} of {sum(1 for i in IDS if ITEMS[i]['category'] == c)}"
    for c in ("moral", "norm", "descr")) + ".", "",
      "Pairs whose class the models read differently from a majority of the raters (at least three of five): " + "; ".join(
    f"{m} {sum(1 for r_ in rows if r_['raters_class_majority'] and r_[m + '_class'] != r_['raters_class_majority'])}" for m in MODELS) + " (listed in pairs.csv).", "",
      "## Answer profiles", "", "| annotator | intended version | other version | no clear difference | unclear | Q3 = N, descriptive pairs | Q3 = N, other pairs | "
      "mean moral rating: moral / norm / descriptive pairs |", "|---|---|---|---|---|---|---|---|"]
def profile(src):
    xs = [(ITEMS[i], src[i]) for i in IDS if src[i]]
    def mean_of(v): return sum(v) / max(1, len(v))
    def share(f, sel=None): return mean_of([f(x) for it, x in xs if sel is None or sel(it)])
    def mm(c): return mean_of([x["moral"] for it, x in xs if it["category"] == c])
    return (f"{share(lambda x: x['better'] == 'perm'):.3f} | {share(lambda x: x['better'] == 'rest'):.3f} | {share(lambda x: x['better'] == 'none'):.3f} | {share(lambda x: x['unclear']):.3f} | "
            f"{share(lambda x: x['judged'] == 'N', lambda it: it['category'] == 'descr'):.3f} | {share(lambda x: x['judged'] == 'N', lambda it: it['category'] != 'descr'):.3f} | "
            f"{mm('moral'):.2f} / {mm('norm'):.2f} / {mm('descr'):.2f}")
L += [f"| {h} | {profile(H[h])} |" for h in RATERS] + [f"| {m} | {profile(M_ANS[m])} |" for m in MODELS]
L += ["", "## Agreement (Krippendorff's alpha)", "", "| raters | " + " | ".join(ALPHA_DEF) + " |", "|---|" + "---|" * len(ALPHA_DEF)]
L += [f"| {k} | " + " | ".join(fmt(v.get(n)) for n in ALPHA_DEF) + " |" for k, v in alphas.items() if v]
L += ["", f"Limits of the check: the raters chose the intended version in {n_better['perm']} of {sum(n_better.values())} answers and saw no clear difference in "
      f"{n_better['none']}, so the check says little about how the models judge pairs without a better option (the follow-up's conduct controls). "
      f"The five raters kept {sum(off)} of {len(IDS)} pairs, and three of them, under the same rule, would have kept between {min(p['kept_of_dropped'] for p in panels3)} and "
      f"{max(p['kept_of_dropped'] for p in panels3)} of the {sum(not v for v in off)} they dropped: most drops come from one or two raters, so the check says little about "
      "whether the models drop the pairs that people would agree to drop; it shows whether they read the pairs as our raters do. "
      "The models' answers are sampled at each provider's default and are not deterministic; this is the one run that is compared.", ""]
open(os.path.join(a.out, "report.md"), "w").write("\n".join(L) + "\n")
def clean_nan(o):
    if isinstance(o, float): return None if math.isnan(o) else o
    if isinstance(o, dict): return {k: clean_nan(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean_nan(v) for v in o]
    return o
json.dump(clean_nan(dict(settings=vars(a), models={m: M_NAMES.get(m, m) for m in MODELS}, raters=RATERS, outcome_all_pass=all_pass, alt_test=ALT, alt_test_raters=ALT_H,
               decisions=dict(models_vs_panel=dict(agree=po_ai, kappa=k_ai, both_keep=conf[(True, True)], raters_only=conf[(True, False)], models_only=conf[(False, True)], both_drop=conf[(False, False)]),
                              three_rater_panels=panels3, splits=splits, split_comparison=split_cmp),
               alpha=alphas, alpha_main_round_check=alpha_main_check, script_check=script_check)),
          open(os.path.join(a.out, "summary.json"), "w"), indent=1)
print("\n".join(L))
