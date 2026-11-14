# Feature results

**Sensitivity run (an option differs from the default; items: accepted, 227 items): not the primary analysis.**
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
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.352, random -0.077, difference -0.275 (-0.331 to -0.220), removed norm set / random 4.35 / 2.78; norm: set -0.219, random -0.021, difference -0.199 (-0.228 to -0.170), removed norm set / random 4.01 / 2.72; descr: set -0.040, random +0.079, difference -0.119 (-0.156 to -0.082), removed norm set / random 3.63 / 2.68
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.026, random +0.002, difference -0.028 (-0.035 to -0.021), removed norm set / random 0.48 / 0.35; norm: set -0.011, random +0.002, difference -0.014 (-0.017 to -0.010), removed norm set / random 0.31 / 0.46; descr: set -0.009, random +0.000, difference -0.009 (-0.015 to -0.005), removed norm set / random 0.25 / 0.51
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.003, random +0.003, difference -0.006 (-0.014 to +0.001), removed norm set / random 1.14 / 0.89; norm: set +0.001, random +0.007, difference -0.006 (-0.012 to +0.001), removed norm set / random 1.09 / 0.86; descr: set -0.002, random +0.011, difference -0.013 (-0.018 to -0.008), removed norm set / random 0.22 / 0.79
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set +0.004, random +0.000, difference +0.004 (-0.000 to +0.008), removed norm set / random 0.28 / 1.11; norm: set +0.009, random +0.001, difference +0.008 (+0.004 to +0.012), removed norm set / random 0.42 / 1.03; descr: set +0.003, random +0.003, difference +0.001 (-0.005 to +0.006), removed norm set / random 0.60 / 0.88

## llama-3.2-1B-IT

Final token (frame A1): relative reconstruction error 0.235; splice mean |dS| 0.088; pair difference captured R2 moral -0.18 (cos 0.39), norm -0.25 (cos 0.36), descr -0.31 (cos 0.35)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.294; splice mean |dS| 0.151; pair difference captured R2 moral 0.19 (cos 0.54), norm 0.13 (cos 0.49), descr 0.11 (cos 0.48)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (86 features): mean activation A1/moral 0.1264, A1/norm 0.1151, A1/descr 0.0995, B/moral 0.0109, B/norm 0.0042, B/descr 0.0022
  ratio_A1_descr_over_moral: 0.79 (0.77 to 0.81) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.89 to 0.93) -> frame-driven
H5 original_vs_norm_sig (20 features): mean activation A1/moral 0.0447, A1/norm 0.0208, A1/descr 0.0100, B/moral 0.0145, B/norm 0.0075, B/descr 0.0051
  ratio_A1_descr_over_moral: 0.22 (0.16 to 0.29) -> content-driven
  ratio_A1_norm_over_moral: 0.47 (0.41 to 0.52) -> inconclusive
H6 frame A1: 228 features tested; moral vs norm at full size: 61 significant; equalised group size 46: moral vs norm 17.4, norm vs norm 0.0, 0.2, 0.1 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 484 features tested; moral vs norm at full size: 73 significant; equalised group size 46: moral vs norm 14.1, norm vs norm 6.9, 3.8, 13.5 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.275, random -0.226, difference -0.049 (-0.092 to -0.005), removed norm set / random 3.35 / 1.70; norm: set -0.266, random -0.183, difference -0.083 (-0.110 to -0.056), removed norm set / random 3.07 / 1.76; descr: set -0.138, random -0.196, difference +0.058 (+0.026 to +0.091), removed norm set / random 2.82 / 1.87
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.002, random +0.009, difference -0.007 (-0.013 to +0.000), removed norm set / random 0.57 / 0.34; norm: set -0.007, random +0.006, difference -0.014 (-0.018 to -0.010), removed norm set / random 0.33 / 0.36; descr: set -0.005, random +0.006, difference -0.011 (-0.018 to -0.005), removed norm set / random 0.19 / 0.36
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.051, random -0.007, difference -0.044 (-0.064 to -0.026), removed norm set / random 0.62 / 0.33; norm: set -0.018, random -0.006, difference -0.012 (-0.018 to -0.006), removed norm set / random 0.28 / 0.34; descr: set -0.004, random -0.000, difference -0.004 (-0.009 to -0.000), removed norm set / random 0.17 / 0.41
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.017, random -0.002, difference -0.016 (-0.023 to -0.009), removed norm set / random 0.29 / 0.18; norm: set -0.004, random -0.001, difference -0.002 (-0.006 to +0.001), removed norm set / random 0.14 / 0.16; descr: set -0.001, random -0.002, difference +0.001 (-0.002 to +0.004), removed norm set / random 0.11 / 0.15

## llama-3.2-1B-IT-k128

