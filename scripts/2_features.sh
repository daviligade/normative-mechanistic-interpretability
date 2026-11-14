# Section 5: activations of the located SAE features, other cue words, and the split-half removal; then the analyses.
# Needs the dictionaries in dictionaries/ (README).
set -e; cd "$(dirname "$0")/.."; source scripts/models.sh
echo "$DICTIONARIES" | while IFS="|" read T M L S; do
  SRC=$(dict_source $T)
  python3 code/run_features.py --model $M $SRC --layer $L --site $S --tag $T --items stimuli/items_run_v1.json --frames A1 B --feature-sets located/feature_sets__$T.json --device $DEVICE --out runs/features
  python3 code/run_features_cues.py --model $M $SRC --layer $L --site $S --tag $T --items stimuli/items_run_v1.json --frames A1l A1p --device $DEVICE --out runs/features_cues
  python3 code/run_features_ethically.py --model $M $SRC --layer $L --site $S --tag $T --items stimuli/items_run_v1.json --frames A1e --device $DEVICE --out runs/features_ethically
  python3 code/run_features_social.py --model $M $SRC --layer $L --site $S --tag $T --items stimuli/items_run_v1.json --frames A1s --device $DEVICE --out runs/features_social
done
F="python3 code/analyze_features.py --runs runs/features --located located/features.json"
$F --items stimuli/items_final.json --out results/features
$F --items stimuli/items_final.json --out results/features__strict --subset strict
$F --items stimuli/items_final.json --out results/features__tau010 --tau 0.10
python3 code/analyze_features_cues.py --runs runs/features --runs-cues runs/features_cues --runs-e runs/features_ethically --items stimuli/items_final.json --located located/features.json --main results/features/summary.json --out results/features_cues
python3 code/analyze_features_ethically.py --runs runs/features --runs-e runs/features_ethically --items stimuli/items_final.json --located located/features.json --main results/features/summary.json --out results/features_ethically
python3 code/analyze_features_social.py --runs runs/features --runs-social runs/features_social --runs-cues runs/features_cues --items stimuli/items_final.json --located located/features.json --main results/features/summary.json --out results/features_social
# split-half removal: lists chosen on one half of the pairs, removed on every pair, read on the other half
python3 code/h6_split_select.py --runs runs/features --items stimuli/items_final.json --out results/features_h6split
echo "$DICTIONARIES" | while IFS="|" read T M L S; do
  [ -f results/features_h6split/sets__$T.json ] || continue
  mkdir -p runs/features_h6split/$T
  ln -sfn ../../features/$T/extract__A1.npz runs/features_h6split/$T/extract__A1.npz; ln -sfn ../../features/$T/extract__B.npz runs/features_h6split/$T/extract__B.npz
  python3 code/run_features.py --model $M $(dict_source $T) --layer $L --site $S --tag $T --items stimuli/items_run_v1.json --frames A1 B --feature-sets results/features_h6split/sets__$T.json --n-random 10 --device $DEVICE --out runs/features_h6split
done
python3 code/analyze_h6_split.py --runs runs/features_h6split --sets results/features_h6split --items stimuli/items_final.json --out results/features_h6split
# contexts of the located features in ordinary text
python3 circuits/run_feature_contexts.py --fetch wikitext
echo "$DICTIONARIES" | while IFS="|" read T M L S; do
  python3 circuits/run_feature_contexts.py --model $M $(dict_source $T) --layer $L --site $S --tag $T --feature-sets located/feature_sets__$T.json --text-file downloads/wikitext103_test.txt --original-pairs stimuli/original_moral_pairs.json --device $DEVICE --out runs/features_contexts
done
