# Neurons: discovery by depth and held-out ablation (exploratory)

Items: stimuli/items_followup_conduct.json is not the set of accepted pairs (stimuli/items_final.json).

## Llama-3.1-8B: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 318077 units at full size over 32 layers (peak at layer 28); halves select 800 / 800 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 277034 units at full size over 32 layers (peak at layer 31); halves select 783 / 800 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.1-8B-Instruct: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 331976 units at full size over 32 layers (peak at layer 28); halves select 800 / 800 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 278871 units at full size over 32 layers (peak at layer 31); halves select 779 / 800 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-1B: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 81925 units at full size over 16 layers (peak at layer 15); halves select 400 / 400 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 67955 units at full size over 16 layers (peak at layer 15); halves select 377 / 400 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-1B-Instruct: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 81549 units at full size over 16 layers (peak at layer 15); halves select 400 / 400 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 65017 units at full size over 16 layers (peak at layer 15); halves select 377 / 400 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-3B: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 154002 units at full size over 28 layers (peak at layer 27); halves select 700 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 135080 units at full size over 28 layers (peak at layer 26); halves select 699 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-3B-Instruct: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 156137 units at full size over 28 layers (peak at layer 26); halves select 700 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 131645 units at full size over 28 layers (peak at layer 27); halves select 685 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-14B: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 393973 units at full size over 48 layers (peak at layer 44); halves select 1092 / 1175 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 337504 units at full size over 48 layers (peak at layer 47); halves select 1076 / 1175 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-14B-Instruct: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 390427 units at full size over 48 layers (peak at layer 45); halves select 1107 / 1175 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 332641 units at full size over 48 layers (peak at layer 47); halves select 1074 / 1175 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-3B: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 216103 units at full size over 36 layers (peak at layer 33); halves select 852 / 882 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 168309 units at full size over 36 layers (peak at layer 1); halves select 717 / 900 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-3B-Instruct: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 237842 units at full size over 36 layers (peak at layer 35); halves select 861 / 900 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 188217 units at full size over 36 layers (peak at layer 1); halves select 760 / 900 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-7B: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 302675 units at full size over 28 layers (peak at layer 27); halves select 682 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 246972 units at full size over 28 layers (peak at layer 27); halves select 616 / 656 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-7B-Instruct: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 303839 units at full size over 28 layers (peak at layer 27); halves select 687 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 235622 units at full size over 28 layers (peak at layer 27); halves select 623 / 658 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## gemma-2b: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 172009 units at full size over 18 layers (peak at layer 16); halves select 450 / 450 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 136728 units at full size over 18 layers (peak at layer 16); halves select 405 / 450 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## gemma-2b-it: discovery

* A1: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 171369 units at full size over 18 layers (peak at layer 16); halves select 426 / 450 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py
* B: lists of the 'stance' contrast (a(perm) - a(rest) per pair, signed; one-sample t across pairs; lists = consistent direction on normative pairs (moral + norm)); 113021 units at full size over 18 layers (peak at layer 17); halves select 414 / 450 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.1-8B: held-out ablation

* A1, all lists: cross-fitted descr: -0.016 [-0.027, -0.007] (n=9)
    relative to the pair's gap: descr: -18.4% [-36.6, -6.6]
* B, all lists: cross-fitted descr: +0.010 [-0.012, +0.030] (n=9)
    relative to the pair's gap: descr: +10.3% [-2.6, +23.8]

## Llama-3.1-8B-Instruct: held-out ablation

* A1, all lists: cross-fitted descr: -0.006 [-0.011, -0.001] (n=8)
    relative to the pair's gap: descr: -5.8% [-11.2, +0.6]
* B, all lists: cross-fitted descr: +0.036 [+0.010, +0.064] (n=10)
    relative to the pair's gap: descr: +25.6% [+2.9, +49.8]

## Llama-3.2-1B: held-out ablation

* A1, all lists: cross-fitted descr: -0.006 [-0.013, +0.001] (n=9)
    relative to the pair's gap: descr: -11.0% [-25.4, +0.8]
* B, all lists: cross-fitted descr: -0.001 [-0.005, +0.004] (n=10)
    relative to the pair's gap: descr: +0.3% [-6.2, +8.6]

## Llama-3.2-1B-Instruct: held-out ablation

