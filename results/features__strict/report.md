# Feature results

**Sensitivity run (an option differs from the default; items: strict, 170 items): not the primary analysis.**
Runs folder: runs/features

## llama-3.1-8B-base

Final token (frame A1): relative reconstruction error 0.373; splice mean |dS| 0.108; pair difference captured R2 moral -0.05 (cos 0.22), norm -0.10 (cos 0.24), descr -0.09 (cos 0.25)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.466; splice mean |dS| 0.087; pair difference captured R2 moral 0.15 (cos 0.43), norm 0.11 (cos 0.40), descr 0.02 (cos 0.30)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (37 features): mean activation A1/moral 1.8174, A1/norm 1.7231, A1/descr 1.5647, B/moral 0.1987, B/norm 0.1808, B/descr 0.0209
  ratio_A1_descr_over_moral: 0.86 (0.83 to 0.89) -> frame-driven
  ratio_A1_norm_over_moral: 0.95 (0.93 to 0.97) -> frame-driven
H5 original_vs_norm_sig (18 features): mean activation A1/moral 0.2350, A1/norm 0.1184, A1/descr 0.0807, B/moral 0.1402, B/norm 0.2028, B/descr 0.2176
  ratio_A1_descr_over_moral: 0.34 (0.19 to 0.53) -> inconclusive
  ratio_A1_norm_over_moral: 0.50 (0.39 to 0.65) -> inconclusive
H6 frame A1: 108 features tested; moral vs norm at full size: 20 significant; equalised group size 37: moral vs norm 4.5, norm vs norm 0.0, 0.1, 8.4 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 301 features tested; moral vs norm at full size: 37 significant; equalised group size 37: moral vs norm 6.0, norm vs norm 1.4, 5.3, 9.9 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.317, random -0.057, difference -0.260 (-0.313 to -0.206), removed norm set / random 4.35 / 2.79; norm: set -0.213, random -0.014, difference -0.200 (-0.231 to -0.168), removed norm set / random 4.01 / 2.74; descr: set -0.049, random +0.062, difference -0.111 (-0.164 to -0.058), removed norm set / random 3.61 / 2.61
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.026, random +0.002, difference -0.028 (-0.035 to -0.021), removed norm set / random 0.47 / 0.34; norm: set -0.010, random +0.003, difference -0.014 (-0.017 to -0.010), removed norm set / random 0.31 / 0.46; descr: set -0.008, random -0.001, difference -0.006 (-0.015 to -0.000), removed norm set / random 0.21 / 0.46
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.005, random +0.002, difference -0.007 (-0.017 to +0.000), removed norm set / random 1.15 / 0.88; norm: set -0.002, random +0.007, difference -0.008 (-0.015 to -0.002), removed norm set / random 1.09 / 0.86; descr: set +0.000, random +0.007, difference -0.007 (-0.010 to -0.003), removed norm set / random 0.11 / 0.75
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set +0.004, random -0.001, difference +0.004 (-0.000 to +0.009), removed norm set / random 0.30 / 1.11; norm: set +0.008, random +0.001, difference +0.007 (+0.002 to +0.011), removed norm set / random 0.40 / 1.03; descr: set +0.002, random +0.001, difference +0.001 (-0.003 to +0.005), removed norm set / random 0.47 / 0.85

## llama-3.2-1B-IT

Final token (frame A1): relative reconstruction error 0.233; splice mean |dS| 0.090; pair difference captured R2 moral -0.19 (cos 0.38), norm -0.24 (cos 0.36), descr -0.30 (cos 0.36)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.292; splice mean |dS| 0.154; pair difference captured R2 moral 0.18 (cos 0.53), norm 0.14 (cos 0.50), descr 0.09 (cos 0.47)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (86 features): mean activation A1/moral 0.1268, A1/norm 0.1149, A1/descr 0.1023, B/moral 0.0108, B/norm 0.0042, B/descr 0.0031
  ratio_A1_descr_over_moral: 0.81 (0.78 to 0.84) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (20 features): mean activation A1/moral 0.0446, A1/norm 0.0213, A1/descr 0.0150, B/moral 0.0141, B/norm 0.0073, B/descr 0.0079
  ratio_A1_descr_over_moral: 0.34 (0.24 to 0.43) -> content-driven
  ratio_A1_norm_over_moral: 0.48 (0.42 to 0.54) -> inconclusive
H6 frame A1: 214 features tested; moral vs norm at full size: 40 significant; equalised group size 37: moral vs norm 8.2, norm vs norm 0.0, 0.0, 0.6 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 442 features tested; moral vs norm at full size: 49 significant; equalised group size 37: moral vs norm 7.5, norm vs norm 3.0, 1.4, 8.7 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.233, random -0.198, difference -0.035 (-0.080 to +0.010), removed norm set / random 3.36 / 1.70; norm: set -0.230, random -0.162, difference -0.068 (-0.097 to -0.038), removed norm set / random 3.07 / 1.77; descr: set -0.095, random -0.134, difference +0.039 (+0.008 to +0.072), removed norm set / random 2.89 / 1.85
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.006, random +0.007, difference -0.002 (-0.009 to +0.006), removed norm set / random 0.57 / 0.34; norm: set -0.008, random +0.006, difference -0.013 (-0.018 to -0.009), removed norm set / random 0.33 / 0.36; descr: set -0.005, random +0.003, difference -0.009 (-0.015 to -0.002), removed norm set / random 0.26 / 0.36
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.041, random -0.006, difference -0.036 (-0.057 to -0.016), removed norm set / random 0.61 / 0.33; norm: set -0.016, random -0.005, difference -0.011 (-0.017 to -0.005), removed norm set / random 0.27 / 0.34; descr: set -0.004, random -0.000, difference -0.004 (-0.010 to +0.002), removed norm set / random 0.22 / 0.41
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.011, random -0.001, difference -0.010 (-0.016 to -0.004), removed norm set / random 0.27 / 0.18; norm: set -0.003, random -0.001, difference -0.002 (-0.005 to +0.001), removed norm set / random 0.12 / 0.16; descr: set -0.000, random -0.001, difference +0.001 (-0.003 to +0.006), removed norm set / random 0.16 / 0.13

