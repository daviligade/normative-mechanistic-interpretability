"""Model wrapper and helpers shared by the circuit scripts."""
import os, sys, json, hashlib, time
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import FRAMES, PRIME, POS, NEG, answer_ids, encode, readouts, check_run_file, RUN_FILE

GROUPS = ["bos", "priming", "stem_before_edit", "edit", "stem_after_edit", "cue"]
READOUT_KEYS = ("S", "LD", "S_hist", "mass", "LD_gb")
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def pick_device(name):
    if name != "auto": return name
    if torch.cuda.is_available(): return "cuda"
    if getattr(torch.backends, "mps", None) is not None and torch.backends.mps.is_available(): return "mps"
    return "cpu"


def first(x):
    return x[0] if isinstance(x, (tuple, list)) else x


class Model:

    def __init__(self, model_name, device, dtype="float32", eager=False, config_only=None):
        from transformers import AutoModelForCausalLM, AutoTokenizer
        td = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[dtype]
        self.tok = AutoTokenizer.from_pretrained(model_name)
        if config_only is not None:
            if eager: config_only._attn_implementation = "eager"
            self.model = AutoModelForCausalLM.from_config(config_only).to(td)
        else:
            kw = {"low_cpu_mem_usage": True}
            if eager: kw["attn_implementation"] = "eager"
            try: self.model = AutoModelForCausalLM.from_pretrained(model_name, dtype=td, **kw)
            except TypeError: self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=td, **kw)
        self.model.to(device).eval(); self.device = device; self.eager = eager
        for p in self.model.parameters(): p.requires_grad_(False)
        cfg = self.model.config; self.L, self.H = cfg.num_hidden_layers, cfg.num_attention_heads
        self.Hkv = getattr(cfg, "num_key_value_heads", None) or self.H
        self.hd = getattr(cfg, "head_dim", None) or cfg.hidden_size // cfg.num_attention_heads; self.d = cfg.hidden_size
        self.layers = self.model.model.layers; self.norm = self.model.model.norm
        assert self.layers[0].self_attn.o_proj.in_features == self.H * self.hd, "unexpected attention layout"
        assert self.H % self.Hkv == 0
        self.A = {k: (torch.tensor(v, device=device) if isinstance(v, list) else v) for k, v in answer_ids(self.tok).items()}
        self.W_U = self.model.lm_head.weight
        self.u_dir = (self.W_U[self.A["pos"]].float().mean(0) - self.W_U[self.A["neg"]].float().mean(0))
        self.gb_dir = (self.W_U[self.A["good"]].float() - self.W_U[self.A["bad"]].float())
        self.norm_w = (1.0 + self.norm.weight.float()) if "gemma" in type(self.norm).__name__.lower() else self.norm.weight.float()
        self.norm_eps = getattr(self.norm, "variance_epsilon", None) or getattr(self.norm, "eps", 1e-6)

    def kv_group(self, h):
        return h // (self.H // self.Hkv)

    def forward_logits(self, ids_batch, **kw):
        x = torch.tensor(ids_batch, device=self.device) if not torch.is_tensor(ids_batch) else ids_batch
        out = self.model.model(input_ids=x, **kw)
        return self.model.lm_head(out.last_hidden_state[:, -1, :])

    def metric(self, lg):
        lg = lg.float(); return lg[:, self.A["pos"]].mean(-1) - lg[:, self.A["neg"]].mean(-1)

    def norm_scale(self, h):
        h = h.float(); rms = torch.sqrt(h.pow(2).mean(-1, keepdim=True) + self.norm_eps)
        return self.norm_w / rms

    def check_norm_scale(self, h):
        with torch.no_grad():
            ref = self.norm(h.to(self.W_U.dtype)).float(); mine = self.norm_scale(h) * h.float()
            return float((ref - mine).abs().max() / ref.abs().max().clamp_min(1e-6))

    def head_outputs(self, z, l):
        W = self.layers[l].self_attn.o_proj.weight.float()
        zz = z.float().view(*z.shape[:-1], self.H, self.hd)
        return torch.einsum("bnhk,dhk->bnhd", zz, W.view(self.d, self.H, self.hd))


