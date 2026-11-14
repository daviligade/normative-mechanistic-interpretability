# Neurons: discovery by depth and held-out ablation (exploratory)

Items: the item file is the set of accepted pairs.

## Llama-3.1-8B: discovery

* A1: 113070 neurons separate moral from norm pairs over 32 layers (peak at layer 29); moral vs norm exceeds every norm-vs-norm split in 29 layers [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; halves select 59949 / 52389
* B: 67282 neurons separate moral from norm pairs over 32 layers (peak at layer 26); moral vs norm exceeds every norm-vs-norm split in 22 layers [2, 4, 5, 8, 9, 10, 11, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; halves select 26146 / 27485

## Llama-3.1-8B-Instruct: discovery

* A1: 114525 neurons separate moral from norm pairs over 32 layers (peak at layer 28); moral vs norm exceeds every norm-vs-norm split in 30 layers [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]; halves select 53082 / 57961
* B: 72330 neurons separate moral from norm pairs over 32 layers (peak at layer 26); moral vs norm exceeds every norm-vs-norm split in 20 layers [1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 23, 24, 25, 26, 27, 28, 29, 30, 31]; halves select 26085 / 33027

## Llama-3.2-1B: discovery

* A1: 5055 neurons separate moral from norm pairs over 16 layers (peak at layer 14); moral vs norm exceeds every norm-vs-norm split in 5 layers [1, 2, 4, 5, 7]; halves select 236 / 311
* B: 8396 neurons separate moral from norm pairs over 16 layers (peak at layer 14); moral vs norm exceeds every norm-vs-norm split in 0 layers []; halves select 1653 / 1930
* C: 81248 neurons separate moral from norm pairs over 16 layers (peak at layer 15); moral vs norm exceeds every norm-vs-norm split in 0 layers []; halves select 62061 / 64868

## Llama-3.2-1B-Instruct: discovery

* A1: 21636 neurons separate moral from norm pairs over 16 layers (peak at layer 13); moral vs norm exceeds every norm-vs-norm split in 15 layers [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]; halves select 8947 / 3452
* B: 10722 neurons separate moral from norm pairs over 16 layers (peak at layer 14); moral vs norm exceeds every norm-vs-norm split in 9 layers [4, 7, 9, 10, 11, 12, 13, 14, 15]; halves select 3195 / 2064
* C: 83426 neurons separate moral from norm pairs over 16 layers (peak at layer 15); moral vs norm exceeds every norm-vs-norm split in 1 layers [7]; halves select 64727 / 67318

## Llama-3.2-3B: discovery

* A1: 33651 neurons separate moral from norm pairs over 28 layers (peak at layer 27); moral vs norm exceeds every norm-vs-norm split in 23 layers [1, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]; halves select 16121 / 6376
* B: 27291 neurons separate moral from norm pairs over 28 layers (peak at layer 27); moral vs norm exceeds every norm-vs-norm split in 18 layers [3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 20, 21, 24, 25, 26, 27]; halves select 11069 / 8565

## Llama-3.2-3B-Instruct: discovery

* A1: 46815 neurons separate moral from norm pairs over 28 layers (peak at layer 27); moral vs norm exceeds every norm-vs-norm split in 23 layers [0, 2, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]; halves select 26200 / 10977
* B: 28701 neurons separate moral from norm pairs over 28 layers (peak at layer 27); moral vs norm exceeds every norm-vs-norm split in 20 layers [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 27]; halves select 9856 / 8911

## Qwen2.5-14B: discovery

* A1: 129474 neurons separate moral from norm pairs over 48 layers (peak at layer 44); moral vs norm exceeds every norm-vs-norm split in 27 layers [5, 8, 9, 16, 17, 18, 19, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]; halves select 61389 / 73697
* B: 73752 neurons separate moral from norm pairs over 48 layers (peak at layer 45); moral vs norm exceeds every norm-vs-norm split in 38 layers [5, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]; halves select 29452 / 32645

## Qwen2.5-14B-Instruct: discovery

* A1: 147276 neurons separate moral from norm pairs over 48 layers (peak at layer 44); moral vs norm exceeds every norm-vs-norm split in 33 layers [8, 9, 10, 12, 17, 18, 19, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]; halves select 84587 / 87196
* B: 81174 neurons separate moral from norm pairs over 48 layers (peak at layer 46); moral vs norm exceeds every norm-vs-norm split in 37 layers [5, 6, 9, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]; halves select 35638 / 38927

## Qwen2.5-3B: discovery

* A1: 42397 neurons separate moral from norm pairs over 36 layers (peak at layer 2); moral vs norm exceeds every norm-vs-norm split in 19 layers [1, 2, 4, 7, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]; halves select 9634 / 6642
* B: 20771 neurons separate moral from norm pairs over 36 layers (peak at layer 33); moral vs norm exceeds every norm-vs-norm split in 14 layers [0, 8, 10, 11, 12, 14, 15, 18, 19, 20, 21, 22, 23, 24]; halves select 4919 / 4991

## Qwen2.5-3B-Instruct: discovery

* A1: 38418 neurons separate moral from norm pairs over 36 layers (peak at layer 34); moral vs norm exceeds every norm-vs-norm split in 7 layers [1, 4, 7, 13, 23, 24, 25]; halves select 15357 / 9912
* B: 31537 neurons separate moral from norm pairs over 36 layers (peak at layer 33); moral vs norm exceeds every norm-vs-norm split in 10 layers [12, 14, 15, 18, 19, 20, 22, 23, 28, 30]; halves select 9276 / 10842

## Qwen2.5-7B: discovery

* A1: 62679 neurons separate moral from norm pairs over 28 layers (peak at layer 26); moral vs norm exceeds every norm-vs-norm split in 19 layers [1, 6, 7, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]; halves select 27384 / 18711
* B: 40118 neurons separate moral from norm pairs over 28 layers (peak at layer 27); moral vs norm exceeds every norm-vs-norm split in 17 layers [2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 24, 25]; halves select 10950 / 15235

## Qwen2.5-7B-Instruct: discovery

* A1: 82827 neurons separate moral from norm pairs over 28 layers (peak at layer 26); moral vs norm exceeds every norm-vs-norm split in 22 layers [1, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]; halves select 45314 / 33647
* B: 41218 neurons separate moral from norm pairs over 28 layers (peak at layer 27); moral vs norm exceeds every norm-vs-norm split in 20 layers [3, 5, 6, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]; halves select 15072 / 13340

## gemma-2b: discovery

* A1: 30174 neurons separate moral from norm pairs over 18 layers (peak at layer 17); moral vs norm exceeds every norm-vs-norm split in 10 layers [1, 2, 3, 6, 7, 8, 9, 10, 11, 12]; halves select 10045 / 4155
* B: 23487 neurons separate moral from norm pairs over 18 layers (peak at layer 17); moral vs norm exceeds every norm-vs-norm split in 11 layers [0, 1, 2, 6, 9, 10, 11, 12, 13, 14, 15]; halves select 7057 / 5792

## gemma-2b-it: discovery

* A1: 41866 neurons separate moral from norm pairs over 18 layers (peak at layer 17); moral vs norm exceeds every norm-vs-norm split in 14 layers [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]; halves select 12198 / 8741
* B: 20785 neurons separate moral from norm pairs over 18 layers (peak at layer 17); moral vs norm exceeds every norm-vs-norm split in 14 layers [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]; halves select 3005 / 4223

## Llama-3.1-8B: held-out ablation

* A1, all lists: cross-fitted moral: -0.062 [-0.100, -0.022] (n=78); norm: +0.003 [-0.028, +0.036] (n=104); descr: +0.047 [+0.016, +0.082] (n=38); moral - norm -0.065 [-0.116, -0.014] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -3.7% [-12.8, +8.3]; norm: +3.8% [-4.2, +12.2]; descr: +26.9% [+6.9, +50.3]; moral - norm -7.5% [-19.9, +6.6] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.056 [+0.043, +0.069] (n=78); norm: +0.026 [+0.019, +0.034] (n=104); descr: +0.002 [-0.002, +0.006] (n=38); moral - norm +0.030 [+0.015, +0.045] -> not moral-specific
    relative to the pair's gap: moral: +7.7% [+5.0, +10.4]; norm: +7.2% [+5.2, +9.4]; descr: +1.5% [-1.9, +5.7]; moral - norm +0.5% [-2.9, +4.0] -> not moral-specific
* B, all lists: cross-fitted moral: -0.069 [-0.092, -0.047] (n=77); norm: -0.047 [-0.062, -0.033] (n=104); descr: -0.090 [-0.110, -0.071] (n=40); moral - norm -0.022 [-0.049, +0.005] -> not moral-specific
    relative to the pair's gap: moral: -12.6% [-19.2, -6.4]; norm: -4.3% [-9.3, +2.3]; descr: -17.1% [-21.9, -12.1]; moral - norm -8.3% [-17.7, +0.2] -> not moral-specific
* B, top lists: cross-fitted moral: -0.001 [-0.003, +0.001] (n=77); norm: +0.000 [-0.001, +0.001] (n=104); descr: -0.001 [-0.003, +0.002] (n=40); moral - norm -0.001 [-0.003, +0.002] -> not moral-specific
    relative to the pair's gap: moral: -0.1% [-0.7, +0.5]; norm: +0.1% [-0.6, +0.9]; descr: -0.1% [-0.6, +0.3]; moral - norm -0.2% [-1.2, +0.7] -> not moral-specific

## Llama-3.1-8B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.146 [-0.169, -0.122] (n=78); norm: -0.057 [-0.074, -0.041] (n=107); descr: -0.116 [-0.141, -0.093] (n=37); moral - norm -0.089 [-0.117, -0.059] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -10.4% [-16.7, -1.9]; norm: -8.5% [-12.9, -3.7]; descr: -48.8% [-57.0, -41.2]; moral - norm -1.9% [-9.9, +7.4] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.041 [+0.032, +0.052] (n=78); norm: +0.022 [+0.014, +0.030] (n=107); descr: +0.011 [+0.003, +0.020] (n=37); moral - norm +0.019 [+0.006, +0.032] -> not moral-specific
    relative to the pair's gap: moral: +4.4% [+3.1, +5.7]; norm: +3.7% [+1.3, +6.1]; descr: +6.3% [+0.7, +12.6]; moral - norm +0.7% [-2.1, +3.4] -> not moral-specific
* B, all lists: cross-fitted moral: -0.119 [-0.164, -0.073] (n=78); norm: -0.114 [-0.143, -0.087] (n=103); descr: -0.105 [-0.139, -0.072] (n=40); moral - norm -0.005 [-0.058, +0.050] -> not moral-specific
    relative to the pair's gap: moral: +0.4% [-14.8, +20.1]; norm: -12.4% [-16.1, -8.7]; descr: -14.9% [-20.9, -8.7]; moral - norm +12.7% [-3.2, +32.3] -> not moral-specific
* B, top lists: cross-fitted moral: +0.004 [-0.002, +0.011] (n=78); norm: -0.007 [-0.010, -0.003] (n=103); descr: -0.007 [-0.011, -0.003] (n=40); moral - norm +0.010 [+0.003, +0.018] -> not moral-specific
    relative to the pair's gap: moral: +1.0% [-0.1, +2.2]; norm: -0.6% [-1.2, +0.1]; descr: -0.8% [-1.4, -0.2]; moral - norm +1.5% [+0.3, +3.0] -> not moral-specific

## Llama-3.2-1B: held-out ablation

* A1, all lists: cross-fitted moral: +0.012 [+0.008, +0.016] (n=78); norm: +0.010 [+0.007, +0.013] (n=97); descr: +0.013 [+0.010, +0.017] (n=39); moral - norm +0.002 [-0.003, +0.006] -> not moral-specific
    relative to the pair's gap: moral: +3.0% [+1.5, +4.5]; norm: +2.3% [+0.8, +3.6]; descr: +5.6% [+3.5, +8.3]; moral - norm +0.6% [-1.4, +2.8] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.014 [+0.009, +0.020] (n=78); norm: +0.012 [+0.008, +0.016] (n=97); descr: +0.020 [+0.015, +0.024] (n=39); moral - norm +0.002 [-0.005, +0.009] -> not moral-specific
    relative to the pair's gap: moral: +2.4% [+1.3, +3.5]; norm: +2.6% [+1.1, +4.0]; descr: +6.8% [+4.9, +9.4]; moral - norm -0.2% [-1.9, +1.7] -> not moral-specific
* B, all lists: cross-fitted moral: -0.045 [-0.055, -0.035] (n=73); norm: -0.015 [-0.021, -0.009] (n=91); descr: -0.003 [-0.010, +0.003] (n=35); moral - norm -0.030 [-0.041, -0.019] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -8.7% [-13.9, -2.4]; norm: -5.1% [-8.4, -1.8]; descr: -1.3% [-4.6, +1.7]; moral - norm -3.6% [-9.8, +3.8] -> not moral-specific
* B, top lists: cross-fitted moral: +0.016 [+0.006, +0.027] (n=73); norm: +0.007 [+0.000, +0.014] (n=91); descr: +0.012 [+0.006, +0.017] (n=35); moral - norm +0.009 [-0.003, +0.022] -> not moral-specific
    relative to the pair's gap: moral: +2.5% [-1.1, +6.0]; norm: +0.6% [-1.5, +2.6]; descr: +2.5% [-0.5, +4.8]; moral - norm +1.9% [-2.1, +5.9] -> not moral-specific

## Llama-3.2-1B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.087 [-0.119, -0.057] (n=69); norm: -0.055 [-0.072, -0.039] (n=92); descr: -0.036 [-0.052, -0.020] (n=38); moral - norm -0.032 [-0.068, +0.003] -> not moral-specific
    relative to the pair's gap: moral: -9.7% [-17.6, -1.1]; norm: -18.0% [-23.9, -12.2]; descr: -13.7% [-21.1, -6.9]; moral - norm +8.3% [-1.3, +18.8] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.007 [-0.001, +0.016] (n=69); norm: +0.009 [+0.004, +0.014] (n=92); descr: +0.019 [+0.012, +0.026] (n=38); moral - norm -0.002 [-0.011, +0.008] -> not moral-specific
    relative to the pair's gap: moral: -0.1% [-2.5, +2.1]; norm: +2.1% [-0.1, +4.3]; descr: +4.7% [+1.3, +7.5]; moral - norm -2.2% [-5.3, +1.1] -> not moral-specific
* B, all lists: cross-fitted moral: -0.056 [-0.080, -0.031] (n=72); norm: -0.015 [-0.030, +0.000] (n=95); descr: +0.038 [+0.008, +0.071] (n=37); moral - norm -0.041 [-0.068, -0.013] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -6.0% [-14.9, +4.1]; norm: -0.8% [-6.1, +4.2]; descr: +5.1% [-6.6, +15.0]; moral - norm -5.2% [-15.6, +6.3] -> not moral-specific
* B, top lists: cross-fitted moral: +0.031 [+0.014, +0.049] (n=72); norm: +0.001 [-0.008, +0.009] (n=95); descr: +0.021 [+0.004, +0.040] (n=37); moral - norm +0.030 [+0.011, +0.051] -> not moral-specific
    relative to the pair's gap: moral: +4.2% [+0.7, +8.2]; norm: -2.7% [-6.2, +0.4]; descr: +1.0% [-7.7, +7.6]; moral - norm +6.9% [+2.0, +12.1] -> not moral-specific

## Llama-3.2-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.014 [-0.034, +0.006] (n=79); norm: -0.022 [-0.037, -0.008] (n=104); descr: -0.076 [-0.095, -0.056] (n=40); moral - norm +0.008 [-0.016, +0.031] -> not moral-specific
    relative to the pair's gap: moral: +0.8% [-4.3, +6.7]; norm: +0.3% [-5.8, +7.8]; descr: -19.6% [-23.7, -15.0]; moral - norm +0.5% [-8.6, +9.3] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.057 [+0.042, +0.073] (n=79); norm: +0.035 [+0.025, +0.046] (n=104); descr: -0.018 [-0.024, -0.011] (n=40); moral - norm +0.021 [+0.003, +0.040] -> not moral-specific
    relative to the pair's gap: moral: +8.5% [+6.0, +11.0]; norm: +7.4% [+3.3, +12.1]; descr: -5.4% [-7.5, -3.3]; moral - norm +1.1% [-4.3, +6.0] -> not moral-specific
* B, all lists: cross-fitted moral: -0.023 [-0.048, +0.002] (n=78); norm: +0.008 [-0.017, +0.034] (n=100); descr: +0.001 [-0.012, +0.014] (n=40); moral - norm -0.031 [-0.068, +0.005] -> not moral-specific
    relative to the pair's gap: moral: -14.4% [-30.0, -2.6]; norm: +4.1% [-2.4, +11.0]; descr: -2.5% [-6.7, +1.3]; moral - norm -18.6% [-34.8, -4.6] -> MORAL-SPECIFIC
* B, top lists: cross-fitted moral: +0.033 [+0.024, +0.043] (n=78); norm: -0.005 [-0.009, -0.001] (n=100); descr: -0.027 [-0.033, -0.021] (n=40); moral - norm +0.038 [+0.029, +0.049] -> not moral-specific
    relative to the pair's gap: moral: +5.8% [+2.0, +9.6]; norm: -1.4% [-2.9, +0.1]; descr: -5.9% [-7.3, -4.6]; moral - norm +7.2% [+3.0, +11.3] -> not moral-specific

## Llama-3.2-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.304 [-0.363, -0.245] (n=72); norm: -0.257 [-0.298, -0.215] (n=103); descr: -0.211 [-0.238, -0.183] (n=39); moral - norm -0.048 [-0.119, +0.023] -> not moral-specific
    relative to the pair's gap: moral: -23.6% [-29.5, -17.2]; norm: -27.7% [-33.7, -20.5]; descr: -33.7% [-37.2, -30.2]; moral - norm +4.1% [-5.2, +12.9] -> not moral-specific
* A1, top lists: cross-fitted moral: -0.009 [-0.014, -0.004] (n=72); norm: -0.000 [-0.005, +0.006] (n=103); descr: -0.005 [-0.011, +0.002] (n=39); moral - norm -0.009 [-0.016, -0.002] -> not moral-specific
    relative to the pair's gap: moral: -0.7% [-1.5, +0.1]; norm: +0.3% [-0.6, +1.3]; descr: -1.2% [-2.0, -0.3]; moral - norm -1.0% [-2.2, +0.2] -> not moral-specific
* B, all lists: cross-fitted moral: +0.066 [+0.026, +0.105] (n=69); norm: +0.001 [-0.031, +0.033] (n=103); descr: -0.051 [-0.081, -0.020] (n=39); moral - norm +0.065 [+0.015, +0.116] -> not moral-specific
    relative to the pair's gap: moral: +11.7% [+5.2, +19.1]; norm: -0.4% [-7.2, +6.4]; descr: -7.4% [-13.8, -0.2]; moral - norm +12.1% [+2.8, +22.0] -> not moral-specific
* B, top lists: cross-fitted moral: +0.003 [-0.024, +0.031] (n=69); norm: -0.003 [-0.017, +0.010] (n=103); descr: -0.023 [-0.037, -0.009] (n=39); moral - norm +0.006 [-0.024, +0.037] -> not moral-specific
    relative to the pair's gap: moral: -3.3% [-8.5, +2.1]; norm: -0.3% [-3.4, +2.8]; descr: -3.4% [-6.1, -0.6]; moral - norm -3.1% [-9.0, +3.1] -> not moral-specific

## Qwen2.5-14B: held-out ablation

* A1, all lists: cross-fitted moral: -0.324 [-0.360, -0.285] (n=79); norm: -0.104 [-0.134, -0.075] (n=99); descr: +0.074 [+0.049, +0.099] (n=36); moral - norm -0.220 [-0.268, -0.172] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -22.9% [-25.8, -19.9]; norm: -8.7% [-13.6, -3.2]; descr: +93.2% [+63.5, +122.5]; moral - norm -14.1% [-20.2, -8.2] -> MORAL-SPECIFIC
* A1, top lists: cross-fitted moral: -0.017 [-0.023, -0.010] (n=79); norm: -0.018 [-0.024, -0.011] (n=99); descr: -0.003 [-0.009, +0.001] (n=36); moral - norm +0.001 [-0.008, +0.011] -> not moral-specific
    relative to the pair's gap: moral: -0.9% [-1.5, -0.2]; norm: -2.0% [-3.6, -0.5]; descr: +1.6% [-1.7, +5.1]; moral - norm +1.2% [-0.4, +2.9] -> not moral-specific
* B, all lists: cross-fitted moral: -0.172 [-0.201, -0.142] (n=79); norm: -0.123 [-0.146, -0.100] (n=106); descr: -0.203 [-0.240, -0.166] (n=40); moral - norm -0.049 [-0.086, -0.011] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -11.3% [-15.4, -6.2]; norm: -9.5% [-15.1, -2.2]; descr: -21.9% [-28.6, -16.4]; moral - norm -1.8% [-10.1, +5.6] -> not moral-specific
* B, top lists: cross-fitted moral: +0.043 [+0.036, +0.049] (n=79); norm: +0.041 [+0.034, +0.049] (n=106); descr: +0.042 [+0.031, +0.052] (n=40); moral - norm +0.002 [-0.009, +0.012] -> not moral-specific
    relative to the pair's gap: moral: +3.9% [+3.0, +4.9]; norm: +4.5% [+2.2, +7.9]; descr: +4.6% [+3.3, +6.0]; moral - norm -0.7% [-4.3, +1.9] -> not moral-specific

## Qwen2.5-14B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.133 [-0.172, -0.095] (n=79); norm: -0.011 [-0.047, +0.023] (n=99); descr: +0.151 [+0.068, +0.240] (n=18); moral - norm -0.122 [-0.172, -0.073] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -6.2% [-10.4, -0.8]; norm: +5.1% [-1.1, +11.6]; descr: +203.4% [+97.2, +338.0]; moral - norm -11.2% [-18.9, -2.8] -> MORAL-SPECIFIC
* A1, top lists: cross-fitted moral: +0.016 [+0.008, +0.024] (n=79); norm: +0.006 [-0.001, +0.014] (n=99); descr: +0.030 [+0.013, +0.054] (n=18); moral - norm +0.010 [-0.001, +0.021] -> not moral-specific
    relative to the pair's gap: moral: +0.7% [-0.3, +1.8]; norm: -0.5% [-2.1, +1.0]; descr: +12.8% [+7.2, +19.1]; moral - norm +1.3% [-0.6, +3.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.120 [-0.162, -0.078] (n=78); norm: -0.178 [-0.215, -0.142] (n=104); descr: -0.269 [-0.306, -0.234] (n=40); moral - norm +0.058 [+0.001, +0.114] -> not moral-specific
    relative to the pair's gap: moral: -7.4% [-11.7, -2.6]; norm: -18.4% [-24.9, -12.3]; descr: -33.0% [-48.4, -22.7]; moral - norm +11.1% [+3.2, +18.9] -> not moral-specific
* B, top lists: cross-fitted moral: +0.021 [-0.000, +0.043] (n=78); norm: -0.013 [-0.035, +0.007] (n=104); descr: -0.019 [-0.042, +0.001] (n=40); moral - norm +0.035 [+0.005, +0.064] -> not moral-specific
    relative to the pair's gap: moral: +1.1% [-1.1, +3.0]; norm: -1.3% [-4.5, +1.6]; descr: -2.4% [-5.3, -0.1]; moral - norm +2.4% [-1.3, +6.1] -> not moral-specific

## Qwen2.5-3B: held-out ablation

* A1, all lists: cross-fitted moral: -0.058 [-0.074, -0.043] (n=78); norm: -0.032 [-0.042, -0.021] (n=98); descr: +0.002 [-0.007, +0.012] (n=39); moral - norm -0.027 [-0.045, -0.008] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -15.3% [-21.8, -8.9]; norm: -16.5% [-23.1, -10.4]; descr: -0.3% [-4.5, +4.1]; moral - norm +1.2% [-7.6, +10.8] -> not moral-specific
* A1, top lists: cross-fitted moral: -0.010 [-0.013, -0.007] (n=78); norm: -0.008 [-0.010, -0.005] (n=98); descr: +0.010 [+0.008, +0.012] (n=39); moral - norm -0.002 [-0.006, +0.001] -> not moral-specific
    relative to the pair's gap: moral: -3.6% [-5.0, -2.4]; norm: -4.3% [-6.1, -2.7]; descr: +3.4% [+2.5, +4.4]; moral - norm +0.8% [-1.3, +2.8] -> not moral-specific
* B, all lists: cross-fitted moral: -0.002 [-0.030, +0.026] (n=75); norm: +0.024 [+0.002, +0.048] (n=101); descr: +0.179 [+0.129, +0.233] (n=40); moral - norm -0.026 [-0.061, +0.010] -> not moral-specific
    relative to the pair's gap: moral: +1.1% [-7.6, +10.4]; norm: +1.2% [-4.8, +7.3]; descr: +40.9% [+32.4, +49.8]; moral - norm -0.1% [-10.9, +10.6] -> not moral-specific
* B, top lists: cross-fitted moral: -0.009 [-0.019, +0.001] (n=75); norm: +0.019 [+0.013, +0.025] (n=101); descr: +0.061 [+0.039, +0.086] (n=40); moral - norm -0.027 [-0.039, -0.016] -> not moral-specific
    relative to the pair's gap: moral: -6.5% [-16.5, -0.2]; norm: +4.0% [+2.2, +5.9]; descr: +13.7% [+7.9, +19.7]; moral - norm -10.5% [-21.0, -3.7] -> MORAL-SPECIFIC

## Qwen2.5-3B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.153 [-0.177, -0.128] (n=76); norm: -0.135 [-0.154, -0.117] (n=103); descr: -0.045 [-0.064, -0.024] (n=40); moral - norm -0.017 [-0.047, +0.012] -> not moral-specific
    relative to the pair's gap: moral: -13.8% [-17.5, -9.6]; norm: -16.7% [-22.0, -12.7]; descr: -4.9% [-8.8, -0.6]; moral - norm +3.0% [-2.9, +9.6] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.015 [+0.002, +0.029] (n=76); norm: +0.018 [+0.008, +0.029] (n=103); descr: -0.023 [-0.029, -0.018] (n=40); moral - norm -0.003 [-0.020, +0.014] -> not moral-specific
    relative to the pair's gap: moral: +1.2% [-1.1, +3.5]; norm: +1.7% [+0.4, +3.1]; descr: -4.3% [-5.8, -3.0]; moral - norm -0.5% [-3.3, +2.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.113 [-0.153, -0.074] (n=76); norm: -0.034 [-0.056, -0.013] (n=104); descr: +0.075 [+0.043, +0.107] (n=40); moral - norm -0.079 [-0.125, -0.033] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -12.2% [-22.5, -3.4]; norm: -6.2% [-10.7, -1.9]; descr: +8.2% [+3.2, +13.5]; moral - norm -6.0% [-17.3, +4.0] -> not moral-specific
* B, top lists: cross-fitted moral: -0.018 [-0.025, -0.010] (n=76); norm: -0.003 [-0.008, +0.002] (n=104); descr: -0.001 [-0.011, +0.011] (n=40); moral - norm -0.015 [-0.023, -0.006] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -3.0% [-5.8, -0.5]; norm: -0.7% [-1.7, +0.4]; descr: -0.7% [-2.6, +1.3]; moral - norm -2.3% [-5.3, +0.5] -> not moral-specific

## Qwen2.5-7B: held-out ablation

* A1, all lists: cross-fitted moral: -0.093 [-0.120, -0.064] (n=79); norm: +0.084 [+0.057, +0.113] (n=104); descr: +0.115 [+0.090, +0.139] (n=40); moral - norm -0.177 [-0.217, -0.138] -> MORAL-SPECIFIC
    relative to the pair's gap: moral: -6.9% [-11.9, -1.1]; norm: +12.6% [+7.8, +17.7]; descr: +30.3% [+22.8, +38.1]; moral - norm -19.5% [-26.7, -12.1] -> MORAL-SPECIFIC
* A1, top lists: cross-fitted moral: +0.051 [+0.027, +0.076] (n=79); norm: +0.054 [+0.033, +0.076] (n=104); descr: +0.040 [+0.033, +0.047] (n=40); moral - norm -0.003 [-0.035, +0.030] -> not moral-specific
    relative to the pair's gap: moral: +2.3% [-1.3, +5.8]; norm: +6.7% [+3.5, +10.0]; descr: +9.6% [+7.9, +11.4]; moral - norm -4.3% [-9.2, +0.5] -> not moral-specific
* B, all lists: cross-fitted moral: -0.154 [-0.186, -0.121] (n=77); norm: -0.130 [-0.148, -0.113] (n=107); descr: -0.094 [-0.112, -0.075] (n=40); moral - norm -0.023 [-0.061, +0.014] -> not moral-specific
    relative to the pair's gap: moral: -7.3% [-18.5, +8.3]; norm: -12.6% [-16.6, -8.3]; descr: -10.1% [-12.9, -7.6]; moral - norm +5.3% [-6.7, +22.3] -> not moral-specific
* B, top lists: cross-fitted moral: -0.010 [-0.024, +0.003] (n=77); norm: -0.002 [-0.011, +0.006] (n=107); descr: -0.006 [-0.020, +0.007] (n=40); moral - norm -0.007 [-0.024, +0.009] -> not moral-specific
    relative to the pair's gap: moral: -2.0% [-4.5, +0.2]; norm: -0.4% [-2.8, +2.0]; descr: -1.0% [-2.6, +0.4]; moral - norm -1.6% [-5.0, +1.6] -> not moral-specific

## Qwen2.5-7B-Instruct: held-out ablation

* A1, all lists: cross-fitted moral: -0.473 [-0.550, -0.393] (n=75); norm: -0.400 [-0.461, -0.340] (n=106); descr: -0.364 [-0.429, -0.302] (n=40); moral - norm -0.073 [-0.172, +0.027] -> not moral-specific
    relative to the pair's gap: moral: -38.6% [-48.3, -27.9]; norm: -47.6% [-57.5, -38.3]; descr: -62.5% [-75.5, -51.6]; moral - norm +9.0% [-4.3, +23.9] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.032 [+0.012, +0.051] (n=75); norm: -0.003 [-0.014, +0.008] (n=106); descr: +0.018 [+0.008, +0.029] (n=40); moral - norm +0.035 [+0.012, +0.057] -> not moral-specific
    relative to the pair's gap: moral: +6.5% [+1.2, +14.5]; norm: -0.8% [-3.5, +1.6]; descr: +1.8% [-0.7, +3.9]; moral - norm +7.2% [+1.5, +15.2] -> not moral-specific
* B, all lists: cross-fitted moral: -0.091 [-0.141, -0.042] (n=77); norm: -0.116 [-0.158, -0.073] (n=104); descr: -0.111 [-0.175, -0.051] (n=40); moral - norm +0.025 [-0.038, +0.092] -> not moral-specific
    relative to the pair's gap: moral: +5.9% [-6.7, +21.7]; norm: +10.5% [-11.1, +46.0]; descr: -11.4% [-18.2, -4.8]; moral - norm -4.5% [-43.9, +24.2] -> not moral-specific
* B, top lists: cross-fitted moral: -0.048 [-0.081, -0.017] (n=77); norm: -0.029 [-0.055, -0.004] (n=104); descr: +0.010 [-0.020, +0.039] (n=40); moral - norm -0.019 [-0.058, +0.020] -> not moral-specific
    relative to the pair's gap: moral: -13.5% [-27.5, -3.1]; norm: +6.5% [-3.9, +24.5]; descr: -0.3% [-4.5, +3.6]; moral - norm -20.0% [-41.3, -3.5] -> MORAL-SPECIFIC

## gemma-2b: held-out ablation

* A1, all lists: cross-fitted moral: -0.133 [-0.168, -0.101] (n=74); norm: -0.101 [-0.122, -0.081] (n=99); descr: -0.082 [-0.103, -0.061] (n=39); moral - norm -0.032 [-0.071, +0.008] -> not moral-specific
    relative to the pair's gap: moral: -16.5% [-24.1, -6.7]; norm: -21.7% [-25.9, -17.8]; descr: -17.1% [-21.1, -12.6]; moral - norm +5.3% [-3.9, +15.5] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.021 [+0.008, +0.034] (n=74); norm: -0.002 [-0.010, +0.006] (n=99); descr: -0.027 [-0.040, -0.015] (n=39); moral - norm +0.023 [+0.008, +0.039] -> not moral-specific
    relative to the pair's gap: moral: +8.2% [+3.3, +15.2]; norm: +0.7% [-1.3, +2.8]; descr: -3.7% [-6.8, -0.5]; moral - norm +7.5% [+2.0, +14.5] -> not moral-specific
* B, all lists: cross-fitted moral: +0.009 [-0.013, +0.030] (n=72); norm: +0.015 [+0.001, +0.029] (n=95); descr: -0.008 [-0.022, +0.005] (n=40); moral - norm -0.007 [-0.031, +0.019] -> not moral-specific
    relative to the pair's gap: moral: +18.4% [-0.3, +50.7]; norm: +4.2% [-4.0, +11.5]; descr: -8.5% [-29.3, +4.7]; moral - norm +14.3% [-8.1, +49.1] -> not moral-specific
* B, top lists: cross-fitted moral: +0.011 [+0.002, +0.021] (n=72); norm: +0.002 [-0.003, +0.008] (n=95); descr: -0.005 [-0.011, -0.000] (n=40); moral - norm +0.009 [-0.002, +0.020] -> not moral-specific
    relative to the pair's gap: moral: +4.3% [+1.1, +8.5]; norm: -0.1% [-3.1, +2.6]; descr: +0.4% [-2.6, +4.5]; moral - norm +4.4% [-0.1, +9.4] -> not moral-specific

## gemma-2b-it: held-out ablation

* A1, all lists: cross-fitted moral: +0.057 [+0.031, +0.084] (n=73); norm: +0.034 [+0.008, +0.060] (n=98); descr: +0.098 [+0.071, +0.127] (n=37); moral - norm +0.023 [-0.014, +0.059] -> not moral-specific
    relative to the pair's gap: moral: +7.9% [+1.5, +14.4]; norm: +2.8% [-4.0, +9.2]; descr: +22.9% [+15.6, +31.2]; moral - norm +5.1% [-4.1, +15.0] -> not moral-specific
* A1, top lists: cross-fitted moral: +0.044 [+0.029, +0.059] (n=73); norm: +0.036 [+0.022, +0.051] (n=98); descr: +0.027 [+0.001, +0.051] (n=37); moral - norm +0.008 [-0.013, +0.029] -> not moral-specific
    relative to the pair's gap: moral: +0.7% [-2.4, +3.8]; norm: +4.3% [+0.4, +8.3]; descr: +4.4% [-6.3, +13.1]; moral - norm -3.6% [-8.6, +1.3] -> not moral-specific
* B, all lists: cross-fitted moral: +0.020 [-0.033, +0.077] (n=67); norm: +0.039 [+0.008, +0.073] (n=88); descr: +0.053 [-0.008, +0.122] (n=34); moral - norm -0.019 [-0.081, +0.044] -> not moral-specific
    relative to the pair's gap: moral: +5.9% [-7.2, +20.7]; norm: +5.3% [-6.1, +17.6]; descr: +9.5% [-9.1, +32.3]; moral - norm +0.6% [-17.1, +18.9] -> not moral-specific
* B, top lists: cross-fitted moral: +0.149 [+0.108, +0.191] (n=67); norm: +0.039 [+0.010, +0.071] (n=88); descr: +0.080 [+0.026, +0.143] (n=34); moral - norm +0.110 [+0.057, +0.161] -> not moral-specific
    relative to the pair's gap: moral: +22.0% [+14.4, +29.8]; norm: +7.5% [-1.5, +18.3]; descr: +19.9% [+0.0, +47.9]; moral - norm +14.5% [+1.5, +26.5] -> not moral-specific

## Count of models with a moral-specific held-out effect

* frame A1, all lists: 6 of 14 models (absolute); relative to the pair's gap: 3 of 14
* frame A1, top lists: 0 of 14 models (absolute); relative to the pair's gap: 0 of 14
* frame B, all lists: 4 of 14 models (absolute); relative to the pair's gap: 1 of 14
* frame B, top lists: 1 of 14 models (absolute); relative to the pair's gap: 2 of 14
