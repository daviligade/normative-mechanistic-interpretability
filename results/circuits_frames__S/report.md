# Removal of the located heads, read on S

Runs: runs/circuits_frames/ablation; positions: all; a pair is included when its gap in S is at least 0.02; 2000 resamples of the pairs.

No check against the study's output was asked for (--check; possible with --readout S --include-on S).

## Per frame and kind of pair

| frame | pairs | models with enough pairs | median pairs included | located heads above every random set | median removed: located heads | median removed: random sets | left out |
|---|---|---|---|---|---|---|---|
| A0s | moral | 14 of 14 | 74 | 13 of 14 | 0.428 | 0.027 | - |
| A0s | norm | 14 of 14 | 74 | 13 of 14 | 0.395 | 0.034 | - |
| A0s | descr | 10 of 14 | 25 | 7 of 10 | 0.292 | 0.020 | Llama-3.2-1B, Qwen2.5-3B, Qwen2.5-14B, Qwen2.5-14B-Instruct |
| B0 | moral | 12 of 14 | 46 | 5 of 12 | 0.173 | 0.007 | Qwen2.5-3B, Qwen2.5-7B-Instruct |
| B0 | norm | 4 of 14 | 22 | 3 of 4 | 0.280 | 0.010 | Llama-3.2-1B, Llama-3.2-1B-Instruct, gemma-2b, gemma-2b-it, Llama-3.2-3B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Qwen2.5-14B-Instruct |
| B0 | descr | 0 of 13 | 10 | 0 of 0 | n/a | n/a | Llama-3.2-1B, Llama-3.2-1B-Instruct, gemma-2b, gemma-2b-it, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-3B-Instruct, Qwen2.5-7B, Qwen2.5-7B-Instruct, Llama-3.1-8B, Llama-3.1-8B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct |

## Per model

