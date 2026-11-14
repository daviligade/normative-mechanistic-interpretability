# Neurons: discovery by depth and held-out ablation (exploratory)

Items: the item file is the set of accepted pairs.

## Llama-3.1-8B: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 199222 units at full size over 32 layers (peak at layer 31); halves select 800 / 800 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.1-8B-Instruct: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 203028 units at full size over 32 layers (peak at layer 31); halves select 800 / 800 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-1B: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 54161 units at full size over 16 layers (peak at layer 15); halves select 400 / 400 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-1B-Instruct: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 54939 units at full size over 16 layers (peak at layer 15); halves select 400 / 400 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-3B: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 100045 units at full size over 28 layers (peak at layer 27); halves select 700 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.2-3B-Instruct: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 100250 units at full size over 28 layers (peak at layer 27); halves select 700 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-14B: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 246641 units at full size over 48 layers (peak at layer 47); halves select 1175 / 1151 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-14B-Instruct: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 248026 units at full size over 48 layers (peak at layer 46); halves select 1175 / 1151 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-3B: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 133685 units at full size over 36 layers (peak at layer 2); halves select 855 / 875 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-3B-Instruct: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 145662 units at full size over 36 layers (peak at layer 2); halves select 870 / 875 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-7B: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 188741 units at full size over 28 layers (peak at layer 27); halves select 700 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Qwen2.5-7B-Instruct: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 181867 units at full size over 28 layers (peak at layer 27); halves select 700 / 700 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## gemma-2b: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 100799 units at full size over 18 layers (peak at layer 17); halves select 450 / 425 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## gemma-2b-it: discovery

