# Section 7: the category prompt, neurons, the Jacobian lens, steering, the logit lens, the twins and what the located heads write.
set -e; cd "$(dirname "$0")/.."; source scripts/models.sh
for M in $MODELS; do
  python3 circuits/run_category_frame.py --model $M --items stimuli/items_run_v1.json --accepted-only --presets zeroshot fewshot --device $DEVICE --out runs/category_frame
  python3 circuits/run_category_frame.py --model $M --items stimuli/items_followup_twins_run.json --any-items --presets fewshot --device $DEVICE --dtype float32 --out runs/category_frame_twins
  python3 circuits/run_steering.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B C --cat-preset fewshot --n-random 5 --device $DEVICE --dtype float32 --out runs/steering
  python3 circuits/run_logit_lens.py --model $M --items stimuli/items_run_v1.json --frames A1 B --device $DEVICE --dtype float32 --out runs/logit_lens
  python3 circuits/run_word_valence.py --model $M --items stimuli/items_final.json --device $DEVICE --dtype float32 --out runs/word_valence
  python3 circuits/run_head_outputs_standard.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B --device $DEVICE --dtype float32 --out runs/head_outputs_standard
  python3 circuits/run_head_outputs_standard.py --model $M --items stimuli/items_followup_twins_run.json --any-items --frames A1 B --device $DEVICE --dtype float32 --out runs/head_outputs_standard_twins
done
for M in $MODELS; do
  python3 circuits/run_units.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B C --cat-preset zeroshot --device $DEVICE --dtype float32 --out runs/units
  python3 circuits/run_unit_ablation.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B C --cat-preset zeroshot --n-random 10 --device $DEVICE --dtype float32 --units runs/units --out runs/units_ablation
  python3 circuits/run_units_contrast.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B --contrasts mvn stance normdescr catC --cat-preset fewshot --device $DEVICE --dtype float32 --out runs/units_contrast
  python3 circuits/run_units_contrast.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B --contrasts mvn --device $DEVICE --dtype float32 --out runs/units_contrast_nulls
  python3 circuits/run_units_contrast.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B --contrasts mvn --null-size 32 --device $DEVICE --dtype float32 --out runs/units_contrast_nulls32
  for C in mvn stance normdescr; do
    python3 circuits/run_unit_ablation.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B --n-random 10 --lists all --device $DEVICE --dtype float32 --units runs/units_contrast/$C --out runs/units_ablation_$C
  done
  python3 circuits/run_unit_ablation_cross.py --model $M --items stimuli/items_run_v1.json --accepted-only --frames A1 B --n-random 10 --lists all --device $DEVICE --dtype float32 --units runs/units_contrast/catC --out runs/units_ablation_cross
  for SET in func conduct twins; do
    for C in mvn stance; do
      python3 circuits/run_unit_ablation.py --model $M --items stimuli/items_followup_${SET}_run.json --any-items --frames A1 B --n-random 10 --lists all --lists-from-other-items --device $DEVICE --dtype float32 --units runs/units_contrast/$C --out runs/units_ablation_${C}_followup_$SET
    done
  done
done
for M in $SMALL_MODELS; do
  T=$(basename $M)
  for SET in func conduct twins; do
    python3 code/run_heads.py --model $M --items stimuli/items_followup_${SET}_run.json --any-items --frames A1 B --directions p2r --positions all --device $DEVICE --out runs/heads_followup_$SET
  done
  python3 circuits/jlens_fit.py --model $M --n-prompts 100 --dim-batch 8 --max-seq-len 128 --device $DEVICE --dtype float32 --out runs/jlens
  python3 circuits/jlens_neuron_weights.py --model $M --lens runs/jlens/$T/lens.pt --device cpu
  python3 circuits/run_jlens_readout.py --model $M --lens runs/jlens/$T/lens.pt --items stimuli/items_run_v1.json --accepted-only --frames A1 B --device $DEVICE --dtype float32 --out runs/jlens_readout
  python3 circuits/run_jlens_swap.py --model $M --lens runs/jlens/$T/lens.pt --items stimuli/items_run_v1.json --accepted-only --frames A1 B --n-random 10 --device $DEVICE --dtype float32 --out runs/jlens_swap
done
python3 circuits/analyze_category_frame.py --runs runs/category_frame --items stimuli/items_final.json --out results/category_frame
python3 circuits/analyze_steering.py --runs runs/steering --items stimuli/items_final.json --out results/steering
python3 circuits/analyze_logit_lens.py --runs runs/logit_lens --items stimuli/items_final.json --out results/logit_lens
python3 circuits/analyze_dip_lexical.py --items stimuli/items_final.json --out results/dip_lexical
python3 code/analyze_unit_ablation.py --units runs/units --runs runs/units_ablation --items stimuli/items_final.json --out results/units
for C in mvn stance normdescr; do python3 code/analyze_unit_ablation.py --units runs/units_contrast/$C --runs runs/units_ablation_$C --items stimuli/items_final.json --out results/units_$C; done
python3 code/analyze_unit_ablation.py --units runs/units_contrast/catC --runs runs/units_ablation_cross --items stimuli/items_final.json --out results/units_cross
for SET in func conduct twins; do for C in mvn stance; do
  python3 code/analyze_unit_ablation.py --units runs/units_contrast/$C --runs runs/units_ablation_${C}_followup_$SET --items stimuli/items_followup_$SET.json --out results/units_${C}_followup_$SET --any-items --all-held-out
done; done
for R in units_contrast units_contrast_nulls units_contrast_nulls32; do python3 code/analyze_unit_contrast.py --runs runs/$R --out results/$R; done
python3 code/analyze_twins.py --items stimuli/items_followup_twins.json --runs runs/units_ablation_mvn_followup_twins runs/units_ablation_stance_followup_twins --heads runs/heads_followup_twins --located located/heads.json --out results/twins --any-items
python3 circuits/analyze_jlens_readout.py --runs runs/jlens_readout --items stimuli/items_final.json --out results/jlens_readout
python3 circuits/analyze_jlens_swap.py --runs runs/jlens_swap --items stimuli/items_final.json --out results/jlens_swap
python3 circuits/analyze_jlens_neurons.py --weights runs/jlens --units runs/units_contrast --contrasts mvn stance normdescr --out results/jlens_neurons
python3 circuits/analyze_head_outputs_standard.py --runs runs/head_outputs_standard --out results/head_outputs_standard
python3 circuits/analyze_head_outputs_perm.py --runs runs/head_outputs_standard --rows results/head_outputs_standard/rows.json --out results/head_outputs_perm
python3 circuits/analyze_twins_standard.py --items stimuli/items_followup_twins.json --cat runs/category_frame_twins --main runs/head_outputs_standard --twins runs/head_outputs_standard_twins --out results/twins_standard
