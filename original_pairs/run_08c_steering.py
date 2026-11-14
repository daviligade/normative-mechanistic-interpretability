"""Run 08c on Llama-3.2-1B (CPU, float32): steering at layer 7 along the moral-stance direction of the original pairs, against 20 random unit directions."""
import argparse, json, os
import numpy as np, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pairs_common import DATA, pairs, save

ap = argparse.ArgumentParser(); ap.add_argument("--model", default="meta-llama/Llama-3.2-1B"); a = ap.parse_args()
torch.set_num_threads(2); torch.manual_seed(0)
tok = AutoTokenizer.from_pretrained(a.model); model = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.float32, low_cpu_mem_usage=True).eval(); LAYER = 7
base = json.load(open(os.path.join(DATA, "replication", "scores_and_mlp.json")))["baseline"]
ids = lambda p: tok(p, return_tensors="pt").input_ids
tids = lambda ws: [tok(" " + w, add_special_tokens=False).input_ids[0] for w in ws]


def hidden(prompt):
    with torch.no_grad(): out = model(ids(prompt), output_hidden_states=True, logits_to_keep=1)
    return out.hidden_states[LAYER + 1][0, -1, :]


vm = [p for p in pairs("moral") if base[p["name"]]["sp"] - base[p["name"]]["sr"] > 0]
P = torch.stack([hidden(p["permissive_prompt"]) for p in vm]); R = torch.stack([hidden(p["restrictive_prompt"]) for p in vm])
d = P.mean(0) - R.mean(0); g = torch.Generator().manual_seed(1); rnd = torch.randn(20, d.shape[0], generator=g); rnd = rnd / rnd.norm(dim=-1, keepdim=True)
dirs = torch.cat([(d / d.norm())[None], rnd]); alphas = [-3., -2., -1., 0., 1., 2., 3.]; shifts = np.zeros((len(vm), len(dirs), len(alphas)))
for n, p in enumerate(vm):
    x = ids(p["restrictive_prompt"]); pi, ri = tids(p["permissive_targets"]), tids(p["restrictive_targets"]); rows = []
    for c0 in range(0, len(dirs), 7):
        add = torch.stack([al * dv for dv in dirs[c0:c0 + 7] for al in alphas])
        def hook(m, a_, o, add=add):
            h = (o[0] if isinstance(o, tuple) else o).clone(); h[:, -1, :] += add
            return (h,) + tuple(o[1:]) if isinstance(o, tuple) else h
        hd = model.model.layers[LAYER].register_forward_hook(hook)
        with torch.no_grad(): lg = model(x.repeat(len(add), 1), logits_to_keep=1).logits
        hd.remove(); pr = torch.softmax(lg[:, -1, :], -1); rows.append((pr[:, pi].sum(-1) - pr[:, ri].sum(-1)).numpy().reshape(-1, len(alphas)))
    sc = np.concatenate(rows); shifts[n] = sc - sc[:, [3]]
ms = shifts.mean(0); ranges = ms[1:, -1] - ms[1:, 0]
out = {"direction_norm": float(d.norm()), "mean_residual_norm": float(R.norm(dim=-1).mean()), "alphas": alphas, "moral_direction_shift": ms[0].tolist(), "moral_range": float(ms[0, -1] - ms[0, 0]),
       "random_ranges": ranges.tolist(), "random_mean_abs_range": float(np.abs(ranges).mean()), "random_max_abs_range": float(np.abs(ranges).max()),
       "random_reaching_half_of_moral": int((np.abs(ranges) >= 0.5 * (ms[0, -1] - ms[0, 0])).sum())}
print(out)
save("run_08c_steering.json", out)
