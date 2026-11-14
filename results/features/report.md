# Feature results

Primary analysis: the item file is the set of accepted pairs; 227 items.
Runs folder: runs/features

## llama-3.1-8B-base

Final token (frame A1): relative reconstruction error 0.377; splice mean |dS| 0.107; pair difference captured R2 moral -0.06 (cos 0.22), norm -0.10 (cos 0.23), descr -0.11 (cos 0.25)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.467; splice mean |dS| 0.092; pair difference captured R2 moral 0.15 (cos 0.43), norm 0.10 (cos 0.40), descr 0.03 (cos 0.32)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (37 features): mean activation A1/moral 1.8264, A1/norm 1.7237, A1/descr 1.5645, B/moral 0.1987, B/norm 0.1810, B/descr 0.0274
  ratio_A1_descr_over_moral: 0.86 (0.84 to 0.88) -> frame-driven
  ratio_A1_norm_over_moral: 0.94 (0.92 to 0.96) -> frame-driven
H5 original_vs_norm_sig (18 features): mean activation A1/moral 0.2390, A1/norm 0.1258, A1/descr 0.0895, B/moral 0.1374, B/norm 0.2099, B/descr 0.2715
  ratio_A1_descr_over_moral: 0.37 (0.27 to 0.50) -> content-driven
  ratio_A1_norm_over_moral: 0.53 (0.42 to 0.67) -> inconclusive
H6 frame A1: 119 features tested; moral vs norm at full size: 29 significant; equalised group size 46: moral vs norm 7.3, norm vs norm 2.5, 1.0, 6.5 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 336 features tested; moral vs norm at full size: 45 significant; equalised group size 46: moral vs norm 10.7, norm vs norm 3.0, 9.1, 18.1 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.335, random -0.068, difference -0.268 (-0.319 to -0.217), removed norm set / random 4.36 / 2.78; norm: set -0.211, random -0.016, difference -0.195 (-0.223 to -0.167), removed norm set / random 3.99 / 2.73; descr: set -0.035, random +0.068, difference -0.103 (-0.136 to -0.071), removed norm set / random 3.61 / 2.67
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.026, random +0.002, difference -0.028 (-0.034 to -0.022), removed norm set / random 0.48 / 0.35; norm: set -0.011, random +0.003, difference -0.014 (-0.017 to -0.011), removed norm set / random 0.31 / 0.46; descr: set -0.008, random +0.000, difference -0.008 (-0.013 to -0.004), removed norm set / random 0.27 / 0.51
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.004, random +0.002, difference -0.006 (-0.014 to +0.001), removed norm set / random 1.13 / 0.88; norm: set +0.001, random +0.007, difference -0.006 (-0.012 to +0.000), removed norm set / random 1.08 / 0.85; descr: set -0.002, random +0.010, difference -0.012 (-0.018 to -0.008), removed norm set / random 0.21 / 0.79
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set +0.004, random -0.000, difference +0.004 (-0.000 to +0.008), removed norm set / random 0.28 / 1.11; norm: set +0.009, random +0.001, difference +0.008 (+0.004 to +0.012), removed norm set / random 0.41 / 1.03; descr: set +0.003, random +0.003, difference +0.001 (-0.005 to +0.006), removed norm set / random 0.60 / 0.88

## llama-3.2-1B-IT

Final token (frame A1): relative reconstruction error 0.235; splice mean |dS| 0.088; pair difference captured R2 moral -0.18 (cos 0.39), norm -0.25 (cos 0.36), descr -0.31 (cos 0.35)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.294; splice mean |dS| 0.151; pair difference captured R2 moral 0.19 (cos 0.54), norm 0.13 (cos 0.49), descr 0.11 (cos 0.48)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (86 features): mean activation A1/moral 0.1264, A1/norm 0.1151, A1/descr 0.0995, B/moral 0.0109, B/norm 0.0042, B/descr 0.0022
  ratio_A1_descr_over_moral: 0.79 (0.77 to 0.81) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.89 to 0.93) -> frame-driven
H5 original_vs_norm_sig (20 features): mean activation A1/moral 0.0447, A1/norm 0.0208, A1/descr 0.0100, B/moral 0.0145, B/norm 0.0075, B/descr 0.0051
  ratio_A1_descr_over_moral: 0.22 (0.16 to 0.29) -> content-driven
  ratio_A1_norm_over_moral: 0.47 (0.42 to 0.52) -> inconclusive
