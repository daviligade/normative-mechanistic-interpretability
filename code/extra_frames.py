"""Further frames: the stem alone, other cue words, a plain question."""
import common

EXTRA = {
    "B0":  lambda stem: f"{stem} is",
    "A0s": lambda stem: f"{stem} is socially",
    "A1s": lambda stem: f"{common.PRIME}{stem} is socially",
    "B0c": lambda stem: f"{stem} is considered",
    "A0e": lambda stem: f"{stem} is ethically",
    "A1e": lambda stem: f"{common.PRIME}{stem} is ethically",
}


def register():
    for k, f in EXTRA.items():
        if k in common.FRAMES and common.FRAMES[k] is not f: raise SystemExit(f"frame name {k} is already taken in code/common.py")
        common.FRAMES[k] = f
    return list(EXTRA)