Final token (frame A1): relative reconstruction error 0.195; splice mean |dS| 0.076; pair difference captured R2 moral -0.14 (cos 0.47), norm -0.28 (cos 0.44), descr -0.22 (cos 0.42)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.244; splice mean |dS| 0.114; pair difference captured R2 moral 0.28 (cos 0.61), norm 0.21 (cos 0.57), descr 0.22 (cos 0.57)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (163 features): mean activation A1/moral 0.0861, A1/norm 0.0782, A1/descr 0.0672, B/moral 0.0123, B/norm 0.0077, B/descr 0.0053
  ratio_A1_descr_over_moral: 0.78 (0.76 to 0.80) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (52 features): mean activation A1/moral 0.0131, A1/norm 0.0027, A1/descr 0.0012, B/moral 0.0098, B/norm 0.0064, B/descr 0.0049
  ratio_A1_descr_over_moral: 0.09 (0.06 to 0.13) -> content-driven
  ratio_A1_norm_over_moral: 0.21 (0.16 to 0.26) -> content-driven
H6 frame A1: 463 features tested; moral vs norm at full size: 98 significant; equalised group size 46: moral vs norm 34.8, norm vs norm 1.6, 6.5, 6.8 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 970 features tested; moral vs norm at full size: 130 significant; equalised group size 46: moral vs norm 17.2, norm vs norm 7.3, 17.8, 20.9 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.338, random -0.173, difference -0.165 (-0.219 to -0.114), removed norm set / random 3.29 / 1.85; norm: set -0.270, random -0.123, difference -0.148 (-0.174 to -0.121), removed norm set / random 3.03 / 1.88; descr: set -0.133, random -0.168, difference +0.035 (-0.002 to +0.073), removed norm set / random 2.77 / 2.03
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.005, random -0.002, difference +0.006 (+0.001 to +0.012), removed norm set / random 0.36 / 0.18; norm: set -0.000, random +0.001, difference -0.002 (-0.004 to +0.001), removed norm set / random 0.11 / 0.17; descr: set -0.000, random -0.002, difference +0.001 (-0.001 to +0.004), removed norm set / random 0.07 / 0.22
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.080, random -0.024, difference -0.056 (-0.073 to -0.040), removed norm set / random 0.78 / 0.62; norm: set -0.062, random -0.015, difference -0.047 (-0.064 to -0.031), removed norm set / random 0.58 / 0.59; descr: set -0.033, random -0.010, difference -0.023 (-0.033 to -0.013), removed norm set / random 0.48 / 0.59
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.055, random -0.002, difference -0.053 (-0.070 to -0.038), removed norm set / random 0.37 / 0.28; norm: set -0.049, random -0.001, difference -0.048 (-0.064 to -0.034), removed norm set / random 0.30 / 0.27; descr: set -0.023, random -0.002, difference -0.021 (-0.030 to -0.013), removed norm set / random 0.25 / 0.24

## llama-3.2-1B-base

Final token (frame A1): relative reconstruction error 0.209; splice mean |dS| 0.088; pair difference captured R2 moral -0.21 (cos 0.38), norm -0.25 (cos 0.36), descr -0.23 (cos 0.37)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.253; splice mean |dS| 0.077; pair difference captured R2 moral 0.11 (cos 0.48), norm 0.11 (cos 0.48), descr 0.09 (cos 0.47)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (91 features): mean activation A1/moral 0.1187, A1/norm 0.1075, A1/descr 0.0828, B/moral 0.0271, B/norm 0.0212, B/descr 0.0065
  ratio_A1_descr_over_moral: 0.70 (0.68 to 0.72) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (32 features): mean activation A1/moral 0.0180, A1/norm 0.0081, A1/descr 0.0022, B/moral 0.0188, B/norm 0.0147, B/descr 0.0091
  ratio_A1_descr_over_moral: 0.12 (0.07 to 0.17) -> content-driven
  ratio_A1_norm_over_moral: 0.45 (0.36 to 0.56) -> inconclusive
H6 frame A1: 232 features tested; moral vs norm at full size: 41 significant; equalised group size 46: moral vs norm 16.4, norm vs norm 0.6, 3.8, 6.2 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 465 features tested; moral vs norm at full size: 58 significant; equalised group size 46: moral vs norm 5.4, norm vs norm 9.2, 2.2, 9.2 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.226, random -0.245, difference +0.019 (-0.008 to +0.046), removed norm set / random 3.15 / 1.63; norm: set -0.198, random -0.185, difference -0.013 (-0.044 to +0.019), removed norm set / random 2.93 / 1.77; descr: set -0.132, random -0.204, difference +0.072 (+0.032 to +0.113), removed norm set / random 2.51 / 1.83
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.017, random -0.000, difference -0.017 (-0.023 to -0.011), removed norm set / random 0.35 / 0.22; norm: set -0.006, random +0.002, difference -0.008 (-0.011 to -0.006), removed norm set / random 0.19 / 0.21; descr: set -0.004, random +0.002, difference -0.006 (-0.009 to -0.004), removed norm set / random 0.08 / 0.26
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.057, random -0.022, difference -0.035 (-0.047 to -0.023), removed norm set / random 1.31 / 0.83; norm: set -0.046, random -0.028, difference -0.018 (-0.029 to -0.008), removed norm set / random 1.20 / 0.82; descr: set -0.017, random -0.020, difference +0.004 (-0.006 to +0.013), removed norm set / random 0.42 / 0.82
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.013, random -0.007, difference -0.006 (-0.010 to -0.001), removed norm set / random 0.51 / 0.49; norm: set -0.010, random -0.009, difference -0.001 (-0.006 to +0.004), removed norm set / random 0.44 / 0.46; descr: set -0.014, random -0.007, difference -0.007 (-0.011 to -0.003), removed norm set / random 0.29 / 0.39

