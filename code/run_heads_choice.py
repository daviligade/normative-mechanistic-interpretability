"""Head patching in the choice frame."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import choice_frames; choice_frames.register()
import run_heads; run_heads.answer_ids = choice_frames.answer_ids
if __name__ == "__main__":
    choice_frames.check_frames(sys.argv, "run_heads_choice")
    run_heads.main()
