"""SAE features with the cue 'socially'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

NEW = {"A1s": lambda stem: f"{common.PRIME}{stem} is socially"}
for k, f in NEW.items():
    if k in common.FRAMES: sys.exit(f"[run_features_social] frame {k} already exists in common.FRAMES; refusing to redefine it")
    common.FRAMES[k] = f
import run_features


def _check_args(argv):
    if "--frames" not in argv: sys.exit("[run_features_social] give --frames A1s")
    frames = []
    for x in argv[argv.index("--frames") + 1:]:
        if x.startswith("--"): break
        frames.append(x)
    if frames != ["A1s"]: sys.exit(f"[run_features_social] this wrapper is for --frames A1s only (got {frames}); the other frames have their own drivers")
    out = argv[argv.index("--out") + 1] if "--out" in argv else "runs/features"
    if os.path.normpath(out) in {os.path.normpath(p) for p in ("runs/features", "runs/features_cues", "runs/features_ethically")}:
        sys.exit("[run_features_social] --out must be a folder of its own (runs/features_social), not one of the earlier feature runs")
    if "--feature-sets" in argv: sys.exit("[run_features_social] pass 1 only: leave out --feature-sets")


if __name__ == "__main__":
    _check_args(sys.argv[1:])
    run_features.main()
