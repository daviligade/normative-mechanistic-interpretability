"""Run 06 on Llama-3.2-1B (CPU, float32): scores of the original moral, control and norm pairs, MLP patching per layer, and head patching on norm pairs (and on six moral pairs, against the stored head effects)."""
import argparse, json, os, random, time
import numpy as np, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pairs_common import DATA, pairs

ap = argparse.ArgumentParser(); ap.add_argument("--model", default="meta-llama/Llama-3.2-1B"); ap.add_argument("--n-norm", type=int, default=81, help="norm pairs for head patching")
ap.add_argument("--out", default=os.path.join(DATA, "replication")); a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
torch.set_num_threads(2); torch.manual_seed(0)
tok = AutoTokenizer.from_pretrained(a.model); model = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.float32, low_cpu_mem_usage=True).eval()
L, H = model.config.num_hidden_layers, model.config.num_attention_heads; hd = model.config.hidden_size // H; layers = model.model.layers
sets = {"moral": pairs("moral"), "control": pairs("control"), "norm": pairs("norm")}
ids = lambda p: tok(p, return_tensors="pt").input_ids
tids = lambda ws: [tok(" " + w, add_special_tokens=False).input_ids[0] for w in ws]


def score(logits, pi, ri):
    pr = torch.softmax(logits[:, -1, :].float(), -1); return pr[:, pi].sum(-1) - pr[:, ri].sum(-1)


cache = {}


def run(x, keep=False):
    hs = []
    if keep:
        cache.clear()
        for l in range(L):
            hs.append(layers[l].self_attn.o_proj.register_forward_pre_hook(lambda m, a_, l=l: cache.__setitem__(("z", l), a_[0].detach().clone())))
            hs.append(layers[l].mlp.register_forward_hook(lambda m, a_, o, l=l: cache.__setitem__(("mlp", l), o.detach().clone())))
    with torch.no_grad(): out = model(x, logits_to_keep=1).logits
    for h in hs: h.remove()
    return out


def prep(p):
    xp, xr = ids(p["permissive_prompt"]), ids(p["restrictive_prompt"]); pi, ri = tids(p["permissive_targets"]), tids(p["restrictive_targets"])
    run(xp, True); c = dict(cache); ml = min(xp.shape[1], xr.shape[1]); return xr, pi, ri, c, ml, float(score(run(xr), pi, ri))


def mlp_patch(p):
    xr, pi, ri, c, ml, base = prep(p); hs = []
    for l in range(L):
        def hook(m, a_, o, l=l):
            o = o.clone(); o[l, :ml] = c[("mlp", l)][0, :ml]; return o
        hs.append(layers[l].mlp.register_forward_hook(hook))
    with torch.no_grad(): out = model(xr.repeat(L, 1), logits_to_keep=1).logits
    for h in hs: h.remove()
    return score(out, pi, ri).numpy() - base


def head_patch(p, B=64):
    xr, pi, ri, c, ml, base = prep(p); eff = np.zeros((L, H)); allh = [(l, h) for l in range(L) for h in range(H)]
    for s in range(0, len(allh), B):
        group = allh[s:s + B]; hs = []
        for l in sorted({g[0] for g in group}):
            def pre(m, a_, l=l):
                x = a_[0].clone()
                for b, (ll, hh) in enumerate(group):
                    if ll == l: x[b, :ml, hh * hd:(hh + 1) * hd] = c[("z", l)][0, :ml, hh * hd:(hh + 1) * hd]
                return (x,)
            hs.append(layers[l].self_attn.o_proj.register_forward_pre_hook(pre))
        with torch.no_grad(): out = model(xr.repeat(len(group), 1), logits_to_keep=1).logits
        for h in hs: h.remove()
        sc = score(out, pi, ri).numpy() - base
        for b, (l, h) in enumerate(group): eff[l, h] = sc[b]
    return eff


res = {"baseline": {}, "mlp": {}}; t0 = time.time()
for name, S in sets.items():
    for p in S:
        xp, xr = ids(p["permissive_prompt"]), ids(p["restrictive_prompt"]); pi, ri = tids(p["permissive_targets"]), tids(p["restrictive_targets"])
        res["baseline"][p["name"]] = {"set": name, "sp": float(score(run(xp), pi, ri)), "sr": float(score(run(xr), pi, ri)), "lp": xp.shape[1], "lr": xr.shape[1]}
valid = {n: [p for p in S if res["baseline"][p["name"]]["sp"] - res["baseline"][p["name"]]["sr"] > (0.02 if n == "norm" else 0.0)] for n, S in sets.items()}
print("pairs with a positive gap:", {k: len(v) for k, v in valid.items()}, flush=True)
for name in sets:
    for p in valid[name]: res["mlp"][p["name"]] = mlp_patch(p).tolist()
    print("MLP patching done:", name, f"{time.time() - t0:.0f} s", flush=True)
json.dump(res, open(os.path.join(a.out, "scores_and_mlp.json"), "w"))
check = ["stealing_medicine_vs_profit", "kill_defense_vs_revenge", "lying_protect_vs_manipulate", "t1_experiment_voluntary_vs_coerced", "t2_riot_oppression_vs_sports", "deception_war_vs_friendship"]
heads = {p["name"]: head_patch(p) for p in valid["moral"] if p["name"] in check}; np.savez(os.path.join(a.out, "heads_moral_check.npz"), **heads)
ref = np.load(os.path.join(DATA, "heads", "Llama-3.2-1B", "head_effects.npz"))
for k, v in heads.items(): print(f"  {k:40s} correlation with the stored head effects {np.corrcoef(v.ravel(), ref[k].ravel())[0, 1]:.4f}", flush=True)
random.seed(0); nv = valid["norm"][:]; random.shuffle(nv); nv = sorted(nv, key=lambda p: res["baseline"][p["name"]]["lp"] != res["baseline"][p["name"]]["lr"])[:a.n_norm]
hn = {}
for i, p in enumerate(nv):
    hn[p["name"]] = head_patch(p)
    if i % 5 == 0 or i == len(nv) - 1: np.savez(os.path.join(a.out, "heads_norm.npz"), **hn); print(f"head patching, norm pairs: {i + 1}/{len(nv)}  {time.time() - t0:.0f} s", flush=True)
