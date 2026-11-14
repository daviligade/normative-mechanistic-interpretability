# Removal of the located heads, read on LD

Runs: runs/circuits_qa/ablation; positions: all; a pair is included when its gap in LD is at least 0.1; 2000 resamples of the pairs.

No check against the study's output was asked for (--check; possible with --readout S --include-on S).

## Per frame and kind of pair

| frame | pairs | models with enough pairs | median pairs included | located heads above every random set | median removed: located heads | median removed: random sets | left out |
|---|---|---|---|---|---|---|---|
| QA | moral | 14 of 14 | 78 | 11 of 14 | 0.301 | 0.030 | - |
| QA | norm | 14 of 14 | 104 | 12 of 14 | 0.353 | 0.043 | - |
| QA | descr | 14 of 14 | 40 | 8 of 14 | 0.297 | 0.037 | - |

## Per model

| model | frame | pairs | included | mean clean gap | removed by the located heads (95 % interval) | rank among random sets | random sets: mean / largest |
|---|---|---|---|---|---|---|---|
| Llama-3.2-1B | QA | moral | 68 of 80 | +0.688 | 0.487 [0.437, 0.538] | 0 of 20 | 0.080 / 0.367 |
| Llama-3.2-1B | QA | norm | 84 of 107 | +0.491 | 0.525 [0.469, 0.585] | 0 of 20 | 0.079 / 0.397 |
| Llama-3.2-1B | QA | descr | 35 of 40 | +0.669 | 0.357 [0.290, 0.415] | 1 of 20 | 0.066 / 0.397 |
| Llama-3.2-1B-Instruct | QA | moral | 76 of 80 | +1.662 | 0.165 [0.118, 0.210] | 7 of 20 | 0.100 / 0.303 |
| Llama-3.2-1B-Instruct | QA | norm | 97 of 107 | +1.114 | 0.115 [0.063, 0.165] | 8 of 20 | 0.095 / 0.336 |
| Llama-3.2-1B-Instruct | QA | descr | 39 of 40 | +1.632 | 0.183 [0.131, 0.240] | 6 of 20 | 0.112 / 0.427 |
| gemma-2b | QA | moral | 74 of 80 | +1.312 | 0.985 [0.886, 1.087] | 0 of 20 | 0.281 / 0.549 |
| gemma-2b | QA | norm | 96 of 107 | +0.770 | 0.860 [0.729, 0.991] | 0 of 20 | 0.310 / 0.486 |
| gemma-2b | QA | descr | 37 of 40 | +1.164 | 0.994 [0.863, 1.111] | 0 of 20 | 0.254 / 0.522 |
| gemma-2b-it | QA | moral | 73 of 80 | +13.437 | 0.327 [0.260, 0.403] | 0 of 20 | 0.122 / 0.258 |
| gemma-2b-it | QA | norm | 102 of 107 | +10.508 | 0.253 [0.196, 0.307] | 2 of 20 | 0.157 / 0.347 |
| gemma-2b-it | QA | descr | 40 of 40 | +12.790 | 0.086 [0.010, 0.153] | 13 of 20 | 0.117 / 0.373 |
| Llama-3.2-3B | QA | moral | 78 of 80 | +1.743 | 0.521 [0.486, 0.563] | 0 of 20 | 0.015 / 0.228 |
| Llama-3.2-3B | QA | norm | 101 of 107 | +1.141 | 0.581 [0.543, 0.617] | 0 of 20 | 0.014 / 0.216 |
| Llama-3.2-3B | QA | descr | 38 of 40 | +0.989 | 0.192 [0.109, 0.275] | 3 of 20 | 0.050 / 0.305 |
| Llama-3.2-3B-Instruct | QA | moral | 79 of 80 | +8.762 | -0.069 [-0.118, -0.022] | 20 of 20 | 0.030 / 0.122 |
| Llama-3.2-3B-Instruct | QA | norm | 103 of 107 | +7.617 | 0.119 [0.088, 0.152] | 0 of 20 | 0.031 / 0.109 |
| Llama-3.2-3B-Instruct | QA | descr | 40 of 40 | +6.591 | 0.048 [0.006, 0.091] | 5 of 20 | 0.025 / 0.155 |
| Qwen2.5-3B | QA | moral | 76 of 80 | +5.111 | 0.973 [0.957, 0.990] | 0 of 20 | 0.052 / 0.229 |
| Qwen2.5-3B | QA | norm | 104 of 107 | +4.195 | 0.979 [0.964, 0.995] | 0 of 20 | 0.069 / 0.232 |
| Qwen2.5-3B | QA | descr | 40 of 40 | +3.910 | 0.989 [0.963, 1.016] | 0 of 20 | 0.033 / 0.287 |
| Qwen2.5-3B-Instruct | QA | moral | 79 of 80 | +12.283 | 0.159 [0.105, 0.214] | 1 of 20 | 0.067 / 0.271 |
| Qwen2.5-3B-Instruct | QA | norm | 106 of 107 | +9.947 | 0.327 [0.274, 0.380] | 0 of 20 | 0.067 / 0.258 |
| Qwen2.5-3B-Instruct | QA | descr | 35 of 40 | +3.689 | 0.387 [0.258, 0.510] | 2 of 20 | 0.058 / 0.500 |
| Qwen2.5-7B | QA | moral | 80 of 80 | +5.070 | 0.244 [0.184, 0.309] | 0 of 20 | 0.012 / 0.155 |
| Qwen2.5-7B | QA | norm | 106 of 107 | +4.066 | 0.379 [0.327, 0.434] | 0 of 20 | 0.019 / 0.214 |
| Qwen2.5-7B | QA | descr | 40 of 40 | +4.013 | 0.319 [0.256, 0.382] | 0 of 20 | 0.029 / 0.206 |
| Qwen2.5-7B-Instruct | QA | moral | 78 of 80 | +14.854 | 0.165 [0.132, 0.198] | 0 of 20 | 0.003 / 0.063 |
| Qwen2.5-7B-Instruct | QA | norm | 104 of 107 | +13.118 | 0.172 [0.134, 0.213] | 0 of 20 | 0.004 / 0.098 |
| Qwen2.5-7B-Instruct | QA | descr | 40 of 40 | +10.983 | 0.276 [0.218, 0.333] | 0 of 20 | 0.004 / 0.116 |
| Llama-3.1-8B | QA | moral | 79 of 80 | +2.372 | 0.516 [0.474, 0.559] | 0 of 20 | 0.030 / 0.124 |
| Llama-3.1-8B | QA | norm | 105 of 107 | +2.180 | 0.590 [0.560, 0.619] | 0 of 20 | 0.055 / 0.185 |
| Llama-3.1-8B | QA | descr | 40 of 40 | +1.339 | 0.444 [0.387, 0.500] | 0 of 20 | 0.040 / 0.215 |
| Llama-3.1-8B-Instruct | QA | moral | 79 of 80 | +6.126 | 0.315 [0.266, 0.366] | 0 of 20 | 0.024 / 0.112 |
| Llama-3.1-8B-Instruct | QA | norm | 106 of 107 | +6.070 | 0.425 [0.398, 0.454] | 0 of 20 | 0.026 / 0.149 |
| Llama-3.1-8B-Instruct | QA | descr | 40 of 40 | +5.919 | 0.259 [0.210, 0.309] | 0 of 20 | 0.029 / 0.130 |
| Qwen2.5-14B | QA | moral | 79 of 80 | +7.498 | 0.189 [0.158, 0.223] | 0 of 20 | 0.002 / 0.047 |
| Qwen2.5-14B | QA | norm | 107 of 107 | +6.574 | 0.254 [0.235, 0.276] | 0 of 20 | -0.000 / 0.049 |
| Qwen2.5-14B | QA | descr | 40 of 40 | +4.858 | 0.253 [0.212, 0.298] | 0 of 20 | 0.008 / 0.072 |
| Qwen2.5-14B-Instruct | QA | moral | 80 of 80 | +25.955 | 0.287 [0.241, 0.336] | 0 of 20 | 0.010 / 0.079 |
| Qwen2.5-14B-Instruct | QA | norm | 107 of 107 | +25.435 | 0.276 [0.244, 0.308] | 0 of 20 | 0.016 / 0.121 |
| Qwen2.5-14B-Instruct | QA | descr | 40 of 40 | +16.079 | 0.365 [0.288, 0.452] | 0 of 20 | 0.011 / 0.111 |

\* fewer included pairs than the minimum; shown, not counted.