H6 frame A1: 228 features tested; moral vs norm at full size: 60 significant; equalised group size 46: moral vs norm 15.0, norm vs norm 0.0, 0.1, 0.7 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 484 features tested; moral vs norm at full size: 72 significant; equalised group size 46: moral vs norm 14.3, norm vs norm 6.8, 3.3, 13.3 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.257, random -0.214, difference -0.043 (-0.085 to -0.002), removed norm set / random 3.36 / 1.69; norm: set -0.227, random -0.160, difference -0.067 (-0.092 to -0.042), removed norm set / random 3.06 / 1.76; descr: set -0.117, random -0.171, difference +0.054 (+0.024 to +0.083), removed norm set / random 2.83 / 1.86
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.003, random +0.008, difference -0.005 (-0.012 to +0.002), removed norm set / random 0.57 / 0.34; norm: set -0.007, random +0.006, difference -0.012 (-0.016 to -0.009), removed norm set / random 0.32 / 0.36; descr: set -0.005, random +0.005, difference -0.010 (-0.016 to -0.004), removed norm set / random 0.19 / 0.36
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.048, random -0.006, difference -0.042 (-0.060 to -0.024), removed norm set / random 0.61 / 0.33; norm: set -0.017, random -0.005, difference -0.012 (-0.017 to -0.006), removed norm set / random 0.28 / 0.34; descr: set -0.004, random +0.000, difference -0.005 (-0.009 to -0.001), removed norm set / random 0.16 / 0.41
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.016, random -0.001, difference -0.015 (-0.021 to -0.008), removed norm set / random 0.29 / 0.17; norm: set -0.003, random -0.001, difference -0.002 (-0.006 to +0.001), removed norm set / random 0.13 / 0.16; descr: set -0.001, random -0.002, difference +0.001 (-0.002 to +0.003), removed norm set / random 0.10 / 0.15

## llama-3.2-1B-IT-k128

Final token (frame A1): relative reconstruction error 0.195; splice mean |dS| 0.076; pair difference captured R2 moral -0.14 (cos 0.47), norm -0.28 (cos 0.44), descr -0.22 (cos 0.42)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.244; splice mean |dS| 0.114; pair difference captured R2 moral 0.28 (cos 0.61), norm 0.21 (cos 0.57), descr 0.22 (cos 0.57)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (163 features): mean activation A1/moral 0.0861, A1/norm 0.0782, A1/descr 0.0672, B/moral 0.0123, B/norm 0.0077, B/descr 0.0053
  ratio_A1_descr_over_moral: 0.78 (0.76 to 0.80) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (52 features): mean activation A1/moral 0.0131, A1/norm 0.0027, A1/descr 0.0012, B/moral 0.0098, B/norm 0.0064, B/descr 0.0049
  ratio_A1_descr_over_moral: 0.09 (0.06 to 0.13) -> content-driven
  ratio_A1_norm_over_moral: 0.21 (0.16 to 0.26) -> content-driven
H6 frame A1: 463 features tested; moral vs norm at full size: 100 significant; equalised group size 46: moral vs norm 30.9, norm vs norm 1.5, 6.8, 5.8 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 970 features tested; moral vs norm at full size: 125 significant; equalised group size 46: moral vs norm 16.9, norm vs norm 8.7, 15.6, 20.0 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.317, random -0.164, difference -0.153 (-0.206 to -0.102), removed norm set / random 3.29 / 1.85; norm: set -0.233, random -0.107, difference -0.125 (-0.151 to -0.099), removed norm set / random 3.02 / 1.88; descr: set -0.111, random -0.147, difference +0.037 (+0.005 to +0.071), removed norm set / random 2.77 / 2.02
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.005, random -0.001, difference +0.007 (+0.002 to +0.012), removed norm set / random 0.37 / 0.18; norm: set +0.000, random +0.001, difference -0.001 (-0.003 to +0.002), removed norm set / random 0.11 / 0.17; descr: set -0.000, random -0.001, difference +0.001 (-0.001 to +0.003), removed norm set / random 0.06 / 0.22
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.074, random -0.023, difference -0.051 (-0.068 to -0.035), removed norm set / random 0.77 / 0.62; norm: set -0.057, random -0.014, difference -0.043 (-0.060 to -0.028), removed norm set / random 0.57 / 0.59; descr: set -0.032, random -0.010, difference -0.022 (-0.032 to -0.013), removed norm set / random 0.48 / 0.58
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.051, random -0.002, difference -0.049 (-0.066 to -0.033), removed norm set / random 0.37 / 0.28; norm: set -0.044, random -0.001, difference -0.044 (-0.058 to -0.031), removed norm set / random 0.28 / 0.27; descr: set -0.022, random -0.001, difference -0.020 (-0.029 to -0.013), removed norm set / random 0.25 / 0.25

## llama-3.2-1B-base

Final token (frame A1): relative reconstruction error 0.209; splice mean |dS| 0.088; pair difference captured R2 moral -0.21 (cos 0.38), norm -0.25 (cos 0.36), descr -0.23 (cos 0.37)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.253; splice mean |dS| 0.077; pair difference captured R2 moral 0.11 (cos 0.48), norm 0.11 (cos 0.48), descr 0.09 (cos 0.47)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (91 features): mean activation A1/moral 0.1187, A1/norm 0.1075, A1/descr 0.0828, B/moral 0.0271, B/norm 0.0212, B/descr 0.0065
  ratio_A1_descr_over_moral: 0.70 (0.68 to 0.72) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (32 features): mean activation A1/moral 0.0180, A1/norm 0.0081, A1/descr 0.0022, B/moral 0.0188, B/norm 0.0147, B/descr 0.0091
  ratio_A1_descr_over_moral: 0.12 (0.07 to 0.17) -> content-driven
  ratio_A1_norm_over_moral: 0.45 (0.36 to 0.56) -> inconclusive
