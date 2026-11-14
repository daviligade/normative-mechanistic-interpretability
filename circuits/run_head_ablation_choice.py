"""Removal of the located heads in the choice frame."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "code")); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import choice_frames; choice_frames.register()
import circ_common; circ_common.answer_ids = choice_frames.answer_ids
import run_head_ablation
if __name__ == "__main__":
    choice_frames.check_frames(sys.argv, "run_head_ablation_choice")
    run_head_ablation.main()
