"""The category prompt: which standard the model assigns to a phrase."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import encode, pick_device, load_items, model_tag, run_config_append, Model
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import accepted_ids, first_token_id

CATEGORY_WORDS = {"moral": ["morality", "ethics"], "prudential": ["prudence", "safety"], "etiquette": ["manners", "politeness"],
                  "aesthetic": ["taste", "beauty"], "epistemic": ["evidence", "logic"], "descriptive": ["fact", "chance"]}
FEWSHOT = ("Keeping a promise to a friend is a matter of morality.\n"
           "Wearing a helmet on a motorcycle is a matter of safety.\n"
           "Thanking the host before leaving is a matter of manners.\n"
           "Choosing the colours of a painting is a matter of taste.\n"
           "Checking the sources before publishing is a matter of evidence.\n")
PRESETS = {"zeroshot": lambda stem: f"{stem} is a matter of", "fewshot": lambda stem: f"{FEWSHOT}{stem} is a matter of"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items"); ap.add_argument("--out", default="runs/category_frame")
    ap.add_argument("--presets", nargs="+", default=["zeroshot", "fewshot"], choices=list(PRESETS)); ap.add_argument("--device", default="auto")
    ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--accepted-only", action="store_true"); ap.add_argument("--tag", default=None); ap.add_argument("--any-items", action="store_true", help="software tests only")
    ap.add_argument("--check-words", action="store_true", help="print how the tokenizer splits the category words and exit"); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    if args.check_words:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained(args.model)
        for c, ws in CATEGORY_WORDS.items():
            for w in ws:
                ids = tok(" " + w, add_special_tokens=False).input_ids; print(f"{c:12s} {w:12s} {len(ids)} token(s): {[tok.decode([i]) for i in ids]}")
        return
    items, sha = load_items(args.items, args.any_items, args.limit)
    if args.accepted_only:
        acc = accepted_ids(); items = [it for it in items if it["id"] in acc]; print(f"[run_category_frame] accepted items only: {len(items)}", flush=True)
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    todo = [p for p in args.presets if not os.path.exists(os.path.join(out, f"cat__{p}.json"))]
    if not todo: print(f"[run_category_frame] {tag}: every preset is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_category_frame] model={args.model} device={dev} presets={todo} items={len(items)}", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg)
    words = {c: {w: first_token_id(M.tok, w, False) for w in ws} for c, ws in CATEGORY_WORDS.items()}
    single = {c: {w: len(M.tok(" " + w, add_special_tokens=False).input_ids) == 1 for w in ws} for c, ws in CATEGORY_WORDS.items()}
    print("[run_category_frame] category words (single token?): " + "; ".join(f"{c}: " + ", ".join(f"{w}{'' if single[c][w] else '*'}" for w in ws) for c, ws in CATEGORY_WORDS.items()) + "   (* = first token of a multi-token word)", flush=True)
    run_config_append(out, {"script": "run_category_frame.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "n_items": len(items),
                            "accepted_only": args.accepted_only, "presets": todo, "category_words": CATEGORY_WORDS, "single_token": single, "fewshot_prefix": FEWSHOT})
    all_ids = [i for c in words.values() for i in c.values()]
    for preset in todo:
        rows = []; t0 = time.time()
        with torch.no_grad():
            for n, it in enumerate(items):
                for side in ("perm", "rest"):
                    ids = encode(M.tok, PRESETS[preset](it[f"{side}_stem"])); x = torch.tensor([ids], device=M.device)
                    pr = torch.softmax(M.model(input_ids=x).logits[0, -1, :].float(), -1)
                    pw = {c: {w: float(pr[i]) for w, i in ws.items()} for c, ws in words.items()}; ps = {c: sum(v.values()) for c, v in pw.items()}; tot = sum(ps.values())
                    rows.append(dict(id=it["id"], side=side, category=it["category"], subtype=it.get("subtype", ""), p_words=pw, p_sets=ps, p_norm={c: v / tot for c, v in ps.items()} if tot > 0 else None, covered=float(tot)))
                if (n + 1) % 50 == 0: print(f"[run_category_frame] {preset} {n + 1}/{len(items)}  {(time.time() - t0) / 60:.1f} min", flush=True)
        tmp = os.path.join(out, f"cat__{preset}.json.tmp"); json.dump({"preset": preset, "prompt": PRESETS[preset]("<stem>"), "model": args.model, "items_sha256": sha, "rows": rows}, open(tmp, "w"), indent=0); os.replace(tmp, os.path.join(out, f"cat__{preset}.json"))
        cov = np.mean([r["covered"] for r in rows]); print(f"[run_category_frame] {preset}: {len(rows)} prompts; the category words cover {cov:.1%} of the next-token distribution on average", flush=True)
    print("[run_category_frame] finished", flush=True)


if __name__ == "__main__":
    main()
