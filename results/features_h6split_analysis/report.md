# Split-half moral-versus-norm features: held-out ablation (exploratory follow-up)

Items: the item file is the set of accepted pairs. Halves: A {'moral': 40, 'norm': 53}, B {'moral': 40, 'norm': 54}; descriptive pairs evaluation-only. Inclusion gap >= 0.02.
Reading: moral-specific = cross-fitted set-minus-random on moral pairs below zero (interval) and moral-minus-norm difference below zero (interval).

## llama-3.1-8B-base

* A1_selA (11 features): moral: +0.024 [+0.017, +0.032] (n=40); norm: +0.021 [+0.014, +0.028] (n=54); descr: +0.034 [+0.026, +0.042] (n=38); moral - norm +0.003 [-0.007, +0.014]
* A1_selB (8 features): moral: +0.000 [-0.008, +0.008] (n=38); norm: +0.039 [+0.030, +0.048] (n=50); descr: +0.047 [+0.036, +0.058] (n=38); moral - norm -0.039 [-0.051, -0.027]
* **A1 cross-fitted**: moral: +0.013 [+0.006, +0.019] (n=78); norm: +0.030 [+0.024, +0.036] (n=104); descr: +0.040 [+0.031, +0.050] (n=38); moral - norm -0.017 [-0.026, -0.009] -> not moral-specific
* B_selA (9 features): moral: -0.036 [-0.054, -0.017] (n=39); norm: -0.020 [-0.027, -0.012] (n=53); descr: -0.011 [-0.015, -0.007] (n=40); moral - norm -0.016 [-0.036, +0.004]
* B_selB (16 features): moral: -0.002 [-0.034, +0.025] (n=38); norm: -0.003 [-0.020, +0.013] (n=51); descr: +0.023 [+0.016, +0.031] (n=40); moral - norm +0.000 [-0.035, +0.033]
* **B cross-fitted**: moral: -0.019 [-0.037, -0.002] (n=77); norm: -0.011 [-0.020, -0.002] (n=104); descr: +0.006 [+0.002, +0.011] (n=40); moral - norm -0.008 [-0.029, +0.011] -> not moral-specific

## llama-3.2-1B-IT

* A1_selA (21 features): moral: -0.024 [-0.038, -0.012] (n=33); norm: -0.021 [-0.028, -0.014] (n=51); descr: -0.005 [-0.012, +0.001] (n=38); moral - norm -0.004 [-0.018, +0.011]
* A1_selB (14 features): moral: +0.004 [-0.002, +0.010] (n=36); norm: -0.005 [-0.010, -0.000] (n=41); descr: -0.009 [-0.016, -0.003] (n=38); moral - norm +0.009 [+0.002, +0.017]
* **A1 cross-fitted**: moral: -0.010 [-0.018, -0.002] (n=69); norm: -0.014 [-0.019, -0.009] (n=92); descr: -0.007 [-0.013, -0.002] (n=38); moral - norm +0.004 [-0.005, +0.013] -> not moral-specific
* B_selA (19 features): moral: -0.069 [-0.097, -0.043] (n=35); norm: +0.002 [-0.005, +0.009] (n=47); descr: +0.005 [+0.000, +0.010] (n=37); moral - norm -0.072 [-0.100, -0.044]
* B_selB (23 features): moral: -0.040 [-0.063, -0.018] (n=37); norm: -0.003 [-0.009, +0.002] (n=48); descr: -0.001 [-0.007, +0.004] (n=37); moral - norm -0.037 [-0.061, -0.014]
* **B cross-fitted**: moral: -0.054 [-0.073, -0.036] (n=72); norm: -0.000 [-0.005, +0.004] (n=95); descr: +0.002 [-0.002, +0.006] (n=37); moral - norm -0.054 [-0.072, -0.036] -> MORAL-SPECIFIC

## llama-3.2-1B-IT-k128