## llama-3.2-1B-IT-k128

Final token (frame A1): relative reconstruction error 0.193; splice mean |dS| 0.080; pair difference captured R2 moral -0.15 (cos 0.47), norm -0.26 (cos 0.44), descr -0.21 (cos 0.42)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.243; splice mean |dS| 0.119; pair difference captured R2 moral 0.28 (cos 0.61), norm 0.22 (cos 0.58), descr 0.20 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (163 features): mean activation A1/moral 0.0863, A1/norm 0.0781, A1/descr 0.0682, B/moral 0.0121, B/norm 0.0078, B/descr 0.0056
  ratio_A1_descr_over_moral: 0.79 (0.76 to 0.82) -> frame-driven
  ratio_A1_norm_over_moral: 0.90 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (52 features): mean activation A1/moral 0.0131, A1/norm 0.0028, A1/descr 0.0015, B/moral 0.0094, B/norm 0.0066, B/descr 0.0053
  ratio_A1_descr_over_moral: 0.12 (0.06 to 0.17) -> content-driven
  ratio_A1_norm_over_moral: 0.21 (0.16 to 0.27) -> content-driven
H6 frame A1: 441 features tested; moral vs norm at full size: 64 significant; equalised group size 37: moral vs norm 19.4, norm vs norm 1.1, 1.4, 5.7 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 887 features tested; moral vs norm at full size: 85 significant; equalised group size 37: moral vs norm 10.3, norm vs norm 4.7, 4.2, 22.2 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.290, random -0.154, difference -0.137 (-0.194 to -0.082), removed norm set / random 3.29 / 1.85; norm: set -0.237, random -0.113, difference -0.124 (-0.154 to -0.094), removed norm set / random 3.03 / 1.89; descr: set -0.112, random -0.123, difference +0.012 (-0.016 to +0.041), removed norm set / random 2.82 / 2.02
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.008, random -0.002, difference +0.009 (+0.004 to +0.015), removed norm set / random 0.37 / 0.18; norm: set +0.001, random +0.001, difference -0.001 (-0.003 to +0.002), removed norm set / random 0.12 / 0.17; descr: set -0.002, random -0.001, difference -0.001 (-0.003 to +0.002), removed norm set / random 0.07 / 0.23
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.057, random -0.020, difference -0.037 (-0.054 to -0.021), removed norm set / random 0.77 / 0.62; norm: set -0.060, random -0.015, difference -0.046 (-0.065 to -0.027), removed norm set / random 0.57 / 0.59; descr: set -0.029, random -0.009, difference -0.020 (-0.033 to -0.008), removed norm set / random 0.49 / 0.58
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.036, random -0.002, difference -0.034 (-0.048 to -0.020), removed norm set / random 0.36 / 0.28; norm: set -0.047, random -0.001, difference -0.046 (-0.064 to -0.031), removed norm set / random 0.29 / 0.27; descr: set -0.024, random -0.001, difference -0.023 (-0.035 to -0.011), removed norm set / random 0.26 / 0.25

## llama-3.2-1B-base

Final token (frame A1): relative reconstruction error 0.207; splice mean |dS| 0.092; pair difference captured R2 moral -0.21 (cos 0.38), norm -0.22 (cos 0.36), descr -0.25 (cos 0.39)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.253; splice mean |dS| 0.080; pair difference captured R2 moral 0.11 (cos 0.47), norm 0.12 (cos 0.49), descr 0.08 (cos 0.45)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (91 features): mean activation A1/moral 0.1183, A1/norm 0.1074, A1/descr 0.0826, B/moral 0.0268, B/norm 0.0214, B/descr 0.0063
  ratio_A1_descr_over_moral: 0.70 (0.67 to 0.73) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.88 to 0.93) -> frame-driven
H5 original_vs_norm_sig (32 features): mean activation A1/moral 0.0179, A1/norm 0.0077, A1/descr 0.0019, B/moral 0.0189, B/norm 0.0146, B/descr 0.0084
  ratio_A1_descr_over_moral: 0.11 (0.05 to 0.18) -> content-driven
  ratio_A1_norm_over_moral: 0.43 (0.34 to 0.55) -> inconclusive
