"""The models' own valence of the single words of the stems."""
import argparse, json, os, re, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import FRAMES, encode, readouts, pick_device, model_tag, run_config_append, Model, READOUT_KEYS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import primary_item_set

STOP = set("""a an the and or but of to in on at for with from by as into onto over under about after before during while when if than then that this these those
his her their its your our my one's someone's one someone anyone everyone it he she they we you i is are be being been was were not no nor so too very
up down out off through again only also just more most less least own same other another each every all any some such what which who whom whose how why
where there here""".split())


def content_words(stem):
    return [w for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", stem) if w.lower() not in STOP]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/word_valence")
    ap.add_argument("--frames", nargs="+", default=["B"], choices=list(FRAMES)); ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"])
    ap.add_argument("--tag", default=None); ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    ok, why = primary_item_set(args.items)
    if not ok and not args.any_items: sys.exit(f"[run_word_valence] {why}; the words come from the accepted pairs (stimuli/items_final.json). Other item files: add --any-items.")
    items = json.load(open(args.items)); items = [i for i in items if i.get("accepted", True)]
    words = sorted({w[0].upper() + w[1:] for it in items for side in ("perm_stem", "rest_stem") for w in content_words(it[side])})
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    todo = [f for f in args.frames if not os.path.exists(os.path.join(out, f"words__{f}.json"))]
    if not todo: print(f"[run_word_valence] {tag}: every word file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_word_valence] model={args.model} device={dev} words={len(words)} frames={todo}", flush=True)
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg)
    run_config_append(out, {"script": "run_word_valence.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "n_items": len(items), "n_words": len(words), "frames": todo})
    for f in todo:
        res = {}; t0 = time.time()
        with torch.no_grad():
            for n, w in enumerate(words):
                ids = encode(M.tok, FRAMES[f](w)); x = torch.tensor([ids], device=M.device); lg = M.model(input_ids=x).logits[0, -1, :][None]; R = readouts(lg, M.A)
                res[w] = {k: float(R[k][0]) for k in READOUT_KEYS}
                if (n + 1) % 100 == 0: print(f"[run_word_valence] {f} {n + 1}/{len(words)}  {(time.time() - t0) / 60:.1f} min", flush=True)
        tmp = os.path.join(out, f"words__{f}.json.tmp"); json.dump({"frame": f, "prompt": FRAMES[f]("<Word>"), "model": args.model, "values": res}, open(tmp, "w"), indent=0); os.replace(tmp, os.path.join(out, f"words__{f}.json"))
        v = np.array([r["S"] for r in res.values()]); print(f"[run_word_valence] {f}: {len(res)} words; S mean {v.mean():+.3f}, {int((v < 0).sum())} negative", flush=True)
    print("[run_word_valence] finished", flush=True)


if __name__ == "__main__":
    main()
