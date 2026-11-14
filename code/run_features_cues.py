"""SAE features with other cue words and positions."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common

NEW = {
    "A1e": lambda stem: f"{common.PRIME}{stem} is ethically",
    "A1l": lambda stem: f"{common.PRIME}{stem} is logically",
    "A1p": lambda stem: f"{common.PRIME}Morally speaking, {stem[:1].lower()}{stem[1:]} is",
}
for k, f in NEW.items():
    if k in common.FRAMES: sys.exit(f"[run_features_cues] frame {k} already exists in common.FRAMES; refusing to redefine it")
    common.FRAMES[k] = f
import run_features


def _check_args(argv):
    if "--frames" not in argv: sys.exit("[run_features_cues] give --frames with frames from A1e, A1l, A1p")
    frames = []
    for x in argv[argv.index("--frames") + 1:]:
        if x.startswith("--"): break
        frames.append(x)
    if not frames or any(f not in NEW for f in frames): sys.exit(f"[run_features_cues] this wrapper runs only the frames {sorted(NEW)} (got {frames}); the main frames are run with code/run_features.py")
    out = argv[argv.index("--out") + 1] if "--out" in argv else "runs/features"
    if os.path.normpath(out) == os.path.normpath("runs/features"): sys.exit("[run_features_cues] --out must not be runs/features (the main runs live there); use runs/features_cues")
    if "--feature-sets" in argv: sys.exit("[run_features_cues] pass 1 only: leave out --feature-sets")


if __name__ == "__main__":
    _check_args(sys.argv[1:])
    run_features.main()