## llama-3.2-1B-base-MLP0

Final token (frame A1): relative reconstruction error 0.192; splice mean |dS| 0.052; pair difference captured R2 moral -1.19 (cos 0.20), norm -2.15 (cos 0.19), descr -1.27 (cos 0.19)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.039; splice mean |dS| 0.003; pair difference captured R2 moral 0.32 (cos 0.63), norm 0.36 (cos 0.64), descr 0.42 (cos 0.66)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (80 features): mean activation A1/moral 0.0775, A1/norm 0.0771, A1/descr 0.0769, B/moral 0.0009, B/norm 0.0010, B/descr 0.0009
  ratio_A1_descr_over_moral: 0.99 (0.99 to 1.00) -> frame-driven
  ratio_A1_norm_over_moral: 0.99 (0.99 to 1.00) -> frame-driven
H5 original_vs_norm_sig (16 features): mean activation A1/moral 0.0096, A1/norm 0.0077, A1/descr 0.0069, B/moral 0.0082, B/norm 0.0084, B/descr 0.0110
  ratio_A1_descr_over_moral: 0.71 (0.62 to 0.83) -> frame-driven
  ratio_A1_norm_over_moral: 0.80 (0.71 to 0.90) -> frame-driven
H6 frame A1: 107 features tested; moral vs norm at full size: 0 significant; equalised group size 46: moral vs norm 0.3, norm vs norm 0.0, 0.6, 0.2 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 176 features tested; moral vs norm at full size: 0 significant; equalised group size 46: moral vs norm 0.1, norm vs norm 0.8, 0.1, 0.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.039, random -0.232, difference +0.271 (+0.211 to +0.329), removed norm set / random 1.30 / 0.65; norm: set +0.037, random -0.129, difference +0.166 (+0.127 to +0.206), removed norm set / random 1.30 / 0.65; descr: set +0.066, random -0.113, difference +0.178 (+0.125 to +0.233), removed norm set / random 1.29 / 0.65
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.003, random +0.002, difference -0.005 (-0.007 to -0.003), removed norm set / random 0.08 / 0.08; norm: set -0.002, random +0.001, difference -0.003 (-0.004 to -0.001), removed norm set / random 0.08 / 0.08; descr: set -0.001, random +0.002, difference -0.003 (-0.005 to -0.001), removed norm set / random 0.07 / 0.08
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.06; norm: set -0.000, random +0.000, difference -0.001 (-0.002 to +0.000), removed norm set / random 0.05 / 0.06; descr: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.04
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random -0.001, difference +0.001 (-0.001 to +0.002), removed norm set / random 0.12 / 0.13; norm: set -0.001, random +0.000, difference -0.001 (-0.003 to +0.001), removed norm set / random 0.12 / 0.13; descr: set +0.001, random -0.001, difference +0.001 (-0.000 to +0.003), removed norm set / random 0.16 / 0.12

## llama-3.2-1B-base-k128

Final token (frame A1): relative reconstruction error 0.166; splice mean |dS| 0.063; pair difference captured R2 moral -0.16 (cos 0.46), norm -0.23 (cos 0.45), descr -0.16 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.206; splice mean |dS| 0.073; pair difference captured R2 moral 0.22 (cos 0.57), norm 0.21 (cos 0.57), descr 0.21 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (175 features): mean activation A1/moral 0.0835, A1/norm 0.0766, A1/descr 0.0606, B/moral 0.0144, B/norm 0.0112, B/descr 0.0070
  ratio_A1_descr_over_moral: 0.73 (0.71 to 0.75) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.89 to 0.94) -> frame-driven
H5 original_vs_norm_sig (66 features): mean activation A1/moral 0.0185, A1/norm 0.0071, A1/descr 0.0021, B/moral 0.0130, B/norm 0.0097, B/descr 0.0074
  ratio_A1_descr_over_moral: 0.11 (0.08 to 0.15) -> content-driven
  ratio_A1_norm_over_moral: 0.38 (0.32 to 0.45) -> content-driven
