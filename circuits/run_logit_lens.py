"""The score read layer by layer through the logit lens."""
import argparse, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, load_items, model_tag, run_config_append, save_npz, existing_ok, all_present, equal_length_or_skip, first, Model, READOUT_KEYS

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids


@torch.no_grad()
def lens_trajectory(M, ids):
    grab = []
    def pre_hook(m, args, kwargs):
        h = args[0] if args else kwargs["hidden_states"]; grab.append(h[0, -1, :].detach().float().clone())
    def post_hook(m, args, out):
        grab.append(first(out)[0, -1, :].detach().float().clone())
    handles = [M.layers[0].register_forward_pre_hook(pre_hook, with_kwargs=True)] + [l.register_forward_hook(post_hook) for l in M.layers]
    try:
        x = torch.tensor([ids], device=M.device); out = M.model(input_ids=x); logits_model = out.logits[0, -1, :].float()
    finally:
        for h in handles: h.remove()
    assert len(grab) == M.L + 1, f"captured {len(grab)} residual states, expected {M.L + 1}"
    H = torch.stack(grab)
    lg = M.model.lm_head(M.norm(H.to(next(M.model.parameters()).dtype))).float()
    R = readouts(lg, M.A); err = float((lg[-1] - logits_model).norm() / (logits_model.norm() + 1e-12))
    return {k: R[k].cpu().numpy().astype(np.float32) for k in READOUT_KEYS}, err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/logit_lens")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--device", default="auto")
    ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true", help="only the accepted pairs of the run file (the analysis uses no other)")
    ap.add_argument("--tag", default=None); ap.add_argument("--any-items", action="store_true", help="software tests only")
    ap.add_argument("--allow-unequal", action="store_true", help="the original pairs: skip pairs whose prompts differ in token count")
    ap.add_argument("--config-only", default=None, help="software tests only: a model name whose CONFIG is used to build a tiny random-weight model")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[run_logit_lens] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model)
    if all_present(os.path.join(args.out, tag), args.frames, items, sha): print(f"[run_logit_lens] {tag}: every result file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_logit_lens] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4
        cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg)
    print(f"[run_logit_lens] layers={M.L}", flush=True)
    out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    run_config_append(out, {"script": "run_logit_lens.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha,
                            "frames": args.frames, "n_items": len(items), "accepted_only": args.accepted_only, "n_layers": M.L, "readouts": list(READOUT_KEYS)})
    todo = [(f, it) for f in args.frames for it in items]; t0 = time.time(); masses = []; checked = False
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, sha): continue
        if not equal_length_or_skip(M, f, it, args.allow_unequal): continue
        t1 = time.time(); res = {}; errs = []
        for side in ("perm", "rest"):
            ids = encode(M.tok, FRAMES[f](it[f"{side}_stem"])); R, err = lens_trajectory(M, ids); errs.append(err)
            for k, v in R.items(): res[f"{side}_{k}"] = v
        if not checked:
            print(f"[run_logit_lens] the lens at the output layer vs the model's logits: rel. err = {max(errs):.2e}", flush=True)
            if max(errs) > 1e-3: sys.exit("[run_logit_lens] the final norm + unembedding do not reproduce the model's own logits; stopping (unexpected architecture?)")
            checked = True
        meta = dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, n_layers=M.L, n_tok=len(ids),
                    readouts=list(READOUT_KEYS), lens_rel_err=round(max(errs), 8), seconds=round(time.time() - t1, 2))
        save_npz(path, meta, res); masses.append(float(res["perm_mass"][-1]))
        shown = f"gap(S)={float(res['perm_S'][-1]) - float(res['rest_S'][-1]):+.3f} " if args.any_items else ""
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} {shown}mean answer-word mass so far={np.mean(masses):.2f} ntok={len(ids)} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
    print("[run_logit_lens] finished", flush=True)


if __name__ == "__main__":
    main()