* A1_selA (31 features): moral: +0.007 [-0.008, +0.023] (n=33); norm: +0.011 [+0.004, +0.018] (n=51); descr: +0.021 [+0.010, +0.033] (n=38); moral - norm -0.004 [-0.020, +0.013]
* A1_selB (39 features): moral: -0.038 [-0.051, -0.026] (n=36); norm: -0.021 [-0.033, -0.011] (n=41); descr: -0.026 [-0.035, -0.018] (n=38); moral - norm -0.017 [-0.033, -0.000]
* **A1 cross-fitted**: moral: -0.017 [-0.028, -0.005] (n=69); norm: -0.003 [-0.011, +0.003] (n=92); descr: -0.002 [-0.010, +0.005] (n=38); moral - norm -0.013 [-0.026, -0.000] -> MORAL-SPECIFIC
* B_selA (15 features): moral: -0.056 [-0.078, -0.035] (n=35); norm: -0.010 [-0.015, -0.005] (n=47); descr: +0.004 [-0.001, +0.008] (n=37); moral - norm -0.046 [-0.068, -0.024]
* B_selB (29 features): moral: -0.068 [-0.099, -0.040] (n=37); norm: -0.015 [-0.030, -0.002] (n=48); descr: +0.004 [+0.001, +0.008] (n=37); moral - norm -0.054 [-0.087, -0.022]
* **B cross-fitted**: moral: -0.062 [-0.081, -0.044] (n=72); norm: -0.012 [-0.020, -0.005] (n=95); descr: +0.004 [+0.001, +0.007] (n=37); moral - norm -0.050 [-0.070, -0.030] -> MORAL-SPECIFIC

## llama-3.2-1B-base

* A1_selA (12 features): moral: -0.016 [-0.025, -0.008] (n=38); norm: +0.015 [+0.009, +0.021] (n=52); descr: +0.016 [+0.010, +0.021] (n=39); moral - norm -0.031 [-0.042, -0.021]
* A1_selB (19 features): moral: -0.015 [-0.024, -0.006] (n=40); norm: +0.005 [-0.002, +0.011] (n=45); descr: -0.002 [-0.008, +0.004] (n=39); moral - norm -0.020 [-0.031, -0.008]
* **A1 cross-fitted**: moral: -0.015 [-0.021, -0.009] (n=78); norm: +0.010 [+0.006, +0.015] (n=97); descr: +0.007 [+0.002, +0.011] (n=39); moral - norm -0.026 [-0.034, -0.018] -> MORAL-SPECIFIC

## llama-3.2-1B-base-k128

* A1_selA (20 features): moral: +0.007 [-0.000, +0.013] (n=38); norm: +0.002 [-0.002, +0.006] (n=52); descr: +0.004 [-0.001, +0.009] (n=39); moral - norm +0.005 [-0.003, +0.013]
* A1_selB (42 features): moral: -0.014 [-0.023, -0.005] (n=40); norm: +0.002 [-0.006, +0.009] (n=45); descr: +0.005 [-0.001, +0.011] (n=39); moral - norm -0.015 [-0.027, -0.004]
* **A1 cross-fitted**: moral: -0.004 [-0.010, +0.002] (n=78); norm: +0.002 [-0.002, +0.006] (n=97); descr: +0.005 [-0.000, +0.009] (n=39); moral - norm -0.006 [-0.013, +0.002] -> not moral-specific
* B_selA (23 features): moral: -0.034 [-0.051, -0.019] (n=35); norm: -0.006 [-0.012, -0.001] (n=48); descr: -0.000 [-0.006, +0.004] (n=35); moral - norm -0.028 [-0.046, -0.011]
* B_selB (19 features): moral: +0.006 [-0.002, +0.015] (n=38); norm: +0.004 [-0.002, +0.010] (n=43); descr: -0.008 [-0.013, -0.004] (n=35); moral - norm +0.002 [-0.008, +0.013]
* **B cross-fitted**: moral: -0.013 [-0.024, -0.003] (n=73); norm: -0.001 [-0.005, +0.003] (n=91); descr: -0.004 [-0.008, -0.001] (n=35); moral - norm -0.012 [-0.023, -0.001] -> MORAL-SPECIFIC

## llama-3.2-3B-IT-L19

