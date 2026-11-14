"""Fit of a Jacobian lens on general text."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import pick_device, model_tag, run_config_append

MIN_WORDS = 60


DEFAULT_CORPUS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stimuli", "jlens_corpus.txt")


def load_prompts(args, rng):
    if args.corpus == "file":
        path = args.corpus_file or DEFAULT_CORPUS
        if not os.path.exists(path): sys.exit(f"[jlens_fit] corpus file not found: {path}")
        paras = [l.strip() for l in open(path, encoding="utf-8") if len(l.split()) >= MIN_WORDS]; src = os.path.relpath(path)
    else:
        try:
            from datasets import load_dataset
            ds = load_dataset("Salesforce/wikitext", "wikitext-103-raw-v1", split=args.split)
        except Exception as e:
            sys.exit(f"[jlens_fit] could not load WikiText-103 from the hub ({type(e).__name__}: {e}); use the default corpus file (--corpus file) or pass --corpus-file")
        paras = [t.strip() for t in ds["text"] if len(t.split()) >= MIN_WORDS and not t.strip().startswith("=")]; src = f"Salesforce/wikitext wikitext-103-raw-v1/{args.split}"
    if len(paras) < args.n_prompts: sys.exit(f"[jlens_fit] only {len(paras)} paragraphs with >= {MIN_WORDS} words in {src}; need {args.n_prompts}")
    idx = rng.choice(len(paras), args.n_prompts, replace=False); return [paras[i] for i in sorted(idx)], src


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--out", default="runs/jlens"); ap.add_argument("--tag", default=None)
    ap.add_argument("--n-prompts", type=int, default=100); ap.add_argument("--max-seq-len", type=int, default=128); ap.add_argument("--dim-batch", type=int, default=8, help="output dimensions per backward pass (memory; FLOPs unchanged)")
    ap.add_argument("--target-layer", type=int, default=None, help="default: the final block; the authors note the penultimate block can be better conditioned")
    ap.add_argument("--corpus", default="file", choices=["file", "hub"], help="file: --corpus-file or the default stimuli/jlens_corpus.txt; hub: WikiText-103 through `datasets`")
    ap.add_argument("--corpus-file", default=None); ap.add_argument("--split", default="test"); ap.add_argument("--seed", type=int, default=20261022)
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"])
    args = ap.parse_args()
    try:
        import jlens
    except ImportError:
        sys.exit("[jlens_fit] the `jlens` package is missing: git clone https://github.com/anthropics/jacobian-lens.git external/jacobian-lens && pip install -e external/jacobian-lens")
    from transformers import AutoModelForCausalLM, AutoTokenizer
    jlens.configure_logging()
    tag = args.tag or model_tag(args.model); out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True); dev = pick_device(args.device); rng = np.random.default_rng(args.seed)
    lens_path = os.path.join(out, "lens.pt")
    if os.path.exists(lens_path): print(f"[jlens_fit] {lens_path} exists; nothing to do", flush=True); return
    pfile = os.path.join(out, "prompts.json")
    if os.path.exists(pfile): P = json.load(open(pfile)); prompts, src = P["prompts"], P["source"]; print(f"[jlens_fit] prompts reloaded from {pfile} ({len(prompts)})", flush=True)
    else:
        prompts, src = load_prompts(args, rng); json.dump({"source": src, "n": len(prompts), "seed": args.seed, "min_words": MIN_WORDS, "prompts": prompts}, open(pfile, "w"))
    print(f"[jlens_fit] {len(prompts)} prompts from {src}", flush=True)
    td = {"float32": torch.float32, "float16": torch.float16, "bfloat16": torch.bfloat16}[args.dtype]
    tok = AutoTokenizer.from_pretrained(args.model)
    try: hf = AutoModelForCausalLM.from_pretrained(args.model, dtype=td, low_cpu_mem_usage=True)
    except TypeError: hf = AutoModelForCausalLM.from_pretrained(args.model, torch_dtype=td, low_cpu_mem_usage=True)
    hf.to(dev); model = jlens.from_hf(hf, tok)
    print(f"[jlens_fit] model={args.model} device={dev} layers={model.n_layers} d_model={model.d_model} prompts={len(prompts)} max_seq_len={args.max_seq_len} dim_batch={args.dim_batch} "
          f"-> {int(np.ceil(model.d_model / args.dim_batch))} backward passes per prompt", flush=True)
    run_config_append(out, {"script": "jlens_fit.py", "model": args.model, "device": dev, "dtype": args.dtype, "n_prompts": len(prompts), "corpus": src, "max_seq_len": args.max_seq_len, "dim_batch": args.dim_batch,
                            "target_layer": args.target_layer, "seed": args.seed, "jlens_version": getattr(jlens, "__version__", "0.1.0")})
    t0 = time.time()
    lens = jlens.fit(model, prompts, target_layer=args.target_layer, dim_batch=args.dim_batch, max_seq_len=args.max_seq_len, checkpoint_path=os.path.join(out, "ckpt.pt"), checkpoint_every=1, resume=True)
    lens.save(lens_path)
    print(f"[jlens_fit] saved {lens_path} ({lens}) in {(time.time() - t0) / 60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
