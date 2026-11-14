"""Jacobian-lens readout of the category words at the final position."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, load_items, model_tag, run_config_append, save_npz, existing_ok, Model, READOUT_KEYS
from run_category_frame import CATEGORY_WORDS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids, first_token_id

EXTRA_WORDS = ["moral", "immoral", "ethical", "unethical", "wrong", "harm", "harmful", "unfair", "dishonest", "cruel", "selfish", "rude", "impolite", "unsafe", "risky",
               "dangerous", "stupid", "ugly", "tasteless", "false", "illogical", "mistake", "crime", "sin", "duty", "consent", "safety", "manners", "beauty", "evidence"]
TOPK = 20


def block_outputs(M, ids):
    rec = {}
    def hook(l):
        def f(m, a_, out): rec[l] = (out[0] if isinstance(out, tuple) else out)[0, -1, :].detach().float()
        return f
    hs = [M.layers[l].register_forward_hook(hook(l)) for l in range(M.L)]
    try:
        with torch.no_grad(): lg = M.model(input_ids=torch.tensor([ids], device=M.device)).logits[0, -1, :].float()
    finally:
        for h in hs: h.remove()
    return torch.stack([rec[l] for l in range(M.L)]), lg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--lens", required=True, help="lens.pt of circuits/jlens_fit.py"); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/jlens_readout")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"]); ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[jlens_readout] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); dev = pick_device(args.device)
    L = torch.load(args.lens, map_location="cpu", weights_only=True); J = {int(l): v.float() for l, v in L["J"].items()}; src_layers = sorted(J)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg)
    assert J[src_layers[0]].shape[0] == M.d, f"lens d_model {J[src_layers[0]].shape[0]} differs from the model's {M.d}"
    Jd = {l: v.to(M.device) for l, v in J.items()}
    sets = {c: [first_token_id(M.tok, w, False) for w in ws] for c, ws in CATEGORY_WORDS.items()}; extra = {w: first_token_id(M.tok, w, False) for w in EXTRA_WORDS}
    set_names = list(sets); extra_names = list(extra)
    print(f"[jlens_readout] model={args.model} device={dev} lens layers {src_layers[0]}..{src_layers[-1]} ({len(src_layers)}) + final; items={len(items)} frames={args.frames}", flush=True)
    run_config_append(out, {"script": "run_jlens_readout.py", "model": args.model, "lens": args.lens, "lens_n_prompts": int(L.get("n_prompts", 0)), "device": dev, "dtype": args.dtype, "items_file": args.items, "items_sha256": sha, "n_items": len(items),
                            "frames": args.frames, "category_words": CATEGORY_WORDS, "extra_words": EXTRA_WORDS, "topk": TOPK, "layers": "every block output, transported with J_l; the last row is the model's own logits"})
    def read(logits):
        R = readouts(logits[None], M.A); lp = torch.log_softmax(logits, -1)
        set_lp = [float(torch.logsumexp(lp[torch.tensor(sets[c], device=lp.device)], 0)) for c in set_names]; ex_lp = [float(lp[extra[w]]) for w in extra_names]
        top = torch.topk(logits, TOPK); return {k: float(R[k][0]) for k in READOUT_KEYS}, set_lp, ex_lp, top.indices.cpu().numpy(), top.values.cpu().numpy()
    with torch.no_grad():
        for f in args.frames:
            t0 = time.time()
            for n, it in enumerate(items):
                path = os.path.join(out, f"{f}__{it['id']}.npz")
                if existing_ok(path, sha): continue
                res = {}
                for s in ("perm", "rest"):
                    H, lg = block_outputs(M, encode(M.tok, FRAMES[f](it[f"{s}_stem"])))
                    rows_R = {k: [] for k in READOUT_KEYS}; rows_set, rows_ex, rows_ti, rows_tv = [], [], [], []
                    for l in range(M.L):
                        if l in Jd: logits = M.model.lm_head(M.norm(H[l] @ Jd[l].T)[None])[0].float()
                        elif l == M.L - 1: logits = lg
                        else: logits = M.model.lm_head(M.norm(H[l])[None])[0].float()
                        R, slp, elp, ti, tv = read(logits)
                        for k in READOUT_KEYS: rows_R[k].append(R[k])
                        rows_set.append(slp); rows_ex.append(elp); rows_ti.append(ti); rows_tv.append(tv)
                    for k in READOUT_KEYS: res[f"{s}_{k}"] = np.array(rows_R[k], dtype=np.float32)
                    res[f"{s}_set_logp"] = np.array(rows_set, dtype=np.float32); res[f"{s}_extra_logp"] = np.array(rows_ex, dtype=np.float32); res[f"{s}_top_ids"] = np.array(rows_ti, dtype=np.int64); res[f"{s}_top_logits"] = np.array(rows_tv, dtype=np.float32)
                meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, n_layers=M.L, lens_layers=src_layers, set_names=set_names, extra_names=extra_names)
                save_npz(path, meta, res)
                if (n + 1) % 25 == 0: print(f"[jlens_readout] {f} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
    print("[jlens_readout] finished", flush=True)


if __name__ == "__main__":
    main()