H6 frame A1: 217 features tested; moral vs norm at full size: 35 significant; equalised group size 37: moral vs norm 9.1, norm vs norm 1.1, 0.7, 4.5 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 416 features tested; moral vs norm at full size: 46 significant; equalised group size 37: moral vs norm 2.8, norm vs norm 4.7, 2.2, 9.3 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.193, random -0.205, difference +0.012 (-0.015 to +0.040), removed norm set / random 3.13 / 1.63; norm: set -0.182, random -0.185, difference +0.003 (-0.027 to +0.033), removed norm set / random 2.94 / 1.77; descr: set -0.083, random -0.167, difference +0.084 (+0.032 to +0.140), removed norm set / random 2.51 / 1.79
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.013, random +0.000, difference -0.013 (-0.019 to -0.007), removed norm set / random 0.34 / 0.22; norm: set -0.005, random +0.002, difference -0.008 (-0.010 to -0.005), removed norm set / random 0.17 / 0.21; descr: set -0.002, random +0.003, difference -0.006 (-0.009 to -0.003), removed norm set / random 0.06 / 0.29
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.054, random -0.023, difference -0.031 (-0.044 to -0.018), removed norm set / random 1.30 / 0.82; norm: set -0.040, random -0.023, difference -0.018 (-0.029 to -0.007), removed norm set / random 1.19 / 0.83; descr: set -0.016, random -0.023, difference +0.007 (-0.007 to +0.021), removed norm set / random 0.41 / 0.81
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.012, random -0.008, difference -0.005 (-0.010 to -0.000), removed norm set / random 0.50 / 0.49; norm: set -0.009, random -0.007, difference -0.002 (-0.007 to +0.002), removed norm set / random 0.43 / 0.46; descr: set -0.013, random -0.008, difference -0.005 (-0.012 to +0.001), removed norm set / random 0.27 / 0.39

## llama-3.2-1B-base-MLP0

Final token (frame A1): relative reconstruction error 0.192; splice mean |dS| 0.053; pair difference captured R2 moral -1.17 (cos 0.20), norm -2.09 (cos 0.19), descr -1.05 (cos 0.21)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.040; splice mean |dS| 0.003; pair difference captured R2 moral 0.31 (cos 0.63), norm 0.37 (cos 0.65), descr 0.49 (cos 0.71)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (80 features): mean activation A1/moral 0.0775, A1/norm 0.0770, A1/descr 0.0769, B/moral 0.0009, B/norm 0.0009, B/descr 0.0009
  ratio_A1_descr_over_moral: 0.99 (0.99 to 1.00) -> frame-driven
  ratio_A1_norm_over_moral: 0.99 (0.99 to 1.00) -> frame-driven
H5 original_vs_norm_sig (16 features): mean activation A1/moral 0.0097, A1/norm 0.0078, A1/descr 0.0069, B/moral 0.0082, B/norm 0.0083, B/descr 0.0110
  ratio_A1_descr_over_moral: 0.72 (0.57 to 0.88) -> frame-driven
  ratio_A1_norm_over_moral: 0.81 (0.72 to 0.91) -> frame-driven
H6 frame A1: 104 features tested; moral vs norm at full size: 1 significant; equalised group size 37: moral vs norm 0.2, norm vs norm 0.0, 0.7, 0.3 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 170 features tested; moral vs norm at full size: 0 significant; equalised group size 37: moral vs norm 0.3, norm vs norm 0.8, 0.0, 0.9 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.035, random -0.190, difference +0.225 (+0.170 to +0.282), removed norm set / random 1.30 / 0.65; norm: set +0.034, random -0.123, difference +0.157 (+0.114 to +0.199), removed norm set / random 1.30 / 0.65; descr: set +0.046, random -0.113, difference +0.159 (+0.058 to +0.260), removed norm set / random 1.29 / 0.65
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.003, random +0.002, difference -0.005 (-0.007 to -0.003), removed norm set / random 0.08 / 0.08; norm: set -0.001, random +0.001, difference -0.002 (-0.004 to -0.001), removed norm set / random 0.08 / 0.08; descr: set -0.000, random +0.002, difference -0.002 (-0.004 to -0.000), removed norm set / random 0.07 / 0.08
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set +0.000, random -0.000, difference +0.000 (+0.000 to +0.001), removed norm set / random 0.05 / 0.06; norm: set -0.000, random +0.000, difference -0.000 (-0.001 to +0.000), removed norm set / random 0.05 / 0.06; descr: set +0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.04
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.001, difference +0.001 (-0.000 to +0.003), removed norm set / random 0.12 / 0.13; norm: set -0.001, random +0.000, difference -0.002 (-0.004 to +0.000), removed norm set / random 0.12 / 0.13; descr: set +0.001, random -0.000, difference +0.001 (-0.001 to +0.003), removed norm set / random 0.16 / 0.12

## llama-3.2-1B-base-k128

Final token (frame A1): relative reconstruction error 0.164; splice mean |dS| 0.066; pair difference captured R2 moral -0.15 (cos 0.46), norm -0.21 (cos 0.45), descr -0.11 (cos 0.48)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.206; splice mean |dS| 0.077; pair difference captured R2 moral 0.22 (cos 0.57), norm 0.22 (cos 0.58), descr 0.20 (cos 0.55)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (175 features): mean activation A1/moral 0.0833, A1/norm 0.0765, A1/descr 0.0615, B/moral 0.0142, B/norm 0.0112, B/descr 0.0068
  ratio_A1_descr_over_moral: 0.74 (0.71 to 0.77) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.89 to 0.94) -> frame-driven
H5 original_vs_norm_sig (66 features): mean activation A1/moral 0.0183, A1/norm 0.0070, A1/descr 0.0024, B/moral 0.0130, B/norm 0.0097, B/descr 0.0073
  ratio_A1_descr_over_moral: 0.13 (0.09 to 0.18) -> content-driven
  ratio_A1_norm_over_moral: 0.38 (0.32 to 0.46) -> content-driven
