"""The annotators' form answered by three language models."""
import argparse, json, os, re, sys, time, urllib.request, urllib.error
import numpy as np

KINDS = ["moral", "prudential", "etiquette", "aesthetic", "epistemic"]
INSTRUCTIONS = """You are helping with a study of how people judge short phrases. You will see two short phrases, Option 1 and Option 2, identical except for one or two words. They are not full sentences; read each as "the act, or the thing, described here". There are no trick questions and no right answers: we want your own judgement as a competent speaker of English. Answer the following questions.

Q1 Which option is better? 1 or 2: the option that is more acceptable, more appropriate, wiser, nicer or of higher quality. 0 only if you see no clear difference.
Q2 How much worse is the worse option? 1 = a little, 2 = clearly, 3 = very much. Keep your numbers comparable from row to row: a small slip gets a lower number than something terrible, even when the rows are about different things. Q2 is only about the size of the gap. If Q1 is 0, answer null.
Q3 Is anyone's action, choice or work being judged? "Y" if the two options differ in what someone does, chooses or makes. "N" if the phrase only describes a thing, condition or situation that is better or worse (the weather, a battery, a piece of fruit): nobody's conduct is in view. Do not answer N just because the row is about facts: when a person's reasoning or belief is judged, the answer is Y.
Q4 to Q8 What kind of difference is it? For each of the five kinds, say how much the difference between the two options is a matter of that kind: 0 = not at all, 1 = slightly, 2 = clearly, 3 = very much. Rate each kind on its own; often only one is high, sometimes two or three are. These answers are about WHAT KIND of difference it is, not how big it is. If Q3 is N, answer null for all five.
  moral: the effects on other people: harm or help, fairness, honesty, rights, consent, duties to others. Helping others is usually also the sensible thing to do; that does not make it prudential. Ask whose safety or interest is at stake.
  prudential: the interests of the person acting: their own goals, safety, money, health or plans, not the people or things affected by what they do.
  etiquette: manners, politeness, custom, dress codes, what is done in a setting.
  aesthetic: beauty, taste, style; how well something was designed, made or performed, so that someone's work is judged. If only the state of a thing is described, with nobody's work in view, the row is a Q3 = N row.
  epistemic: one option shows better reasoning, or is more reasonable to believe or conclude, than the other; evidence, belief, how a conclusion was reached.
If you hesitate: whose interest is at stake decides between moral and prudential (other people's -> moral; the doer's own -> prudential; both -> rate both). Manners that also cost the doer something are etiquette first, prudential a little. A judged piece of work is aesthetic; a thing in a certain state is N. A person drawing a conclusion is epistemic, even when the topic is factual.
unclear: true if a phrase is hard to understand, ungrammatical, or depends on something you would have to guess; still answer the row as well as you can.

Answer with one JSON object and nothing else, with exactly these keys:
{"q1": 1|2|0, "q2": 1|2|3|null, "q3": "Y"|"N", "moral": 0-3|null, "prudential": 0-3|null, "etiquette": 0-3|null, "aesthetic": 0-3|null, "epistemic": 0-3|null, "unclear": true|false, "comment": "optional, short"}"""

EXAMPLES = [("Letting an ambulance pass in heavy traffic", "Blocking an ambulance in heavy traffic", {"q1": 1, "q2": 3, "q3": "Y", "moral": 3, "prudential": 0, "etiquette": 0, "aesthetic": 0, "epistemic": 0, "unclear": False, "comment": "harm to others; very much worse"}),
            ("Cycling in city traffic without a helmet", "Cycling in city traffic with a helmet", {"q1": 2, "q2": 2, "q3": "Y", "moral": 0, "prudential": 3, "etiquette": 0, "aesthetic": 0, "epistemic": 0, "unclear": False, "comment": "own safety"}),
            ("The coffee from a moldy machine", "The coffee from a clean machine", {"q1": 2, "q2": 3, "q3": "N", "moral": None, "prudential": None, "etiquette": None, "aesthetic": None, "epistemic": None, "unclear": False, "comment": "no one's conduct is judged"}),
            ("Setting off fireworks in a crowded yard", "Setting off fireworks in an empty field", {"q1": 2, "q2": 3, "q3": "Y", "moral": 3, "prudential": 2, "etiquette": 0, "aesthetic": 0, "epistemic": 0, "unclear": False, "comment": "others' safety first, the doer's own safety too"})]


def prompt_for(o1, o2):
    ex = "\n\n".join(f"Example.\nOption 1: {a}\nOption 2: {b}\nAnswer: {json.dumps(ans)}" for a, b, ans in EXAMPLES)
    return f"{INSTRUCTIONS}\n\n{ex}\n\nNow this row.\nOption 1: {o1}\nOption 2: {o2}\nAnswer:"


