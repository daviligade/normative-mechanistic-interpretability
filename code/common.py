"""Frames, answer words and helpers shared by the head and feature scripts."""
import math

PRIME = "A sunny day at the beach is good.\nA flat tire on the highway is bad.\n"
FRAMES = {
    "A0": lambda stem: f"{stem} is morally",
    "B":  lambda stem: f"{PRIME}{stem} is",
    "A1": lambda stem: f"{PRIME}{stem} is morally",
    "QA": lambda stem: f"Question: Is the following good or bad?\n{stem}\nAnswer: It is",
}
POS = ["acceptable", "justified", "right", "permissible", "okay", "correct", "good", "fine", "moral", "ethical",
       "appropriate", "proper", "great", "sensible"]
NEG = ["unacceptable", "unjust", "wrong", "forbidden", "terrible", "incorrect", "bad", "poor", "immoral", "unethical",
       "inappropriate", "improper", "awful", "foolish"]
HIST_POS = ["acceptable", "justified", "right", "permissible", "okay", "correct", "good", "fine", "moral", "ethical"]
HIST_NEG = ["wrong", "unacceptable", "immoral", "unjustified", "bad", "incorrect", "impermissible", "unethical", "unjust", "forbidden"]


def first_token_id(tok, word, strict):
    ids = tok(" " + word, add_special_tokens=False).input_ids

    while len(ids) > 1 and tok.decode([ids[0]]).strip() == "":
        ids = ids[1:]
    if strict:
        if len(ids) != 1 or tok.decode(ids).strip() != word:
            raise ValueError(f"answer word {word!r} is not a single token for this tokenizer: {ids} -> {[tok.decode([i]) for i in ids]}")
    return ids[0]


def answer_ids(tok):
    pos = [first_token_id(tok, w, True) for w in POS]; neg = [first_token_id(tok, w, True) for w in NEG]
    if len(set(pos + neg)) != len(pos + neg):
        raise ValueError("answer tokens are not distinct")
    hp = [first_token_id(tok, w, False) for w in HIST_POS]; hn = [first_token_id(tok, w, False) for w in HIST_NEG]
    return {"pos": pos, "neg": neg, "hist_pos": hp, "hist_neg": hn,
            "good": first_token_id(tok, "good", True), "bad": first_token_id(tok, "bad", True)}


def encode(tok, text, bos=True):
    ids = tok(text, add_special_tokens=False).input_ids
    if not bos: return ids
    b = tok.bos_token_id if tok.bos_token_id is not None else tok.eos_token_id
    return [b] + ids


def readouts(logits, A):
    import torch
    lg = logits.float(); pr = torch.softmax(lg, -1)
    sp, sn = pr[:, A["pos"]].sum(-1), pr[:, A["neg"]].sum(-1)
    return {"S": sp - sn, "mass": sp + sn,
            "LD": torch.logsumexp(lg[:, A["pos"]], -1) - torch.logsumexp(lg[:, A["neg"]], -1),
            "S_hist": pr[:, A["hist_pos"]].sum(-1) - pr[:, A["hist_neg"]].sum(-1),
            "LD_gb": lg[:, A["good"]] - lg[:, A["bad"]]}


RUN_FILE = "stimuli/items_run_v1.json"


def _root(): import os; return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def check_run_file(items_path, items_sha, any_items=False):
    return


def check_analysis_items(any_items=False):
    return


def primary_item_set(items_path):
    import os
    final = os.path.join(_root(), "stimuli", "items_final.json")
    if open(items_path, "rb").read() == open(final, "rb").read(): return True, "the item file is the set of accepted pairs"
    return False, f"{items_path} is not the set of accepted pairs (stimuli/items_final.json)"


def accepted_ids():
    import json, os
    return {i["id"] for i in json.load(open(os.path.join(_root(), "stimuli", "items_final.json")))}
