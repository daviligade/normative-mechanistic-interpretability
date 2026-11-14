# Neurons: discovery by depth and held-out ablation (exploratory)

Items: stimuli/items_followup_func.json is not the set of accepted pairs (stimuli/items_final.json).

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

* A1, all lists: cross-fitted moral: -0.052 [-0.064, -0.040] (n=35); norm: -0.038 [-0.049, -0.026] (n=32); moral - norm -0.015 [-0.032, +0.002] -> not moral-specific
    relative to the pair's gap: moral: -11.1% [-14.8, -7.6]; norm: -12.1% [-18.2, -6.8]; moral - norm +1.0% [-5.6, +7.8] -> not moral-specific
* B, all lists: cross-fitted moral: +0.046 [+0.023, +0.068] (n=34); norm: +0.014 [-0.006, +0.035] (n=35); moral - norm +0.032 [-0.000, +0.063] -> not moral-specific
    relative to the pair's gap: moral: +8.5% [+3.3, +13.7]; norm: -0.8% [-13.2, +9.9]; moral - norm +9.3% [-2.6, +22.0] -> not moral-specific

## Llama-3.1-8B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.016 [-0.024, -0.010] (n=35); norm: -0.024 [-0.033, -0.015] (n=34); moral - norm +0.008 [-0.004, +0.019] -> not moral-specific
    relative to the pair's gap: moral: -1.7% [-2.8, -0.6]; norm: -3.0% [-5.2, -0.6]; moral - norm +1.2% [-1.4, +3.7] -> not moral-specific
* B, all lists: cross-fitted moral: +0.036 [+0.009, +0.065] (n=35); norm: +0.023 [-0.005, +0.050] (n=34); moral - norm +0.013 [-0.025, +0.052] -> not moral-specific
    relative to the pair's gap: moral: +2.7% [-2.7, +8.7]; norm: +12.8% [-1.6, +32.3]; moral - norm -10.0% [-30.7, +6.4] -> not moral-specific

## Llama-3.2-1B: held-out ablation

* A1, all lists: cross-fitted moral: -0.006 [-0.018, +0.006] (n=35); norm: -0.028 [-0.045, -0.012] (n=28); moral - norm +0.022 [+0.002, +0.043] -> not moral-specific
    relative to the pair's gap: moral: -2.7% [-10.6, +6.6]; norm: -8.9% [-16.7, -0.7]; moral - norm +6.2% [-5.6, +18.6] -> not moral-specific
* B, all lists: cross-fitted moral: -0.026 [-0.036, -0.016] (n=30); norm: -0.029 [-0.044, -0.015] (n=28); moral - norm +0.003 [-0.015, +0.021] -> not moral-specific
    relative to the pair's gap: moral: -7.9% [-12.1, -3.4]; norm: -9.5% [-16.1, -3.3]; moral - norm +1.6% [-6.0, +9.9] -> not moral-specific

## Llama-3.2-1B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.043 [-0.055, -0.030] (n=32); norm: -0.050 [-0.064, -0.037] (n=29); moral - norm +0.008 [-0.011, +0.026] -> not moral-specific
    relative to the pair's gap: moral: -9.6% [-15.7, -2.3]; norm: -27.6% [-39.8, -18.2]; moral - norm +18.0% [+6.7, +32.8] -> not moral-specific
* B, all lists: cross-fitted moral: -0.055 [-0.077, -0.033] (n=31); norm: -0.045 [-0.070, -0.021] (n=30); moral - norm -0.011 [-0.043, +0.022] -> not moral-specific
    relative to the pair's gap: moral: -7.1% [-16.8, +3.2]; norm: -14.5% [-25.4, -4.4]; moral - norm +7.4% [-6.9, +22.3] -> not moral-specific

## Llama-3.2-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.054 [-0.070, -0.040] (n=32); norm: -0.071 [-0.088, -0.054] (n=32); moral - norm +0.017 [-0.006, +0.040] -> not moral-specific
    relative to the pair's gap: moral: -9.8% [-12.4, -7.4]; norm: -16.1% [-19.7, -12.3]; moral - norm +6.3% [+1.6, +10.6] -> not moral-specific