def http_json(url, headers, body, timeout=120):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=dict(headers, **{"Content-Type": "application/json"}), method="POST")
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r: return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace")[:300]
            if e.code in (429, 500, 502, 503, 529) and attempt < 4: time.sleep(5 * (attempt + 1)); continue
            raise RuntimeError(f"HTTP {e.code}: {msg}")
        except (urllib.error.URLError, TimeoutError):
            if attempt < 4: time.sleep(5 * (attempt + 1)); continue
            raise


def ask(rater, model, text, opt):
    if rater == "anthropic":
        key = os.environ.get("ANTHROPIC_API_KEY"); assert key, "ANTHROPIC_API_KEY not set"
        r = http_json("https://api.anthropic.com/v1/messages", {"x-api-key": key, "anthropic-version": "2023-06-01"}, {"model": model, "max_tokens": opt["max_tokens"], "messages": [{"role": "user", "content": text}]})
        u = r.get("usage", {}); return "".join(b.get("text", "") for b in r.get("content", []) if b.get("type") == "text"), dict(input=u.get("input_tokens", 0), output=u.get("output_tokens", 0), stop=r.get("stop_reason"))
    if rater == "openai":
        key = os.environ.get("OPENAI_API_KEY"); assert key, "OPENAI_API_KEY not set"
        body = {"model": model, "messages": [{"role": "user", "content": text}], "max_completion_tokens": opt["max_tokens"]}
        if opt["openai_effort"]: body["reasoning_effort"] = opt["openai_effort"]
        r = http_json("https://api.openai.com/v1/chat/completions", {"Authorization": f"Bearer {key}"}, body)
        u = r.get("usage", {}); ch = r["choices"][0]
        return ch["message"].get("content") or "", dict(input=u.get("prompt_tokens", 0), output=u.get("completion_tokens", 0), reasoning=(u.get("completion_tokens_details") or {}).get("reasoning_tokens"), stop=ch.get("finish_reason"))
    if rater == "google":
        key = os.environ.get("GOOGLE_API_KEY"); assert key, "GOOGLE_API_KEY not set"
        gc = {"maxOutputTokens": opt["max_tokens"]}
        if opt["google_thinking"]: gc["thinkingConfig"] = {"thinkingLevel": opt["google_thinking"]}
        r = http_json(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}", {}, {"contents": [{"parts": [{"text": text}]}], "generationConfig": gc})
        u = r.get("usageMetadata", {}); c = (r.get("candidates") or [{}])[0]
        txt = "".join(p.get("text", "") for p in (c.get("content") or {}).get("parts", []) if not p.get("thought"))
        return txt, dict(input=u.get("promptTokenCount", 0), output=(u.get("candidatesTokenCount", 0) or 0) + (u.get("thoughtsTokenCount", 0) or 0), reasoning=u.get("thoughtsTokenCount"), stop=c.get("finishReason"))
    raise ValueError(rater)


def parse_answer(text):
    m = re.search(r"\{.*\}", text, re.S)
    if not m: return None
    try: a = json.loads(m.group(0))
    except json.JSONDecodeError: return None
    out = {}
    out["q1"] = a.get("q1"); out["q2"] = a.get("q2"); out["q3"] = str(a.get("q3", "")).strip().upper()[:1] or None
    for k in KINDS: out[k] = a.get(k)
    out["unclear"] = bool(a.get("unclear", False)); out["comment"] = str(a.get("comment", ""))[:300]
    if out["q1"] not in (0, 1, 2) or out["q3"] not in ("Y", "N"): return None
    return out