H6 frame A1: 232 features tested; moral vs norm at full size: 43 significant; equalised group size 46: moral vs norm 14.3, norm vs norm 0.3, 4.0, 6.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 465 features tested; moral vs norm at full size: 58 significant; equalised group size 46: moral vs norm 6.2, norm vs norm 8.8, 2.3, 9.7 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.206, random -0.220, difference +0.015 (-0.010 to +0.039), removed norm set / random 3.14 / 1.63; norm: set -0.183, random -0.169, difference -0.014 (-0.042 to +0.014), removed norm set / random 2.94 / 1.77; descr: set -0.117, random -0.178, difference +0.062 (+0.026 to +0.098), removed norm set / random 2.50 / 1.82
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.015, random +0.000, difference -0.015 (-0.021 to -0.010), removed norm set / random 0.34 / 0.22; norm: set -0.005, random +0.002, difference -0.008 (-0.010 to -0.005), removed norm set / random 0.18 / 0.21; descr: set -0.003, random +0.003, difference -0.006 (-0.008 to -0.004), removed norm set / random 0.07 / 0.26
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.052, random -0.020, difference -0.032 (-0.043 to -0.021), removed norm set / random 1.30 / 0.83; norm: set -0.039, random -0.023, difference -0.016 (-0.025 to -0.007), removed norm set / random 1.19 / 0.83; descr: set -0.016, random -0.019, difference +0.003 (-0.005 to +0.011), removed norm set / random 0.42 / 0.82
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.011, random -0.007, difference -0.005 (-0.009 to -0.001), removed norm set / random 0.51 / 0.49; norm: set -0.008, random -0.007, difference -0.001 (-0.005 to +0.003), removed norm set / random 0.43 / 0.46; descr: set -0.013, random -0.006, difference -0.007 (-0.011 to -0.003), removed norm set / random 0.29 / 0.39

## llama-3.2-1B-base-MLP0

Final token (frame A1): relative reconstruction error 0.192; splice mean |dS| 0.052; pair difference captured R2 moral -1.19 (cos 0.20), norm -2.15 (cos 0.19), descr -1.27 (cos 0.19)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.039; splice mean |dS| 0.003; pair difference captured R2 moral 0.32 (cos 0.63), norm 0.36 (cos 0.64), descr 0.42 (cos 0.66)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (80 features): mean activation A1/moral 0.0775, A1/norm 0.0771, A1/descr 0.0769, B/moral 0.0009, B/norm 0.0010, B/descr 0.0009
  ratio_A1_descr_over_moral: 0.99 (0.99 to 1.00) -> frame-driven
  ratio_A1_norm_over_moral: 0.99 (0.99 to 1.00) -> frame-driven
H5 original_vs_norm_sig (16 features): mean activation A1/moral 0.0096, A1/norm 0.0077, A1/descr 0.0069, B/moral 0.0082, B/norm 0.0084, B/descr 0.0110
  ratio_A1_descr_over_moral: 0.71 (0.61 to 0.83) -> frame-driven
  ratio_A1_norm_over_moral: 0.80 (0.71 to 0.90) -> frame-driven
H6 frame A1: 107 features tested; moral vs norm at full size: 0 significant; equalised group size 46: moral vs norm 0.2, norm vs norm 0.0, 0.9, 0.5 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 176 features tested; moral vs norm at full size: 0 significant; equalised group size 46: moral vs norm 0.1, norm vs norm 0.7, 0.1, 0.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.037, random -0.209, difference +0.246 (+0.193 to +0.302), removed norm set / random 1.30 / 0.65; norm: set +0.035, random -0.117, difference +0.152 (+0.115 to +0.189), removed norm set / random 1.30 / 0.65; descr: set +0.052, random -0.098, difference +0.150 (+0.096 to +0.204), removed norm set / random 1.29 / 0.65
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.002, random +0.002, difference -0.004 (-0.007 to -0.002), removed norm set / random 0.08 / 0.08; norm: set -0.001, random +0.001, difference -0.002 (-0.004 to -0.001), removed norm set / random 0.08 / 0.08; descr: set -0.001, random +0.002, difference -0.003 (-0.004 to -0.001), removed norm set / random 0.07 / 0.08
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.06; norm: set -0.000, random +0.000, difference -0.000 (-0.001 to +0.000), removed norm set / random 0.05 / 0.06; descr: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.04
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.001, difference +0.001 (-0.000 to +0.002), removed norm set / random 0.12 / 0.13; norm: set -0.001, random +0.000, difference -0.001 (-0.003 to +0.001), removed norm set / random 0.12 / 0.13; descr: set +0.001, random -0.000, difference +0.001 (-0.000 to +0.002), removed norm set / random 0.16 / 0.12

## llama-3.2-1B-base-k128

Final token (frame A1): relative reconstruction error 0.166; splice mean |dS| 0.063; pair difference captured R2 moral -0.16 (cos 0.46), norm -0.23 (cos 0.45), descr -0.16 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.206; splice mean |dS| 0.073; pair difference captured R2 moral 0.22 (cos 0.57), norm 0.21 (cos 0.57), descr 0.21 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (175 features): mean activation A1/moral 0.0835, A1/norm 0.0766, A1/descr 0.0606, B/moral 0.0144, B/norm 0.0112, B/descr 0.0070
  ratio_A1_descr_over_moral: 0.73 (0.70 to 0.75) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.89 to 0.94) -> frame-driven