* B, all lists: cross-fitted moral: -0.084 [-0.103, -0.065] (n=33); norm: -0.059 [-0.076, -0.042] (n=30); moral - norm -0.025 [-0.052, +0.001] -> not moral-specific
    relative to the pair's gap: moral: -18.0% [-25.6, -11.0]; norm: -15.1% [-20.0, -9.5]; moral - norm -2.9% [-12.7, +5.9] -> not moral-specific

## Llama-3.2-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.171 [-0.214, -0.127] (n=33); norm: -0.144 [-0.187, -0.100] (n=31); moral - norm -0.027 [-0.087, +0.034] -> not moral-specific
    relative to the pair's gap: moral: -14.1% [-21.7, -4.5]; norm: -20.1% [-25.9, -14.1]; moral - norm +6.0% [-3.6, +17.3] -> not moral-specific
* B, all lists: cross-fitted moral: -0.086 [-0.119, -0.053] (n=31); norm: -0.061 [-0.095, -0.027] (n=30); moral - norm -0.025 [-0.073, +0.022] -> not moral-specific
    relative to the pair's gap: moral: -12.5% [-17.6, -7.3]; norm: -10.5% [-20.7, -1.0]; moral - norm -2.0% [-13.2, +9.4] -> not moral-specific

## Qwen2.5-14B: held-out ablation

* A1, all lists: cross-fitted moral: -0.011 [-0.025, +0.002] (n=36); norm: -0.021 [-0.030, -0.012] (n=33); moral - norm +0.010 [-0.006, +0.026] -> not moral-specific
    relative to the pair's gap: moral: +3.4% [-1.0, +8.8]; norm: -3.2% [-5.0, -1.4]; moral - norm +6.6% [+1.8, +12.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.038 [-0.063, -0.013] (n=33); norm: -0.087 [-0.109, -0.066] (n=33); moral - norm +0.050 [+0.017, +0.083] -> not moral-specific
    relative to the pair's gap: moral: -2.3% [-6.4, +2.7]; norm: -13.6% [-20.1, -7.6]; moral - norm +11.4% [+3.9, +19.5] -> not moral-specific

## Qwen2.5-14B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.044 [-0.057, -0.030] (n=36); norm: -0.056 [-0.073, -0.038] (n=31); moral - norm +0.012 [-0.011, +0.032] -> not moral-specific
    relative to the pair's gap: moral: -2.8% [-4.5, -1.0]; norm: -5.6% [-9.4, -0.7]; moral - norm +2.8% [-2.1, +7.0] -> not moral-specific
* B, all lists: cross-fitted moral: -0.058 [-0.093, -0.016] (n=34); norm: -0.048 [-0.078, -0.018] (n=31); moral - norm -0.010 [-0.059, +0.042] -> not moral-specific
    relative to the pair's gap: moral: -4.7% [-9.8, +1.9]; norm: -3.5% [-10.2, +4.1]; moral - norm -1.1% [-10.4, +7.8] -> not moral-specific

## Qwen2.5-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.030 [-0.041, -0.020] (n=32); norm: -0.023 [-0.030, -0.016] (n=28); moral - norm -0.007 [-0.021, +0.005] -> not moral-specific
    relative to the pair's gap: moral: -9.5% [-12.9, -6.4]; norm: -12.2% [-19.9, -7.4]; moral - norm +2.7% [-3.5, +11.1] -> not moral-specific
* B, all lists: cross-fitted moral: -0.033 [-0.058, -0.011] (n=32); norm: -0.018 [-0.040, +0.002] (n=33); moral - norm -0.015 [-0.046, +0.017] -> not moral-specific
    relative to the pair's gap: moral: -4.6% [-14.3, +7.3]; norm: -10.6% [-17.8, -3.5]; moral - norm +6.0% [-6.2, +19.5] -> not moral-specific

## Qwen2.5-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.039 [-0.053, -0.024] (n=33); norm: -0.037 [-0.049, -0.025] (n=32); moral - norm -0.002 [-0.020, +0.017] -> not moral-specific
    relative to the pair's gap: moral: -2.9% [-6.2, +0.6]; norm: -7.3% [-11.3, -3.8]; moral - norm +4.4% [-0.5, +9.6] -> not moral-specific
