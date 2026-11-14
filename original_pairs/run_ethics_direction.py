"""The moral-stance direction of the original pairs applied to scenarios of the ETHICS benchmark (commonsense morality, test split): projection (ROC-AUC) and steering."""
import argparse, csv, os
import numpy as np, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pairs_common import pairs, save

PERM = ["acceptable", "justified", "right", "permissible", "okay", "correct", "good", "fine", "moral", "ethical"]
REST = ["wrong", "unacceptable", "immoral", "unjustified", "bad", "incorrect", "impermissible", "unethical", "unjust", "forbidden"]
ap = argparse.ArgumentParser(); ap.add_argument("--model", required=True); ap.add_argument("--layer", type=int, required=True, help="7 for Llama-3.2-1B, 12 for Llama-3.1-8B")
ap.add_argument("--ethics-csv", required=True, help="the commonsense test split of ETHICS (CSV with the columns label and input)"); ap.add_argument("--max-n", type=int, default=800); ap.add_argument("--device", default="cpu")
ap.add_argument("--steer", action="store_true"); ap.add_argument("--alphas", type=float, nargs="+", default=[-3., -2., -1., 0., 1., 2., 3.]); a = ap.parse_args()
rows = []
with open(a.ethics_csv, newline="", encoding="utf-8", errors="replace") as f:
    for r in csv.DictReader(f):
        try: rows.append((int(r["label"]), r["input"].strip()))
        except (ValueError, KeyError): continue
rows = [x for x in rows if x[1]]
if a.max_n and len(rows) > a.max_n: rows = [rows[i] for i in np.random.default_rng(0).choice(len(rows), a.max_n, replace=False)]
y = np.array([l for l, _ in rows])
tok = AutoTokenizer.from_pretrained(a.model); model = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.float32).to(a.device).eval()


def resid(text):
    with torch.no_grad(): out = model(tok(text, return_tensors="pt").input_ids.to(a.device), output_hidden_states=True, logits_to_keep=1)
    return out.hidden_states[a.layer + 1][0, -1, :].float().cpu()


moral = pairs("moral"); d = torch.stack([resid(p["permissive_prompt"]) for p in moral]).mean(0) - torch.stack([resid(p["restrictive_prompt"]) for p in moral]).mean(0)
proj = np.array([float(resid(t + " This is morally") @ (d / d.norm())) for _, t in rows])
rank = np.empty(len(proj)); rank[proj.argsort()] = np.arange(1, len(proj) + 1); n1 = y.sum(); n0 = len(y) - n1
auc = float((rank[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)); out = {"model": a.model, "layer": a.layer, "n": len(rows), "direction_norm": float(d.norm()), "auc": max(auc, 1 - auc)}
print(out, flush=True)
if a.steer:
    one = lambda ws: [i for i in (tok(" " + w, add_special_tokens=False).input_ids for w in ws) if len(i) == 1]
    pi, ri = [i[0] for i in one(PERM)], [i[0] for i in one(REST)]; state = {"alpha": 0.0}; dd = d.to(a.device)

    def hook(m, a_, o):
        if state["alpha"] == 0.0: return o
        h = (o[0] if isinstance(o, tuple) else o).clone(); h[:, -1, :] += state["alpha"] * dd
        return (h,) + tuple(o[1:]) if isinstance(o, tuple) else h

    hd = model.model.layers[a.layer].register_forward_hook(hook); curve = []
    for al in a.alphas:
        state["alpha"] = al; S = []
        for _, t in rows:
            with torch.no_grad(): pr = torch.softmax(model(tok(t + " This is morally", return_tensors="pt").input_ids.to(a.device), logits_to_keep=1).logits[0, -1].float(), -1)
            S.append(float(pr[pi].sum() - pr[ri].sum()))
        S = np.array(S); curve.append({"alpha": al, "mean_S": float(S.mean()), "mean_S_label_0": float(S[y == 0].mean()), "mean_S_label_1": float(S[y == 1].mean())}); print(curve[-1], flush=True)
    hd.remove(); out["steering"] = curve
save(f"ethics_direction_{a.model.split('/')[-1]}.json", out)
