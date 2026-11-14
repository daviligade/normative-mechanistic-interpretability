"""The choice between two options and its control."""
import common

ENDS = {"CH": "\nI choose Option", "CW": '" is in Option'}


def _frame(name):
    def f(text):
        if not (text.startswith("Option A: ") and "\nOption B: " in text and text.endswith(ENDS[name])):
            raise SystemExit(f"frame {name} takes the prompts of stimuli/make_choice_items.py (items_choice_run.json for CH, items_choice_word_run.json for CW), not: {text[:60]!r}")
        return text
    return f


EXTRA = {name: _frame(name) for name in ENDS}


def register():
    for k, f in EXTRA.items():
        if k in common.FRAMES and common.FRAMES[k] is not f: raise SystemExit(f"frame name {k} is already taken in code/common.py")
        common.FRAMES[k] = f
    return list(EXTRA)


def answer_ids(tok):
    a, b = common.first_token_id(tok, "A", True), common.first_token_id(tok, "B", True)
    if a == b: raise ValueError("the two labels are the same token")
    return {"pos": [a], "neg": [b], "hist_pos": [a], "hist_neg": [b], "good": a, "bad": b}


def check_frames(argv, who):
    fr = []
    if "--frames" in argv:
        for x in argv[argv.index("--frames") + 1:]:
            if x.startswith("--"): break
            fr.append(x)
    if not fr or any(f not in EXTRA for f in fr): raise SystemExit(f"[{who}] this wrapper reads the answer from the labels A and B: give --frames CH or --frames CW (got {fr or 'none'})")
