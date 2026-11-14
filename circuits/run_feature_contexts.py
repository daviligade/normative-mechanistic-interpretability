"""Top-activating contexts of the located features in ordinary text."""
import argparse, json, os, sys, time, heapq
import numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code"))
from circ_common import FRAMES, encode, pick_device, run_config_append
from run_features import SAEWrap, LM


def fetch_wikitext(out_path):
    import urllib.request
    def detok(t):
        for a, b in ((" @-@ ", "-"), (" @,@ ", ","), (" @.@ ", "."), (" ,", ","), (" .", "."), (" ;", ";"), (" :", ":"), (" '", "'"), (" n't", "n't"), ("( ", "("), (" )", ")"), ('" ', '"'), (' "', '"')): t = t.replace(a, b)
        return t.strip()
    texts = []
    try:
        base = "https://datasets-server.huggingface.co/rows?dataset=Salesforce/wikitext&config=wikitext-103-raw-v1&split=test&length=100&offset="
        off, total = 0, None
        while total is None or off < total:
            with urllib.request.urlopen(base + str(off), timeout=60) as r: d = json.loads(r.read())
            total = d["num_rows_total"]; texts += [row["row"]["text"] for row in d["rows"]]; off += 100
    except Exception as e:
        print(f"[run_feature_contexts] rows API failed ({type(e).__name__}: {e}); trying the parquet file", flush=True)
        from huggingface_hub import hf_hub_download
        import pandas as pd
        p = hf_hub_download("Salesforce/wikitext", "wikitext-103-raw-v1/test-00000-of-00001.parquet", repo_type="dataset", local_dir="downloads")
        try: texts = pd.read_parquet(p)["text"].tolist()
        except Exception as e2: sys.exit(f"[run_feature_contexts] pandas cannot read the parquet file ({type(e2).__name__}: {e2}); pip install pyarrow, or give any plain-text corpus with --text-file")
    lines = [detok(t) for t in texts if len(t.strip()) > 80 and not t.strip().startswith("=")]
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True); open(out_path, "w").write("\n".join(lines) + "\n")
    print(f"[run_feature_contexts] {len(lines)} passages written to {out_path}")


def passages_from_args(a):
    P = []
    if a.text_file:
        if not os.path.exists(a.text_file): sys.exit(f"[run_feature_contexts] corpus file not found: {a.text_file} (run --fetch wikitext first, or give another --text-file)")
        for line in open(a.text_file, encoding="utf-8", errors="replace"):
            t = line.strip()
            if len(t) > 20: P.append(("text", t))
    if a.original_pairs:
        pairs = json.load(open(a.original_pairs))
        for p in pairs:
            if "perm_stem" in p: stems = [p["perm_stem"], p["rest_stem"]]
            else:
                stems = []
                for side in ("permissive_prompt", "restrictive_prompt"):
                    stem = p[side]
                    for suffix in (" is morally", " is ethically"):
                        if stem.endswith(suffix): stem = stem[:-len(suffix)]
                    stems.append(stem)
            for stem in stems:
                for f in ("A0", "A1", "B"): P.append((f"old_{f}", FRAMES[f](stem)))
    if a.limit: P = P[:a.limit]
    return P