| model | frame | pairs | included | mean clean gap | removed by the located heads (95 % interval) | rank among random sets | random sets: mean / largest |
|---|---|---|---|---|---|---|---|
| Llama-3.2-1B | A0s | moral | 68 of 80 | +0.297 | 0.267 [0.182, 0.349] | 1 of 20 | 0.029 / 0.271 |
| Llama-3.2-1B | A0s | norm | 79 of 107 | +0.258 | 0.357 [0.269, 0.448] | 0 of 20 | 0.054 / 0.236 |
| Llama-3.2-1B | A0s | descr | 19 of 40* | +0.179 | 0.365 [0.212, 0.531] | 1 of 20 | 0.062 / 0.518 |
| Llama-3.2-1B | B0 | moral | 38 of 80 | +0.054 | 0.183 [0.053, 0.325] | 1 of 20 | 0.057 / 0.185 |
| Llama-3.2-1B | B0 | norm | 14 of 107* | +0.034 | 0.237 [0.117, 0.333] | 0 of 20 | 0.070 / 0.210 |
| Llama-3.2-1B | B0 | descr | 9 of 40* | +0.040 | 0.239 [0.068, 0.429] | 0 of 20 | 0.046 / 0.204 |
| Llama-3.2-1B-Instruct | A0s | moral | 74 of 80 | +0.432 | 0.223 [0.159, 0.289] | 0 of 20 | 0.021 / 0.196 |
| Llama-3.2-1B-Instruct | A0s | norm | 79 of 107 | +0.307 | 0.120 [0.054, 0.193] | 2 of 20 | 0.033 / 0.186 |
| Llama-3.2-1B-Instruct | A0s | descr | 24 of 40 | +0.198 | 0.307 [0.174, 0.453] | 0 of 20 | 0.032 / 0.199 |
| Llama-3.2-1B-Instruct | B0 | moral | 34 of 80 | +0.048 | 0.161 [-0.007, 0.374] | 1 of 20 | 0.002 / 0.175 |
| Llama-3.2-1B-Instruct | B0 | norm | 11 of 107* | +0.049 | -0.008 [-0.243, 0.173] | 13 of 20 | 0.012 / 0.171 |
| Llama-3.2-1B-Instruct | B0 | descr | 3 of 40* | +0.030 | 0.288 [0.096, 0.806] | 1 of 20 | -0.018 / 0.294 |
| gemma-2b | A0s | moral | 59 of 80 | +0.350 | 0.904 [0.771, 1.025] | 0 of 20 | 0.128 / 0.364 |
| gemma-2b | A0s | norm | 72 of 107 | +0.292 | 0.880 [0.747, 1.012] | 0 of 20 | 0.102 / 0.355 |
| gemma-2b | A0s | descr | 23 of 40 | +0.138 | 0.617 [0.150, 0.894] | 0 of 20 | 0.159 / 0.389 |
| gemma-2b | B0 | moral | 40 of 80 | +0.048 | 0.889 [0.809, 0.959] | 0 of 20 | 0.152 / 0.337 |
| gemma-2b | B0 | norm | 22 of 107* | +0.040 | 0.387 [-0.754, 0.970] | 0 of 20 | 0.161 / 0.363 |
| gemma-2b | B0 | descr | 10 of 40* | +0.053 | 0.862 [0.705, 0.994] | 0 of 20 | 0.243 / 0.447 |
| gemma-2b-it | A0s | moral | 74 of 80 | +0.543 | 0.445 [0.305, 0.602] | 0 of 20 | 0.077 / 0.274 |
| gemma-2b-it | A0s | norm | 82 of 107 | +0.518 | 0.476 [0.346, 0.609] | 0 of 20 | 0.067 / 0.210 |
| gemma-2b-it | A0s | descr | 32 of 40 | +0.565 | 0.136 [-0.088, 0.304] | 2 of 20 | 0.065 / 0.158 |
| gemma-2b-it | B0 | moral | 49 of 80 | +0.151 | 0.166 [-0.031, 0.353] | 1 of 20 | -0.013 / 0.176 |
| gemma-2b-it | B0 | norm | 22 of 107* | +0.080 | 0.521 [0.197, 0.762] | 0 of 20 | 0.000 / 0.217 |
| gemma-2b-it | B0 | descr | 9 of 40* | +0.123 | 0.525 [0.418, 0.703] | 0 of 20 | 0.024 / 0.309 |
| Llama-3.2-3B | A0s | moral | 67 of 80 | +0.392 | 0.792 [0.691, 0.900] | 0 of 20 | 0.034 / 0.176 |
| Llama-3.2-3B | A0s | norm | 70 of 107 | +0.279 | 0.651 [0.549, 0.768] | 0 of 20 | 0.019 / 0.130 |
| Llama-3.2-3B | A0s | descr | 30 of 40 | +0.200 | 0.490 [0.337, 0.630] | 0 of 20 | 0.026 / 0.145 |
| Llama-3.2-3B | B0 | moral | 54 of 80 | +0.054 | 0.444 [0.389, 0.495] | 0 of 20 | 0.018 / 0.079 |
| Llama-3.2-3B | B0 | norm | 32 of 107 | +0.040 | 0.521 [0.436, 0.613] | 0 of 20 | 0.022 / 0.093 |
| Llama-3.2-3B | B0 | descr | 10 of 40* | +0.056 | 0.478 [0.302, 0.635] | 0 of 20 | 0.031 / 0.148 |
| Llama-3.2-3B-Instruct | A0s | moral | 79 of 80 | +0.764 | 0.158 [0.102, 0.215] | 0 of 20 | 0.029 / 0.097 |
| Llama-3.2-3B-Instruct | A0s | norm | 85 of 107 | +0.464 | 0.328 [0.271, 0.394] | 0 of 20 | 0.018 / 0.082 |
| Llama-3.2-3B-Instruct | A0s | descr | 39 of 40 | +0.255 | 0.270 [0.173, 0.373] | 0 of 20 | 0.027 / 0.238 |
| Llama-3.2-3B-Instruct | B0 | moral | 40 of 80 | +0.061 | 0.038 [-0.084, 0.159] | 5 of 20 | 0.008 / 0.201 |
| Llama-3.2-3B-Instruct | B0 | norm | 16 of 107* | +0.043 | 0.082 [-0.177, 0.362] | 3 of 20 | 0.023 / 0.282 |
| Llama-3.2-3B-Instruct | B0 | descr | 5 of 40* | +0.081 | 0.069 [-0.423, 0.308] | 8 of 20 | 0.020 / 0.206 |
| Qwen2.5-3B | A0s | moral | 54 of 80 | +0.417 | 1.000 [0.999, 1.001] | 0 of 20 | 0.095 / 0.449 |
| Qwen2.5-3B | A0s | norm | 59 of 107 | +0.285 | 1.000 [0.999, 1.001] | 0 of 20 | 0.092 / 0.625 |
| Qwen2.5-3B | A0s | descr | 2 of 40* | +0.046 | 1.053 [0.997, 1.078] | 1 of 20 | -0.553 / 1.057 |
| Qwen2.5-3B | B0 | moral | 26 of 80* | +0.076 | 0.996 [0.984, 1.005] | 0 of 20 | 0.154 / 0.507 |
| Qwen2.5-3B | B0 | norm | 13 of 107* | +0.042 | 0.991 [0.971, 1.002] | 0 of 20 | 0.086 / 0.644 |
| Qwen2.5-3B-Instruct | A0s | moral | 76 of 80 | +0.647 | 0.253 [0.200, 0.311] | 0 of 20 | 0.017 / 0.068 |
| Qwen2.5-3B-Instruct | A0s | norm | 86 of 107 | +0.403 | 0.349 [0.261, 0.447] | 0 of 20 | 0.034 / 0.113 |
| Qwen2.5-3B-Instruct | A0s | descr | 26 of 40 | +0.154 | 0.285 [0.112, 0.485] | 0 of 20 | 0.015 / 0.159 |
| Qwen2.5-3B-Instruct | B0 | moral | 49 of 80 | +0.066 | 0.046 [-0.091, 0.160] | 3 of 20 | -0.015 / 0.103 |
| Qwen2.5-3B-Instruct | B0 | norm | 23 of 107* | +0.041 | 0.059 [-0.080, 0.219] | 2 of 20 | 0.008 / 0.126 |
| Qwen2.5-3B-Instruct | B0 | descr | 10 of 40* | +0.038 | 0.255 [-0.231, 1.184] | 1 of 20 | 0.000 / 0.313 |
| Qwen2.5-7B | A0s | moral | 77 of 80 | +0.469 | 0.218 [0.124, 0.305] | 0 of 20 | 0.026 / 0.141 |
| Qwen2.5-7B | A0s | norm | 74 of 107 | +0.381 | 0.307 [0.167, 0.462] | 0 of 20 | 0.040 / 0.199 |
| Qwen2.5-7B | A0s | descr | 29 of 40 | +0.160 | 0.002 [-0.309, 0.245] | 9 of 20 | 0.009 / 0.219 |
| Qwen2.5-7B | B0 | moral | 58 of 80 | +0.063 | 0.236 [0.114, 0.361] | 0 of 20 | 0.019 / 0.074 |
| Qwen2.5-7B | B0 | norm | 37 of 107 | +0.049 | 0.323 [0.177, 0.473] | 0 of 20 | 0.016 / 0.107 |
| Qwen2.5-7B | B0 | descr | 14 of 40* | +0.074 | 0.013 [-0.345, 0.231] | 8 of 20 | -0.003 / 0.139 |
| Qwen2.5-7B-Instruct | A0s | moral | 72 of 80 | +0.387 | 0.435 [0.275, 0.588] | 0 of 20 | 0.036 / 0.179 |
| Qwen2.5-7B-Instruct | A0s | norm | 71 of 107 | +0.328 | 0.450 [0.227, 0.665] | 0 of 20 | 0.065 / 0.237 |
| Qwen2.5-7B-Instruct | A0s | descr | 28 of 40 | +0.140 | -0.179 [-0.775, 0.194] | 19 of 20 | -0.024 / 0.151 |
| Qwen2.5-7B-Instruct | B0 | moral | 25 of 80* | +0.070 | 0.808 [0.531, 0.979] | 0 of 20 | 0.076 / 0.246 |
| Qwen2.5-7B-Instruct | B0 | norm | 15 of 107* | +0.046 | 0.413 [-0.055, 1.009] | 0 of 20 | 0.017 / 0.284 |
| Qwen2.5-7B-Instruct | B0 | descr | 8 of 40* | +0.147 | 0.990 [0.941, 1.000] | 0 of 20 | -0.076 / 0.201 |
| Llama-3.1-8B | A0s | moral | 73 of 80 | +0.423 | 0.473 [0.414, 0.535] | 0 of 20 | 0.013 / 0.145 |
| Llama-3.1-8B | A0s | norm | 78 of 107 | +0.341 | 0.372 [0.308, 0.438] | 0 of 20 | 0.014 / 0.108 |
| Llama-3.1-8B | A0s | descr | 29 of 40 | +0.162 | 0.309 [0.202, 0.417] | 0 of 20 | 0.002 / 0.211 |
| Llama-3.1-8B | B0 | moral | 62 of 80 | +0.064 | 0.180 [0.121, 0.242] | 0 of 20 | -0.003 / 0.048 |
| Llama-3.1-8B | B0 | norm | 39 of 107 | +0.053 | 0.237 [0.162, 0.310] | 0 of 20 | 0.004 / 0.047 |
| Llama-3.1-8B | B0 | descr | 13 of 40* | +0.054 | 0.116 [-0.013, 0.247] | 1 of 20 | -0.006 / 0.154 |
| Llama-3.1-8B-Instruct | A0s | moral | 75 of 80 | +0.511 | 0.420 [0.361, 0.485] | 0 of 20 | 0.007 / 0.083 |
| Llama-3.1-8B-Instruct | A0s | norm | 73 of 107 | +0.315 | 0.417 [0.346, 0.503] | 0 of 20 | 0.001 / 0.068 |
| Llama-3.1-8B-Instruct | A0s | descr | 23 of 40 | +0.130 | 0.300 [0.174, 0.402] | 0 of 20 | 0.005 / 0.173 |
| Llama-3.1-8B-Instruct | B0 | moral | 54 of 80 | +0.052 | -0.006 [-0.070, 0.065] | 13 of 20 | 0.006 / 0.055 |
| Llama-3.1-8B-Instruct | B0 | norm | 27 of 107* | +0.039 | 0.155 [0.040, 0.301] | 0 of 20 | 0.025 / 0.121 |
| Llama-3.1-8B-Instruct | B0 | descr | 10 of 40* | +0.066 | -0.061 [-0.151, 0.048] | 19 of 20 | 0.027 / 0.148 |
| Qwen2.5-14B | A0s | moral | 78 of 80 | +0.560 | 0.109 [0.019, 0.190] | 0 of 20 | -0.002 / 0.047 |
| Qwen2.5-14B | A0s | norm | 67 of 107 | +0.350 | 0.229 [0.092, 0.365] | 0 of 20 | -0.002 / 0.044 |
| Qwen2.5-14B | A0s | descr | 18 of 40* | +0.092 | 0.186 [-0.417, 0.727] | 0 of 20 | 0.008 / 0.094 |
| Qwen2.5-14B | B0 | moral | 64 of 80 | +0.060 | -0.102 [-0.376, 0.090] | 20 of 20 | -0.002 / 0.031 |
| Qwen2.5-14B | B0 | norm | 33 of 107 | +0.051 | -0.032 [-0.291, 0.166] | 18 of 20 | -0.012 / 0.011 |
| Qwen2.5-14B | B0 | descr | 15 of 40* | +0.068 | -0.167 [-0.440, 0.103] | 19 of 20 | -0.005 / 0.188 |
| Qwen2.5-14B-Instruct | A0s | moral | 75 of 80 | +0.596 | 0.599 [0.489, 0.709] | 0 of 20 | 0.022 / 0.077 |
| Qwen2.5-14B-Instruct | A0s | norm | 53 of 107 | +0.359 | 0.697 [0.510, 0.864] | 0 of 20 | 0.024 / 0.077 |
| Qwen2.5-14B-Instruct | A0s | descr | 12 of 40* | +0.085 | 0.583 [-0.776, 1.321] | 0 of 20 | -0.029 / 0.087 |
| Qwen2.5-14B-Instruct | B0 | moral | 42 of 80 | +0.066 | 0.584 [0.421, 0.729] | 0 of 20 | 0.018 / 0.097 |
| Qwen2.5-14B-Instruct | B0 | norm | 21 of 107* | +0.051 | 0.927 [0.472, 1.516] | 0 of 20 | 0.011 / 0.075 |
| Qwen2.5-14B-Instruct | B0 | descr | 12 of 40* | +0.089 | 0.792 [0.234, 0.997] | 0 of 20 | -0.010 / 0.154 |

\* fewer included pairs than the minimum; shown, not counted.