H6 frame A1: 445 features tested; moral vs norm at full size: 59 significant; equalised group size 37: moral vs norm 12.3, norm vs norm 1.9, 4.7, 12.2 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 835 features tested; moral vs norm at full size: 61 significant; equalised group size 37: moral vs norm 10.8, norm vs norm 3.0, 7.3, 14.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.312, random -0.195, difference -0.117 (-0.150 to -0.085), removed norm set / random 3.16 / 1.82; norm: set -0.260, random -0.155, difference -0.105 (-0.142 to -0.068), removed norm set / random 3.00 / 1.90; descr: set -0.111, random -0.148, difference +0.037 (-0.015 to +0.095), removed norm set / random 2.58 / 1.99
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.014, random +0.003, difference -0.017 (-0.022 to -0.012), removed norm set / random 0.46 / 0.27; norm: set -0.004, random +0.003, difference -0.007 (-0.010 to -0.004), removed norm set / random 0.24 / 0.30; descr: set -0.004, random -0.002, difference -0.003 (-0.007 to +0.002), removed norm set / random 0.14 / 0.35
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.038, random -0.018, difference -0.020 (-0.031 to -0.011), removed norm set / random 0.88 / 0.76; norm: set -0.038, random -0.016, difference -0.023 (-0.031 to -0.014), removed norm set / random 0.73 / 0.70; descr: set -0.017, random -0.005, difference -0.012 (-0.024 to -0.000), removed norm set / random 0.51 / 0.66
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.003, random -0.007, difference +0.003 (-0.002 to +0.008), removed norm set / random 0.54 / 0.48; norm: set -0.005, random -0.006, difference +0.001 (-0.003 to +0.005), removed norm set / random 0.45 / 0.47; descr: set -0.012, random -0.009, difference -0.003 (-0.009 to +0.004), removed norm set / random 0.34 / 0.39

## llama-3.2-3B-IT-L19

Final token (frame A1): relative reconstruction error 0.125; splice mean |dS| 0.133; pair difference captured R2 moral 0.43 (cos 0.70), norm 0.35 (cos 0.65), descr 0.37 (cos 0.66)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.182; splice mean |dS| 0.062; pair difference captured R2 moral 0.49 (cos 0.73), norm 0.48 (cos 0.72), descr 0.51 (cos 0.73)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (153 features): mean activation A1/moral 0.5173, A1/norm 0.5065, A1/descr 0.4910, B/moral 0.1694, B/norm 0.1313, B/descr 0.0748
  ratio_A1_descr_over_moral: 0.95 (0.93 to 0.97) -> frame-driven
  ratio_A1_norm_over_moral: 0.98 (0.97 to 0.99) -> frame-driven
H5 original_vs_norm_sig (49 features): mean activation A1/moral 0.2299, A1/norm 0.1991, A1/descr 0.1746, B/moral 0.1299, B/norm 0.1061, B/descr 0.1016
  ratio_A1_descr_over_moral: 0.76 (0.71 to 0.82) -> frame-driven
  ratio_A1_norm_over_moral: 0.87 (0.82 to 0.91) -> frame-driven
H6 frame A1: 362 features tested; moral vs norm at full size: 99 significant; equalised group size 37: moral vs norm 38.4, norm vs norm 5.2, 14.6, 37.1 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 783 features tested; moral vs norm at full size: 188 significant; equalised group size 37: moral vs norm 53.5, norm vs norm 29.5, 36.5, 69.5 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.034, random -0.317, difference +0.283 (+0.232 to +0.335), removed norm set / random 18.27 / 11.12; norm: set -0.032, random -0.310, difference +0.278 (+0.230 to +0.326), removed norm set / random 18.14 / 10.66; descr: set +0.087, random -0.245, difference +0.332 (+0.232 to +0.436), removed norm set / random 17.98 / 11.43
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.053, random -0.009, difference -0.044 (-0.065 to -0.023), removed norm set / random 3.71 / 3.14; norm: set +0.005, random -0.022, difference +0.027 (+0.007 to +0.046), removed norm set / random 3.26 / 3.12; descr: set -0.009, random -0.012, difference +0.002 (-0.028 to +0.037), removed norm set / random 3.17 / 3.28
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.306, random -0.093, difference -0.213 (-0.253 to -0.174), removed norm set / random 7.82 / 5.44; norm: set -0.261, random -0.088, difference -0.173 (-0.208 to -0.137), removed norm set / random 6.44 / 5.48; descr: set -0.258, random -0.052, difference -0.206 (-0.273 to -0.140), removed norm set / random 4.75 / 5.32
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.140, random -0.028, difference -0.112 (-0.138 to -0.087), removed norm set / random 3.63 / 2.62; norm: set -0.214, random -0.006, difference -0.208 (-0.242 to -0.173), removed norm set / random 3.53 / 2.44; descr: set -0.236, random +0.001, difference -0.238 (-0.315 to -0.171), removed norm set / random 3.59 / 2.14

## llama-3.2-3B-IT-L3