class Top:
    def __init__(self, k): self.k = k; self.h = []; self.n_active = 0; self.sum_active = 0.0
    def add(self, act, key):
        if act <= 0: return
        self.n_active += 1; self.sum_active += act
        if len(self.h) < self.k: heapq.heappush(self.h, (act, key))
        elif act > self.h[0][0]: heapq.heapreplace(self.h, (act, key))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", choices=["wikitext"], help="download a public corpus into downloads/ and exit")
    ap.add_argument("--model"); ap.add_argument("--sae-dir"); ap.add_argument("--llama-scope"); ap.add_argument("--layer", type=int); ap.add_argument("--site", default="resid_post", choices=["resid_post", "mlp_out"])
    ap.add_argument("--tag"); ap.add_argument("--feature-sets", help="JSON {set_name: [feature ids]}"); ap.add_argument("--features", nargs="+", type=int, help="feature ids given directly (set name 'given')")
    ap.add_argument("--text-file"); ap.add_argument("--original-pairs"); ap.add_argument("--limit", type=int, default=0); ap.add_argument("--max-tokens", type=int, default=64)
    ap.add_argument("--top", type=int, default=20); ap.add_argument("--context", type=int, default=12, help="tokens of context on each side"); ap.add_argument("--device", default="auto"); ap.add_argument("--dtype", default="float32")
    ap.add_argument("--out", default="runs/features_contexts")
    a = ap.parse_args()
    if a.fetch: fetch_wikitext("downloads/wikitext103_test.txt"); return
    for f in (a.text_file, a.original_pairs):
        if f and os.path.basename(f).startswith("items_") and "stimuli" in os.path.abspath(f): sys.exit("[run_feature_contexts] study item files are not used here")
    assert a.model and a.layer is not None and a.tag and bool(a.sae_dir) != bool(a.llama_scope), "give --model, --layer, --tag and exactly one of --sae-dir / --llama-scope"
    assert a.feature_sets or a.features, "give --feature-sets or --features"
    P = passages_from_args(a); assert P, "no passages: give --text-file and/or --original-pairs"
    sets = {k: [int(i) for i in v] for k, v in json.load(open(a.feature_sets)).items()} if a.feature_sets else {}
    if a.features: sets["given"] = list(a.features)
    feats = sorted({i for v in sets.values() for i in v}); fidx = {f: j for j, f in enumerate(feats)}
    dev = pick_device(a.device); print(f"[run_feature_contexts] model={a.model} device={dev} site=L{a.layer}.{a.site} passages={len(P)} features={len(feats)}", flush=True)
    lm = LM(a.model, dev, a.dtype, a.layer, a.site); sae = SAEWrap(a.sae_dir, a.llama_scope, dev); idx_t = torch.tensor(feats, device=dev)
    out = os.path.join(a.out, a.tag); os.makedirs(out, exist_ok=True)
    run_config_append(out, {"script": "run_feature_contexts.py", "model": a.model, "sae_dir": a.sae_dir, "llama_scope": a.llama_scope, "layer": a.layer, "site": a.site, "text_file": a.text_file,
                            "original_pairs": a.original_pairs, "n_passages": len(P), "max_tokens": a.max_tokens, "feature_sets": a.feature_sets, "n_features": len(feats)})
    tops = {f: Top(a.top) for f in feats}; n_tok = 0; t0 = time.time(); grab = {}
    hook = lm.module.register_forward_hook(lambda m, i, o: grab.__setitem__("h", (o[0] if isinstance(o, tuple) else o).detach()))
    try:
        with torch.no_grad():
            for pi, (kind, text) in enumerate(P):
                ids = encode(lm.tok, text)[:a.max_tokens]; lm.model.model(input_ids=torch.tensor([ids], device=dev))
                h = grab["h"][0].float()
                f = sae.encode(h)[:, idx_t].cpu().numpy()
                f[0] = 0
                n_tok += len(ids) - 1
                for j, feat in enumerate(feats):
                    col = f[:, j]
                    for pos in np.nonzero(col > 0)[0]: tops[feat].add(float(col[pos]), (pi, int(pos)))
                if (pi + 1) % 200 == 0: print(f"  {pi + 1}/{len(P)} passages, {(time.time() - t0) / 60:.1f} min", flush=True)
    finally: hook.remove()
    def context(pi, pos):
        ids = encode(lm.tok, P[pi][1])[:a.max_tokens]; lo, hi = max(1, pos - a.context), min(len(ids), pos + a.context + 1)
        return lm.tok.decode(ids[lo:pos]) + "[[" + lm.tok.decode([ids[pos]]) + "]]" + lm.tok.decode(ids[pos + 1:hi])
    for name, F in sets.items():
        res = {"condition": a.tag, "set": name, "n_passages": len(P), "n_tokens": n_tok, "features": {}}
        for feat in F:
            t = tops[feat]; top = sorted(t.h, reverse=True)
            res["features"][str(feat)] = {"freq": t.n_active / max(n_tok, 1), "mean_active": (t.sum_active / t.n_active) if t.n_active else 0.0, "n_active": t.n_active,
                                          "top": [{"act": round(act, 4), "kind": P[pi][0], "passage": pi, "pos": pos, "context": context(pi, pos)} for act, (pi, pos) in top]}
        json.dump(res, open(os.path.join(out, f"contexts__{name}.json"), "w"), indent=1)
        with open(os.path.join(out, f"contexts__{name}.md"), "w") as md:
            md.write(f"# {a.tag}: feature set {name} ({len(F)} features) on {len(P)} passages, {n_tok} tokens\n\n")
            for feat in F:
                r = res["features"][str(feat)]
                md.write(f"## feature {feat}: active on {100 * r['freq']:.2f} % of tokens, mean activation when active {r['mean_active']:.2f}\n\n")
                for e in r["top"][:8]: md.write(f"* {e['act']:.2f} ({e['kind']}): {e['context'].replace(chr(10), ' / ')}\n")
                md.write("\n")
        print(f"[run_feature_contexts] {name}: {len(F)} features -> {out}/contexts__{name}.{{json,md}}", flush=True)
    print("[run_feature_contexts] finished", flush=True)


if __name__ == "__main__":
    main()
