"""Mechanical checks of candidate pairs (tokenizers only)."""
import json, os, sys, re, argparse, collections, importlib.util
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../code"))
from common import FRAMES, POS, NEG, HIST_POS, HIST_NEG
ap = argparse.ArgumentParser(); ap.add_argument("--candidates", required=True); ap.add_argument("--tok-dir", required=True); ap.add_argument("--hist-root", default=None); ap.add_argument("--out", default=None)
ap.add_argument("--allow-twins", action="store_true", help="within-set near-duplicates are allowed between items whose ids share the part before the underscore (twin pairs)")
a = ap.parse_args()
spec = importlib.util.spec_from_file_location("cand", a.candidates); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); C = mod.C
from tokenizers import Tokenizer
T = {k: Tokenizer.from_file(os.path.join(a.tok_dir, f"{k}_tokenizer.json")) for k in ["llama", "qwen", "gemma"]}
enc = lambda t, s: t.encode(s, add_special_tokens=False).ids
ANSW = set(POS + NEG + HIST_POS + HIST_NEG)
STOP = set("a an the of to in on at for with without by from and or is are was be as that this it its his her their your you he she they who when while before after than".split())
content = lambda s: {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 2}
hist = []
if a.hist_root:
    for f in ["stimuli/original_moral_pairs.json", "stimuli/original_control_pairs.json", "stimuli/original_norm_pairs.json", "stimuli/original_neutral_pairs.json"]:
        for p in json.load(open(os.path.join(a.hist_root, f))): hist += [(p["name"], p["permissive_prompt"]), (p["name"], p["restrictive_prompt"])]
def span(x, y):
    i = 0
    while i < min(len(x), len(y)) and x[i] == y[i]: i += 1
    j = 0
    while j < min(len(x), len(y)) - i and x[-1 - j] == y[-1 - j]: j += 1
    return i, j, len(x) - i - j, len(y) - i - j
rows, fails = [], collections.defaultdict(list)
for cid, cat, sub, tpl, pf, rf, tt in C:
    ps, rs = tpl.replace("{X}", pf), tpl.replace("{X}", rf); row = dict(id=cid, category=cat, subtype=sub, template_type=tt, perm_stem=ps, rest_stem=rs, perm_fill=pf, rest_fill=rf)
    assert tpl.count("{X}") == 1
    for w in re.findall(r"[A-Za-z]+", pf + " " + rf):
        if w.lower() in ANSW: fails[cid].append(f"flip word '{w}' is an answer word")
    for w in re.findall(r"[A-Za-z]+", ps):
        if w.lower() in ANSW: fails[cid].append(f"stem contains answer word '{w}'")
    for tk, t in T.items():
        for fr in ["A0", "B", "A1"]:
            x, y = enc(t, FRAMES[fr](ps)), enc(t, FRAMES[fr](rs))
            if len(x) != len(y): fails[cid].append(f"{tk}/{fr}: {len(x)} vs {len(y)} tokens");
        x, y = enc(t, FRAMES["A0"](ps)), enc(t, FRAMES["A0"](rs)); i, j, ex, ey = span(x, y)
        row[f"{tk}_ntok"] = len(x); row[f"{tk}_edit_perm"] = ex; row[f"{tk}_edit_rest"] = ey; row[f"{tk}_after_edit"] = j - len(enc(t, " is morally"))
    if hist:
        cs = content(ps) | content(rs); best = max(((len(cs & content(h)) / max(1, len(cs | content(h)))), n) for n, h in hist)
        row["max_jaccard_hist"] = round(best[0], 2); row["nearest_hist"] = best[1]
        if best[0] >= 0.5: fails[cid].append(f"near-duplicate of historical item {best[1]} (Jaccard {best[0]:.2f})")
    rows.append(row)
for i, r in enumerate(rows):
    for q in rows[:i]:
        if a.allow_twins and r["id"].split("_")[0] == q["id"].split("_")[0]: continue
        c1, c2 = content(r["perm_stem"]) | content(r["rest_stem"]), content(q["perm_stem"]) | content(q["rest_stem"]); jac = len(c1 & c2) / max(1, len(c1 | c2))
        if jac >= 0.5: fails[r["id"]].append(f"near-duplicate of {q['id']} (Jaccard {jac:.2f})")
ok = [r for r in rows if r["id"] not in fails]
print(f"{len(rows)} candidates, {len(ok)} pass all mechanical checks, {len(fails)} fail")
for cid, f in fails.items(): print("  FAIL", cid, "|", "; ".join(f))
by = collections.Counter((r["category"], r["subtype"]) for r in ok); print("passing by group:", dict(by))
if a.out: json.dump({"rows": rows, "fails": fails}, open(a.out, "w"), indent=1)
