# Removal of the located heads, read on LD

Runs: runs/circuits_choice_word/ablation; positions: all; a pair is included when its gap in LD is at least 0.1; 2000 resamples of the pairs.

No check against the study's output was asked for (--check; possible with --readout S --include-on S).

## Per frame and kind of pair

| frame | pairs | models with enough pairs | median pairs included | located heads above every random set | median removed: located heads | median removed: random sets | left out |
|---|---|---|---|---|---|---|---|
| CW | moral | 14 of 14 | 80 | 3 of 14 | 0.071 | 0.052 | - |
| CW | norm | 14 of 14 | 106 | 3 of 14 | 0.063 | 0.056 | - |
| CW | descr | 14 of 14 | 40 | 3 of 14 | 0.069 | 0.056 | - |

## Per model

| model | frame | pairs | included | mean clean gap | removed by the located heads (95 % interval) | rank among random sets | random sets: mean / largest |
|---|---|---|---|---|---|---|---|
| Llama-3.2-1B | CW | moral | 80 of 80 | +4.892 | 0.053 [0.032, 0.073] | 10 of 20 | 0.085 / 0.490 |
| Llama-3.2-1B | CW | norm | 105 of 107 | +5.036 | -0.032 [-0.055, -0.009] | 18 of 20 | 0.089 / 0.454 |
| Llama-3.2-1B | CW | descr | 40 of 40 | +5.004 | -0.046 [-0.082, -0.011] | 18 of 20 | 0.088 / 0.494 |
| Llama-3.2-1B-Instruct | CW | moral | 80 of 80 | +7.011 | -0.178 [-0.204, -0.150] | 20 of 20 | 0.108 / 0.894 |
| Llama-3.2-1B-Instruct | CW | norm | 106 of 107 | +7.295 | -0.128 [-0.153, -0.103] | 20 of 20 | 0.110 / 0.881 |
| Llama-3.2-1B-Instruct | CW | descr | 40 of 40 | +8.121 | -0.176 [-0.209, -0.146] | 19 of 20 | 0.104 / 0.912 |
| gemma-2b | CW | moral | 79 of 80 | +6.278 | 0.993 [0.973, 1.014] | 0 of 20 | 0.341 / 0.883 |
| gemma-2b | CW | norm | 106 of 107 | +5.828 | 0.990 [0.971, 1.009] | 0 of 20 | 0.336 / 0.883 |
| gemma-2b | CW | descr | 40 of 40 | +6.524 | 1.002 [0.980, 1.023] | 0 of 20 | 0.335 / 0.863 |
| gemma-2b-it | CW | moral | 79 of 80 | +20.899 | 0.102 [0.073, 0.132] | 11 of 20 | 0.167 / 0.692 |
| gemma-2b-it | CW | norm | 105 of 107 | +20.035 | 0.055 [0.034, 0.074] | 15 of 20 | 0.196 / 0.747 |
| gemma-2b-it | CW | descr | 40 of 40 | +20.702 | 0.087 [0.062, 0.113] | 11 of 20 | 0.167 / 0.694 |
| Llama-3.2-3B | CW | moral | 79 of 80 | +6.441 | 0.064 [0.035, 0.089] | 10 of 20 | 0.163 / 0.660 |
| Llama-3.2-3B | CW | norm | 105 of 107 | +6.499 | 0.042 [0.019, 0.065] | 11 of 20 | 0.162 / 0.607 |
| Llama-3.2-3B | CW | descr | 40 of 40 | +4.893 | -0.212 [-0.268, -0.162] | 20 of 20 | 0.162 / 0.684 |
| Llama-3.2-3B-Instruct | CW | moral | 79 of 80 | +14.133 | -0.001 [-0.022, 0.019] | 16 of 20 | 0.051 / 0.194 |
| Llama-3.2-3B-Instruct | CW | norm | 105 of 107 | +12.356 | -0.013 [-0.030, 0.003] | 18 of 20 | 0.056 / 0.295 |
| Llama-3.2-3B-Instruct | CW | descr | 40 of 40 | +13.385 | -0.089 [-0.108, -0.070] | 19 of 20 | 0.052 / 0.255 |
| Qwen2.5-3B | CW | moral | 80 of 80 | +6.117 | 0.987 [0.965, 1.008] | 0 of 20 | 0.105 / 0.683 |
| Qwen2.5-3B | CW | norm | 106 of 107 | +5.803 | 0.986 [0.965, 1.006] | 0 of 20 | 0.105 / 0.662 |
| Qwen2.5-3B | CW | descr | 40 of 40 | +6.096 | 0.997 [0.954, 1.039] | 0 of 20 | 0.090 / 0.614 |
| Qwen2.5-3B-Instruct | CW | moral | 80 of 80 | +13.201 | 0.052 [0.025, 0.079] | 9 of 20 | 0.053 / 0.398 |
| Qwen2.5-3B-Instruct | CW | norm | 107 of 107 | +12.992 | 0.072 [0.048, 0.095] | 8 of 20 | 0.055 / 0.445 |
| Qwen2.5-3B-Instruct | CW | descr | 40 of 40 | +13.735 | 0.095 [0.069, 0.122] | 9 of 20 | 0.057 / 0.430 |
| Qwen2.5-7B | CW | moral | 80 of 80 | +9.448 | 0.077 [0.058, 0.097] | 1 of 20 | -0.011 / 0.120 |
| Qwen2.5-7B | CW | norm | 106 of 107 | +8.928 | 0.079 [0.059, 0.098] | 1 of 20 | -0.010 / 0.118 |
| Qwen2.5-7B | CW | descr | 40 of 40 | +8.892 | 0.061 [0.035, 0.086] | 2 of 20 | -0.013 / 0.118 |
| Qwen2.5-7B-Instruct | CW | moral | 80 of 80 | +19.557 | -0.034 [-0.059, -0.010] | 20 of 20 | 0.043 / 0.088 |
| Qwen2.5-7B-Instruct | CW | norm | 106 of 107 | +19.100 | -0.061 [-0.086, -0.036] | 20 of 20 | 0.048 / 0.103 |
| Qwen2.5-7B-Instruct | CW | descr | 40 of 40 | +19.188 | -0.097 [-0.141, -0.055] | 20 of 20 | 0.056 / 0.118 |
| Llama-3.1-8B | CW | moral | 80 of 80 | +6.496 | 0.153 [0.121, 0.185] | 1 of 20 | 0.039 / 0.261 |
| Llama-3.1-8B | CW | norm | 105 of 107 | +6.611 | 0.161 [0.135, 0.187] | 1 of 20 | 0.042 / 0.280 |
| Llama-3.1-8B | CW | descr | 40 of 40 | +6.055 | 0.077 [0.040, 0.113] | 5 of 20 | 0.043 / 0.291 |
| Llama-3.1-8B-Instruct | CW | moral | 80 of 80 | +10.451 | 0.103 [0.080, 0.127] | 1 of 20 | 0.017 / 0.184 |
| Llama-3.1-8B-Instruct | CW | norm | 106 of 107 | +10.255 | 0.109 [0.091, 0.129] | 1 of 20 | 0.024 / 0.215 |
| Llama-3.1-8B-Instruct | CW | descr | 40 of 40 | +10.616 | 0.077 [0.047, 0.108] | 2 of 20 | 0.022 / 0.198 |
| Qwen2.5-14B | CW | moral | 80 of 80 | +11.355 | 0.105 [0.093, 0.117] | 0 of 20 | 0.011 / 0.068 |
| Qwen2.5-14B | CW | norm | 106 of 107 | +10.651 | 0.094 [0.081, 0.109] | 0 of 20 | 0.010 / 0.076 |
| Qwen2.5-14B | CW | descr | 40 of 40 | +10.856 | 0.115 [0.099, 0.130] | 0 of 20 | 0.013 / 0.079 |
| Qwen2.5-14B-Instruct | CW | moral | 80 of 80 | +20.060 | -0.079 [-0.130, -0.033] | 20 of 20 | 0.005 / 0.064 |
| Qwen2.5-14B-Instruct | CW | norm | 107 of 107 | +19.416 | 0.015 [-0.021, 0.047] | 5 of 20 | 0.005 / 0.058 |
| Qwen2.5-14B-Instruct | CW | descr | 40 of 40 | +20.890 | 0.013 [-0.021, 0.051] | 7 of 20 | 0.006 / 0.063 |

\* fewer included pairs than the minimum; shown, not counted.