H6 frame A1: 470 features tested; moral vs norm at full size: 79 significant; equalised group size 46: moral vs norm 24.6, norm vs norm 2.9, 10.8, 5.6 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 911 features tested; moral vs norm at full size: 77 significant; equalised group size 46: moral vs norm 15.9, norm vs norm 8.6, 12.8, 19.4 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.356, random -0.231, difference -0.126 (-0.159 to -0.094), removed norm set / random 3.17 / 1.82; norm: set -0.277, random -0.156, difference -0.121 (-0.156 to -0.084), removed norm set / random 3.00 / 1.90; descr: set -0.161, random -0.167, difference +0.005 (-0.040 to +0.051), removed norm set / random 2.56 / 2.02
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.015, random +0.003, difference -0.018 (-0.024 to -0.014), removed norm set / random 0.46 / 0.27; norm: set -0.004, random +0.003, difference -0.007 (-0.010 to -0.005), removed norm set / random 0.25 / 0.30; descr: set -0.004, random -0.000, difference -0.004 (-0.007 to -0.002), removed norm set / random 0.13 / 0.34
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.040, random -0.021, difference -0.019 (-0.029 to -0.010), removed norm set / random 0.90 / 0.76; norm: set -0.044, random -0.017, difference -0.027 (-0.036 to -0.018), removed norm set / random 0.74 / 0.70; descr: set -0.019, random -0.005, difference -0.014 (-0.022 to -0.007), removed norm set / random 0.53 / 0.67
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.004, random -0.006, difference +0.003 (-0.002 to +0.007), removed norm set / random 0.54 / 0.48; norm: set -0.005, random -0.007, difference +0.002 (-0.002 to +0.006), removed norm set / random 0.46 / 0.47; descr: set -0.016, random -0.008, difference -0.008 (-0.013 to -0.004), removed norm set / random 0.34 / 0.40

## llama-3.2-3B-IT-L19

Final token (frame A1): relative reconstruction error 0.126; splice mean |dS| 0.133; pair difference captured R2 moral 0.45 (cos 0.70), norm 0.32 (cos 0.64), descr 0.37 (cos 0.67)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.181; splice mean |dS| 0.060; pair difference captured R2 moral 0.49 (cos 0.73), norm 0.47 (cos 0.71), descr 0.51 (cos 0.73)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (153 features): mean activation A1/moral 0.5187, A1/norm 0.5080, A1/descr 0.4781, B/moral 0.1700, B/norm 0.1305, B/descr 0.0715
  ratio_A1_descr_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
  ratio_A1_norm_over_moral: 0.98 (0.97 to 0.99) -> frame-driven
H5 original_vs_norm_sig (49 features): mean activation A1/moral 0.2337, A1/norm 0.1998, A1/descr 0.1683, B/moral 0.1325, B/norm 0.1067, B/descr 0.1028
  ratio_A1_descr_over_moral: 0.72 (0.68 to 0.76) -> frame-driven
  ratio_A1_norm_over_moral: 0.85 (0.81 to 0.90) -> frame-driven
H6 frame A1: 387 features tested; moral vs norm at full size: 116 significant; equalised group size 46: moral vs norm 54.9, norm vs norm 8.3, 14.6, 37.2 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 876 features tested; moral vs norm at full size: 243 significant; equalised group size 46: moral vs norm 70.8, norm vs norm 43.9, 54.9, 85.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.055, random -0.344, difference +0.289 (+0.239 to +0.340), removed norm set / random 18.32 / 11.11; norm: set -0.026, random -0.312, difference +0.286 (+0.244 to +0.329), removed norm set / random 18.15 / 10.70; descr: set +0.085, random -0.257, difference +0.342 (+0.280 to +0.407), removed norm set / random 17.78 / 11.40
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.061, random -0.010, difference -0.051 (-0.072 to -0.031), removed norm set / random 3.75 / 3.14; norm: set +0.002, random -0.020, difference +0.022 (+0.005 to +0.040), removed norm set / random 3.26 / 3.13; descr: set -0.001, random -0.013, difference +0.012 (-0.005 to +0.031), removed norm set / random 3.03 / 3.26
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.310, random -0.094, difference -0.217 (-0.253 to -0.180), removed norm set / random 7.85 / 5.43; norm: set -0.283, random -0.090, difference -0.192 (-0.226 to -0.159), removed norm set / random 6.45 / 5.49; descr: set -0.249, random -0.061, difference -0.188 (-0.232 to -0.143), removed norm set / random 4.53 / 5.48
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.143, random -0.029, difference -0.114 (-0.138 to -0.091), removed norm set / random 3.67 / 2.62; norm: set -0.233, random -0.006, difference -0.227 (-0.259 to -0.194), removed norm set / random 3.52 / 2.44; descr: set -0.217, random +0.000, difference -0.217 (-0.265 to -0.170), removed norm set / random 3.58 / 2.17

## llama-3.2-3B-IT-L3

Final token (frame A1): relative reconstruction error 0.162; splice mean |dS| 0.025; pair difference captured R2 moral 0.02 (cos 0.42), norm -0.05 (cos 0.41), descr -0.08 (cos 0.40)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.147; splice mean |dS| 0.018; pair difference captured R2 moral 0.27 (cos 0.57), norm 0.22 (cos 0.55), descr 0.21 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (171 features): mean activation A1/moral 0.0898, A1/norm 0.0870, A1/descr 0.0770, B/moral 0.0105, B/norm 0.0088, B/descr 0.0052
  ratio_A1_descr_over_moral: 0.86 (0.84 to 0.87) -> frame-driven
  ratio_A1_norm_over_moral: 0.97 (0.95 to 0.98) -> frame-driven
