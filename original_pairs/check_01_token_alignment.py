"""Check 01: the upstream profiles of the path patching on the original pairs are flat exactly when the restrictive prompt is not longer than the permissive one."""
import json, os
from pairs_common import DATA, MODELS, pairs, family, token_counter, save

ntok = token_counter(); P = {p["name"]: p for p in pairs("moral")}; out = {}; total = mismatches = 0
for m in MODELS:
    path = os.path.join(DATA, "heads", m, "flatness.json")
    if not os.path.exists(path): continue
    flat = json.load(open(path)); n = nonflat = bad = 0
    for k, v in flat.items():
        lp, lr = ntok(family(m), P[k]["permissive_prompt"]), ntok(family(m), P[k]["restrictive_prompt"])
        n += 1; nonflat += v > 1e-6; bad += (v > 1e-6) != (lr > lp)
    out[m] = {"pairs": n, "not_flat": int(nonflat), "mismatches": int(bad)}; total += n; mismatches += bad
    print(f"{m:24s} pairs {n:3d}  not flat {nonflat:3d}  cases where 'not flat' and 'restrictive prompt longer' disagree: {bad}")
print(f"all models: {total} (model, pair) cases, {mismatches} disagreements")
save("check_01_token_alignment.json", out)
