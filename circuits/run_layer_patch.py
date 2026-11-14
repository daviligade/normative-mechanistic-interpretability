"""Layer-by-layer patching of the hidden state, attention and MLP outputs."""
import argparse, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from circ_common import (FRAMES, READOUT_KEYS, Model, pick_device, token_groups, load_items, save_npz, existing_ok, run_config_append, model_tag, readouts,
                         first, equal_length_or_skip, all_present)

COMPONENTS = ["mlp_all", "mlp_final", "attn_all", "attn_final", "resid_final", "resid_edit"]


def with_first(out, new):
    if isinstance(out, tuple): return (new,) + tuple(out[1:])
    if isinstance(out, list): return [new] + list(out[1:])
    return new


@torch.no_grad()
def clean_caches(M, ids):
    c = {"attn": {}, "mlp": {}, "resid": {}}; hooks = []
    for l, layer in enumerate(M.layers):
        hooks.append(layer.self_attn.register_forward_hook(lambda m, a, out, l=l: c["attn"].__setitem__(l, first(out).detach())))
        hooks.append(layer.mlp.register_forward_hook(lambda m, a, out, l=l: c["mlp"].__setitem__(l, first(out).detach())))
        hooks.append(layer.register_forward_hook(lambda m, a, out, l=l: c["resid"].__setitem__(l, first(out).detach())))
    try: lg = M.forward_logits([ids])
    finally:
        for h in hooks: h.remove()
    return readouts(lg, M.A), c


@torch.no_grad()
def patch_layers(M, recv_ids, donor, component, edit_span, batch):
    kind, where = component.split("_"); src = {"mlp": "mlp", "attn": "attn", "resid": "resid"}[kind]
    out = {k: np.zeros(M.L, np.float32) for k in READOUT_KEYS}; e0, e1 = edit_span
    for s in range(0, M.L, batch):
        layers = list(range(s, min(s + batch, M.L))); hooks = []
        for b, l in enumerate(layers):
            d = donor[src][l]
            def hook(m, a, o, b=b, d=d):
                x = first(o).clone()
                if where == "all": x[b] = d[0].to(x.dtype)
                elif where == "final": x[b, -1] = d[0, -1].to(x.dtype)
                else: x[b, e0:e1] = d[0, e0:e1].to(x.dtype)
                return with_first(o, x)
            mod = {"mlp": M.layers[l].mlp, "attn": M.layers[l].self_attn, "resid": M.layers[l]}[src]
            hooks.append(mod.register_forward_hook(hook))
        try: lg = M.forward_logits([recv_ids] * len(layers))
        finally:
            for h in hooks: h.remove()
        R = readouts(lg, M.A)
        for k in out: out[k][s:s + len(layers)] = R[k].float().cpu().numpy()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--items", required=True); ap.add_argument("--out", default="runs/circuits/layers")
    ap.add_argument("--frames", nargs="+", default=["A1", "B"], choices=list(FRAMES)); ap.add_argument("--directions", nargs="+", default=["p2r"], choices=["p2r", "r2p"])
    ap.add_argument("--components", nargs="+", default=COMPONENTS, choices=COMPONENTS)
    ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32", choices=["float32", "float16", "bfloat16"]); ap.add_argument("--batch", type=int, default=32)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--categories", nargs="+", default=None); ap.add_argument("--tag", default=None)
    ap.add_argument("--any-items", action="store_true", help="software tests only"); ap.add_argument("--allow-unequal", action="store_true", help="the original pairs: skip pairs whose prompts differ in token count")
    args = ap.parse_args()
    items, sha = load_items(args.items, args.any_items, args.limit, args.categories)
    tag = args.tag or model_tag(args.model)
    if all_present(os.path.join(args.out, tag), args.frames, items, sha): print(f"[run_layer_patch] {tag}: every result file is already there; nothing to do", flush=True); return
    dev = pick_device(args.device); print(f"[run_layer_patch] model={args.model} device={dev} dtype={args.dtype}", flush=True)
    M = Model(args.model, dev, args.dtype); print(f"[run_layer_patch] layers={M.L} heads={M.H}", flush=True)
    out = os.path.join(args.out, tag); os.makedirs(out, exist_ok=True)
    run_config_append(out, {"script": "run_layer_patch.py", "model": args.model, "dtype": args.dtype, "device": dev, "items_file": args.items, "items_sha256": sha, "frames": args.frames,
                            "directions": args.directions, "components": args.components, "n_items": len(items), "n_layers": M.L, "n_heads": M.H})
    todo = [(f, it) for f in args.frames for it in items]; t0 = time.time(); masses = []; checked = False
    for done, (f, it) in enumerate(todo, start=1):
        path = os.path.join(out, f"{f}__{it['id']}.npz")
        if existing_ok(path, sha): continue
        if not equal_length_or_skip(M, f, it, args.allow_unequal): continue
        t1 = time.time(); ids, g, span = token_groups(M, f, it); res = {"groups": g, "edit_span": np.array(span)}
        base, cache = {}, {}
        for side in ("perm", "rest"):
            base[side], cache[side] = clean_caches(M, ids[side])
            for k in READOUT_KEYS: res[f"{side}_{k}"] = np.array(float(base[side][k][0]))
        if not checked:
            r = patch_layers(M, ids["rest"], cache["rest"], "resid_final", span, args.batch); err = float(np.abs(r["S"] - float(base["rest"]["S"][0])).max())
            print(f"[run_layer_patch] self-patch check on the first item: max|dS| = {err:.2e}", flush=True)
            if err > 1e-4: sys.exit("[run_layer_patch] patching a prompt's own activations changed its readout; stopping")
            checked = True
        for d in args.directions:
            recv, donor = ("rest", "perm") if d == "p2r" else ("perm", "rest")
            for comp in args.components:
                r = patch_layers(M, ids[recv], cache[donor], comp, span, args.batch)
                for k in READOUT_KEYS: res[f"{d}_{comp}_{k}"] = r[k]
        save_npz(path, dict(id=it["id"], frame=f, category=it["category"], subtype=it.get("subtype"), model=args.model, items_sha256=sha, directions=args.directions, components=args.components,
                            n_layers=M.L, n_heads=M.H, n_tok=len(ids["perm"]), seconds=round(time.time() - t1, 2)), res)
        masses.append(float(res["perm_mass"]))
        shown = (f"gap(S)={float(res['perm_S']) - float(res['rest_S']):+.3f} best layer (resid_final, p2r): L{int(np.argmax(res['p2r_resid_final_S'] - float(res['rest_S'])))} " if args.any_items and "p2r" in args.directions and "resid_final" in args.components else "")
        print(f"[{done}/{len(todo)}] {f} {it['id']:10s} {shown}mean answer-word mass so far={np.mean(masses):.2f} elapsed={(time.time() - t0) / 60:.1f} min", flush=True)
    print("[run_layer_patch] finished", flush=True)


if __name__ == "__main__":
    main()