H5 original_vs_norm_sig (30 features): mean activation A1/moral 0.0074, A1/norm 0.0034, A1/descr 0.0028, B/moral 0.0076, B/norm 0.0018, B/descr 0.0017
  ratio_A1_descr_over_moral: 0.37 (0.27 to 0.50) -> inconclusive
  ratio_A1_norm_over_moral: 0.46 (0.33 to 0.62) -> inconclusive
H6 frame A1: 401 features tested; moral vs norm at full size: 6 significant; equalised group size 46: moral vs norm 1.1, norm vs norm 3.4, 0.1, 2.9 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 1014 features tested; moral vs norm at full size: 24 significant; equalised group size 46: moral vs norm 4.3, norm vs norm 3.7, 1.2, 1.1 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.302, random -0.499, difference +0.197 (+0.130 to +0.263), removed norm set / random 3.68 / 1.60; norm: set -0.195, random -0.371, difference +0.175 (+0.113 to +0.239), removed norm set / random 3.64 / 1.63; descr: set -0.118, random -0.073, difference -0.046 (-0.122 to +0.032), removed norm set / random 3.46 / 1.65
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.001, random -0.000, difference +0.001 (+0.000 to +0.003), removed norm set / random 0.14 / 0.09; norm: set +0.001, random -0.000, difference +0.001 (-0.000 to +0.001), removed norm set / random 0.07 / 0.10; descr: set +0.002, random -0.000, difference +0.002 (+0.001 to +0.004), removed norm set / random 0.08 / 0.09
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.000, random +0.001, difference -0.000 (-0.006 to +0.006), removed norm set / random 0.79 / 0.60; norm: set -0.002, random -0.007, difference +0.005 (+0.002 to +0.009), removed norm set / random 0.78 / 0.63; descr: set -0.001, random -0.007, difference +0.006 (+0.002 to +0.011), removed norm set / random 0.51 / 0.54
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.002, random -0.000, difference -0.002 (-0.003 to -0.000), removed norm set / random 0.15 / 0.10; norm: set -0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.09; descr: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.06 / 0.10

## llama-3.2-3B-IT-L7

Final token (frame A1): relative reconstruction error 0.209; splice mean |dS| 0.042; pair difference captured R2 moral -0.09 (cos 0.41), norm -0.19 (cos 0.39), descr -0.23 (cos 0.37)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.277; splice mean |dS| 0.046; pair difference captured R2 moral 0.33 (cos 0.63), norm 0.27 (cos 0.59), descr 0.21 (cos 0.55)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (205 features): mean activation A1/moral 0.1162, A1/norm 0.1068, A1/descr 0.0891, B/moral 0.0038, B/norm 0.0019, B/descr 0.0020
  ratio_A1_descr_over_moral: 0.77 (0.75 to 0.79) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
H5 original_vs_norm_sig (62 features): mean activation A1/moral 0.0144, A1/norm 0.0079, A1/descr 0.0058, B/moral 0.0112, B/norm 0.0086, B/descr 0.0075
  ratio_A1_descr_over_moral: 0.40 (0.33 to 0.49) -> content-driven
  ratio_A1_norm_over_moral: 0.55 (0.48 to 0.64) -> inconclusive
H6 frame A1: 467 features tested; moral vs norm at full size: 56 significant; equalised group size 46: moral vs norm 17.0, norm vs norm 0.7, 3.7, 14.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1312 features tested; moral vs norm at full size: 148 significant; equalised group size 46: moral vs norm 18.9, norm vs norm 6.8, 15.5, 27.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.277, random -0.409, difference +0.132 (+0.051 to +0.211), removed norm set / random 5.28 / 2.74; norm: set -0.203, random -0.342, difference +0.140 (+0.091 to +0.191), removed norm set / random 5.03 / 2.84; descr: set -0.042, random -0.116, difference +0.074 (-0.011 to +0.162), removed norm set / random 4.66 / 3.06
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random +0.003, difference -0.003 (-0.005 to -0.001), removed norm set / random 0.47 / 0.36; norm: set -0.002, random +0.004, difference -0.005 (-0.007 to -0.004), removed norm set / random 0.34 / 0.36; descr: set -0.001, random +0.008, difference -0.009 (-0.011 to -0.007), removed norm set / random 0.32 / 0.38
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.008, random -0.001, difference -0.006 (-0.011 to -0.001), removed norm set / random 0.43 / 0.36; norm: set -0.003, random -0.000, difference -0.003 (-0.005 to -0.001), removed norm set / random 0.27 / 0.35; descr: set +0.000, random -0.002, difference +0.002 (-0.000 to +0.004), removed norm set / random 0.25 / 0.34
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.006, random -0.006, difference -0.000 (-0.003 to +0.002), removed norm set / random 0.46 / 0.43; norm: set -0.003, random -0.004, difference +0.001 (-0.002 to +0.003), removed norm set / random 0.38 / 0.41; descr: set -0.004, random -0.002, difference -0.001 (-0.004 to +0.001), removed norm set / random 0.38 / 0.35