def token_groups(M, frame, item):
    texts = {"perm": FRAMES[frame](item["perm_stem"]), "rest": FRAMES[frame](item["rest_stem"])}
    ids = {k: encode(M.tok, t) for k, t in texts.items()}
    if len(ids["perm"]) != len(ids["rest"]): raise ValueError("the two prompts differ in token count")
    diff = [i for i, (a, b) in enumerate(zip(ids["perm"], ids["rest"])) if a != b]
    e0, e1 = (min(diff), max(diff) + 1) if diff else (0, 0)
    offs = M.tok(texts["perm"], add_special_tokens=False, return_offsets_mapping=True)["offset_mapping"]
    assert len(offs) == len(ids["perm"]) - 1, "offset mapping does not match the token count"
    prime_len = len(PRIME) if texts["perm"].startswith(PRIME) else 0
    stem_end = prime_len + len(item["perm_stem"])
    g = np.zeros(len(ids["perm"]), dtype=np.int8)
    for i, (a, b) in enumerate(offs, start=1):
        if prime_len and b <= prime_len: g[i] = 1
        elif prime_len and a < prime_len < b: g[i] = 1 if (prime_len - a) >= (b - prime_len) else 2
        elif a >= stem_end: g[i] = 5
        else: g[i] = 2
    for i in range(1, len(g)):
        if g[i] == 2 and i >= e1 and e1 > 0: g[i] = 4
    for i in range(e0, e1): g[i] = 3
    if e1 > 0 and not (g[e0:e1] == 3).all(): raise AssertionError("edit span not inside the stem")
    return ids, g, (e0, e1)


def sha(path): return hashlib.sha256(open(path, "rb").read()).hexdigest()


def load_items(path, any_items, limit=0, categories=None):
    s = sha(path); check_run_file(path, s, any_items)
    items = json.load(open(path))
    if categories: items = [it for it in items if it["category"] in categories]
    if limit: items = items[:limit]
    return items, s


SETS_FILE = os.path.join(ROOT, "located", "heads_old.json")


def head_sets(tag, path=None):
    path = path or SETS_FILE; fz = json.load(open(path))
    if tag not in fz: sys.exit(f"[circuits] no located head sets for model tag {tag!r} in {path}; known tags: {sorted(fz)}")
    e = fz[tag]; sets = {"located": e["located"], "topshare10": e["topshare10"], "located_top5": e["located_top5"], "located_top1": e["located_top1"]}
    return {k: [tuple(int(x) for x in p) for p in v] for k, v in sets.items()}, e


def random_head_sets(tag, L, H, sizes=(10, 5, 1), n_sets=20, seed=20261006, exclude=()):
    rng = np.random.default_rng(seed + int(hashlib.sha256(tag.encode()).hexdigest(), 16) % 10**6)
    pool = [(l, h) for l in range(L) for h in range(H) if (l, h) not in set(exclude)]; out = {}
    if len(pool) < max(sizes):
        print("[circuits] too few heads outside the located sets; random sets are drawn from all heads", flush=True); pool = [(l, h) for l in range(L) for h in range(H)]
    for size in sizes:
        out[size] = [[pool[i] for i in rng.choice(len(pool), size=size, replace=False)] for _ in range(n_sets)]
    return out


def save_npz(path, meta, arrays):
    tmp = path + ".tmp.npz"; np.savez_compressed(tmp, __meta__=np.array(json.dumps(meta)), **arrays); os.replace(tmp, path)


def existing_ok(path, items_sha):
    if not os.path.exists(path): return False
    try: z = np.load(path, allow_pickle=False); meta = json.loads(str(z["__meta__"]))
    except Exception as e: print(f"[circuits] unreadable file, recomputing: {path} ({type(e).__name__})", flush=True); return False
    if meta.get("items_sha256") != items_sha: sys.exit(f"[circuits] {path} was made from a different item file; move it away or use another --out / --tag")
    return True


def all_present(out_dir, frames, items, items_sha, extra=()):
    if not os.path.isdir(out_dir): return False
    for name in extra:
        if not os.path.exists(os.path.join(out_dir, name)): return False
    for f in frames:
        for it in items:
            p = os.path.join(out_dir, f"{f}__{it['id']}.npz")
            if not os.path.exists(p): return False
            try:
                if json.loads(str(np.load(p, allow_pickle=False)["__meta__"])).get("items_sha256") != items_sha: return False
            except Exception: return False
    return True


def run_config_append(out_dir, entry):
    import transformers
    p = os.path.join(out_dir, "run_config.json"); hist = json.load(open(p)) if os.path.exists(p) else []
    hist.append(dict(entry, torch=torch.__version__, transformers=transformers.__version__, started=time.strftime("%Y-%m-%d %H:%M:%S")))
    json.dump(hist, open(p, "w"), indent=1)


def model_tag(name): return name.rstrip("/").split("/")[-1]


def progress(done, total, frame, item_id, t0, extra, blind):
    el = time.time() - t0
    print(f"[{done}/{total}] {frame} {item_id:10s} {extra if (not blind) or extra.startswith('mass') else ''} elapsed={el / 60:.1f} min", flush=True)


def equal_length_or_skip(M, frame, item, allow_skip):
    pi, ri = encode(M.tok, FRAMES[frame](item["perm_stem"])), encode(M.tok, FRAMES[frame](item["rest_stem"]))
    if len(pi) == len(ri): return True
    if allow_skip: print(f"[circuits] skipping {item['id']} ({frame}): the two prompts differ in token count (the original pairs only)", flush=True); return False
    sys.exit(f"[circuits] item {item['id']} frame {frame}: the two prompts differ in token count; the study items never should")
