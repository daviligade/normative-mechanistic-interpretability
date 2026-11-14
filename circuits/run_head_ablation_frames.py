"""Removal of the located heads in the further frames."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extra_frames; extra_frames.register()
import run_head_ablation
if __name__ == "__main__": run_head_ablation.main()