H5 original_vs_norm_sig (66 features): mean activation A1/moral 0.0185, A1/norm 0.0071, A1/descr 0.0021, B/moral 0.0130, B/norm 0.0097, B/descr 0.0074
  ratio_A1_descr_over_moral: 0.11 (0.08 to 0.15) -> content-driven
  ratio_A1_norm_over_moral: 0.38 (0.32 to 0.45) -> content-driven
H6 frame A1: 470 features tested; moral vs norm at full size: 77 significant; equalised group size 46: moral vs norm 23.4, norm vs norm 3.0, 11.6, 6.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 911 features tested; moral vs norm at full size: 73 significant; equalised group size 46: moral vs norm 16.4, norm vs norm 8.2, 13.0, 18.6 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.324, random -0.208, difference -0.116 (-0.146 to -0.087), removed norm set / random 3.16 / 1.82; norm: set -0.253, random -0.141, difference -0.112 (-0.144 to -0.079), removed norm set / random 3.00 / 1.90; descr: set -0.141, random -0.147, difference +0.006 (-0.032 to +0.045), removed norm set / random 2.55 / 2.01
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.014, random +0.003, difference -0.017 (-0.022 to -0.013), removed norm set / random 0.46 / 0.27; norm: set -0.004, random +0.003, difference -0.007 (-0.009 to -0.004), removed norm set / random 0.25 / 0.30; descr: set -0.004, random -0.000, difference -0.004 (-0.006 to -0.001), removed norm set / random 0.13 / 0.34
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.036, random -0.019, difference -0.017 (-0.027 to -0.008), removed norm set / random 0.89 / 0.75; norm: set -0.037, random -0.015, difference -0.022 (-0.030 to -0.015), removed norm set / random 0.73 / 0.71; descr: set -0.018, random -0.005, difference -0.014 (-0.021 to -0.007), removed norm set / random 0.52 / 0.67
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.003, random -0.006, difference +0.003 (-0.001 to +0.007), removed norm set / random 0.54 / 0.48; norm: set -0.004, random -0.006, difference +0.002 (-0.002 to +0.005), removed norm set / random 0.45 / 0.47; descr: set -0.015, random -0.007, difference -0.008 (-0.012 to -0.004), removed norm set / random 0.34 / 0.40

## llama-3.2-3B-IT-L19

Final token (frame A1): relative reconstruction error 0.126; splice mean |dS| 0.133; pair difference captured R2 moral 0.45 (cos 0.70), norm 0.32 (cos 0.64), descr 0.37 (cos 0.67)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.181; splice mean |dS| 0.060; pair difference captured R2 moral 0.49 (cos 0.73), norm 0.47 (cos 0.71), descr 0.51 (cos 0.73)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (153 features): mean activation A1/moral 0.5187, A1/norm 0.5080, A1/descr 0.4781, B/moral 0.1700, B/norm 0.1305, B/descr 0.0715
  ratio_A1_descr_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
  ratio_A1_norm_over_moral: 0.98 (0.97 to 0.99) -> frame-driven
H5 original_vs_norm_sig (49 features): mean activation A1/moral 0.2337, A1/norm 0.1998, A1/descr 0.1683, B/moral 0.1325, B/norm 0.1067, B/descr 0.1028
  ratio_A1_descr_over_moral: 0.72 (0.68 to 0.76) -> frame-driven
  ratio_A1_norm_over_moral: 0.85 (0.81 to 0.90) -> frame-driven
H6 frame A1: 387 features tested; moral vs norm at full size: 116 significant; equalised group size 46: moral vs norm 54.9, norm vs norm 10.3, 14.2, 39.2 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 876 features tested; moral vs norm at full size: 252 significant; equalised group size 46: moral vs norm 77.4, norm vs norm 44.4, 53.4, 81.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.050, random -0.320, difference +0.269 (+0.219 to +0.319), removed norm set / random 18.30 / 11.11; norm: set -0.025, random -0.304, difference +0.279 (+0.237 to +0.321), removed norm set / random 18.13 / 10.68; descr: set +0.085, random -0.257, difference +0.342 (+0.279 to +0.405), removed norm set / random 17.78 / 11.40
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.057, random -0.009, difference -0.048 (-0.068 to -0.028), removed norm set / random 3.75 / 3.13; norm: set +0.001, random -0.020, difference +0.021 (+0.003 to +0.038), removed norm set / random 3.24 / 3.12; descr: set -0.001, random -0.013, difference +0.012 (-0.006 to +0.031), removed norm set / random 3.03 / 3.26
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.306, random -0.093, difference -0.214 (-0.251 to -0.177), removed norm set / random 7.85 / 5.44; norm: set -0.266, random -0.087, difference -0.179 (-0.214 to -0.144), removed norm set / random 6.44 / 5.48; descr: set -0.249, random -0.061, difference -0.188 (-0.230 to -0.144), removed norm set / random 4.53 / 5.48
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.140, random -0.028, difference -0.112 (-0.136 to -0.089), removed norm set / random 3.66 / 2.62; norm: set -0.220, random -0.006, difference -0.214 (-0.247 to -0.180), removed norm set / random 3.52 / 2.44; descr: set -0.217, random +0.000, difference -0.217 (-0.264 to -0.170), removed norm set / random 3.58 / 2.17