Final token (frame A1): relative reconstruction error 0.161; splice mean |dS| 0.024; pair difference captured R2 moral 0.02 (cos 0.43), norm -0.04 (cos 0.42), descr -0.04 (cos 0.41)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.146; splice mean |dS| 0.018; pair difference captured R2 moral 0.27 (cos 0.57), norm 0.24 (cos 0.56), descr 0.26 (cos 0.58)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (171 features): mean activation A1/moral 0.0898, A1/norm 0.0871, A1/descr 0.0777, B/moral 0.0104, B/norm 0.0090, B/descr 0.0057
  ratio_A1_descr_over_moral: 0.87 (0.85 to 0.89) -> frame-driven
  ratio_A1_norm_over_moral: 0.97 (0.95 to 0.99) -> frame-driven
H5 original_vs_norm_sig (30 features): mean activation A1/moral 0.0078, A1/norm 0.0036, A1/descr 0.0032, B/moral 0.0075, B/norm 0.0019, B/descr 0.0018
  ratio_A1_descr_over_moral: 0.42 (0.28 to 0.58) -> inconclusive
  ratio_A1_norm_over_moral: 0.46 (0.32 to 0.64) -> inconclusive
H6 frame A1: 378 features tested; moral vs norm at full size: 9 significant; equalised group size 37: moral vs norm 1.4, norm vs norm 0.2, 0.0, 6.2 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 919 features tested; moral vs norm at full size: 15 significant; equalised group size 37: moral vs norm 1.2, norm vs norm 1.5, 1.9, 1.0 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.252, random -0.461, difference +0.208 (+0.138 to +0.279), removed norm set / random 3.67 / 1.59; norm: set -0.201, random -0.371, difference +0.170 (+0.096 to +0.241), removed norm set / random 3.65 / 1.63; descr: set -0.073, random -0.048, difference -0.026 (-0.128 to +0.083), removed norm set / random 3.47 / 1.61
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.001, random -0.000, difference +0.002 (+0.000 to +0.003), removed norm set / random 0.15 / 0.09; norm: set +0.001, random -0.000, difference +0.001 (-0.000 to +0.001), removed norm set / random 0.08 / 0.10; descr: set +0.003, random +0.000, difference +0.003 (+0.001 to +0.005), removed norm set / random 0.10 / 0.09
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.000, random +0.001, difference -0.001 (-0.008 to +0.006), removed norm set / random 0.78 / 0.60; norm: set -0.001, random -0.005, difference +0.004 (+0.001 to +0.008), removed norm set / random 0.78 / 0.62; descr: set +0.003, random -0.007, difference +0.009 (+0.001 to +0.019), removed norm set / random 0.55 / 0.54
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.002, random -0.000, difference -0.001 (-0.002 to -0.000), removed norm set / random 0.15 / 0.10; norm: set -0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.05 / 0.09; descr: set +0.000, random -0.000, difference +0.001 (-0.000 to +0.002), removed norm set / random 0.07 / 0.11

## llama-3.2-3B-IT-L7

Final token (frame A1): relative reconstruction error 0.208; splice mean |dS| 0.042; pair difference captured R2 moral -0.09 (cos 0.41), norm -0.18 (cos 0.40), descr -0.20 (cos 0.38)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.277; splice mean |dS| 0.042; pair difference captured R2 moral 0.33 (cos 0.63), norm 0.29 (cos 0.60), descr 0.22 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (205 features): mean activation A1/moral 0.1158, A1/norm 0.1064, A1/descr 0.0912, B/moral 0.0038, B/norm 0.0019, B/descr 0.0025
  ratio_A1_descr_over_moral: 0.79 (0.76 to 0.82) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
H5 original_vs_norm_sig (62 features): mean activation A1/moral 0.0142, A1/norm 0.0079, A1/descr 0.0061, B/moral 0.0111, B/norm 0.0085, B/descr 0.0081
  ratio_A1_descr_over_moral: 0.43 (0.33 to 0.56) -> inconclusive
  ratio_A1_norm_over_moral: 0.56 (0.47 to 0.66) -> inconclusive
H6 frame A1: 440 features tested; moral vs norm at full size: 40 significant; equalised group size 37: moral vs norm 6.2, norm vs norm 0.1, 0.3, 5.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1173 features tested; moral vs norm at full size: 111 significant; equalised group size 37: moral vs norm 11.8, norm vs norm 1.8, 8.3, 22.8 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.254, random -0.384, difference +0.130 (+0.044 to +0.211), removed norm set / random 5.26 / 2.74; norm: set -0.195, random -0.348, difference +0.154 (+0.096 to +0.212), removed norm set / random 5.03 / 2.84; descr: set -0.073, random -0.080, difference +0.007 (-0.127 to +0.154), removed norm set / random 4.71 / 3.00
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random +0.002, difference -0.003 (-0.005 to -0.001), removed norm set / random 0.46 / 0.36; norm: set -0.002, random +0.004, difference -0.005 (-0.007 to -0.004), removed norm set / random 0.34 / 0.36; descr: set -0.001, random +0.007, difference -0.008 (-0.010 to -0.005), removed norm set / random 0.33 / 0.38
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.008, random -0.002, difference -0.007 (-0.012 to -0.001), removed norm set / random 0.45 / 0.36; norm: set -0.002, random -0.000, difference -0.002 (-0.004 to +0.000), removed norm set / random 0.28 / 0.35; descr: set +0.000, random -0.001, difference +0.001 (-0.003 to +0.006), removed norm set / random 0.30 / 0.34
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.007, random -0.006, difference -0.001 (-0.005 to +0.002), removed norm set / random 0.44 / 0.43; norm: set -0.003, random -0.004, difference +0.001 (-0.002 to +0.004), removed norm set / random 0.38 / 0.41; descr: set -0.001, random -0.003, difference +0.001 (-0.002 to +0.004), removed norm set / random 0.39 / 0.34

