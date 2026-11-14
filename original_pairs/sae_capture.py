"""Reconstruction of the hidden state by a dictionary on the original pairs: with and without the first token, at the final token, and the part of the pair difference it captures."""
import argparse, json, os, sys
import numpy as np, torch
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../code"))
from common import encode, readouts
from run_features import SAEWrap, LM
from run_heads import pick_device
ap = argparse.ArgumentParser(); ap.add_argument("--model", required=True); ap.add_argument("--sae-dir"); ap.add_argument("--llama-scope"); ap.add_argument("--layer", type=int, required=True)
ap.add_argument("--site", default="resid_post"); ap.add_argument("--original-pairs", required=True); ap.add_argument("--stored-gate"); ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32")
ap.add_argument("--limit", type=int, default=0); ap.add_argument("--out", default=None); a = ap.parse_args()
dev = pick_device(a.device); lm = LM(a.model, dev, a.dtype, a.layer, a.site); sae = SAEWrap(a.sae_dir, a.llama_scope, dev); pairs = json.load(open(a.original_pairs)); pairs = pairs[:a.limit] if a.limit else pairs
@torch.no_grad()
def run_full(ids, override=None, where=None):
    grab = {}
    def hook(m, args, out):
        h = out[0] if isinstance(out, tuple) else out; grab["h"] = h[0].detach().float().clone()
        if override is not None:
            if where == "all": h[0] = override.to(h.dtype)
            elif where == "nobos": h[0, 1:] = override[1:].to(h.dtype)
            else: h[0, -1] = override[-1].to(h.dtype)
        return out
    hd = lm.module.register_forward_hook(hook)
    try: x = torch.tensor([ids], device=dev); lg = lm.model.lm_head(lm.model.model(input_ids=x).last_hidden_state[:, -1, :])
    finally: hd.remove()
    return float(readouts(lg, lm.A)["S_hist"][0]), grab["h"]
rows = []; dP, dH = [], []
for n, p in enumerate(pairs):
    fin = {}
    for side in ("restrictive_prompt", "permissive_prompt"):
        ids = encode(lm.tok, p[side]); s0, h = run_full(ids); xh = sae.decode(sae.encode(h)); fin[side] = (h[-1], xh[-1])
        if side == "restrictive_prompt":
            ve = lambda x, r: 1 - ((x - r).var() / x.var()).item()
            rows.append(dict(name=p["name"], ve_with_bos=ve(h, xh), ve_nobos=ve(h[1:], xh[1:]), rel_final=(((h[-1] - xh[-1]) ** 2).sum() / (h[-1] ** 2).sum()).item(),
                             rel_bos=(((h[0] - xh[0]) ** 2).sum() / (h[0] ** 2).sum()).item(), norm_bos=h[0].norm().item(), norm_other=h[1:].norm(dim=-1).mean().item(),
                             l0_bos=int((sae.encode(h[0]) > 0).sum()), l0_final=int((sae.encode(h[-1]) > 0).sum()),
                             dS_all=run_full(ids, xh, "all")[0] - s0, dS_nobos=run_full(ids, xh, "nobos")[0] - s0, dS_final=run_full(ids, xh, "final")[0] - s0))
    d = fin["permissive_prompt"][0] - fin["restrictive_prompt"][0]; dh = fin["permissive_prompt"][1] - fin["restrictive_prompt"][1]; dP.append(d); dH.append(dh)
    if (n + 1) % 20 == 0: print(f"  {n + 1}/{len(pairs)}", flush=True)
D, DH = torch.stack(dP), torch.stack(dH); r2 = 1 - ((D - DH) ** 2).sum(-1) / (D ** 2).sum(-1); cos = torch.nn.functional.cosine_similarity(D, DH, dim=-1); proj = (D * DH).sum(-1) / (D ** 2).sum(-1)
m = lambda k: float(np.mean([r[k] for r in rows])); ma = lambda k: float(np.mean([abs(r[k]) for r in rows])); mx = lambda k: float(np.max([abs(r[k]) for r in rows]))
res = {"n_pairs": len(pairs), "norm_bos": m("norm_bos"), "norm_other_positions": m("norm_other"), "L0_bos": m("l0_bos"), "L0_final": m("l0_final"),
       "VE_with_BOS": m("ve_with_bos"), "VE_without_BOS": m("ve_nobos"), "rel_error_BOS": m("rel_bos"), "rel_error_final_token": m("rel_final"),
       "splice_all_positions": {"mean_abs_dS": ma("dS_all"), "max_abs_dS": mx("dS_all")}, "splice_without_BOS": {"mean_abs_dS": ma("dS_nobos"), "max_abs_dS": mx("dS_nobos")},
       "splice_final_token_only": {"mean_abs_dS": ma("dS_final"), "max_abs_dS": mx("dS_final")},
       "pair_difference_at_final_token": {"R2_mean": float(r2.mean()), "R2_median": float(r2.median()), "cosine_mean": float(cos.mean()), "projection_mean": float(proj.mean())}}
if a.stored_gate:
    g = json.load(open(a.stored_gate)); res["stored_gate"] = {"mean_var_explained": g["mean_var_explained"], "mean_abs_delta_score": g["mean_abs_delta_score"], "max_abs_delta_score": g["max_abs_delta_score"]}
print(json.dumps(res, indent=1))
if a.out: json.dump({"summary": res, "per_pair": rows}, open(a.out, "w"), indent=1)