def aggregate(items, answers, keys, control_set=False):
    R = len(answers); need = -(-2 * R // 3); unclear_max = -(-R // 2) - 1; out = []
    for it in items:
        i = it["id"]; rows = [(r, answers[r].get(i), keys[r][i]) for r in answers if answers[r].get(i)]
        if len(rows) < R: out.append(dict(id=i, category=it["category"], subtype=it.get("subtype"), accepted=False, reason="missing answers")); continue
        if control_set:
            no_better = sum(1 for _, a, _ in rows if a["q1"] == 0); conduct = sum(1 for _, a, _ in rows if a["q3"] == "Y"); unclear = sum(1 for _, a, _ in rows if a["unclear"])
            acc = no_better >= need and conduct >= need and unclear <= unclear_max
            out.append(dict(id=i, category=it["category"], subtype=it.get("subtype"), accepted=bool(acc), no_better_votes=no_better, conduct_votes=conduct, unclear=unclear,
                            reasons=[r for r, ok in (("an option was judged better", no_better >= need), ("no conduct", conduct >= need), ("unclear", unclear <= unclear_max)) if not ok])); continue
        better_perm = sum(1 for r, a, side in rows if a["q1"] == side)
        def cls(a):
            if a["q3"] == "N": return "N"
            g = {k: (a[k] or 0) for k in KINDS}
            if max(g.values()) == 0: return "N"
            top = [k for k, v in g.items() if v == max(g.values())]
            if len(top) == 1: return top[0]
            return None if "moral" in top else "norm_tie"
        classes = [cls(a) for _, a, _ in rows]
        intended = "moral" if it["category"] == "moral" else ("N" if it["category"] == "descr" else "norm")
        class_ok = sum(1 for c in classes if (c == "moral" if intended == "moral" else (c == "N" if intended == "N" else c in ("prudential", "etiquette", "aesthetic", "epistemic", "norm_tie"))))
        moral_med = float(np.median([(a["moral"] or 0) if a["q3"] == "Y" else 0 for _, a, _ in rows]))
        moral_ok = moral_med >= 2 if intended == "moral" else moral_med <= 1
        unclear = sum(1 for _, a, _ in rows if a["unclear"]); kind = it.get("subtype")
        kind_conf = it["category"] == "norm" and sum(1 for _, a, _ in rows if a["q3"] == "Y" and (a.get(kind) or 0) >= 2 and cls(a) == kind) >= need
        acc = better_perm >= need and class_ok >= need and moral_ok and unclear <= unclear_max
        out.append(dict(id=i, category=it["category"], subtype=kind, accepted=bool(acc), direction_votes=better_perm, class_votes=class_ok, classes=classes, moral_median=moral_med, unclear=unclear, kind_confirmed=bool(kind_conf),
                        reasons=[r for r, ok in (("direction", better_perm >= need), ("class", class_ok >= need), ("moral rating", moral_ok), ("unclear", unclear <= unclear_max)) if not ok]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", required=True, help="candidate pairs: id, category, subtype, perm_stem, rest_stem (the labels are used only for scoring)")
    ap.add_argument("--out", default="ratings_llm"); ap.add_argument("--raters", nargs="+", default=["anthropic", "openai", "google"], choices=["anthropic", "openai", "google"])
    ap.add_argument("--model-anthropic", default="claude-sonnet-5-5"); ap.add_argument("--model-openai", default="gpt-5.5"); ap.add_argument("--model-google", default="gemini-3.1-pro-preview")
    ap.add_argument("--openai-effort", default="low", help="reasoning_effort for the OpenAI model ('' to leave the provider default)"); ap.add_argument("--google-thinking", default="low", help="thinkingLevel for the Gemini model ('' for the default)")
    ap.add_argument("--max-tokens", type=int, default=8000, help="output limit per call, thinking included (only a cap; billed by use)")
    ap.add_argument("--prices", nargs=6, type=float, default=[2, 10, 5, 30, 2, 12], metavar=("ANT_IN", "ANT_OUT", "OAI_IN", "OAI_OUT", "GOO_IN", "GOO_OUT"), help="USD per 1M tokens, for the cost estimate only")
    ap.add_argument("--seed", type=int, default=20261021); ap.add_argument("--max-items", type=int, default=0, help="smoke test: call for the first N pairs of the file only (every answer printed)")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--sleep", type=float, default=0.5); ap.add_argument("--attempts", type=int, default=2, help="calls per pair and rater when an answer cannot be parsed")
    ap.add_argument("--control-set", action="store_true", help="conduct-without-evaluation controls: keep a pair when the raters find NO better option and see someone acting (see aggregate)")
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True); items = json.load(open(a.items))
    rng = np.random.default_rng(a.seed); models = {"anthropic": a.model_anthropic, "openai": a.model_openai, "google": a.model_google}
    keys = {r: {it["id"]: int(rng.integers(1, 3)) for it in items} for r in a.raters}; orders = {r: [items[i] for i in rng.permutation(len(items))] for r in a.raters}
    json.dump({"seed": a.seed, "sides": keys, "note": "side 1 = the permissive version was shown as Option 1; never shown to the raters"}, open(os.path.join(a.out, "KEY_llm_do_not_share.json"), "w"), indent=1)
    subset = {it["id"] for it in items[: a.max_items]} if a.max_items else None
    if a.dry_run:
        for it in items[:2]:
            side = keys[a.raters[0]][it["id"]]; o1, o2 = (it["perm_stem"], it["rest_stem"]) if side == 1 else (it["rest_stem"], it["perm_stem"]); print(prompt_for(o1, o2)); print("\n" + "=" * 100 + "\n")
        print(f"[dry run] {len(items)} items x {len(a.raters)} raters = {len(items) * len(a.raters)} calls; models {models}"); return
    opt = dict(max_tokens=a.max_tokens, openai_effort=a.openai_effort, google_thinking=a.google_thinking); price = dict(anthropic=a.prices[0:2], openai=a.prices[2:4], google=a.prices[4:6])
    answers, sides_used, cost_lines = {}, {}, []
    for r in a.raters:
        path = os.path.join(a.out, f"answers_{r}.json"); done = json.load(open(path)) if os.path.exists(path) else {}; t0 = time.time(); n_call = 0
        for n, it in enumerate(orders[r]):
            if subset is not None and it["id"] not in subset: continue
            if it["id"] in done and done[it["id"]].get("parsed"): continue
            side = keys[r][it["id"]]; o1, o2 = (it["perm_stem"], it["rest_stem"]) if side == 1 else (it["rest_stem"], it["perm_stem"]); usage = []; raw, parsed = "", None
            for attempt in range(a.attempts):
                try: raw, u = ask(r, models[r], prompt_for(o1, o2), opt); usage.append(u); parsed = parse_answer(raw)
                except Exception as e: raw, parsed = f"ERROR {type(e).__name__}: {e}", None
                n_call += 1
                if parsed: break
                time.sleep(a.sleep)
            done[it["id"]] = dict(raw=raw, parsed=parsed, model=models[r], side=side, usage=usage); json.dump(done, open(path, "w"), indent=1)
            if subset is not None: print(f"[{r}] {it['id']} side {side}: {'parsed' if parsed else 'NOT PARSED'}; usage {usage}; answer: {raw[:400]!r}", flush=True)
            elif (n + 1) % 10 == 0: print(f"[{r}] {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
            time.sleep(a.sleep)
        answers[r] = {i: d["parsed"] for i, d in done.items() if d.get("parsed") and (subset is None or i in subset)}
        sides_used[r] = {i: d.get("side", keys[r][i]) for i, d in done.items() if i in keys[r]}
        for i in keys[r]: sides_used[r].setdefault(i, keys[r][i])
        tin = sum(u.get("input", 0) for d in done.values() for u in d.get("usage", [])); tout = sum(u.get("output", 0) for d in done.values() for u in d.get("usage", []))
        cost = tin / 1e6 * price[r][0] + tout / 1e6 * price[r][1]
        cost_lines.append(f"{r} ({models[r]}): {tin} input and {tout} output tokens (thinking included) so far, about ${cost:.2f} at {price[r][0]:g}/{price[r][1]:g} per 1M")
        print(f"[{r}] {len(answers[r])} answers parsed ({n_call} calls this run); " + cost_lines[-1], flush=True)
    scored = [it for it in items if subset is None or it["id"] in subset]
    res = aggregate(scored, answers, sides_used, control_set=a.control_set)
    if subset is not None:
        print("[smoke test] " + "; ".join(f"{x['id']}: {'accepted' if x['accepted'] else 'rejected (' + ', '.join(x.get('reasons', [x.get('reason', '')])) + ')'}" for x in res)); print("[smoke test] nothing written as items_llm.json; run without --max-items for the whole file"); return
    json.dump(res, open(os.path.join(a.out, "items_llm.json"), "w"), indent=1)
    acc = [x for x in res if x["accepted"]]; by = {}
    for x in res: by.setdefault((x["category"], x.get("subtype")), [0, 0]); by[(x["category"], x.get("subtype"))][1] += 1; by[(x["category"], x.get("subtype"))][0] += x["accepted"]
    lines = ["# Annotation by language models", "", f"Raters: {', '.join(f'{r} ({models[r]})' for r in a.raters)}; rule with R = {len(a.raters)} (two thirds = {-(-2 * len(a.raters) // 3)}).", "",
             f"Accepted {len(acc)} of {len(res)} candidates: " + ", ".join(f"{c}/{k}: {v[0]}/{v[1]}" for (c, k), v in sorted(by.items(), key=lambda t: (str(t[0][0]), str(t[0][1])))), "",
             "Rejected: " + "; ".join(f"{x['id']} ({', '.join(x.get('reasons', [x.get('reason', '')]))})" for x in res if not x["accepted"]) if any(not x["accepted"] for x in res) else "Rejected: none", "",
             "Tokens and approximate cost: " + "; ".join(cost_lines), ""]
    open(os.path.join(a.out, "report_llm.md"), "w").write("\n".join(lines) + "\n"); print("\n".join(lines))


if __name__ == "__main__":
    main()