## llama-3.2-3B-IT-k128

Final token (frame A1): relative reconstruction error 0.215; splice mean |dS| 0.070; pair difference captured R2 moral 0.02 (cos 0.45), norm -0.04 (cos 0.44), descr -0.07 (cos 0.46)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.295; splice mean |dS| 0.092; pair difference captured R2 moral 0.37 (cos 0.64), norm 0.35 (cos 0.64), descr 0.27 (cos 0.58)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (212 features): mean activation A1/moral 0.1345, A1/norm 0.1241, A1/descr 0.1125, B/moral 0.0248, B/norm 0.0182, B/descr 0.0173
  ratio_A1_descr_over_moral: 0.84 (0.80 to 0.87) -> frame-driven
  ratio_A1_norm_over_moral: 0.92 (0.90 to 0.94) -> frame-driven
H5 original_vs_norm_sig (97 features): mean activation A1/moral 0.0456, A1/norm 0.0240, A1/descr 0.0154, B/moral 0.0227, B/norm 0.0202, B/descr 0.0194
  ratio_A1_descr_over_moral: 0.34 (0.30 to 0.38) -> content-driven
  ratio_A1_norm_over_moral: 0.53 (0.48 to 0.58) -> inconclusive
H6 frame A1: 529 features tested; moral vs norm at full size: 130 significant; equalised group size 37: moral vs norm 42.1, norm vs norm 2.1, 3.5, 13.6 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1064 features tested; moral vs norm at full size: 118 significant; equalised group size 37: moral vs norm 18.7, norm vs norm 0.8, 0.4, 37.5 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.643, random -0.354, difference -0.289 (-0.348 to -0.230), removed norm set / random 6.07 / 3.95; norm: set -0.369, random -0.219, difference -0.150 (-0.195 to -0.106), removed norm set / random 5.84 / 3.84; descr: set -0.167, random +0.015, difference -0.182 (-0.276 to -0.089), removed norm set / random 5.59 / 3.94
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.025, random +0.009, difference -0.034 (-0.041 to -0.026), removed norm set / random 1.39 / 1.17; norm: set -0.008, random +0.017, difference -0.025 (-0.030 to -0.019), removed norm set / random 1.00 / 1.15; descr: set -0.015, random +0.017, difference -0.032 (-0.041 to -0.024), removed norm set / random 0.76 / 1.14
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.026, random -0.004, difference -0.022 (-0.043 to -0.002), removed norm set / random 1.81 / 1.59; norm: set -0.009, random -0.015, difference +0.006 (-0.009 to +0.021), removed norm set / random 1.40 / 1.57; descr: set -0.010, random -0.020, difference +0.010 (-0.015 to +0.036), removed norm set / random 1.34 / 1.39
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.031, random -0.007, difference -0.024 (-0.034 to -0.014), removed norm set / random 1.05 / 1.27; norm: set -0.033, random -0.016, difference -0.017 (-0.027 to -0.007), removed norm set / random 0.94 / 1.21; descr: set -0.027, random -0.025, difference -0.002 (-0.018 to +0.012), removed norm set / random 0.83 / 1.00

## llama-3.2-3B-base

Final token (frame A1): relative reconstruction error 0.250; splice mean |dS| 0.069; pair difference captured R2 moral -0.08 (cos 0.36), norm -0.12 (cos 0.35), descr -0.10 (cos 0.39)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.322; splice mean |dS| 0.075; pair difference captured R2 moral 0.26 (cos 0.57), norm 0.24 (cos 0.54), descr 0.14 (cos 0.47)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (100 features): mean activation A1/moral 0.1867, A1/norm 0.1703, A1/descr 0.1409, B/moral 0.0265, B/norm 0.0199, B/descr 0.0063
  ratio_A1_descr_over_moral: 0.75 (0.72 to 0.79) -> frame-driven
  ratio_A1_norm_over_moral: 0.91 (0.89 to 0.94) -> frame-driven
H5 original_vs_norm_sig (56 features): mean activation A1/moral 0.0389, A1/norm 0.0184, A1/descr 0.0101, B/moral 0.0202, B/norm 0.0156, B/descr 0.0154
  ratio_A1_descr_over_moral: 0.26 (0.20 to 0.33) -> content-driven
  ratio_A1_norm_over_moral: 0.47 (0.41 to 0.55) -> inconclusive
H6 frame A1: 278 features tested; moral vs norm at full size: 63 significant; equalised group size 37: moral vs norm 16.1, norm vs norm 0.2, 0.0, 3.5 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 601 features tested; moral vs norm at full size: 71 significant; equalised group size 37: moral vs norm 9.1, norm vs norm 0.4, 0.3, 13.6 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.452, random -0.289, difference -0.163 (-0.199 to -0.128), removed norm set / random 5.68 / 2.91; norm: set -0.295, random -0.274, difference -0.021 (-0.041 to -0.003), removed norm set / random 5.29 / 2.90; descr: set -0.141, random -0.067, difference -0.074 (-0.137 to -0.010), removed norm set / random 4.66 / 3.02
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.004, random +0.000, difference +0.004 (-0.002 to +0.010), removed norm set / random 0.95 / 0.63; norm: set +0.008, random -0.000, difference +0.008 (+0.003 to +0.013), removed norm set / random 0.63 / 0.75; descr: set -0.006, random +0.004, difference -0.010 (-0.017 to -0.004), removed norm set / random 0.41 / 0.74
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.011, random -0.008, difference -0.004 (-0.013 to +0.006), removed norm set / random 1.70 / 0.91; norm: set -0.001, random -0.008, difference +0.006 (-0.003 to +0.016), removed norm set / random 1.49 / 0.91; descr: set -0.004, random -0.006, difference +0.001 (-0.006 to +0.009), removed norm set / random 0.59 / 0.71
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.018, random -0.003, difference -0.015 (-0.021 to -0.010), removed norm set / random 0.71 / 0.83; norm: set -0.007, random -0.003, difference -0.003 (-0.008 to +0.002), removed norm set / random 0.59 / 0.80; descr: set -0.006, random -0.003, difference -0.003 (-0.010 to +0.003), removed norm set / random 0.57 / 0.58