* A1_selA (63 features): moral: -0.181 [-0.221, -0.140] (n=36); norm: -0.173 [-0.207, -0.139] (n=53); descr: -0.152 [-0.181, -0.125] (n=39); moral - norm -0.008 [-0.060, +0.046]
* A1_selB (48 features): moral: -0.220 [-0.258, -0.181] (n=36); norm: -0.178 [-0.207, -0.148] (n=50); descr: -0.137 [-0.160, -0.115] (n=39); moral - norm -0.042 [-0.090, +0.007]
* **A1 cross-fitted**: moral: -0.201 [-0.228, -0.172] (n=72); norm: -0.176 [-0.198, -0.152] (n=103); descr: -0.145 [-0.168, -0.121] (n=39); moral - norm -0.025 [-0.061, +0.011] -> not moral-specific
* B_selA (65 features): moral: +0.226 [+0.160, +0.287] (n=35); norm: +0.122 [+0.090, +0.156] (n=52); descr: +0.075 [+0.051, +0.101] (n=39); moral - norm +0.104 [+0.031, +0.173]
* B_selB (97 features): moral: +0.058 [+0.008, +0.106] (n=34); norm: +0.014 [-0.003, +0.031] (n=51); descr: +0.007 [-0.012, +0.024] (n=39); moral - norm +0.044 [-0.009, +0.096]
* **B cross-fitted**: moral: +0.143 [+0.099, +0.188] (n=69); norm: +0.069 [+0.048, +0.091] (n=103); descr: +0.041 [+0.023, +0.060] (n=39); moral - norm +0.074 [+0.024, +0.124] -> not moral-specific

## llama-3.2-3B-IT-L3

* B_selA (1 features): moral: -0.000 [-0.001, -0.000] (n=35); norm: -0.000 [-0.000, +0.000] (n=52); descr: -0.000 [-0.000, +0.000] (n=39); moral - norm -0.000 [-0.001, -0.000]
* B_selB (13 features): moral: +0.002 [-0.002, +0.006] (n=34); norm: +0.001 [-0.001, +0.002] (n=51); descr: +0.000 [-0.001, +0.001] (n=39); moral - norm +0.002 [-0.003, +0.005]
* **B cross-fitted**: moral: +0.001 [-0.001, +0.003] (n=69); norm: +0.000 [-0.000, +0.001] (n=103); descr: +0.000 [-0.001, +0.001] (n=39); moral - norm +0.001 [-0.002, +0.002] -> not moral-specific

## llama-3.2-3B-IT-L7

* A1_selA (11 features): moral: +0.031 [+0.020, +0.042] (n=36); norm: +0.039 [+0.030, +0.048] (n=53); descr: +0.009 [+0.001, +0.017] (n=39); moral - norm -0.008 [-0.022, +0.006]
* A1_selB (21 features): moral: +0.022 [+0.008, +0.035] (n=36); norm: +0.038 [+0.025, +0.050] (n=50); descr: -0.002 [-0.011, +0.007] (n=39); moral - norm -0.016 [-0.035, +0.002]
* **A1 cross-fitted**: moral: +0.026 [+0.018, +0.035] (n=72); norm: +0.039 [+0.031, +0.046] (n=103); descr: +0.004 [-0.005, +0.012] (n=39); moral - norm -0.012 [-0.024, -0.001] -> not moral-specific
* B_selA (39 features): moral: -0.001 [-0.009, +0.008] (n=35); norm: +0.003 [-0.000, +0.007] (n=52); descr: +0.003 [-0.000, +0.007] (n=39); moral - norm -0.004 [-0.013, +0.005]
* B_selB (30 features): moral: -0.001 [-0.006, +0.005] (n=34); norm: +0.004 [+0.000, +0.007] (n=51); descr: +0.004 [+0.002, +0.007] (n=39); moral - norm -0.004 [-0.011, +0.003]
* **B cross-fitted**: moral: -0.001 [-0.006, +0.005] (n=69); norm: +0.004 [+0.001, +0.006] (n=103); descr: +0.004 [+0.001, +0.006] (n=39); moral - norm -0.004 [-0.010, +0.002] -> not moral-specific

## llama-3.2-3B-IT-k128

