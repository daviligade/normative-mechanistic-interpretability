# Neurons: discovery by depth and held-out ablation (exploratory)

Items: stimuli/items_followup_twins.json is not the set of accepted pairs (stimuli/items_final.json).

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

* A1, all lists: cross-fitted moral: -0.066 [-0.079, -0.053] (n=28); norm: -0.064 [-0.074, -0.052] (n=29); moral - norm -0.002 [-0.019, +0.014] -> not moral-specific
    relative to the pair's gap: moral: -15.3% [-20.0, -10.9]; norm: -14.1% [-17.0, -10.5]; moral - norm -1.2% [-7.0, +4.0] -> not moral-specific
* B, all lists: cross-fitted moral: +0.074 [+0.056, +0.093] (n=29); norm: +0.078 [+0.049, +0.104] (n=29); moral - norm -0.004 [-0.036, +0.030] -> not moral-specific
    relative to the pair's gap: moral: +15.4% [+10.1, +21.4]; norm: +14.1% [+8.5, +19.4]; moral - norm +1.3% [-6.5, +9.7] -> not moral-specific

## Llama-3.1-8B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.027 [-0.036, -0.018] (n=29); norm: -0.030 [-0.037, -0.021] (n=29); moral - norm +0.003 [-0.009, +0.015] -> not moral-specific
    relative to the pair's gap: moral: -2.6% [-4.5, -0.2]; norm: -3.9% [-5.2, -2.3]; moral - norm +1.3% [-1.2, +4.0] -> not moral-specific
* B, all lists: cross-fitted moral: +0.086 [+0.059, +0.113] (n=28); norm: +0.092 [+0.062, +0.120] (n=29); moral - norm -0.006 [-0.046, +0.034] -> not moral-specific
    relative to the pair's gap: moral: +21.3% [+9.0, +40.7]; norm: +17.6% [+10.2, +26.8]; moral - norm +3.8% [-12.1, +24.6] -> not moral-specific

## Llama-3.2-1B: held-out ablation

* A1, all lists: cross-fitted moral: -0.023 [-0.039, -0.008] (n=27); norm: -0.028 [-0.041, -0.015] (n=27); moral - norm +0.005 [-0.015, +0.025] -> not moral-specific
    relative to the pair's gap: moral: -5.1% [-9.2, -1.5]; norm: -7.9% [-12.9, -3.6]; moral - norm +2.8% [-3.1, +9.1] -> not moral-specific
* B, all lists: cross-fitted moral: -0.034 [-0.044, -0.024] (n=28); norm: -0.043 [-0.060, -0.027] (n=27); moral - norm +0.009 [-0.009, +0.028] -> not moral-specific
    relative to the pair's gap: moral: -14.4% [-19.7, -9.5]; norm: -17.9% [-29.7, -10.1]; moral - norm +3.6% [-6.4, +16.5] -> not moral-specific

## Llama-3.2-1B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.051 [-0.067, -0.035] (n=26); norm: -0.046 [-0.061, -0.030] (n=26); moral - norm -0.005 [-0.028, +0.017] -> not moral-specific
    relative to the pair's gap: moral: -13.5% [-17.9, -9.2]; norm: -13.7% [-19.1, -7.0]; moral - norm +0.3% [-7.6, +7.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.075 [-0.104, -0.047] (n=28); norm: -0.110 [-0.139, -0.080] (n=27); moral - norm +0.035 [-0.006, +0.076] -> not moral-specific
    relative to the pair's gap: moral: -14.6% [-21.7, -8.5]; norm: -23.1% [-30.5, -16.2]; moral - norm +8.4% [-1.2, +18.0] -> not moral-specific

## Llama-3.2-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.051 [-0.071, -0.032] (n=28); norm: -0.056 [-0.072, -0.040] (n=29); moral - norm +0.005 [-0.020, +0.030] -> not moral-specific
    relative to the pair's gap: moral: -7.1% [-10.1, -3.7]; norm: -8.7% [-11.1, -6.4]; moral - norm +1.6% [-2.2, +5.8] -> not moral-specific