## llama-3.2-3B-base-k128

Final token (frame A1): relative reconstruction error 0.211; splice mean |dS| 0.060; pair difference captured R2 moral -0.01 (cos 0.44), norm -0.03 (cos 0.43), descr 0.03 (cos 0.47)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.267; splice mean |dS| 0.069; pair difference captured R2 moral 0.35 (cos 0.64), norm 0.33 (cos 0.62), descr 0.26 (cos 0.56)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (222 features): mean activation A1/moral 0.1162, A1/norm 0.1027, A1/descr 0.0872, B/moral 0.0213, B/norm 0.0164, B/descr 0.0090
  ratio_A1_descr_over_moral: 0.75 (0.72 to 0.78) -> frame-driven
  ratio_A1_norm_over_moral: 0.88 (0.86 to 0.91) -> frame-driven
H5 original_vs_norm_sig (124 features): mean activation A1/moral 0.0295, A1/norm 0.0126, A1/descr 0.0098, B/moral 0.0129, B/norm 0.0128, B/descr 0.0133
  ratio_A1_descr_over_moral: 0.33 (0.27 to 0.39) -> content-driven
  ratio_A1_norm_over_moral: 0.43 (0.37 to 0.49) -> content-driven
H6 frame A1: 599 features tested; moral vs norm at full size: 126 significant; equalised group size 37: moral vs norm 36.0, norm vs norm 1.4, 6.3, 15.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 1094 features tested; moral vs norm at full size: 108 significant; equalised group size 37: moral vs norm 16.5, norm vs norm 3.1, 10.8, 33.0 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.478, random -0.162, difference -0.316 (-0.362 to -0.269), removed norm set / random 5.74 / 3.10; norm: set -0.333, random -0.154, difference -0.178 (-0.210 to -0.147), removed norm set / random 5.35 / 3.20; descr: set -0.133, random +0.038, difference -0.171 (-0.241 to -0.103), removed norm set / random 4.77 / 3.35
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.010, random -0.002, difference -0.008 (-0.015 to -0.002), removed norm set / random 1.08 / 0.65; norm: set -0.001, random -0.006, difference +0.005 (+0.000 to +0.009), removed norm set / random 0.64 / 0.79; descr: set -0.002, random -0.005, difference +0.003 (-0.004 to +0.011), removed norm set / random 0.58 / 0.89
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.007, random -0.010, difference +0.003 (-0.008 to +0.015), removed norm set / random 2.01 / 1.46; norm: set +0.004, random -0.007, difference +0.010 (+0.000 to +0.021), removed norm set / random 1.74 / 1.41; descr: set -0.007, random -0.008, difference +0.001 (-0.010 to +0.012), removed norm set / random 1.00 / 1.15
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.021, random -0.008, difference -0.013 (-0.019 to -0.008), removed norm set / random 0.73 / 0.91; norm: set -0.010, random -0.010, difference -0.001 (-0.006 to +0.004), removed norm set / random 0.80 / 0.88; descr: set -0.014, random -0.001, difference -0.013 (-0.026 to -0.003), removed norm set / random 0.80 / 0.68

## qwen-2.5-7b-IT

Final token (frame A1): relative reconstruction error 0.148; splice mean |dS| 0.020; pair difference captured R2 moral -0.09 (cos 0.49), norm -0.17 (cos 0.45), descr 0.14 (cos 0.52)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.036; splice mean |dS| 0.005; pair difference captured R2 moral 0.32 (cos 0.60), norm 0.39 (cos 0.65), descr 0.48 (cos 0.69)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (154 features): mean activation A1/moral 0.4662, A1/norm 0.4601, A1/descr 0.4595, B/moral 0.0282, B/norm 0.0282, B/descr 0.0284
  ratio_A1_descr_over_moral: 0.99 (0.97 to 1.00) -> frame-driven
  ratio_A1_norm_over_moral: 0.99 (0.98 to 1.00) -> frame-driven
H5 original_vs_norm_sig (21 features): mean activation A1/moral 0.0531, A1/norm 0.0206, A1/descr 0.0155, B/moral 0.0224, B/norm 0.0194, B/descr 0.0205
  ratio_A1_descr_over_moral: 0.29 (0.19 to 0.40) -> content-driven
  ratio_A1_norm_over_moral: 0.39 (0.30 to 0.50) -> content-driven