* A1_selA (58 features): moral: +0.035 [+0.021, +0.050] (n=36); norm: +0.057 [+0.047, +0.067] (n=53); descr: +0.070 [+0.055, +0.086] (n=39); moral - norm -0.022 [-0.039, -0.005]
* A1_selB (83 features): moral: -0.388 [-0.463, -0.316] (n=36); norm: -0.282 [-0.347, -0.220] (n=50); descr: -0.076 [-0.123, -0.029] (n=39); moral - norm -0.106 [-0.203, -0.010]
* **A1 cross-fitted**: moral: -0.177 [-0.239, -0.116] (n=72); norm: -0.108 [-0.155, -0.064] (n=103); descr: -0.003 [-0.026, +0.021] (n=39); moral - norm -0.069 [-0.146, +0.005] -> not moral-specific
* B_selA (39 features): moral: +0.019 [-0.018, +0.051] (n=35); norm: -0.025 [-0.041, -0.010] (n=52); descr: +0.022 [+0.012, +0.031] (n=39); moral - norm +0.044 [+0.005, +0.080]
* B_selB (44 features): moral: -0.009 [-0.044, +0.017] (n=34); norm: -0.000 [-0.011, +0.010] (n=51); descr: -0.005 [-0.015, +0.005] (n=39); moral - norm -0.009 [-0.045, +0.020]
* **B cross-fitted**: moral: +0.005 [-0.020, +0.026] (n=69); norm: -0.013 [-0.023, -0.003] (n=103); descr: +0.008 [+0.001, +0.016] (n=39); moral - norm +0.018 [-0.009, +0.041] -> not moral-specific

## llama-3.2-3B-base

* A1_selA (29 features): moral: +0.086 [+0.068, +0.104] (n=39); norm: +0.106 [+0.086, +0.127] (n=54); descr: +0.068 [+0.051, +0.085] (n=40); moral - norm -0.020 [-0.048, +0.007]
* A1_selB (19 features): moral: -0.002 [-0.008, +0.005] (n=40); norm: -0.000 [-0.005, +0.004] (n=50); descr: +0.008 [+0.002, +0.014] (n=40); moral - norm -0.001 [-0.009, +0.006]
* **A1 cross-fitted**: moral: +0.042 [+0.028, +0.056] (n=79); norm: +0.055 [+0.041, +0.070] (n=104); descr: +0.038 [+0.028, +0.048] (n=40); moral - norm -0.013 [-0.034, +0.007] -> not moral-specific
* B_selA (25 features): moral: -0.043 [-0.064, -0.024] (n=39); norm: -0.029 [-0.038, -0.021] (n=52); descr: -0.002 [-0.007, +0.003] (n=40); moral - norm -0.014 [-0.036, +0.007]
* B_selB (26 features): moral: -0.022 [-0.035, -0.008] (n=39); norm: -0.004 [-0.010, +0.002] (n=48); descr: -0.007 [-0.012, -0.003] (n=40); moral - norm -0.017 [-0.032, -0.003]
* **B cross-fitted**: moral: -0.032 [-0.045, -0.020] (n=78); norm: -0.017 [-0.023, -0.012] (n=100); descr: -0.005 [-0.008, -0.002] (n=40); moral - norm -0.015 [-0.029, -0.002] -> MORAL-SPECIFIC

## llama-3.2-3B-base-k128

* A1_selA (67 features): moral: -0.003 [-0.016, +0.010] (n=39); norm: -0.006 [-0.021, +0.008] (n=54); descr: -0.019 [-0.031, -0.006] (n=40); moral - norm +0.004 [-0.016, +0.023]
* A1_selB (64 features): moral: -0.015 [-0.025, -0.006] (n=40); norm: -0.009 [-0.015, -0.004] (n=50); descr: -0.011 [-0.019, -0.003] (n=40); moral - norm -0.006 [-0.017, +0.005]
* **A1 cross-fitted**: moral: -0.009 [-0.017, -0.001] (n=79); norm: -0.008 [-0.016, +0.000] (n=104); descr: -0.015 [-0.023, -0.006] (n=40); moral - norm -0.001 [-0.013, +0.010] -> not moral-specific
* B_selA (42 features): moral: -0.020 [-0.048, +0.006] (n=39); norm: -0.018 [-0.030, -0.007] (n=52); descr: -0.002 [-0.007, +0.004] (n=40); moral - norm -0.002 [-0.032, +0.026]
* B_selB (41 features): moral: -0.017 [-0.037, +0.002] (n=39); norm: -0.019 [-0.027, -0.011] (n=48); descr: -0.006 [-0.011, -0.001] (n=40); moral - norm +0.001 [-0.020, +0.023]
* **B cross-fitted**: moral: -0.019 [-0.036, -0.002] (n=78); norm: -0.018 [-0.026, -0.012] (n=100); descr: -0.004 [-0.008, +0.001] (n=40); moral - norm -0.000 [-0.019, +0.018] -> not moral-specific

## Count

* frame A1: moral-specific causal effect (held-out, cross-fitted) in 2 of 10 dictionaries
* frame B: moral-specific causal effect (held-out, cross-fitted) in 4 of 10 dictionaries