## llama-3.2-3B-IT-L3

Final token (frame A1): relative reconstruction error 0.162; splice mean |dS| 0.025; pair difference captured R2 moral 0.02 (cos 0.42), norm -0.05 (cos 0.41), descr -0.08 (cos 0.40)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.147; splice mean |dS| 0.018; pair difference captured R2 moral 0.27 (cos 0.57), norm 0.22 (cos 0.55), descr 0.21 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (171 features): mean activation A1/moral 0.0898, A1/norm 0.0870, A1/descr 0.0770, B/moral 0.0105, B/norm 0.0088, B/descr 0.0052
  ratio_A1_descr_over_moral: 0.86 (0.84 to 0.87) -> frame-driven
  ratio_A1_norm_over_moral: 0.97 (0.95 to 0.98) -> frame-driven
H5 original_vs_norm_sig (30 features): mean activation A1/moral 0.0074, A1/norm 0.0034, A1/descr 0.0028, B/moral 0.0076, B/norm 0.0018, B/descr 0.0017
  ratio_A1_descr_over_moral: 0.37 (0.27 to 0.50) -> inconclusive
  ratio_A1_norm_over_moral: 0.46 (0.33 to 0.63) -> inconclusive
H6 frame A1: 401 features tested; moral vs norm at full size: 6 significant; equalised group size 46: moral vs norm 0.9, norm vs norm 3.4, 0.0, 2.4 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 1014 features tested; moral vs norm at full size: 22 significant; equalised group size 46: moral vs norm 4.4, norm vs norm 3.4, 1.8, 0.2 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.274, random -0.467, difference +0.193 (+0.129 to +0.258), removed norm set / random 3.68 / 1.59; norm: set -0.186, random -0.360, difference +0.174 (+0.113 to +0.236), removed norm set / random 3.64 / 1.64; descr: set -0.118, random -0.073, difference -0.046 (-0.123 to +0.033), removed norm set / random 3.46 / 1.65
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.001, random -0.000, difference +0.001 (+0.000 to +0.002), removed norm set / random 0.14 / 0.09; norm: set +0.001, random -0.000, difference +0.001 (-0.000 to +0.001), removed norm set / random 0.07 / 0.10; descr: set +0.002, random -0.000, difference +0.002 (+0.001 to +0.003), removed norm set / random 0.08 / 0.09
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.000, random +0.001, difference -0.000 (-0.006 to +0.006), removed norm set / random 0.80 / 0.60; norm: set -0.002, random -0.006, difference +0.005 (+0.002 to +0.008), removed norm set / random 0.77 / 0.63; descr: set -0.001, random -0.007, difference +0.006 (+0.002 to +0.011), removed norm set / random 0.51 / 0.54
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.002, random -0.000, difference -0.002 (-0.003 to -0.000), removed norm set / random 0.16 / 0.10; norm: set -0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.09; descr: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.06 / 0.10

## llama-3.2-3B-IT-L7

Final token (frame A1): relative reconstruction error 0.209; splice mean |dS| 0.042; pair difference captured R2 moral -0.09 (cos 0.41), norm -0.19 (cos 0.39), descr -0.23 (cos 0.37)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.277; splice mean |dS| 0.046; pair difference captured R2 moral 0.33 (cos 0.63), norm 0.27 (cos 0.59), descr 0.21 (cos 0.55)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (205 features): mean activation A1/moral 0.1162, A1/norm 0.1068, A1/descr 0.0891, B/moral 0.0038, B/norm 0.0019, B/descr 0.0020
  ratio_A1_descr_over_moral: 0.77 (0.75 to 0.79) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
H5 original_vs_norm_sig (62 features): mean activation A1/moral 0.0144, A1/norm 0.0079, A1/descr 0.0058, B/moral 0.0112, B/norm 0.0086, B/descr 0.0075
  ratio_A1_descr_over_moral: 0.40 (0.32 to 0.48) -> content-driven
  ratio_A1_norm_over_moral: 0.55 (0.47 to 0.64) -> inconclusive
H6 frame A1: 467 features tested; moral vs norm at full size: 57 significant; equalised group size 46: moral vs norm 15.1, norm vs norm 0.3, 3.5, 13.3 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1312 features tested; moral vs norm at full size: 145 significant; equalised group size 46: moral vs norm 19.8, norm vs norm 4.9, 15.8, 27.4 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.264, random -0.384, difference +0.120 (+0.044 to +0.195), removed norm set / random 5.28 / 2.73; norm: set -0.195, random -0.334, difference +0.138 (+0.091 to +0.189), removed norm set / random 5.03 / 2.84; descr: set -0.042, random -0.116, difference +0.074 (-0.015 to +0.163), removed norm set / random 4.66 / 3.06
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random +0.002, difference -0.003 (-0.005 to -0.001), removed norm set / random 0.47 / 0.36; norm: set -0.002, random +0.004, difference -0.005 (-0.007 to -0.004), removed norm set / random 0.34 / 0.36; descr: set -0.001, random +0.008, difference -0.009 (-0.011 to -0.007), removed norm set / random 0.32 / 0.38
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.008, random -0.001, difference -0.006 (-0.011 to -0.001), removed norm set / random 0.44 / 0.36; norm: set -0.003, random -0.001, difference -0.003 (-0.005 to -0.000), removed norm set / random 0.28 / 0.35; descr: set +0.000, random -0.002, difference +0.002 (-0.000 to +0.004), removed norm set / random 0.25 / 0.34
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.006, random -0.006, difference -0.000 (-0.003 to +0.002), removed norm set / random 0.45 / 0.43; norm: set -0.003, random -0.004, difference +0.001 (-0.002 to +0.003), removed norm set / random 0.39 / 0.41; descr: set -0.004, random -0.002, difference -0.001 (-0.003 to +0.001), removed norm set / random 0.38 / 0.35