H6 frame A1: 283 features tested; moral vs norm at full size: 1 significant; equalised group size 37: moral vs norm 0.1, norm vs norm 0.0, 0.0, 0.0 -> moral vs norm yields more features than any split of the norm kinds
H6 frame B: 813 features tested; moral vs norm at full size: 0 significant; equalised group size 37: moral vs norm 0.0, norm vs norm 0.0, 0.1, 0.0 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.612, random -0.911, difference +0.298 (+0.184 to +0.418), removed norm set / random 10.28 / 6.66; norm: set -0.460, random -0.659, difference +0.198 (+0.106 to +0.290), removed norm set / random 10.19 / 6.54; descr: set -0.286, random -0.376, difference +0.090 (-0.022 to +0.215), removed norm set / random 10.19 / 6.70
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set -0.001, random +0.000, difference -0.001 (-0.002 to +0.000), removed norm set / random 0.63 / 0.43; norm: set -0.000, random +0.000, difference -0.000 (-0.001 to +0.001), removed norm set / random 0.32 / 0.45; descr: set -0.000, random +0.001, difference -0.001 (-0.002 to -0.000), removed norm set / random 0.31 / 0.43
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.008, random -0.004, difference -0.004 (-0.012 to +0.005), removed norm set / random 2.93 / 1.71; norm: set -0.006, random -0.004, difference -0.002 (-0.009 to +0.009), removed norm set / random 2.93 / 1.74; descr: set +0.002, random -0.003, difference +0.005 (-0.004 to +0.014), removed norm set / random 2.99 / 1.76
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.000, difference +0.000 (-0.000 to +0.001), removed norm set / random 0.32 / 0.35; norm: set +0.000, random -0.000, difference +0.000 (-0.001 to +0.002), removed norm set / random 0.30 / 0.37; descr: set -0.001, random +0.000, difference -0.001 (-0.002 to -0.000), removed norm set / random 0.35 / 0.38

## qwen-2.5-7b-base

Final token (frame A1): relative reconstruction error 0.143; splice mean |dS| 0.012; pair difference captured R2 moral -0.04 (cos 0.50), norm -0.13 (cos 0.46), descr 0.15 (cos 0.53)  **flagged: feature-level nulls are uninformative in this frame**
Final token (frame B): relative reconstruction error 0.036; splice mean |dS| 0.004; pair difference captured R2 moral 0.30 (cos 0.59), norm 0.39 (cos 0.65), descr 0.49 (cos 0.70)  **flagged: feature-level nulls are uninformative in this frame**

H5 original_vs_neutral_sig (153 features): mean activation A1/moral 0.4817, A1/norm 0.4678, A1/descr 0.4731, B/moral 0.0205, B/norm 0.0211, B/descr 0.0204
  ratio_A1_descr_over_moral: 0.98 (0.97 to 0.99) -> frame-driven
  ratio_A1_norm_over_moral: 0.97 (0.96 to 0.98) -> frame-driven
H5 original_vs_norm_sig (22 features): mean activation A1/moral 0.0514, A1/norm 0.0224, A1/descr 0.0202, B/moral 0.0193, B/norm 0.0142, B/descr 0.0151
  ratio_A1_descr_over_moral: 0.39 (0.30 to 0.51) -> inconclusive
  ratio_A1_norm_over_moral: 0.44 (0.33 to 0.56) -> inconclusive
H6 frame A1: 291 features tested; moral vs norm at full size: 1 significant; equalised group size 37: moral vs norm 0.1, norm vs norm 0.0, 0.0, 0.1 -> moral vs norm yields no more features than norm kinds among themselves
H6 frame B: 811 features tested; moral vs norm at full size: 0 significant; equalised group size 37: moral vs norm 0.1, norm vs norm 0.0, 0.0, 0.1 -> moral vs norm yields no more features than norm kinds among themselves
Ablation A1/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.372, random -0.844, difference +0.472 (+0.390 to +0.560), removed norm set / random 10.80 / 6.47; norm: set -0.191, random -0.657, difference +0.466 (+0.395 to +0.536), removed norm set / random 10.60 / 6.41; descr: set +0.264, random -0.195, difference +0.459 (+0.320 to +0.602), removed norm set / random 10.70 / 6.57
Ablation A1/original_vs_norm_sig (change of the behavioural gap): moral: set +0.002, random -0.000, difference +0.002 (+0.001 to +0.003), removed norm set / random 0.67 / 0.47; norm: set +0.001, random +0.000, difference +0.001 (+0.000 to +0.002), removed norm set / random 0.35 / 0.48; descr: set +0.001, random +0.000, difference +0.001 (-0.000 to +0.001), removed norm set / random 0.39 / 0.41
Ablation B/original_vs_neutral_sig (change of the behavioural gap): moral: set -0.005, random -0.000, difference -0.004 (-0.008 to -0.002), removed norm set / random 2.32 / 1.13; norm: set -0.004, random -0.000, difference -0.004 (-0.010 to +0.000), removed norm set / random 2.34 / 1.16; descr: set +0.001, random -0.000, difference +0.001 (-0.003 to +0.007), removed norm set / random 2.32 / 1.23
Ablation B/original_vs_norm_sig (change of the behavioural gap): moral: set -0.000, random -0.000, difference +0.000 (-0.000 to +0.000), removed norm set / random 0.26 / 0.26; norm: set +0.000, random +0.000, difference +0.000 (-0.000 to +0.000), removed norm set / random 0.21 / 0.24; descr: set -0.000, random -0.000, difference -0.000 (-0.001 to +0.000), removed norm set / random 0.21 / 0.23

