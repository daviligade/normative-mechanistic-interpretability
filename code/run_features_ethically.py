"""SAE features with the cue 'ethically'."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

common.FRAMES["A1e"] = lambda stem: f"{common.PRIME}{stem} is ethically"
import run_features


def _check_args(argv):
    if "--frames" not in argv: sys.exit("[run_features_ethically] give --frames A1e")
    frames = []
    for x in argv[argv.index("--frames") + 1:]:
        if x.startswith("--"): break
        frames.append(x)
    if frames != ["A1e"]: sys.exit(f"[run_features_ethically] this wrapper is for --frames A1e only (got {frames}); the other frames are run with code/run_features.py")
    out = argv[argv.index("--out") + 1] if "--out" in argv else "runs/features"
    if os.path.normpath(out) == os.path.normpath("runs/features"): sys.exit("[run_features_ethically] --out must not be runs/features (the main runs live there); use runs/features_ethically")
    if "--feature-sets" in argv: sys.exit("[run_features_ethically] pass 1 only: leave out --feature-sets")


if __name__ == "__main__":
    _check_args(sys.argv[1:])
    run_features.main()