## llama-3.2-3B-IT-k128

Final token (frame A1): relative reconstruction error 0.215; splice mean |dS| 0.073; pair difference captured R2 moral 0.02 (cos 0.45), norm -0.08 (cos 0.43), descr -0.07 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.297; splice mean |dS| 0.094; pair difference captured R2 moral 0.38 (cos 0.65), norm 0.34 (cos 0.63), descr 0.28 (cos 0.59)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (212 features): mean activation A1/moral 0.1347, A1/norm 0.1245, A1/descr 0.1093, B/moral 0.0253, B/norm 0.0184, B/descr 0.0172
  ratio_A1_descr_over_moral: 0.81 (0.79 to 0.83) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.91 to 0.94) -> frame-driven
H5 original_vs_norm_sig (97 features): mean activation A1/moral 0.0455, A1/norm 0.0241, A1/descr 0.0144, B/moral 0.0227, B/norm 0.0204, B/descr 0.0189
  ratio_A1_descr_over_moral: 0.32 (0.29 to 0.35) -> content-driven
  ratio_A1_norm_over_moral: 0.53 (0.49 to 0.58) -> inconclusive
H6 frame A1: 575 features tested; moral vs norm at full size: 164 significant; equalised group size 46: moral vs norm 59.5, norm vs norm 4.0, 4.0, 19.4 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1201 features tested; moral vs norm at full size: 146 significant; equalised group size 46: moral vs norm 32.0, norm vs norm 15.0, 1.9, 49.1 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.648, random -0.359, difference -0.289 (-0.344 to -0.234), removed norm set / random 6.07 / 3.95; norm: set -0.347, random -0.208, difference -0.139 (-0.178 to -0.100), removed norm set / random 5.85 / 3.83; descr: set -0.193, random -0.022, difference -0.171 (-0.233 to -0.109), removed norm set / random 5.51 / 4.01
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.023, random +0.009, difference -0.032 (-0.038 to -0.025), removed norm set / random 1.39 / 1.17; norm: set -0.008, random +0.017, difference -0.026 (-0.030 to -0.021), removed norm set / random 1.00 / 1.15; descr: set -0.015, random +0.018, difference -0.032 (-0.039 to -0.026), removed norm set / random 0.77 / 1.13
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.025, random -0.005, difference -0.020 (-0.039 to -0.002), removed norm set / random 1.82 / 1.60; norm: set -0.006, random -0.016, difference +0.010 (-0.005 to +0.026), removed norm set / random 1.41 / 1.55; descr: set -0.009, random -0.024, difference +0.015 (-0.000 to +0.031), removed norm set / random 1.36 / 1.45
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.032, random -0.008, difference -0.024 (-0.033 to -0.015), removed norm set / random 1.04 / 1.28; norm: set -0.031, random -0.017, difference -0.014 (-0.023 to -0.004), removed norm set / random 0.95 / 1.20; descr: set -0.029, random -0.018, difference -0.011 (-0.021 to +0.000), removed norm set / random 0.84 / 1.05

## llama-3.2-3B-base

Final token (frame A1): relative reconstruction error 0.252; splice mean |dS| 0.067; pair difference captured R2 moral -0.08 (cos 0.36), norm -0.15 (cos 0.35), descr -0.11 (cos 0.38)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.322; splice mean |dS| 0.076; pair difference captured R2 moral 0.26 (cos 0.56), norm 0.22 (cos 0.53), descr 0.15 (cos 0.48)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (100 features): mean activation A1/moral 0.1865, A1/norm 0.1713, A1/descr 0.1401, B/moral 0.0272, B/norm 0.0200, B/descr 0.0057
  ratio_A1_descr_over_moral: 0.75 (0.73 to 0.78) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
H5 original_vs_norm_sig (56 features): mean activation A1/moral 0.0387, A1/norm 0.0191, A1/descr 0.0103, B/moral 0.0209, B/norm 0.0161, B/descr 0.0129
  ratio_A1_descr_over_moral: 0.27 (0.21 to 0.32) -> content-driven
  ratio_A1_norm_over_moral: 0.49 (0.43 to 0.57) -> inconclusive
