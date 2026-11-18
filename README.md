# Normative mechanistic interpretability

Code and data for the paper [*Disambiguating Moral Circuits and Moral Features in Language Models*](https://arxiv.org/abs/2611.21705). The pairs and annotations are also a Hugging Face dataset (https://huggingface.co/datasets/davideliga/normative-minimal-pairs); the trained SAE dictionaries are at https://huggingface.co/davideliga/normative-sae-dictionaries.

The paper asks whether attention heads and sparse-autoencoder (SAE) features that change a model's answer to a moral prompt respond to moral content, to the judgment of conduct by any norm, or to the word "morally" in the prompt. It tests them on minimal pairs of short phrases that differ in a moral standard, in another kind of norm (prudence, etiquette, aesthetics, evidence) or in a descriptive quality, in 14 open-weight models.

## Contents

| Folder | What it holds |
|---|---|
| `stimuli/` | The pairs. `items_run_v1.json`: every candidate pair the models were run on; `items_final.json`: the pairs retained after the annotators' ratings (227); `items_rated.json`, `items_clean.json`: the rated pairs and a stricter subset; `items_followup_*`: the follow-up pairs (function-word pairs, conduct pairs, twins, descriptive pairs about a person); `items_choice_*`: the choice prompts; `items_ethics_cm.json`: the 400 ETHICS scenarios; `original_*`: the original pairs on which the heads and features were located. |
| `located/` | The located heads of each model (`heads.json`) and the located features of each dictionary (`features.json`, `feature_sets__<dictionary>.json`). |
| `code/`, `circuits/` | Model runs (`run_*.py`) and analyses (`analyze_*.py`). |
| `ratings/` | The annotators' ratings: one row per annotator and pair (`ratings_long*.csv`) and the outcome for each pair (`ratings_items*.csv`); `_round2` holds the second round on the spare prudential pairs. |
| `annotation_llm/` | The annotators' form answered by three language models (`answers/`, one folder per set of pairs) and the code that asks the models and compares them with the annotators. |
| `original_pairs/` | The original pairs (Section 3 and the appendices on them): the stored head effects of every model (`data/heads/`), the permutation counts and the final-token activations of the SAE features (`data/features/`, `data/activations/`), the outputs of run 06 (`data/replication/`), and the scripts: selection of the located heads and features, the checks 01 to 09, the runs on Llama-3.2-1B, the reconstruction by the dictionaries, the ETHICS direction, the "is ethically" frame and the training of a dictionary. |
| `scripts/` | One script per part of the paper, with every command. |
| `results/` | The result files behind every table and figure (those of the original pairs are in `original_pairs/results/`). |

## Setup

Python 3.11 and the packages in `requirements.txt`:

```
pip install -r requirements.txt
```

The models are loaded from Hugging Face (the Llama and Gemma models need an accepted licence on Hugging Face). All runs of the paper used one Apple M2 Max computer with 96 GB of memory (`DEVICE=mps`, float32); `DEVICE=cuda` or `DEVICE=cpu` also work.

The feature scripts need the SAE dictionaries in `dictionaries/<dictionary>/`. The 13 trained dictionaries and the Llama Scope dictionary of Llama-3.1-8B:

```
hf download davideliga/normative-sae-dictionaries --local-dir dictionaries
huggingface-cli download fnlp/Llama3_1-8B-Base-LXR-8x --include 'Llama3_1-8B-Base-L12R-8x/*' --local-dir dictionaries
```

## Running

From the repository folder:

```
bash scripts/0_original_pairs.sh   # the original pairs: located heads and features, checks
bash scripts/1_heads.sh            # head patching and the analyses of the located heads
bash scripts/2_features.sh         # the located SAE features
bash scripts/3_circuits.sh         # removal of the located heads, roles, layer profiles, edges, further prompts
bash scripts/4_beyond.sh           # category prompt, neurons, Jacobian lens, steering, twins
```

The ETHICS direction of `scripts/0_original_pairs.sh` reads `ethics_cm_test.csv`, the commonsense test split of ETHICS (https://huggingface.co/datasets/hendrycks/ethics/resolve/main/data/commonsense/test.csv), from the repository folder. `original_pairs/train_sae.py` needs `pip install sae-lens==6.43.0`.

The comparison of the language models with the annotators:

```
python3 annotation_llm/compare_with_humans.py --llm annotation_llm/answers/calibration --out results/llm_calibration
```

Each model run writes to `runs/`, each analysis to `results/`. A run that is complete is skipped when a script is started again. The model runs take from minutes (1B models) to several hours (14B models) per script on the computer above; the analyses run on a CPU.

## Citation

If you use this material, please cite the paper:

```bibtex
@misc{liga2026disambiguating,
  title         = {Disambiguating Moral Circuits and Moral Features in Language Models: Moral content, normative judgment or cue words? Evidence from 14 models},
  author        = {Liga, Davide and Yu, Liuwen and Magnini, Matteo},
  year          = {2026},
  eprint        = {2611.21705},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2611.21705}
}
```

## Licence

Code: MIT. Data: CC BY 4.0.