## llama-3.2-3B-IT-k128

Final token (frame A1): relative reconstruction error 0.215; splice mean |dS| 0.073; pair difference captured R2 moral 0.02 (cos 0.45), norm -0.08 (cos 0.43), descr -0.07 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.297; splice mean |dS| 0.094; pair difference captured R2 moral 0.38 (cos 0.65), norm 0.34 (cos 0.63), descr 0.28 (cos 0.59)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (212 features): mean activation A1/moral 0.1347, A1/norm 0.1245, A1/descr 0.1093, B/moral 0.0253, B/norm 0.0184, B/descr 0.0172
  ratio_A1_descr_over_moral: 0.81 (0.79 to 0.83) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.91 to 0.94) -> frame-driven
H5 original_vs_norm_sig (97 features): mean activation A1/moral 0.0455, A1/norm 0.0241, A1/descr 0.0144, B/moral 0.0227, B/norm 0.0204, B/descr 0.0189
  ratio_A1_descr_over_moral: 0.32 (0.29 to 0.35) -> content-driven
  ratio_A1_norm_over_moral: 0.53 (0.49 to 0.57) -> inconclusive
H6 frame A1: 575 features tested; moral vs norm at full size: 164 significant; equalised group size 46: moral vs norm 54.4, norm vs norm 4.8, 3.9, 20.4 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1201 features tested; moral vs norm at full size: 145 significant; equalised group size 46: moral vs norm 29.7, norm vs norm 14.1, 4.0, 49.1 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.694, random -0.382, difference -0.312 (-0.366 to -0.257), removed norm set / random 6.07 / 3.96; norm: set -0.355, random -0.213, difference -0.142 (-0.181 to -0.103), removed norm set / random 5.86 / 3.84; descr: set -0.193, random -0.022, difference -0.171 (-0.232 to -0.108), removed norm set / random 5.51 / 4.01
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.025, random +0.009, difference -0.034 (-0.041 to -0.028), removed norm set / random 1.38 / 1.17; norm: set -0.009, random +0.018, difference -0.026 (-0.031 to -0.022), removed norm set / random 1.00 / 1.15; descr: set -0.015, random +0.018, difference -0.032 (-0.039 to -0.026), removed norm set / random 0.77 / 1.13
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.024, random -0.005, difference -0.019 (-0.038 to -0.001), removed norm set / random 1.82 / 1.60; norm: set -0.007, random -0.018, difference +0.011 (-0.005 to +0.027), removed norm set / random 1.41 / 1.55; descr: set -0.009, random -0.024, difference +0.015 (-0.000 to +0.030), removed norm set / random 1.36 / 1.45
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.032, random -0.008, difference -0.024 (-0.033 to -0.015), removed norm set / random 1.04 / 1.28; norm: set -0.032, random -0.018, difference -0.013 (-0.023 to -0.004), removed norm set / random 0.94 / 1.20; descr: set -0.029, random -0.018, difference -0.011 (-0.021 to -0.000), removed norm set / random 0.84 / 1.05

## llama-3.2-3B-base

Final token (frame A1): relative reconstruction error 0.252; splice mean |dS| 0.067; pair difference captured R2 moral -0.08 (cos 0.36), norm -0.15 (cos 0.35), descr -0.11 (cos 0.38)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.322; splice mean |dS| 0.076; pair difference captured R2 moral 0.26 (cos 0.56), norm 0.22 (cos 0.53), descr 0.15 (cos 0.48)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (100 features): mean activation A1/moral 0.1865, A1/norm 0.1713, A1/descr 0.1401, B/moral 0.0272, B/norm 0.0200, B/descr 0.0057
  ratio_A1_descr_over_moral: 0.75 (0.73 to 0.78) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
H5 original_vs_norm_sig (56 features): mean activation A1/moral 0.0387, A1/norm 0.0191, A1/descr 0.0103, B/moral 0.0209, B/norm 0.0161, B/descr 0.0129
  ratio_A1_descr_over_moral: 0.27 (0.21 to 0.32) -> content-driven
  ratio_A1_norm_over_moral: 0.49 (0.43 to 0.57) -> inconclusive