* B, all lists: cross-fitted moral: -0.056 [-0.075, -0.037] (n=28); norm: -0.057 [-0.076, -0.037] (n=29); moral - norm +0.001 [-0.027, +0.028] -> not moral-specific
    relative to the pair's gap: moral: -9.3% [-13.4, -5.1]; norm: -7.8% [-12.6, -1.7]; moral - norm -1.6% [-8.7, +4.9] -> not moral-specific

## Llama-3.2-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.147 [-0.193, -0.102] (n=27); norm: -0.202 [-0.246, -0.157] (n=27); moral - norm +0.055 [-0.008, +0.117] -> not moral-specific
    relative to the pair's gap: moral: -14.5% [-20.1, -8.7]; norm: -22.6% [-30.2, -15.8]; moral - norm +8.1% [-0.8, +17.5] -> not moral-specific
* B, all lists: cross-fitted moral: -0.050 [-0.085, -0.016] (n=24); norm: -0.057 [-0.085, -0.028] (n=25); moral - norm +0.007 [-0.039, +0.050] -> not moral-specific
    relative to the pair's gap: moral: -0.2% [-11.4, +13.7]; norm: -2.4% [-11.1, +7.9]; moral - norm +2.2% [-13.3, +18.4] -> not moral-specific

## Qwen2.5-14B: held-out ablation

* A1, all lists: cross-fitted moral: +0.014 [+0.001, +0.027] (n=29); norm: +0.000 [-0.015, +0.015] (n=29); moral - norm +0.014 [-0.006, +0.034] -> not moral-specific
    relative to the pair's gap: moral: +8.8% [+0.5, +22.6]; norm: +0.8% [-0.9, +2.5]; moral - norm +8.0% [-0.7, +23.1] -> not moral-specific
* B, all lists: cross-fitted moral: -0.020 [-0.051, +0.018] (n=29); norm: -0.038 [-0.066, -0.008] (n=29); moral - norm +0.019 [-0.025, +0.065] -> not moral-specific
    relative to the pair's gap: moral: +1.0% [-3.1, +6.4]; norm: +9.0% [-5.5, +35.5]; moral - norm -8.0% [-35.4, +8.4] -> not moral-specific

## Qwen2.5-14B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.045 [-0.059, -0.029] (n=29); norm: -0.058 [-0.077, -0.038] (n=29); moral - norm +0.013 [-0.012, +0.038] -> not moral-specific
    relative to the pair's gap: moral: -2.2% [-4.7, +1.1]; norm: -3.4% [-6.2, +0.7]; moral - norm +1.2% [-3.5, +5.5] -> not moral-specific
* B, all lists: cross-fitted moral: -0.021 [-0.050, +0.010] (n=29); norm: -0.035 [-0.073, +0.008] (n=28); moral - norm +0.014 [-0.036, +0.060] -> not moral-specific
    relative to the pair's gap: moral: +0.0% [-6.0, +6.8]; norm: -4.6% [-10.3, +1.0]; moral - norm +4.6% [-3.5, +13.5] -> not moral-specific

## Qwen2.5-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.017 [-0.022, -0.012] (n=27); norm: -0.020 [-0.025, -0.015] (n=28); moral - norm +0.003 [-0.004, +0.011] -> not moral-specific
    relative to the pair's gap: moral: -3.9% [-5.8, -1.4]; norm: -5.1% [-6.3, -4.0]; moral - norm +1.2% [-1.1, +4.1] -> not moral-specific
* B, all lists: cross-fitted moral: -0.043 [-0.062, -0.025] (n=28); norm: -0.052 [-0.071, -0.033] (n=29); moral - norm +0.009 [-0.018, +0.036] -> not moral-specific
    relative to the pair's gap: moral: -10.1% [-14.5, -5.6]; norm: -15.0% [-20.5, -9.3]; moral - norm +4.9% [-2.3, +12.2] -> not moral-specific

## Qwen2.5-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.028 [-0.041, -0.014] (n=27); norm: -0.034 [-0.045, -0.023] (n=29); moral - norm +0.006 [-0.011, +0.025] -> not moral-specific
    relative to the pair's gap: moral: -0.7% [-3.5, +2.6]; norm: -3.3% [-5.0, -1.7]; moral - norm +2.6% [-0.7, +6.3] -> not moral-specific
