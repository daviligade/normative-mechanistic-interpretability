# Section 6 and the further tests: removal of the located heads, roles, layer profiles, edges; then the analyses.
set -e; cd "$(dirname "$0")/.."; source scripts/models.sh
for M in $MODELS; do
  python3 circuits/run_head_ablation.py --model $M --items stimuli/items_run_v1.json --frames A1 B --device $DEVICE --dtype float32 --out runs/circuits/ablation
  python3 circuits/run_head_ablation_layer.py --model $M --items stimuli/items_run_v1.json --accepted-only --means-dir runs/circuits/ablation --out runs/circuits_layer --frames A1 B --device $DEVICE --dtype float32
  python3 circuits/run_head_ablation.py --model $M --items stimuli/items_run_v1.json --frames QA --sizes 10 --modes all --device $DEVICE --dtype float32 --out runs/circuits_qa/ablation
  python3 circuits/run_head_ablation_frames.py --model $M --items stimuli/items_run_v1.json --frames B0 A0s --sizes 10 --modes all --device $DEVICE --dtype float32 --out runs/circuits_frames/ablation
  python3 circuits/run_head_ablation_choice.py --model $M --items stimuli/items_choice_run.json --any-items --frames CH --sizes 10 --modes all --device $DEVICE --dtype float32 --out runs/circuits_choice/ablation
  python3 circuits/run_head_ablation_choice.py --model $M --items stimuli/items_choice_word_run.json --any-items --frames CW --sizes 10 --modes all --device $DEVICE --dtype float32 --out runs/circuits_choice_word/ablation
  python3 circuits/run_head_ablation_ethics.py --model $M --items stimuli/items_ethics_cm.json --frames EA1 EB EQA --device $DEVICE --dtype float32 --out runs/ethics
  python3 circuits/run_head_roles.py --model $M --items stimuli/items_run_v1.json --frames A1 B --device $DEVICE --dtype float32 --out runs/circuits/roles
  python3 circuits/run_layer_patch.py --model $M --items stimuli/items_run_v1.json --frames A1 B --device $DEVICE --dtype float32 --out runs/circuits/layers
  python3 circuits/run_edges.py --model $M --items stimuli/items_run_v1.json --frames A1 B --device $DEVICE --dtype float32 --out runs/circuits/edges
done
for M in google/gemma-2b-it Qwen/Qwen2.5-3B Qwen/Qwen2.5-7B-Instruct Qwen/Qwen2.5-14B; do
  python3 circuits/run_edges_exact.py --model $M --items stimuli/items_run_v1.json --frames A1 B --device $DEVICE --dtype float32 --out runs/circuits/edges_exact
done
A="--items stimuli/items_final.json --located located/heads.json"
python3 circuits/analyze_circuits.py --runs runs/circuits --heads-runs runs/heads $A --out results/circuits
python3 circuits/analyze_circuits.py --runs runs/circuits_layer --stages ablation $A --out results/circuits_layer
python3 circuits/analyze_circuits.py --runs runs/circuits_qa --stages ablation $A --out results/circuits_qa
python3 circuits/analyze_ablation_frames.py --runs runs/circuits --frames A1 B --readout LD --include-on LD --out results/circuits__logodds
python3 circuits/analyze_ablation_frames.py --runs runs/circuits_frames --readout LD --include-on LD --out results/circuits_frames__logodds
python3 circuits/analyze_ablation_frames.py --runs runs/circuits_frames --readout S --include-on S --out results/circuits_frames__S
python3 circuits/analyze_ablation_frames.py --runs runs/circuits_qa --readout LD --include-on LD --out results/circuits_qa__logodds
python3 circuits/analyze_ablation_frames.py --runs runs/circuits_choice --frames CH --readout LD --include-on LD --out results/circuits_choice__logodds
python3 circuits/analyze_ablation_frames.py --runs runs/circuits_choice_word --frames CW --readout LD --include-on LD --out results/circuits_choice_word__logodds
python3 circuits/analyze_choice_behaviour.py --out results/choice_behaviour
python3 circuits/analyze_ethics.py --runs runs/ethics --out results/ethics
