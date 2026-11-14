"""Run 08 on Llama-3.2-1B (CPU, float32): (a) the moral-versus-neutral features of the layer-7 dictionary when the frame word is swapped; (b) the late-layer dip read through the logit lens on moral, control and norm pairs."""
import argparse, json, os, random
import numpy as np, torch
from safetensors.torch import load_file
from transformers import AutoModelForCausalLM, AutoTokenizer
from pairs_common import HERE, DATA, ACTIVATIONS, pairs, bh, save

ap = argparse.ArgumentParser(); ap.add_argument("--model", default="meta-llama/Llama-3.2-1B")
ap.add_argument("--sae", default=os.path.join(HERE, "..", "dictionaries", "llama-3.2-1B-base", "sae_weights.safetensors")); a = ap.parse_args()
torch.set_num_threads(2); torch.manual_seed(0)
tok = AutoTokenizer.from_pretrained(a.model); model = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.float32, low_cpu_mem_usage=True).eval(); LAYER = 7
moral, ctrl, norm, neut = pairs("moral"), pairs("control"), pairs("norm"), pairs("neutral")
base = json.load(open(os.path.join(DATA, "replication", "scores_and_mlp.json")))["baseline"]
ids = lambda p: tok(p, return_tensors="pt").input_ids
tids = lambda ws: [tok(" " + w, add_special_tokens=False).input_ids[0] for w in ws]


def hidden(prompt):
    with torch.no_grad(): out = model(ids(prompt), output_hidden_states=True, logits_to_keep=1)
    return [h[0, -1, :] for h in out.hidden_states]


w = load_file(a.sae); W_enc, b_enc, W_dec, b_dec = (w[k].float() for k in ("W_enc", "b_enc", "W_dec", "b_dec")); dn = W_dec.norm(dim=-1)


def encode(x, k=64):
    pre = torch.relu((x - b_dec) @ W_enc + b_enc) * dn; v, i = torch.topk(pre, k, dim=-1); f = torch.zeros_like(pre); f.scatter_(-1, i, v); return f


feats = lambda prompts: torch.stack([encode(hidden(p)[LAYER + 1]) for p in prompts]).numpy()
out = {}
ref = np.load(os.path.join(ACTIVATIONS, "llama-3.2-1B-base", "moral.npz")); names = [str(n) for n in ref["names"]]; mp = {p["name"]: p for p in moral}
mine = feats([mp[n]["permissive_prompt"] for n in names[:12]])
out["encoder_check"] = {"max_abs_diff": float(np.abs(mine - ref["perm"][:12]).max()), "same_active_set": float(((mine > 0) == (ref["perm"][:12] > 0)).mean())}; print(out["encoder_check"], flush=True)
s = np.load(os.path.join(DATA, "features", "llama-3.2-1B-base", "vs_neutral.npz")); sig = np.where(bh((s["r_count"] + 1) / (int(s["done"]) + 1)) < .05)[0]
swap = lambda p, word: " ".join(p.split()[:-1]) + " " + word
both = lambda S: [p["permissive_prompt"] for p in S] + [p["restrictive_prompt"] for p in S]
random.seed(0); norm_s = random.sample(norm, 110)
variants = {"moral, is morally": both(moral), "norm, is morally": both(norm_s), "neutral, is typically": both(neut), "neutral content, is morally": [swap(p, "morally") for p in both(neut)],
            "moral content, is typically": [swap(p, "typically") for p in both(moral)], "norm content, is typically": [swap(p, "typically") for p in both(norm_s)]}
out["n_features"] = int(len(sig)); out["frame_swap"] = {}
for tag, prompts in variants.items():
    A = feats(prompts)[:, sig]
    out["frame_swap"][tag] = {"n_prompts": len(prompts), "mean_activation": float(A.mean()), "frac_features_on_ge_10pct_of_prompts": float(((A > 0).mean(0) >= .10).mean()),
                              "frac_features_never_firing": float(((A > 0).sum(0) == 0).mean())}
    print(tag, out["frame_swap"][tag], flush=True)
fn, lm = model.model.norm, model.lm_head


def dip(p):
    pi, ri = tids(p["permissive_targets"]), tids(p["restrictive_targets"])
    with torch.no_grad(): pr = [torch.softmax(lm(fn(h)), -1) for h in hidden(p["permissive_prompt"])]
    tr = np.array([float(x[pi].sum() - x[ri].sum()) for x in pr]); half = len(tr) // 2; mi = half + int(np.argmin(tr[half:-1])); peak = tr[:mi].max() if mi > 0 else tr[0]
    return float(peak - tr[mi]), bool(tr[mi] < 0 and tr[-1] > 0)


out["dip"] = {}
for tag, S, thr in (("moral", moral, 0.0), ("control", ctrl, 0.0), ("norm", norm, 0.02)):
    v = [p for p in S if base[p["name"]]["sp"] - base[p["name"]]["sr"] > thr]; d = [dip(p) for p in v]; dd = np.array([x[0] for x in d])
    gap = np.array([base[p["name"]]["sp"] - base[p["name"]]["sr"] for p in v])
    out["dip"][tag] = {"n": len(v), "mean": float(dd.mean()), "sd": float(dd.std()), "median": float(np.median(dd)), "mean_relative_to_gap": float(dd.mean() / gap.mean()), "median_relative_to_gap": float(np.median(dd / gap)), "sign_reversal_rate": float(np.mean([x[1] for x in d]))}
    print("dip", tag, out["dip"][tag], flush=True)
save("run_08_frame_swap_and_dip.json", out)
