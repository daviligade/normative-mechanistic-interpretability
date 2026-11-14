"""Head patching in the further frames."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import extra_frames; extra_frames.register()
import run_heads
if __name__ == "__main__": run_heads.main()