* C: lists of the 'catC' contrast (a_C - a_B per pair (mean over the two versions); lists ordered by the moral-minus-norm difference of the frame-C activation times the unit's weight on the category direction); 90303 units at full size over 18 layers (peak at layer 11); halves select 450 / 425 (capped at 25 per layer). Discovery summary: code/analyze_unit_contrast.py

## Llama-3.1-8B: held-out ablation

* A1, all lists: cross-fitted moral: -0.029 [-0.040, -0.018] (n=78); norm: -0.010 [-0.018, -0.002] (n=104); descr: +0.016 [+0.010, +0.023] (n=38); moral - norm -0.019 [-0.032, -0.005] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -3.6% [-7.6, +0.1]; norm: -2.1% [-3.9, -0.3]; descr: +11.3% [+7.3, +15.7]; moral - norm -1.5% [-5.9, +2.6] -> not moral-specific
* B, all lists: cross-fitted moral: -0.023 [-0.036, -0.011] (n=77); norm: -0.012 [-0.018, -0.006] (n=104); descr: -0.014 [-0.020, -0.008] (n=40); moral - norm -0.011 [-0.026, +0.002] -> not moral-specific
    relative to the pair's gap: moral: -3.8% [-7.1, -0.4]; norm: -0.8% [-2.5, +1.1]; descr: -3.0% [-4.6, -1.5]; moral - norm -3.0% [-6.8, +0.9] -> not moral-specific

## Llama-3.1-8B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.011 [-0.018, -0.003] (n=78); norm: -0.028 [-0.035, -0.022] (n=107); descr: +0.023 [+0.016, +0.030] (n=37); moral - norm +0.018 [+0.008, +0.027] -> not moral-specific
    relative to the pair's gap: moral: -0.5% [-1.6, +0.6]; norm: -4.4% [-5.7, -3.1]; descr: +11.4% [+8.6, +14.1]; moral - norm +3.9% [+2.3, +5.7] -> not moral-specific
* B, all lists: cross-fitted moral: -0.027 [-0.042, -0.014] (n=78); norm: +0.001 [-0.008, +0.010] (n=103); descr: -0.010 [-0.021, +0.002] (n=40); moral - norm -0.028 [-0.044, -0.012] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -2.7% [-8.2, +3.0]; norm: +0.9% [-0.7, +2.7]; descr: -0.8% [-2.8, +1.3]; moral - norm -3.7% [-9.5, +2.1] -> not moral-specific

## Llama-3.2-1B: held-out ablation

* A1, all lists: cross-fitted moral: +0.011 [+0.003, +0.019] (n=78); norm: +0.000 [-0.006, +0.007] (n=97); descr: -0.001 [-0.013, +0.012] (n=39); moral - norm +0.010 [+0.001, +0.021] -> not moral-specific
    relative to the pair's gap: moral: +4.4% [+1.3, +7.6]; norm: -1.4% [-6.9, +3.7]; descr: +4.0% [-2.5, +12.4]; moral - norm +5.8% [-0.2, +12.0] -> not moral-specific
* B, all lists: cross-fitted moral: -0.004 [-0.013, +0.006] (n=73); norm: -0.008 [-0.015, -0.001] (n=91); descr: -0.005 [-0.019, +0.009] (n=35); moral - norm +0.004 [-0.008, +0.016] -> not moral-specific
    relative to the pair's gap: moral: +0.1% [-5.0, +4.9]; norm: +0.4% [-3.4, +4.4]; descr: -0.4% [-5.4, +5.0]; moral - norm -0.4% [-6.7, +5.7] -> not moral-specific

## Llama-3.2-1B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.050 [-0.064, -0.037] (n=69); norm: -0.027 [-0.036, -0.017] (n=92); descr: -0.019 [-0.028, -0.009] (n=38); moral - norm -0.023 [-0.040, -0.007] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -6.2% [-10.3, -1.3]; norm: -4.7% [-9.7, +2.5]; descr: -8.3% [-13.1, -4.3]; moral - norm -1.6% [-9.5, +5.5] -> not moral-specific
* B, all lists: cross-fitted moral: -0.025 [-0.052, +0.002] (n=72); norm: -0.030 [-0.043, -0.017] (n=95); descr: -0.008 [-0.021, +0.005] (n=37); moral - norm +0.005 [-0.024, +0.034] -> not moral-specific
    relative to the pair's gap: moral: -1.0% [-9.2, +7.2]; norm: -6.0% [-10.2, -1.8]; descr: +4.3% [-3.7, +17.1]; moral - norm +5.0% [-4.5, +14.5] -> not moral-specific

## Llama-3.2-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.020 [-0.032, -0.009] (n=79); norm: -0.011 [-0.019, -0.004] (n=104); descr: +0.004 [-0.011, +0.019] (n=40); moral - norm -0.009 [-0.023, +0.005] -> not moral-specific
    relative to the pair's gap: moral: -0.2% [-2.8, +2.6]; norm: -0.7% [-4.1, +3.0]; descr: +5.2% [-0.7, +12.1]; moral - norm +0.4% [-4.0, +4.8] -> not moral-specific
* B, all lists: cross-fitted moral: -0.017 [-0.024, -0.011] (n=78); norm: +0.005 [+0.001, +0.009] (n=100); descr: +0.014 [+0.004, +0.024] (n=40); moral - norm -0.022 [-0.031, -0.014] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -1.9% [-4.2, +0.8]; norm: +0.7% [-0.5, +2.1]; descr: +4.4% [+1.8, +7.0]; moral - norm -2.6% [-5.4, +0.3] -> not moral-specific

## Llama-3.2-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.055 [-0.067, -0.044] (n=72); norm: -0.013 [-0.022, -0.004] (n=103); descr: +0.011 [-0.001, +0.024] (n=39); moral - norm -0.042 [-0.056, -0.028] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -5.2% [-7.1, -3.1]; norm: -0.8% [-2.8, +1.4]; descr: +2.1% [-0.2, +4.6]; moral - norm -4.4% [-7.4, -1.5] -> MORAL-SPECIFIC
* B, all lists: cross-fitted moral: -0.019 [-0.039, -0.001] (n=69); norm: +0.026 [+0.017, +0.035] (n=103); descr: +0.028 [+0.018, +0.038] (n=39); moral - norm -0.044 [-0.067, -0.025] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -3.6% [-9.1, +0.9]; norm: +4.8% [+1.9, +7.9]; descr: +4.2% [+2.1, +6.6]; moral - norm -8.3% [-14.8, -3.1] -> not moral-specific

## Qwen2.5-14B: held-out ablation

* A1, all lists: cross-fitted moral: -0.031 [-0.040, -0.022] (n=79); norm: +0.015 [+0.005, +0.024] (n=99); descr: +0.043 [+0.030, +0.057] (n=36); moral - norm -0.045 [-0.059, -0.032] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -1.8% [-2.5, -0.8]; norm: +5.4% [+2.7, +8.6]; descr: +26.5% [+20.9, +32.4]; moral - norm -7.2% [-10.6, -4.3] -> not moral-specific
* B, all lists: cross-fitted moral: -0.013 [-0.024, -0.002] (n=79); norm: +0.042 [+0.035, +0.049] (n=106); descr: -0.004 [-0.014, +0.006] (n=40); moral - norm -0.055 [-0.067, -0.042] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -0.0% [-1.7, +1.9]; norm: +4.8% [+3.6, +6.3]; descr: -0.9% [-2.7, +0.6]; moral - norm -4.8% [-7.1, -2.5] -> not moral-specific

## Qwen2.5-14B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.031 [-0.041, -0.020] (n=79); norm: -0.000 [-0.012, +0.012] (n=99); descr: +0.051 [+0.018, +0.087] (n=18); moral - norm -0.031 [-0.047, -0.015] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -0.2% [-2.0, +2.2]; norm: +2.1% [-0.8, +5.1]; descr: +32.1% [+16.6, +48.9]; moral - norm -2.4% [-6.0, +1.2] -> not moral-specific
* B, all lists: cross-fitted moral: +0.002 [-0.018, +0.022] (n=78); norm: +0.056 [+0.045, +0.067] (n=104); descr: -0.025 [-0.041, -0.009] (n=40); moral - norm -0.054 [-0.076, -0.031] -> not moral-specific
    relative to the pair's gap: moral: +1.3% [-1.9, +5.8]; norm: +6.5% [+4.9, +8.1]; descr: -2.7% [-4.7, -0.8]; moral - norm -5.1% [-8.8, -0.5] -> not moral-specific

## Qwen2.5-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.030 [-0.039, -0.022] (n=78); norm: -0.001 [-0.006, +0.004] (n=98); descr: +0.024 [+0.018, +0.030] (n=39); moral - norm -0.029 [-0.039, -0.018] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -7.3% [-10.1, -4.6]; norm: +0.2% [-2.6, +3.0]; descr: +10.4% [+7.5, +13.4]; moral - norm -7.5% [-11.2, -3.6] -> MORAL-SPECIFIC
* B, all lists: cross-fitted moral: -0.018 [-0.025, -0.011] (n=75); norm: +0.011 [+0.007, +0.016] (n=101); descr: +0.013 [+0.007, +0.019] (n=40); moral - norm -0.029 [-0.038, -0.021] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -6.7% [-11.9, -3.0]; norm: +3.0% [+1.4, +4.6]; descr: +4.6% [+2.7, +6.6]; moral - norm -9.7% [-14.8, -5.6] -> MORAL-SPECIFIC

## Qwen2.5-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.018 [-0.027, -0.009] (n=76); norm: +0.006 [-0.003, +0.016] (n=103); descr: +0.047 [+0.033, +0.062] (n=40); moral - norm -0.024 [-0.038, -0.011] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -2.4% [-6.2, +0.4]; norm: +1.1% [-0.8, +3.2]; descr: +9.6% [+6.4, +12.9]; moral - norm -3.5% [-7.8, -0.0] -> not moral-specific
* B, all lists: cross-fitted moral: -0.037 [-0.053, -0.021] (n=76); norm: -0.012 [-0.028, +0.003] (n=104); descr: -0.038 [-0.055, -0.022] (n=40); moral - norm -0.024 [-0.047, -0.002] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -7.9% [-15.4, -2.2]; norm: -2.7% [-5.7, +0.2]; descr: -3.2% [-5.9, -0.2]; moral - norm -5.2% [-13.2, +1.4] -> not moral-specific

## Qwen2.5-7B: held-out ablation

* A1, all lists: cross-fitted moral: -0.086 [-0.104, -0.068] (n=79); norm: -0.046 [-0.060, -0.031] (n=104); descr: +0.049 [+0.040, +0.059] (n=40); moral - norm -0.040 [-0.063, -0.018] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -5.0% [-8.2, -1.5]; norm: -3.1% [-5.1, -0.9]; descr: +11.1% [+8.8, +13.2]; moral - norm -2.0% [-5.8, +2.3] -> not moral-specific
* B, all lists: cross-fitted moral: -0.014 [-0.027, -0.001] (n=77); norm: +0.013 [+0.005, +0.020] (n=107); descr: +0.032 [+0.023, +0.041] (n=40); moral - norm -0.027 [-0.042, -0.011] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: +0.8% [-1.5, +3.6]; norm: +3.3% [+1.6, +5.2]; descr: +4.0% [+2.7, +5.6]; moral - norm -2.4% [-5.5, +0.7] -> not moral-specific

## Qwen2.5-7B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.099 [-0.120, -0.077] (n=75); norm: -0.043 [-0.060, -0.026] (n=106); descr: +0.088 [+0.065, +0.111] (n=40); moral - norm -0.056 [-0.085, -0.027] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -5.9% [-9.4, -2.0]; norm: -2.7% [-6.3, +1.0]; descr: +16.6% [+11.5, +22.2]; moral - norm -3.2% [-8.4, +2.1] -> not moral-specific
* B, all lists: cross-fitted moral: -0.008 [-0.028, +0.011] (n=77); norm: +0.000 [-0.014, +0.014] (n=104); descr: +0.030 [+0.014, +0.047] (n=40); moral - norm -0.008 [-0.032, +0.017] -> not moral-specific
    relative to the pair's gap: moral: +0.9% [-2.2, +4.0]; norm: +7.8% [+0.6, +20.5]; descr: +3.0% [+1.0, +5.1]; moral - norm -6.9% [-20.9, +1.6] -> not moral-specific

## gemma-2b: held-out ablation

* A1, all lists: cross-fitted moral: -0.053 [-0.064, -0.043] (n=74); norm: -0.012 [-0.020, -0.005] (n=99); descr: +0.002 [-0.005, +0.010] (n=39); moral - norm -0.041 [-0.054, -0.028] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -8.7% [-12.8, -4.7]; norm: -2.3% [-4.2, -0.4]; descr: +2.2% [-0.3, +4.8]; moral - norm -6.4% [-10.9, -2.0] -> MORAL-SPECIFIC
* B, all lists: cross-fitted moral: -0.051 [-0.061, -0.041] (n=72); norm: -0.018 [-0.024, -0.012] (n=95); descr: -0.017 [-0.025, -0.010] (n=40); moral - norm -0.033 [-0.045, -0.022] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -7.9% [-12.6, -2.6]; norm: -2.6% [-4.1, -1.1]; descr: -4.2% [-6.3, -2.2]; moral - norm -5.3% [-10.1, +0.2] -> not moral-specific

## gemma-2b-it: held-out ablation

* A1, all lists: cross-fitted moral: -0.011 [-0.027, +0.006] (n=73); norm: +0.009 [-0.005, +0.024] (n=98); descr: +0.048 [+0.027, +0.069] (n=37); moral - norm -0.020 [-0.042, +0.002] -> not moral-specific
    relative to the pair's gap: moral: +0.2% [-2.9, +3.4]; norm: +2.1% [-2.5, +6.6]; descr: +12.3% [+6.6, +18.9]; moral - norm -1.9% [-7.4, +3.5] -> not moral-specific
* B, all lists: cross-fitted moral: -0.047 [-0.071, -0.025] (n=67); norm: -0.006 [-0.015, +0.003] (n=88); descr: -0.001 [-0.014, +0.010] (n=34); moral - norm -0.041 [-0.066, -0.018] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -5.9% [-17.8, +5.0]; norm: -2.8% [-7.5, +1.4]; descr: +0.1% [-3.4, +4.0]; moral - norm -3.1% [-15.9, +9.1] -> not moral-specific

## Count of models with a moral-specific held-out effect

* frame A1, all lists: 10 of 14 models (absolute); relative to the pair's gap: 3 of 14
* frame B, all lists: 9 of 14 models (absolute); relative to the pair's gap: 1 of 14