H6 frame A1: 301 features tested; moral vs norm at full size: 73 significant; equalised group size 46: moral vs norm 23.8, norm vs norm 6.2, 5.3, 10.5 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 693 features tested; moral vs norm at full size: 79 significant; equalised group size 46: moral vs norm 17.6, norm vs norm 2.5, 3.6, 16.4 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.478, random -0.318, difference -0.160 (-0.196 to -0.123), removed norm set / random 5.67 / 2.92; norm: set -0.307, random -0.279, difference -0.029 (-0.047 to -0.011), removed norm set / random 5.32 / 2.90; descr: set -0.147, random -0.099, difference -0.048 (-0.090 to -0.008), removed norm set / random 4.68 / 3.06
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.003, random -0.001, difference +0.004 (-0.001 to +0.010), removed norm set / random 0.95 / 0.64; norm: set +0.008, random +0.000, difference +0.008 (+0.003 to +0.012), removed norm set / random 0.64 / 0.75; descr: set -0.006, random +0.006, difference -0.012 (-0.017 to -0.007), removed norm set / random 0.42 / 0.75
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.009, random -0.010, difference +0.001 (-0.010 to +0.012), removed norm set / random 1.71 / 0.90; norm: set -0.001, random -0.008, difference +0.007 (-0.002 to +0.016), removed norm set / random 1.52 / 0.92; descr: set -0.009, random -0.006, difference -0.003 (-0.008 to +0.003), removed norm set / random 0.59 / 0.75
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.018, random -0.004, difference -0.013 (-0.019 to -0.008), removed norm set / random 0.73 / 0.83; norm: set -0.008, random -0.004, difference -0.004 (-0.009 to +0.000), removed norm set / random 0.61 / 0.80; descr: set -0.013, random -0.005, difference -0.008 (-0.013 to -0.003), removed norm set / random 0.51 / 0.64

## llama-3.2-3B-base-k128

Final token (frame A1): relative reconstruction error 0.213; splice mean |dS| 0.060; pair difference captured R2 moral -0.02 (cos 0.44), norm -0.04 (cos 0.43), descr 0.01 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.267; splice mean |dS| 0.071; pair difference captured R2 moral 0.35 (cos 0.63), norm 0.32 (cos 0.61), descr 0.26 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (222 features): mean activation A1/moral 0.1163, A1/norm 0.1032, A1/descr 0.0849, B/moral 0.0214, B/norm 0.0165, B/descr 0.0095
  ratio_A1_descr_over_moral: 0.73 (0.71 to 0.75) -> frame-driven
  ratio_A1_norm_over_moral: 0.89 (0.87 to 0.91) -> frame-driven
H5 original_vs_norm_sig (124 features): mean activation A1/moral 0.0296, A1/norm 0.0129, A1/descr 0.0079, B/moral 0.0130, B/norm 0.0129, B/descr 0.0139
  ratio_A1_descr_over_moral: 0.27 (0.23 to 0.31) -> content-driven
  ratio_A1_norm_over_moral: 0.43 (0.38 to 0.49) -> content-driven
H6 frame A1: 646 features tested; moral vs norm at full size: 164 significant; equalised group size 46: moral vs norm 52.6, norm vs norm 11.7, 21.2, 20.6 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1255 features tested; moral vs norm at full size: 144 significant; equalised group size 46: moral vs norm 27.3, norm vs norm 10.5, 14.5, 33.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.513, random -0.173, difference -0.340 (-0.383 to -0.297), removed norm set / random 5.74 / 3.10; norm: set -0.344, random -0.150, difference -0.194 (-0.222 to -0.164), removed norm set / random 5.37 / 3.19; descr: set -0.151, random +0.024, difference -0.174 (-0.219 to -0.131), removed norm set / random 4.74 / 3.43
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.012, random -0.002, difference -0.010 (-0.017 to -0.004), removed norm set / random 1.09 / 0.66; norm: set -0.003, random -0.005, difference +0.003 (-0.001 to +0.007), removed norm set / random 0.66 / 0.78; descr: set -0.002, random -0.009, difference +0.007 (+0.002 to +0.012), removed norm set / random 0.50 / 0.89
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.006, random -0.012, difference +0.006 (-0.004 to +0.017), removed norm set / random 2.01 / 1.46; norm: set +0.004, random -0.007, difference +0.011 (+0.001 to +0.022), removed norm set / random 1.78 / 1.41; descr: set -0.007, random -0.007, difference -0.000 (-0.007 to +0.007), removed norm set / random 1.03 / 1.21
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.022, random -0.010, difference -0.012 (-0.018 to -0.006), removed norm set / random 0.74 / 0.91; norm: set -0.012, random -0.009, difference -0.003 (-0.009 to +0.002), removed norm set / random 0.81 / 0.88; descr: set -0.013, random -0.002, difference -0.011 (-0.018 to -0.004), removed norm set / random 0.79 / 0.71

## qwen-2.5-7b-IT

Final token (frame A1): relative reconstruction error 0.148; splice mean |dS| 0.022; pair difference captured R2 moral -0.09 (cos 0.48), norm -0.20 (cos 0.44), descr 0.12 (cos 0.52)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.036; splice mean |dS| 0.005; pair difference captured R2 moral 0.32 (cos 0.60), norm 0.38 (cos 0.64), descr 0.45 (cos 0.68)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (154 features): mean activation A1/moral 0.4660, A1/norm 0.4587, A1/descr 0.4582, B/moral 0.0283, B/norm 0.0282, B/descr 0.0290
  ratio_A1_descr_over_moral: 0.98 (0.98 to 0.99) -> frame-driven
  ratio_A1_norm_over_moral: 0.98 (0.98 to 0.99) -> frame-driven
H5 original_vs_norm_sig (21 features): mean activation A1/moral 0.0519, A1/norm 0.0214, A1/descr 0.0158, B/moral 0.0218, B/norm 0.0192, B/descr 0.0210
  ratio_A1_descr_over_moral: 0.31 (0.22 to 0.40) -> content-driven
  ratio_A1_norm_over_moral: 0.41 (0.32 to 0.52) -> inconclusive
