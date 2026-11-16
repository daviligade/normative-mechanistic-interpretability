# Section 4: head patching on every pair, in the three frames and the further prompts; then the analyses.
set -e; cd "$(dirname "$0")/.."; source scripts/models.sh
for M in $MODELS; do
  python3 code/run_heads.py --model $M --items stimuli/items_run_v1.json --frames A1 B A0 --directions p2r r2p --positions all final --device $DEVICE --dtype float32 --out runs/heads
  python3 code/run_heads.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames QA --directions p2r --positions all --device $DEVICE --dtype float32 --out runs/heads_qa
  python3 code/run_heads_frames.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames B0 A0s --directions p2r --positions all --device $DEVICE --dtype float32 --out runs/heads_frames
  python3 code/run_heads_frames.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1e A0e --directions p2r --positions all --device $DEVICE --dtype float32 --out runs/heads_frames_eth
  python3 code/run_heads_choice.py --model $M --items stimuli/items_choice_run.json --any-items --frames CH --directions p2r --positions all --device $DEVICE --dtype float32 --out runs/heads_choice
  python3 code/run_heads.py --model $M --items stimuli/items_followup_person_run.json --any-items --frames A1 B --directions p2r --positions all --device $DEVICE --dtype float32 --out runs/heads_followup_person
done
H="python3 code/analyze_heads.py --runs runs/heads --located located/heads.json"
$H --items stimuli/items_final.json --out results/heads
$H --items stimuli/items_final.json --out results/heads__strict --subset strict
$H --items stimuli/items_final.json --out results/heads__tau010 --tau 0.10
$H --items stimuli/items_final.json --out results/heads__LD --readout LD
$H --items stimuli/items_final.json --out results/heads__Shist --readout S_hist
$H --items stimuli/items_final.json --out results/heads__located_top5 --headset located_top5
$H --items stimuli/items_final.json --out results/heads__r2p_all --condition r2p_all
$H --items stimuli/items_final.json --out results/heads__p2r_final --condition p2r_final
$H --items stimuli/items_rated.json --out results/heads__allrated --subset all
$H --items stimuli/items_clean.json --out results/heads__clean
python3 code/analyze_heads.py --runs runs/heads_qa --items stimuli/items_final.json --located located/heads.json --out results/heads__qa
python3 code/analyze_heads.py --runs runs/heads_frames --items stimuli/items_final.json --located located/heads.json --out results/heads__frames
python3 code/analyze_heads_specific.py --runs runs/heads --items stimuli/items_final.json --located located/heads.json --out results/heads_specific
python3 code/analyze_heads_controls.py --check results/heads --out results/heads_person
python3 code/analyze_heads_controls.py --check results/heads --subset all --out results/heads_person__all
python3 code/analyze_heads_controls.py --study-runs runs/heads --new-runs runs/heads_frames --no-controls --frames A0 A0s --kind etiquette --out results/heads__frames_socially
python3 code/analyze_heads.py --runs runs/heads_frames_eth --items stimuli/items_final.json --located located/heads.json --out results/heads__frames_ethically
python3 code/analyze_heads_controls.py --study-runs runs/heads --new-runs runs/heads_frames_eth --no-controls --frames A1 A1e A0 A0e --kind etiquette --out results/heads__frames_ethically_vs_morally
python3 code/analyze_heads_controls.py --study-runs runs/heads --new-runs runs/heads_frames runs/heads_qa --no-controls --frames A1 B A0 QA B0 A0s --readout LD --include-on LD --kind etiquette --out results/heads__frames_logodds
python3 code/analyze_heads_controls.py --study-runs runs/heads_qa --frames QA --no-controls --check results/heads__qa --out results/heads__qa_levels
python3 code/analyze_heads_controls.py --study-runs runs/heads --new-runs runs/heads_choice --no-controls --frames CH --readout LD --include-on LD --out results/heads__choice_logodds