* A1, all lists: cross-fitted descr: -0.023 [-0.042, -0.006] (n=8)
    relative to the pair's gap: descr: -18.8% [-47.2, +5.7]
* B, all lists: cross-fitted descr: -0.004 [-0.020, +0.011] (n=13)
    relative to the pair's gap: descr: -1.6% [-26.3, +23.3]

## Llama-3.2-3B: held-out ablation

* A1, all lists: cross-fitted descr: -0.021 [-0.029, -0.014] (n=12)
    relative to the pair's gap: descr: -29.5% [-39.9, -20.3]
* B, all lists: cross-fitted descr: -0.011 [-0.016, -0.006] (n=12)
    relative to the pair's gap: descr: -11.6% [-17.4, -6.6]

## Llama-3.2-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted descr: -0.090 [-0.145, -0.048] (n=9)
    relative to the pair's gap: descr: -49.7% [-62.0, -38.0]
* B, all lists: cross-fitted descr: -0.005 [-0.037, +0.027] (n=10)
    relative to the pair's gap: descr: -21.0% [-51.2, +3.7]

## Qwen2.5-14B: held-out ablation

* A1, all lists: cross-fitted descr: -0.008 [-0.016, -0.002] (n=6)
    relative to the pair's gap: descr: -3.8% [-8.5, +2.2]
* B, all lists: cross-fitted descr: +0.004 [-0.019, +0.026] (n=9)
    relative to the pair's gap: descr: +6.9% [-2.3, +18.3]

## Qwen2.5-14B-Instruct: held-out ablation

* A1, all lists: cross-fitted 
    relative to the pair's gap: 
* B, all lists: cross-fitted descr: +0.076 [+0.009, +0.156] (n=10)
    relative to the pair's gap: descr: +36.9% [-7.6, +89.3]

## Qwen2.5-3B: held-out ablation

* A1, all lists: cross-fitted descr: -0.004 [-0.009, -0.001] (n=7)
    relative to the pair's gap: descr: -7.2% [-12.9, -2.3]
* B, all lists: cross-fitted descr: -0.003 [-0.018, +0.007] (n=7)
    relative to the pair's gap: descr: -4.5% [-29.0, +13.3]

## Qwen2.5-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted descr: -0.011 [-0.020, -0.005] (n=11)
    relative to the pair's gap: descr: -12.5% [-18.3, -6.7]
* B, all lists: cross-fitted descr: +0.023 [+0.005, +0.040] (n=11)
    relative to the pair's gap: descr: +32.4% [+11.3, +55.4]

## Qwen2.5-7B: held-out ablation

* A1, all lists: cross-fitted descr: +0.013 [-0.010, +0.039] (n=9)
    relative to the pair's gap: descr: +3.0% [-11.6, +14.5]
* B, all lists: cross-fitted descr: +0.055 [+0.024, +0.091] (n=14)
    relative to the pair's gap: descr: +33.6% [+5.9, +76.8]

## Qwen2.5-7B-Instruct: held-out ablation

* A1, all lists: cross-fitted descr: -0.044 [-0.099, -0.005] (n=9)
    relative to the pair's gap: descr: -19.0% [-35.4, +0.1]
* B, all lists: cross-fitted descr: -0.010 [-0.040, +0.021] (n=9)
    relative to the pair's gap: descr: -12.9% [-39.1, +14.0]

## gemma-2b: held-out ablation

* A1, all lists: cross-fitted descr: -0.045 [-0.079, -0.018] (n=9)
    relative to the pair's gap: descr: -23.0% [-27.9, -17.9]
* B, all lists: cross-fitted descr: -0.004 [-0.023, +0.018] (n=6)
    relative to the pair's gap: descr: -2.5% [-24.4, +26.5]

## gemma-2b-it: held-out ablation

* A1, all lists: cross-fitted descr: -0.018 [-0.026, -0.010] (n=13)
    relative to the pair's gap: descr: -14.0% [-21.2, -7.1]
* B, all lists: cross-fitted descr: -0.012 [-0.026, +0.002] (n=11)
    relative to the pair's gap: descr: -8.1% [-17.8, +2.7]

## Count of models with a moral-specific held-out effect

* frame A1, all lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
* frame B, all lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