* B, all lists: cross-fitted moral: +0.011 [-0.020, +0.043] (n=27); norm: +0.006 [-0.035, +0.042] (n=28); moral - norm +0.006 [-0.042, +0.055] -> not moral-specific
    relative to the pair's gap: moral: +0.8% [-4.2, +6.0]; norm: -2.3% [-8.6, +3.1]; moral - norm +3.1% [-4.0, +11.1] -> not moral-specific

## Qwen2.5-7B: held-out ablation

* A1, all lists: cross-fitted moral: +0.016 [+0.002, +0.031] (n=29); norm: +0.004 [-0.015, +0.026] (n=29); moral - norm +0.012 [-0.014, +0.037] -> not moral-specific
    relative to the pair's gap: moral: +2.7% [-0.0, +6.0]; norm: +3.4% [-1.3, +9.3]; moral - norm -0.7% [-7.3, +4.9] -> not moral-specific
* B, all lists: cross-fitted moral: +0.198 [+0.152, +0.240] (n=29); norm: +0.182 [+0.136, +0.225] (n=28); moral - norm +0.016 [-0.043, +0.080] -> not moral-specific
    relative to the pair's gap: moral: +18.8% [+13.2, +24.0]; norm: +17.7% [+11.8, +23.4]; moral - norm +1.2% [-6.9, +9.1] -> not moral-specific

## Qwen2.5-7B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.087 [-0.114, -0.061] (n=29); norm: -0.110 [-0.135, -0.085] (n=27); moral - norm +0.022 [-0.013, +0.058] -> not moral-specific
    relative to the pair's gap: moral: -6.4% [-10.7, -1.0]; norm: -12.6% [-15.1, -10.0]; moral - norm +6.2% [+1.1, +11.9] -> not moral-specific
* B, all lists: cross-fitted moral: +0.246 [+0.184, +0.312] (n=29); norm: +0.236 [+0.160, +0.302] (n=29); moral - norm +0.010 [-0.082, +0.109] -> not moral-specific
    relative to the pair's gap: moral: +23.3% [+13.4, +34.0]; norm: +19.5% [+5.9, +33.2]; moral - norm +3.8% [-13.1, +20.5] -> not moral-specific

## gemma-2b: held-out ablation

* A1, all lists: cross-fitted moral: -0.059 [-0.080, -0.039] (n=25); norm: -0.082 [-0.102, -0.063] (n=27); moral - norm +0.023 [-0.006, +0.051] -> not moral-specific
    relative to the pair's gap: moral: -6.5% [-12.7, +0.9]; norm: -16.0% [-19.6, -10.7]; moral - norm +9.5% [+1.6, +18.3] -> not moral-specific
* B, all lists: cross-fitted moral: -0.072 [-0.096, -0.048] (n=27); norm: -0.078 [-0.097, -0.059] (n=28); moral - norm +0.006 [-0.024, +0.037] -> not moral-specific
    relative to the pair's gap: moral: -14.2% [-22.1, -6.2]; norm: -22.0% [-27.0, -16.8]; moral - norm +7.8% [-1.4, +17.0] -> not moral-specific

## gemma-2b-it: held-out ablation

* A1, all lists: cross-fitted moral: -0.065 [-0.093, -0.036] (n=26); norm: -0.065 [-0.092, -0.037] (n=28); moral - norm +0.000 [-0.040, +0.041] -> not moral-specific
    relative to the pair's gap: moral: -3.9% [-7.3, -0.1]; norm: +16.8% [-7.5, +61.9]; moral - norm -20.8% [-67.6, +4.6] -> not moral-specific
* B, all lists: cross-fitted moral: -0.090 [-0.118, -0.063] (n=27); norm: -0.090 [-0.104, -0.075] (n=26); moral - norm -0.001 [-0.033, +0.029] -> not moral-specific
    relative to the pair's gap: moral: -19.5% [-29.2, -6.7]; norm: -25.6% [-32.5, -19.5]; moral - norm +6.1% [-5.8, +20.0] -> not moral-specific

## Count of models with a moral-specific held-out effect

* frame A1, all lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
* frame B, all lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
