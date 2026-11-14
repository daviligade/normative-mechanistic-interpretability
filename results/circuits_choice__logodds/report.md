# Removal of the located heads, read on LD

Runs: runs/circuits_choice/ablation; positions: all; a pair is included when its gap in LD is at least 0.1; 2000 resamples of the pairs.

No check against the study's output was asked for (--check; possible with --readout S --include-on S).

## Per frame and kind of pair

| frame | pairs | models with enough pairs | median pairs included | located heads above every random set | median removed: located heads | median removed: random sets | left out |
|---|---|---|---|---|---|---|---|
| CH | moral | 14 of 14 | 73 | 6 of 14 | 0.239 | 0.053 | - |
| CH | norm | 14 of 14 | 100 | 7 of 14 | 0.215 | 0.068 | - |
| CH | descr | 12 of 14 | 30 | 3 of 12 | 0.131 | 0.049 | Qwen2.5-3B, Qwen2.5-7B-Instruct |

## Per model

| model | frame | pairs | included | mean clean gap | removed by the located heads (95 % interval) | rank among random sets | random sets: mean / largest |
|---|---|---|---|---|---|---|---|
| Llama-3.2-1B | CH | moral | 64 of 80 | +0.494 | 0.184 [0.119, 0.246] | 5 of 20 | 0.113 / 0.344 |
| Llama-3.2-1B | CH | norm | 67 of 107 | +0.355 | 0.006 [-0.061, 0.077] | 13 of 20 | 0.075 / 0.322 |
| Llama-3.2-1B | CH | descr | 26 of 40 | +0.239 | -0.334 [-0.524, -0.175] | 20 of 20 | 0.071 / 0.342 |
| Llama-3.2-1B-Instruct | CH | moral | 75 of 80 | +2.668 | -0.176 [-0.239, -0.118] | 18 of 20 | 0.130 / 0.531 |
| Llama-3.2-1B-Instruct | CH | norm | 101 of 107 | +1.460 | -0.291 [-0.376, -0.212] | 19 of 20 | 0.139 / 0.492 |
| Llama-3.2-1B-Instruct | CH | descr | 26 of 40 | +0.989 | -0.695 [-0.971, -0.494] | 20 of 20 | 0.093 / 0.662 |
| gemma-2b | CH | moral | 72 of 80 | +0.995 | 1.041 [0.954, 1.131] | 0 of 20 | 0.437 / 0.675 |
| gemma-2b | CH | norm | 87 of 107 | +1.029 | 1.013 [0.906, 1.116] | 0 of 20 | 0.458 / 0.687 |
| gemma-2b | CH | descr | 24 of 40 | +0.322 | 0.636 [0.149, 1.053] | 2 of 20 | 0.389 / 0.716 |
| gemma-2b-it | CH | moral | 77 of 80 | +8.561 | 0.287 [0.233, 0.339] | 6 of 20 | 0.180 / 0.590 |
| gemma-2b-it | CH | norm | 98 of 107 | +8.660 | 0.314 [0.256, 0.375] | 4 of 20 | 0.166 / 0.567 |
| gemma-2b-it | CH | descr | 27 of 40 | +4.977 | 0.143 [-0.048, 0.312] | 9 of 20 | 0.149 / 0.562 |
| Llama-3.2-3B | CH | moral | 73 of 80 | +1.450 | 0.244 [0.192, 0.294] | 1 of 20 | 0.057 / 0.256 |
| Llama-3.2-3B | CH | norm | 96 of 107 | +0.945 | 0.309 [0.253, 0.365] | 0 of 20 | 0.062 / 0.207 |
| Llama-3.2-3B | CH | descr | 37 of 40 | +0.753 | 0.252 [0.168, 0.331] | 2 of 20 | 0.086 / 0.303 |
| Llama-3.2-3B-Instruct | CH | moral | 80 of 80 | +7.399 | 0.081 [0.047, 0.117] | 9 of 20 | 0.078 / 0.309 |
| Llama-3.2-3B-Instruct | CH | norm | 107 of 107 | +5.270 | 0.115 [0.075, 0.156] | 5 of 20 | 0.077 / 0.372 |
| Llama-3.2-3B-Instruct | CH | descr | 35 of 40 | +2.470 | 0.002 [-0.081, 0.073] | 13 of 20 | 0.049 / 0.319 |
| Qwen2.5-3B | CH | moral | 65 of 80 | +1.182 | 1.034 [0.799, 1.258] | 0 of 20 | 0.050 / 0.368 |
| Qwen2.5-3B | CH | norm | 100 of 107 | +1.496 | 0.980 [0.824, 1.132] | 0 of 20 | 0.076 / 0.662 |
| Qwen2.5-3B | CH | descr | 18 of 40* | +0.883 | 0.905 [0.087, 1.678] | 0 of 20 | 0.054 / 0.312 |
| Qwen2.5-3B-Instruct | CH | moral | 73 of 80 | +5.263 | 0.181 [0.103, 0.255] | 3 of 20 | 0.072 / 0.331 |
| Qwen2.5-3B-Instruct | CH | norm | 104 of 107 | +6.211 | 0.217 [0.168, 0.267] | 3 of 20 | 0.077 / 0.360 |
| Qwen2.5-3B-Instruct | CH | descr | 34 of 40 | +3.373 | 0.120 [-0.058, 0.353] | 6 of 20 | 0.049 / 0.339 |
| Qwen2.5-7B | CH | moral | 66 of 80 | +4.531 | 0.173 [0.101, 0.253] | 1 of 20 | 0.009 / 0.245 |
| Qwen2.5-7B | CH | norm | 105 of 107 | +4.139 | 0.213 [0.162, 0.266] | 1 of 20 | 0.006 / 0.217 |
| Qwen2.5-7B | CH | descr | 25 of 40 | +1.656 | 0.052 [-0.165, 0.211] | 8 of 20 | -0.009 / 0.314 |
| Qwen2.5-7B-Instruct | CH | moral | 61 of 80 | +11.610 | -0.233 [-0.337, -0.138] | 20 of 20 | -0.003 / 0.346 |
| Qwen2.5-7B-Instruct | CH | norm | 95 of 107 | +9.616 | -0.274 [-0.379, -0.167] | 17 of 20 | -0.073 / 0.294 |
| Qwen2.5-7B-Instruct | CH | descr | 11 of 40* | +4.385 | -0.560 [-1.328, -0.007] | 19 of 20 | -0.093 / 0.721 |
| Llama-3.1-8B | CH | moral | 70 of 80 | +1.145 | 0.435 [0.383, 0.479] | 0 of 20 | 0.026 / 0.318 |
| Llama-3.1-8B | CH | norm | 88 of 107 | +1.053 | 0.436 [0.387, 0.485] | 0 of 20 | 0.020 / 0.296 |
| Llama-3.1-8B | CH | descr | 36 of 40 | +0.687 | 0.361 [0.280, 0.436] | 0 of 20 | 0.016 / 0.357 |
| Llama-3.1-8B-Instruct | CH | moral | 79 of 80 | +4.149 | 0.327 [0.299, 0.356] | 0 of 20 | 0.018 / 0.189 |
| Llama-3.1-8B-Instruct | CH | norm | 106 of 107 | +3.357 | 0.300 [0.267, 0.335] | 0 of 20 | 0.025 / 0.169 |
| Llama-3.1-8B-Instruct | CH | descr | 38 of 40 | +1.829 | 0.307 [0.248, 0.360] | 0 of 20 | 0.008 / 0.265 |
| Qwen2.5-14B | CH | moral | 78 of 80 | +4.862 | 0.241 [0.217, 0.269] | 0 of 20 | 0.012 / 0.110 |
| Qwen2.5-14B | CH | norm | 107 of 107 | +4.997 | 0.197 [0.179, 0.216] | 0 of 20 | 0.012 / 0.088 |
| Qwen2.5-14B | CH | descr | 37 of 40 | +2.229 | 0.187 [0.134, 0.237] | 0 of 20 | 0.006 / 0.146 |
| Qwen2.5-14B-Instruct | CH | moral | 80 of 80 | +20.308 | 0.237 [0.181, 0.290] | 0 of 20 | 0.003 / 0.078 |
| Qwen2.5-14B-Instruct | CH | norm | 107 of 107 | +19.697 | 0.196 [0.151, 0.240] | 0 of 20 | 0.001 / 0.069 |
| Qwen2.5-14B-Instruct | CH | descr | 38 of 40 | +11.706 | 0.114 [0.020, 0.201] | 1 of 20 | -0.003 / 0.118 |

\* fewer included pairs than the minimum; shown, not counted.
