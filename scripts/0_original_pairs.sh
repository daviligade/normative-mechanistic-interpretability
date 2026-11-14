# Section 3 and the appendices on the original pairs: the stored head effects reproduced by the head driver, the selection of the located heads and
# features, the checks on the original pairs, the runs on Llama-3.2-1B, the dictionaries' reconstruction, the ETHICS direction and the "is ethically" frame.
set -e; cd "$(dirname "$0")/.."; source scripts/models.sh
for M in $MODELS; do python3 code/run_heads.py --model $M --selftest original_pairs --device $DEVICE; done
for T in $(echo "$DICTIONARIES" | cut -d'|' -f1); do python3 original_pairs/feature_tests.py --dictionary $T; done
python3 original_pairs/select_located.py
python3 original_pairs/check_01_token_alignment.py
python3 original_pairs/check_02_head_shares.py
python3 original_pairs/check_03_base_instruct.py
python3 original_pairs/check_04_tier_splits.py
python3 original_pairs/check_05_frame_features.py
python3 original_pairs/check_05b_frame_general_features.py
python3 original_pairs/run_06_llama1b.py
python3 original_pairs/check_07_norm_pairs_heads.py
python3 original_pairs/run_08_frame_swap_and_dip.py
python3 original_pairs/run_08c_steering.py
python3 original_pairs/check_09_raw_test_all_heads.py
python3 original_pairs/run_ethically_frame.py --model meta-llama/Llama-3.2-1B --device $DEVICE
python3 original_pairs/run_ethically_frame.py --model meta-llama/Llama-3.1-8B --device $DEVICE
python3 original_pairs/run_ethics_direction.py --model meta-llama/Llama-3.2-1B --layer 7 --ethics-csv ethics_cm_test.csv --steer
python3 original_pairs/run_ethics_direction.py --model meta-llama/Llama-3.1-8B --layer 12 --ethics-csv ethics_cm_test.csv
echo "$DICTIONARIES" | while IFS='|' read T M L S; do
  python3 original_pairs/sae_capture.py --model $M $(dict_source $T) --layer $L --site $S --original-pairs stimuli/original_moral_pairs.json --device $DEVICE --out original_pairs/results/sae_capture/$T.json
done
# training of one dictionary (the 13 trained dictionaries are released; the arguments of each are in its cfg.json), for example:
#   python3 original_pairs/train_sae.py --model meta-llama/Llama-3.2-1B --hook blocks.7.hook_resid_post --d-in 2048 --k 64 --out dictionaries_trained/llama-3.2-1B-base
