"""Checks that every language model answered for every pair."""
import argparse, json, os, re, sys
ap = argparse.ArgumentParser(); ap.add_argument("--items", required=True); ap.add_argument("--out", required=True); ap.add_argument("--first", type=int, default=0, help="only the first N pairs of the file (the smoke test)")
ap.add_argument("--raters", nargs="+", default=["anthropic", "openai", "google"])
a = ap.parse_args(); items = json.load(open(a.items)); ids = [it["id"] for it in (items[:a.first] if a.first else items)]; bad = []
for r in a.raters:
    p = os.path.join(a.out, f"answers_{r}.json"); done = json.load(open(p)) if os.path.exists(p) else {}
    miss = [i for i in ids if not (done.get(i) or {}).get("parsed")]
    if miss:
        raw = re.sub(r"(key=|Bearer |x-api-key)\S+", r"\1...", str((done.get(miss[0]) or {}).get("raw", "no call was made")))[:200]
        bad.append(f"{r}: {len(miss)} of {len(ids)} pairs without a usable answer (first: {miss[0]}; the provider said: {raw!r})")
if bad:
    print("[check_screen] the screen is not complete:\n  " + "\n  ".join(bad) + "\n  Nothing is lost: run the same stage file again, it asks only for the missing answers. "
          "If a provider refuses the model name, the model was retired.", flush=True); sys.exit(1)
if not a.first:
    res = json.load(open(os.path.join(a.out, "items_llm.json"))); gone = [x["id"] for x in res if x.get("reason") == "missing answers"]
    if len(res) != len(ids) or gone: print(f"[check_screen] items_llm.json does not cover every pair ({len(res)} of {len(ids)}; missing answers: {gone[:5]}): run the stage file again", flush=True); sys.exit(1)
    print(f"[check_screen] complete: {len(ids)} pairs, {len(a.raters)} raters; accepted {sum(bool(x['accepted']) for x in res)} of {len(res)}", flush=True)
else: print(f"[check_screen] smoke test complete: {len(ids)} pairs answered by each of the {len(a.raters)} raters", flush=True)