H6 frame A1: 301 features tested; moral vs norm at full size: 69 significant; equalised group size 46: moral vs norm 21.9, norm vs norm 4.7, 5.5, 9.2 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 693 features tested; moral vs norm at full size: 79 significant; equalised group size 46: moral vs norm 17.6, norm vs norm 2.6, 3.9, 17.7 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.454, random -0.301, difference -0.153 (-0.189 to -0.118), removed norm set / random 5.68 / 2.91; norm: set -0.289, random -0.261, difference -0.027 (-0.044 to -0.010), removed norm set / random 5.31 / 2.90; descr: set -0.139, random -0.093, difference -0.045 (-0.085 to -0.007), removed norm set / random 4.69 / 3.07
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.003, random -0.001, difference +0.004 (-0.002 to +0.009), removed norm set / random 0.95 / 0.64; norm: set +0.008, random -0.000, difference +0.008 (+0.003 to +0.012), removed norm set / random 0.64 / 0.75; descr: set -0.006, random +0.006, difference -0.012 (-0.017 to -0.007), removed norm set / random 0.41 / 0.75
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.008, random -0.009, difference +0.001 (-0.009 to +0.012), removed norm set / random 1.71 / 0.91; norm: set -0.002, random -0.008, difference +0.006 (-0.003 to +0.015), removed norm set / random 1.49 / 0.91; descr: set -0.009, random -0.006, difference -0.003 (-0.008 to +0.002), removed norm set / random 0.59 / 0.75
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.017, random -0.003, difference -0.014 (-0.019 to -0.009), removed norm set / random 0.73 / 0.83; norm: set -0.007, random -0.004, difference -0.003 (-0.008 to +0.001), removed norm set / random 0.60 / 0.79; descr: set -0.013, random -0.005, difference -0.008 (-0.013 to -0.003), removed norm set / random 0.51 / 0.64

## llama-3.2-3B-base-k128

Final token (frame A1): relative reconstruction error 0.213; splice mean |dS| 0.060; pair difference captured R2 moral -0.02 (cos 0.44), norm -0.04 (cos 0.43), descr 0.01 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.267; splice mean |dS| 0.071; pair difference captured R2 moral 0.35 (cos 0.63), norm 0.32 (cos 0.61), descr 0.26 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (222 features): mean activation A1/moral 0.1163, A1/norm 0.1032, A1/descr 0.0849, B/moral 0.0214, B/norm 0.0165, B/descr 0.0095
  ratio_A1_descr_over_moral: 0.73 (0.71 to 0.75) -> frame-driven
  ratio_A1_norm_over_moral: 0.89 (0.87 to 0.91) -> frame-driven
H5 original_vs_norm_sig (124 features): mean activation A1/moral 0.0296, A1/norm 0.0129, A1/descr 0.0079, B/moral 0.0130, B/norm 0.0129, B/descr 0.0139
  ratio_A1_descr_over_moral: 0.27 (0.23 to 0.31) -> content-driven
  ratio_A1_norm_over_moral: 0.43 (0.38 to 0.50) -> content-driven
H6 frame A1: 646 features tested; moral vs norm at full size: 165 significant; equalised group size 46: moral vs norm 52.4, norm vs norm 10.8, 20.6, 19.4 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1255 features tested; moral vs norm at full size: 149 significant; equalised group size 46: moral vs norm 24.6, norm vs norm 11.6, 15.3, 34.0 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.488, random -0.164, difference -0.324 (-0.368 to -0.280), removed norm set / random 5.74 / 3.10; norm: set -0.320, random -0.140, difference -0.180 (-0.209 to -0.152), removed norm set / random 5.36 / 3.19; descr: set -0.144, random +0.022, difference -0.165 (-0.208 to -0.124), removed norm set / random 4.75 / 3.43
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.012, random -0.002, difference -0.010 (-0.017 to -0.004), removed norm set / random 1.09 / 0.66; norm: set -0.002, random -0.005, difference +0.003 (-0.001 to +0.007), removed norm set / random 0.65 / 0.78; descr: set -0.002, random -0.008, difference +0.006 (+0.002 to +0.011), removed norm set / random 0.49 / 0.89
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.005, random -0.011, difference +0.006 (-0.004 to +0.017), removed norm set / random 2.01 / 1.46; norm: set +0.004, random -0.007, difference +0.011 (+0.001 to +0.021), removed norm set / random 1.75 / 1.41; descr: set -0.007, random -0.007, difference -0.001 (-0.008 to +0.006), removed norm set / random 1.04 / 1.21
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.021, random -0.009, difference -0.012 (-0.018 to -0.006), removed norm set / random 0.74 / 0.91; norm: set -0.011, random -0.009, difference -0.003 (-0.008 to +0.002), removed norm set / random 0.80 / 0.87; descr: set -0.012, random -0.002, difference -0.010 (-0.017 to -0.004), removed norm set / random 0.79 / 0.71

## qwen-2.5-7b-IT

Final token (frame A1): relative reconstruction error 0.148; splice mean |dS| 0.022; pair difference captured R2 moral -0.09 (cos 0.48), norm -0.20 (cos 0.44), descr 0.12 (cos 0.52)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.036; splice mean |dS| 0.005; pair difference captured R2 moral 0.32 (cos 0.60), norm 0.38 (cos 0.64), descr 0.45 (cos 0.68)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (154 features): mean activation A1/moral 0.4660, A1/norm 0.4587, A1/descr 0.4582, B/moral 0.0283, B/norm 0.0282, B/descr 0.0290
  ratio_A1_descr_over_moral: 0.98 (0.98 to 0.99) -> frame-driven
  ratio_A1_norm_over_moral: 0.98 (0.98 to 0.99) -> frame-driven