H6 frame A1: 292 features tested; moral vs norm at full size: 2 significant; equalised group size 46: moral vs norm 0.5, norm vs norm 0.0, 0.0, 0.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 888 features tested; moral vs norm at full size: 2 significant; equalised group size 46: moral vs norm 0.1, norm vs norm 0.1, 0.1, 0.0 -> moral vs norm yields more features than any split of the norm kinds
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.695, random -0.976, difference +0.281 (+0.173 to +0.390), removed norm set / random 10.27 / 6.68; norm: set -0.489, random -0.702, difference +0.213 (+0.132 to +0.293), removed norm set / random 10.16 / 6.55; descr: set -0.317, random -0.338, difference +0.021 (-0.076 to +0.126), removed norm set / random 10.17 / 6.68
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random +0.000, difference -0.001 (-0.002 to +0.000), removed norm set / random 0.61 / 0.43; norm: set -0.000, random +0.000, difference -0.001 (-0.001 to +0.000), removed norm set / random 0.32 / 0.45; descr: set +0.000, random +0.001, difference -0.000 (-0.001 to +0.001), removed norm set / random 0.31 / 0.43
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.009, random -0.004, difference -0.006 (-0.013 to +0.003), removed norm set / random 2.94 / 1.71; norm: set -0.005, random -0.003, difference -0.002 (-0.008 to +0.006), removed norm set / random 2.94 / 1.73; descr: set +0.001, random -0.002, difference +0.004 (-0.002 to +0.010), removed norm set / random 3.01 / 1.76
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.32 / 0.35; norm: set +0.000, random -0.000, difference +0.000 (-0.001 to +0.001), removed norm set / random 0.30 / 0.37; descr: set -0.001, random +0.000, difference -0.001 (-0.001 to -0.000), removed norm set / random 0.36 / 0.38

## qwen-2.5-7b-base

Final token (frame A1): relative reconstruction error 0.144; splice mean |dS| 0.012; pair difference captured R2 moral -0.07 (cos 0.49), norm -0.12 (cos 0.45), descr 0.12 (cos 0.52)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.036; splice mean |dS| 0.004; pair difference captured R2 moral 0.30 (cos 0.59), norm 0.38 (cos 0.64), descr 0.46 (cos 0.68)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (153 features): mean activation A1/moral 0.4811, A1/norm 0.4670, A1/descr 0.4713, B/moral 0.0207, B/norm 0.0210, B/descr 0.0209
  ratio_A1_descr_over_moral: 0.98 (0.97 to 0.99) -> frame-driven
  ratio_A1_norm_over_moral: 0.97 (0.96 to 0.98) -> frame-driven
H5 original_vs_norm_sig (22 features): mean activation A1/moral 0.0510, A1/norm 0.0230, A1/descr 0.0197, B/moral 0.0194, B/norm 0.0142, B/descr 0.0146
  ratio_A1_descr_over_moral: 0.39 (0.31 to 0.48) -> content-driven
  ratio_A1_norm_over_moral: 0.45 (0.36 to 0.57) -> inconclusive
H6 frame A1: 312 features tested; moral vs norm at full size: 2 significant; equalised group size 46: moral vs norm 0.1, norm vs norm 0.0, 0.0, 0.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 910 features tested; moral vs norm at full size: 1 significant; equalised group size 46: moral vs norm 0.1, norm vs norm 0.0, 0.0, 0.1 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.406, random -0.879, difference +0.473 (+0.396 to +0.550), removed norm set / random 10.79 / 6.48; norm: set -0.173, random -0.653, difference +0.480 (+0.419 to +0.539), removed norm set / random 10.59 / 6.41; descr: set +0.295, random -0.189, difference +0.484 (+0.391 to +0.575), removed norm set / random 10.66 / 6.58
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.002, random +0.000, difference +0.002 (+0.001 to +0.003), removed norm set / random 0.67 / 0.47; norm: set +0.001, random +0.000, difference +0.001 (+0.001 to +0.002), removed norm set / random 0.37 / 0.48; descr: set +0.001, random +0.000, difference +0.001 (+0.000 to +0.001), removed norm set / random 0.38 / 0.45
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.006, random -0.000, difference -0.005 (-0.008 to -0.003), removed norm set / random 2.33 / 1.14; norm: set -0.003, random -0.000, difference -0.003 (-0.008 to +0.000), removed norm set / random 2.34 / 1.15; descr: set +0.001, random -0.000, difference +0.001 (-0.002 to +0.005), removed norm set / random 2.36 / 1.23
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.000, difference -0.000 (-0.000 to +0.000), removed norm set / random 0.26 / 0.26; norm: set +0.000, random +0.000, difference +0.000 (-0.000 to +0.000), removed norm set / random 0.21 / 0.24; descr: set -0.000, random -0.000, difference -0.000 (-0.000 to +0.000), removed norm set / random 0.21 / 0.23

