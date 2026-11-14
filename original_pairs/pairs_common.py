"""Shared helpers for the analyses on the original pairs."""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
RESULTS = os.path.join(HERE, "results")
STIMULI = os.path.join(HERE, "..", "stimuli")
ACTIVATIONS = os.path.join(DATA, "activations")      # <dictionary>/{moral,neutral,norm}.npz: final-token feature activations of the original pairs
MODELS = ["Llama-3.2-1B", "Llama-3.2-1B-Instruct", "Llama-3.2-3B", "Llama-3.2-3B-Instruct", "gemma-2b", "gemma-2b-it", "Qwen2.5-3B", "Qwen2.5-3B-Instruct",
          "Qwen2.5-7B", "Qwen2.5-7B-Instruct", "Llama-3.1-8B", "Llama-3.1-8B-Instruct", "Qwen2.5-14B", "Qwen2.5-14B-Instruct"]
BASE_INSTRUCT = [("Llama-3.2-1B", "Llama-3.2-1B-Instruct"), ("gemma-2b", "gemma-2b-it"), ("Qwen2.5-3B", "Qwen2.5-3B-Instruct"), ("Llama-3.2-3B", "Llama-3.2-3B-Instruct"),
                 ("Qwen2.5-7B", "Qwen2.5-7B-Instruct"), ("Llama-3.1-8B", "Llama-3.1-8B-Instruct"), ("Qwen2.5-14B", "Qwen2.5-14B-Instruct")]
DICTIONARIES = ["llama-3.2-1B-base", "llama-3.2-1B-base-k128", "llama-3.2-1B-IT", "llama-3.2-1B-IT-k128", "llama-3.2-1B-base-MLP0", "llama-3.2-3B-base",
                "llama-3.2-3B-base-k128", "llama-3.2-3B-IT-k128", "llama-3.2-3B-IT-L3", "llama-3.2-3B-IT-L7", "llama-3.2-3B-IT-L19", "llama-3.1-8B-base",
                "qwen-2.5-7b-base", "qwen-2.5-7b-IT"]


def pairs(kind):
    """kind: moral, control, norm or neutral."""
    return json.load(open(os.path.join(STIMULI, f"original_{kind}_pairs.json")))


def head_effects(model):
    """|head effect| per pair, flattened over (layer, head): moral matrix, control matrix, pair names, number of heads per layer."""
    z = np.load(os.path.join(DATA, "heads", model, "head_effects.npz")); zc = np.load(os.path.join(DATA, "heads", model, "control_head_effects.npz"))
    mn, cn = list(z.files), list(zc.files)
    M = np.stack([np.abs(z[k]).ravel() for k in mn]); C = np.stack([np.abs(zc[k]).ravel() for k in cn])
    return M, C, mn, cn, z[mn[0]].shape[1]


def shares(X):
    return X / X.sum(1, keepdims=True)


def top_head(model):
    """The first located head of a model (located/heads.json)."""
    l, h = json.load(open(os.path.join(HERE, "..", "located", "heads.json")))[model]["located"][0]
    return l, h


def bh(p):
    p = np.asarray(p, dtype=float); n = len(p); o = np.argsort(p); q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]
    r = np.empty(n); r[o] = np.minimum(q, 1); return r


def perm_test(A, B, nperm, seed, chunk=2000):
    """One-sided permutation test of mean(A) > mean(B) per column; returns the difference, p and the Benjamini-Hochberg q."""
    na, nb = len(A), len(B); X = np.concatenate([A, B]); n = na + nb; tot = X.sum(0); obs = A.mean(0) - B.mean(0)
    rng = np.random.default_rng(seed); r = np.zeros(X.shape[1]); done = 0
    while done < nperm:
        k = min(chunk, nperm - done); idx = np.argsort(rng.random((k, n)), axis=1)[:, :na]; W = np.zeros((k, n)); np.put_along_axis(W, idx, 1.0, axis=1)
        sm = W @ X; r += ((sm / na - (tot - sm) / nb) >= obs - 1e-15).sum(0); done += k
    p = (r + 1) / (nperm + 1); return obs, p, bh(p)


def family(model):
    return "llama" if model.lower().startswith("llama") else ("gemma" if model.lower().startswith("gemma") else "qwen")


def token_counter():
    """Number of tokens of a text in the Llama-3, Qwen2.5 and Gemma tokenizers (no special tokens)."""
    from transformers import AutoTokenizer
    T = {"llama": AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B"), "qwen": AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B"), "gemma": AutoTokenizer.from_pretrained("google/gemma-2b")}
    return lambda fam, text: len(T[fam](text, add_special_tokens=False).input_ids)


def save(name, obj):
    os.makedirs(RESULTS, exist_ok=True); json.dump(obj, open(os.path.join(RESULTS, name), "w"), indent=1)