H5 original_vs_norm_sig (21 features): mean activation A1/moral 0.0519, A1/norm 0.0214, A1/descr 0.0158, B/moral 0.0218, B/norm 0.0192, B/descr 0.0210
  ratio_A1_descr_over_moral: 0.31 (0.22 to 0.40) -> content-driven
  ratio_A1_norm_over_moral: 0.41 (0.32 to 0.52) -> inconclusive
H6 frame A1: 292 features tested; moral vs norm at full size: 4 significant; equalised group size 46: moral vs norm 0.3, norm vs norm 0.1, 0.0, 0.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 888 features tested; moral vs norm at full size: 1 significant; equalised group size 46: moral vs norm 0.2, norm vs norm 0.1, 0.1, 0.0 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.674, random -0.951, difference +0.277 (+0.176 to +0.381), removed norm set / random 10.27 / 6.68; norm: set -0.463, random -0.670, difference +0.207 (+0.129 to +0.285), removed norm set / random 10.16 / 6.55; descr: set -0.304, random -0.330, difference +0.026 (-0.070 to +0.128), removed norm set / random 10.16 / 6.69
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random +0.000, difference -0.001 (-0.002 to +0.000), removed norm set / random 0.61 / 0.43; norm: set -0.000, random +0.000, difference -0.001 (-0.001 to +0.000), removed norm set / random 0.33 / 0.44; descr: set +0.000, random +0.000, difference -0.000 (-0.001 to +0.001), removed norm set / random 0.32 / 0.43
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.010, random -0.004, difference -0.006 (-0.013 to +0.002), removed norm set / random 2.94 / 1.71; norm: set -0.005, random -0.003, difference -0.002 (-0.008 to +0.006), removed norm set / random 2.94 / 1.73; descr: set +0.001, random -0.002, difference +0.004 (-0.002 to +0.010), removed norm set / random 3.01 / 1.76
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.32 / 0.35; norm: set +0.000, random -0.000, difference +0.000 (-0.001 to +0.001), removed norm set / random 0.30 / 0.37; descr: set -0.001, random +0.000, difference -0.001 (-0.001 to -0.000), removed norm set / random 0.36 / 0.38

## qwen-2.5-7b-base

Final token (frame A1): relative reconstruction error 0.144; splice mean |dS| 0.012; pair difference captured R2 moral -0.07 (cos 0.49), norm -0.12 (cos 0.45), descr 0.12 (cos 0.52)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.036; splice mean |dS| 0.004; pair difference captured R2 moral 0.30 (cos 0.59), norm 0.38 (cos 0.64), descr 0.46 (cos 0.68)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (153 features): mean activation A1/moral 0.4811, A1/norm 0.4670, A1/descr 0.4713, B/moral 0.0207, B/norm 0.0210, B/descr 0.0209
  ratio_A1_descr_over_moral: 0.98 (0.97 to 0.99) -> frame-driven
  ratio_A1_norm_over_moral: 0.97 (0.96 to 0.98) -> frame-driven
H5 original_vs_norm_sig (22 features): mean activation A1/moral 0.0510, A1/norm 0.0230, A1/descr 0.0197, B/moral 0.0194, B/norm 0.0142, B/descr 0.0146
  ratio_A1_descr_over_moral: 0.39 (0.31 to 0.48) -> content-driven
  ratio_A1_norm_over_moral: 0.45 (0.36 to 0.57) -> inconclusive
H6 frame A1: 312 features tested; moral vs norm at full size: 2 significant; equalised group size 46: moral vs norm 0.2, norm vs norm 0.1, 0.1, 0.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 910 features tested; moral vs norm at full size: 2 significant; equalised group size 46: moral vs norm 0.1, norm vs norm 0.0, 0.0, 0.3 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.400, random -0.865, difference +0.466 (+0.389 to +0.543), removed norm set / random 10.79 / 6.48; norm: set -0.170, random -0.641, difference +0.471 (+0.412 to +0.531), removed norm set / random 10.59 / 6.41; descr: set +0.295, random -0.189, difference +0.484 (+0.393 to +0.573), removed norm set / random 10.66 / 6.58
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.002, random +0.000, difference +0.002 (+0.001 to +0.003), removed norm set / random 0.67 / 0.47; norm: set +0.001, random +0.000, difference +0.001 (+0.001 to +0.002), removed norm set / random 0.37 / 0.48; descr: set +0.001, random +0.000, difference +0.001 (+0.000 to +0.001), removed norm set / random 0.38 / 0.45
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.005, random -0.000, difference -0.005 (-0.008 to -0.002), removed norm set / random 2.33 / 1.14; norm: set -0.003, random -0.000, difference -0.003 (-0.007 to +0.000), removed norm set / random 2.35 / 1.15; descr: set +0.001, random -0.000, difference +0.001 (-0.002 to +0.005), removed norm set / random 2.36 / 1.23
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.000, difference -0.000 (-0.000 to +0.000), removed norm set / random 0.26 / 0.26; norm: set +0.000, random +0.000, difference +0.000 (-0.000 to +0.000), removed norm set / random 0.21 / 0.24; descr: set -0.000, random -0.000, difference -0.000 (-0.000 to +0.000), removed norm set / random 0.21 / 0.23