* B, all lists: cross-fitted moral: -0.033 [-0.065, +0.003] (n=32); norm: -0.013 [-0.046, +0.020] (n=33); moral - norm -0.019 [-0.067, +0.029] -> not moral-specific
    relative to the pair's gap: moral: -5.4% [-15.0, +5.4]; norm: -3.7% [-12.8, +4.9]; moral - norm -1.7% [-15.5, +12.1] -> not moral-specific

## Qwen2.5-7B: held-out ablation

* A1, all lists: cross-fitted moral: +0.015 [+0.000, +0.029] (n=34); norm: -0.021 [-0.038, -0.004] (n=33); moral - norm +0.035 [+0.013, +0.058] -> not moral-specific
    relative to the pair's gap: moral: +6.6% [-2.0, +21.5]; norm: -9.3% [-18.3, -2.4]; moral - norm +16.0% [+3.6, +33.7] -> not moral-specific
* B, all lists: cross-fitted moral: +0.149 [+0.106, +0.195] (n=34); norm: +0.125 [+0.073, +0.176] (n=35); moral - norm +0.025 [-0.043, +0.093] -> not moral-specific
    relative to the pair's gap: moral: +14.1% [+5.8, +21.6]; norm: +18.9% [+3.6, +38.0]; moral - norm -4.9% [-25.2, +13.1] -> not moral-specific

## Qwen2.5-7B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.092 [-0.121, -0.059] (n=32); norm: -0.119 [-0.151, -0.086] (n=33); moral - norm +0.027 [-0.018, +0.073] -> not moral-specific
    relative to the pair's gap: moral: +1.7% [-9.1, +16.2]; norm: -12.5% [-18.9, -5.0]; moral - norm +14.2% [+0.9, +30.3] -> not moral-specific
* B, all lists: cross-fitted moral: +0.159 [+0.093, +0.227] (n=31); norm: +0.107 [+0.043, +0.173] (n=34); moral - norm +0.052 [-0.042, +0.146] -> not moral-specific
    relative to the pair's gap: moral: +17.9% [+8.1, +28.9]; norm: +7.2% [-7.6, +21.1]; moral - norm +10.7% [-6.3, +28.3] -> not moral-specific

## gemma-2b: held-out ablation

* A1, all lists: cross-fitted moral: -0.062 [-0.076, -0.046] (n=35); norm: -0.086 [-0.111, -0.061] (n=31); moral - norm +0.024 [-0.005, +0.054] -> not moral-specific
    relative to the pair's gap: moral: -13.4% [-17.2, -9.1]; norm: -16.1% [-21.0, -10.6]; moral - norm +2.7% [-4.2, +9.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.067 [-0.088, -0.045] (n=35); norm: -0.062 [-0.087, -0.039] (n=31); moral - norm -0.005 [-0.037, +0.028] -> not moral-specific
    relative to the pair's gap: moral: -15.3% [-23.2, -6.8]; norm: -15.4% [-25.2, -4.4]; moral - norm +0.1% [-13.5, +13.0] -> not moral-specific

## gemma-2b-it: held-out ablation

* A1, all lists: cross-fitted moral: -0.027 [-0.053, +0.003] (n=33); norm: -0.054 [-0.078, -0.031] (n=30); moral - norm +0.027 [-0.010, +0.065] -> not moral-specific
    relative to the pair's gap: moral: -1.9% [-6.4, +3.2]; norm: -5.5% [-13.7, +2.3]; moral - norm +3.7% [-5.9, +13.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.077 [-0.099, -0.057] (n=31); norm: -0.059 [-0.087, -0.034] (n=27); moral - norm -0.018 [-0.051, +0.016] -> not moral-specific
    relative to the pair's gap: moral: -21.7% [-34.5, -10.3]; norm: -14.9% [-29.2, -0.3]; moral - norm -6.8% [-25.5, +12.1] -> not moral-specific

## Count of models with a moral-specific held-out effect

* frame A1, all lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
* frame B, all lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
