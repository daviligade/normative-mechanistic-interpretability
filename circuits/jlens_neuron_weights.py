"""Neuron weights carried to the output through the Jacobian lens."""
import argparse, json, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import pick_device, model_tag, Model
from run_category_frame import CATEGORY_WORDS
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from common import first_token_id

NORM_KINDS = ("prudential", "etiquette", "aesthetic", "epistemic")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--lens", required=True); ap.add_argument("--out", default=None, help="default: next to the lens"); ap.add_argument("--tag", default=None)
    ap.add_argument("--device", default="cpu"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--config-only", default=None, help="software tests only")
    args = ap.parse_args()
    tag = args.tag or model_tag(args.model); out = args.out or os.path.join(os.path.dirname(args.lens), "neuron_weights.npz"); dev = pick_device(args.device)
    Lz = torch.load(args.lens, map_location="cpu", weights_only=True); J = {int(l): v.float() for l, v in Lz["J"].items()}
    cfg = None
    if args.config_only:
        from transformers import AutoConfig
        cfg = AutoConfig.from_pretrained(args.config_only); cfg.num_hidden_layers = 4; cfg.hidden_size = 64; cfg.intermediate_size = 128; cfg.num_attention_heads = 4; cfg.num_key_value_heads = 2; cfg.head_dim = 16; torch.manual_seed(0)
    M = Model(args.model, dev, args.dtype, config_only=cfg); L = M.L; W = M.W_U.float(); nw = M.norm_w
    u_set = {c: W[[first_token_id(M.tok, w, False) for w in ws]].mean(0) for c, ws in CATEGORY_WORDS.items()}
    u = {"answer": M.u_dir.float() * nw, "category": (u_set["moral"] - torch.stack([u_set[k] for k in NORM_KINDS]).mean(0)) * nw}
    outw = {f"{k}_{how}": [] for k in u for how in ("transported", "direct")}
    with torch.no_grad():
        for l in range(L):
            Wd = M.layers[l].mlp.down_proj.weight.float().to(M.device)
            Jl = J[l].to(M.device) if l in J else None
            for k, vec in u.items():
                vec = vec.to(M.device); outw[f"{k}_direct"].append((vec @ Wd).cpu().numpy())
                outw[f"{k}_transported"].append(((Jl.T @ vec) @ Wd).cpu().numpy() if Jl is not None else (vec @ Wd).cpu().numpy())
    arrays = {k: np.stack(v).astype(np.float32) for k, v in outw.items()}
    for k in u:
        c = [float(np.corrcoef(arrays[f"{k}_direct"][l], arrays[f"{k}_transported"][l])[0, 1]) for l in range(L)]
        print(f"[jlens_neuron_weights] {k}: correlation of direct and transported weights by layer " + " ".join(f"{x:+.2f}" for x in c), flush=True)
        arrays[f"{k}_corr_direct_transported"] = np.array(c, dtype=np.float32)
    np.savez_compressed(out, model=np.array(args.model), lens=np.array(args.lens), n_layers=L, d_mlp=arrays["answer_direct"].shape[1], lens_layers=np.array(sorted(J)), **arrays)
    print(f"[jlens_neuron_weights] wrote {out}", flush=True)


if __name__ == "__main__":
    main()
