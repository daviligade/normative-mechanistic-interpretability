"""The 400 ETHICS scenarios used in the removal test."""
import argparse, csv, hashlib, json, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import POS, NEG, HIST_POS, HIST_NEG

ap = argparse.ArgumentParser(); ap.add_argument("--csv", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--n-per-class", type=int, default=200); ap.add_argument("--seed", type=int, default=20261111)
ap.add_argument("--min-words", type=int, default=6); ap.add_argument("--max-words", type=int, default=20)
a = ap.parse_args()
ANSW = set(POS + NEG + HIST_POS + HIST_NEG)
raw = open(a.csv, "rb").read(); rows = list(csv.DictReader(raw.decode("utf-8").splitlines()))
assert rows and set(rows[0]) == {"label", "input", "is_short", "edited"}, f"unexpected columns: {sorted(rows[0]) if rows else None}"


def passes(t):
    if not t.isascii() or "\n" in t or '"' in t or not t.startswith("I ") or not t.endswith("."): return False
    if t.count(".") != 1 or "?" in t or "!" in t: return False
    if not a.min_words <= len(t.split()) <= a.max_words: return False
    return not any(w.lower() in ANSW for w in re.findall(r"[A-Za-z]+", t))


seen, pool = set(), {0: [], 1: []}
for k, r in enumerate(rows):
    t = r["input"].strip()
    if r["is_short"] != "True" or r["label"] not in ("0", "1") or t in seen or not passes(t): continue
    seen.add(t); pool[int(r["label"])].append((k, t))
if min(len(pool[0]), len(pool[1])) < a.n_per_class: sys.exit(f"too few scenarios pass the rule: {len(pool[0])} acceptable, {len(pool[1])} unacceptable")
rng = random.Random(a.seed); pick = {c: sorted(rng.sample(pool[c], a.n_per_class)) for c in (0, 1)}
for c in (0, 1): rng.shuffle(pick[c])
items = []
for j in range(a.n_per_class):
    for c, name, short in ((0, "acceptable", "a"), (1, "unacceptable", "u")):
        k, t = pick[c][j]; items.append(dict(id=f"eth_{short}{j + 1:03d}", label=c, category=name, text=t, n_words=len(t.split()), source_row=k))
out = dict(source=dict(dataset="ETHICS, commonsense morality, test split (Hendrycks et al. 2021)", licence="MIT", url="https://huggingface.co/datasets/hendrycks/ethics/resolve/main/data/commonsense/test.csv",
                       sha256=hashlib.sha256(raw).hexdigest(), rows=len(rows), short_rows=sum(r["is_short"] == "True" for r in rows)),
           rule=dict(words=[a.min_words, a.max_words], n_per_class=a.n_per_class, seed=a.seed, passing={"acceptable": len(pool[0]), "unacceptable": len(pool[1])},
                     label="0 = acceptable, 1 = unacceptable (the benchmark's own labels)"),
           items=items)
json.dump(out, open(a.out, "w"), indent=1)
print(f"{len(rows)} rows, {out['source']['short_rows']} short; pass the rule: {len(pool[0])} acceptable, {len(pool[1])} unacceptable; written {len(items)} scenarios to {a.out} "
      f"(sha256 {hashlib.sha256(open(a.out, 'rb').read()).hexdigest()[:16]}); words per scenario: {min(i['n_words'] for i in items)} to {max(i['n_words'] for i in items)}")
