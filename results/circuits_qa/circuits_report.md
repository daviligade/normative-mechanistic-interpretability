# Circuit-level results

Item set: the item file is the set of accepted pairs (the accepted pairs).

Items: 227 (moral 80, norm 107, descr 40, prudential 15, etiquette 18, aesthetic 22, epistemic 24); inclusion S(perm) - S(rest) >= 0.02; subset: accepted; bootstrap 2000 item resamples.
These analyses are exploratory.

## Necessity (mean-ablation of head sets against size-matched random sets)

Fraction of the clean gap removed = 1 - mean(gap after ablation) / mean(clean gap) over the included items of a group (ratio of means). Rank = number of random sets of the same size that remove at least as much as the located set (0 means the located set beats all of them; with 20 random sets, a rank of 0 corresponds to the 95th percentile). Mode `all`: every non-BOS position ablated; `final`: the final position only (the cleaner test).

| model | frame | mode | group | n | located removes | 95 % CI | rank among 20 random10 | random10 mean | topshare10 | located_top5 (rank/20) | located_top1 (rank/20) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | all | moral | 79 | 0.382 | [0.332, 0.433] | 0 | 0.051 | 0.524 (0) | 0.428 (None) | 0.113 (None) |
| Llama-3.1-8B | QA | all | norm | 106 | 0.468 | [0.430, 0.506] | 0 | 0.062 | 0.604 (0) | 0.540 (None) | 0.156 (None) |
| Llama-3.1-8B | QA | all | descr | 40 | 0.380 | [0.319, 0.439] | 0 | 0.059 | 0.604 (0) | 0.415 (None) | 0.076 (None) |
| Llama-3.1-8B-Instruct | QA | all | moral | 79 | 0.240 | [0.184, 0.300] | 0 | 0.017 | 0.459 (0) | 0.258 (None) | 0.071 (None) |
| Llama-3.1-8B-Instruct | QA | all | norm | 106 | 0.300 | [0.264, 0.336] | 0 | 0.020 | 0.525 (0) | 0.304 (None) | 0.092 (None) |
| Llama-3.1-8B-Instruct | QA | all | descr | 40 | 0.187 | [0.145, 0.230] | 0 | 0.021 | 0.497 (0) | 0.217 (None) | 0.038 (None) |
| Llama-3.2-1B | QA | all | moral | 72 | 0.440 | [0.385, 0.493] | 0 | 0.101 | 0.663 (0) | 0.218 (None) | 0.082 (None) |
| Llama-3.2-1B | QA | all | norm | 89 | 0.498 | [0.431, 0.564] | 0 | 0.098 | 0.730 (0) | 0.196 (None) | 0.090 (None) |
| Llama-3.2-1B | QA | all | descr | 37 | 0.273 | [0.191, 0.340] | 3 | 0.070 | 0.675 (0) | 0.072 (None) | -0.004 (None) |
| Llama-3.2-1B-Instruct | QA | all | moral | 75 | 0.185 | [0.104, 0.263] | 7 | 0.130 | 0.352 (2) | 0.099 (None) | -0.026 (None) |
| Llama-3.2-1B-Instruct | QA | all | norm | 91 | 0.060 | [-0.015, 0.126] | 10 | 0.099 | 0.359 (2) | -0.051 (None) | -0.020 (None) |
| Llama-3.2-1B-Instruct | QA | all | descr | 37 | 0.262 | [0.200, 0.328] | 3 | 0.079 | 0.632 (0) | 0.086 (None) | -0.023 (None) |
| Llama-3.2-3B | QA | all | moral | 79 | 0.471 | [0.428, 0.518] | 0 | 0.016 | 0.480 (0) | 0.120 (None) | 0.093 (None) |
| Llama-3.2-3B | QA | all | norm | 101 | 0.572 | [0.537, 0.608] | 0 | 0.021 | 0.643 (0) | 0.266 (None) | 0.153 (None) |
| Llama-3.2-3B | QA | all | descr | 38 | 0.218 | [0.129, 0.306] | 3 | 0.068 | 0.402 (1) | -0.119 (None) | -0.089 (None) |
| Llama-3.2-3B-Instruct | QA | all | moral | 75 | -0.138 | [-0.219, -0.067] | 20 | 0.012 | 0.133 (0) | -0.037 (None) | -0.010 (None) |
| Llama-3.2-3B-Instruct | QA | all | norm | 104 | 0.095 | [0.051, 0.141] | 1 | 0.013 | 0.331 (0) | 0.110 (None) | 0.063 (None) |
| Llama-3.2-3B-Instruct | QA | all | descr | 40 | 0.035 | [-0.016, 0.087] | 5 | 0.004 | 0.245 (0) | 0.101 (None) | 0.021 (None) |
| Qwen2.5-14B | QA | all | moral | 80 | 0.206 | [0.167, 0.248] | 0 | 0.021 | 0.276 (0) | 0.201 (None) | 0.051 (None) |
| Qwen2.5-14B | QA | all | norm | 107 | 0.247 | [0.218, 0.276] | 0 | 0.022 | 0.315 (0) | 0.234 (None) | 0.079 (None) |
| Qwen2.5-14B | QA | all | descr | 39 | 0.204 | [0.123, 0.277] | 0 | 0.019 | 0.357 (0) | 0.177 (None) | 0.088 (None) |
| Qwen2.5-14B-Instruct | QA | all | moral | 75 | 0.578 | [0.496, 0.664] | 0 | 0.004 | 0.613 (0) | 0.443 (None) | 0.058 (None) |
| Qwen2.5-14B-Instruct | QA | all | norm | 95 | 0.482 | [0.377, 0.575] | 0 | 0.011 | 0.267 (0) | 0.404 (None) | 0.108 (None) |
| Qwen2.5-14B-Instruct | QA | all | descr | 23 | 0.321 | [-0.053, 0.606] | 1 | -0.023 | 0.293 (1) | 0.324 (None) | 0.026 (None) |
| Qwen2.5-3B | QA | all | moral | 74 | 0.998 | [0.996, 0.999] | 0 | 0.053 | 0.998 (0) | 0.409 (None) | 0.018 (None) |
| Qwen2.5-3B | QA | all | norm | 104 | 0.999 | [0.997, 1.000] | 0 | 0.076 | 0.999 (0) | 0.639 (None) | 0.033 (None) |
| Qwen2.5-3B | QA | all | descr | 40 | 0.999 | [0.996, 1.001] | 0 | 0.066 | 0.996 (0) | 0.760 (None) | 0.023 (None) |
| Qwen2.5-3B-Instruct | QA | all | moral | 70 | 0.695 | [0.571, 0.795] | 0 | -0.180 | 0.915 (0) | 0.607 (None) | 0.389 (None) |
| Qwen2.5-3B-Instruct | QA | all | norm | 68 | 0.846 | [0.805, 0.880] | 0 | -0.304 | 0.919 (0) | 0.593 (None) | 0.404 (None) |
| Qwen2.5-3B-Instruct | QA | all | descr | 8* | 0.877 | [0.734, 0.988] | 1 | -0.396 | 0.361 (10) | 0.736 (None) | 0.449 (None) |
| Qwen2.5-7B | QA | all | moral | 80 | 0.299 | [0.224, 0.374] | 0 | 0.011 | 0.967 (0) | 0.220 (None) | -0.131 (None) |
| Qwen2.5-7B | QA | all | norm | 105 | 0.390 | [0.328, 0.452] | 0 | 0.008 | 0.977 (0) | 0.249 (None) | -0.103 (None) |
| Qwen2.5-7B | QA | all | descr | 40 | 0.326 | [0.272, 0.381] | 0 | 0.025 | 0.959 (0) | 0.201 (None) | -0.182 (None) |
| Qwen2.5-7B-Instruct | QA | all | moral | 70 | 0.120 | [0.031, 0.202] | 5 | 0.009 | 0.998 (0) | 0.380 (None) | 0.053 (None) |
| Qwen2.5-7B-Instruct | QA | all | norm | 80 | 0.210 | [0.098, 0.306] | 3 | 0.033 | 1.000 (0) | 0.159 (None) | 0.050 (None) |
| Qwen2.5-7B-Instruct | QA | all | descr | 28 | 0.157 | [-0.176, 0.381] | 6 | 0.004 | 1.001 (0) | 0.171 (None) | -0.007 (None) |
| gemma-2b | QA | all | moral | 73 | 0.993 | [0.912, 1.075] | 0 | 0.265 | 0.933 (0) | 0.708 (None) | -0.056 (None) |
| gemma-2b | QA | all | norm | 92 | 0.892 | [0.796, 0.981] | 0 | 0.284 | 0.972 (0) | 0.642 (None) | -0.053 (None) |
| gemma-2b | QA | all | descr | 38 | 1.009 | [0.917, 1.087] | 0 | 0.222 | 0.964 (0) | 0.518 (None) | -0.322 (None) |
| gemma-2b-it | QA | all | moral | 70 | 0.258 | [0.142, 0.371] | 9 | 0.192 | 0.189 (13) | -0.145 (None) | -0.055 (None) |
| gemma-2b-it | QA | all | norm | 93 | 0.175 | [0.053, 0.273] | 10 | 0.148 | 0.110 (13) | -0.230 (None) | -0.030 (None) |
| gemma-2b-it | QA | all | descr | 35 | -0.098 | [-0.298, 0.070] | 17 | 0.124 | -0.211 (17) | -0.454 (None) | 0.070 (None) |

\* fewer included items than the minimum of the plan; shown, not pooled.

Moral-specificity of the necessity: fraction removed by located on moral items minus on norm items (bootstrap interval, independent resamples).

| model | frame | mode | moral | norm | difference | 95 % CI |
|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | all | 0.382 | 0.468 | -0.086 | [-0.149, -0.020] |
| Llama-3.1-8B-Instruct | QA | all | 0.240 | 0.300 | -0.060 | [-0.130, +0.006] |
| Llama-3.2-1B | QA | all | 0.440 | 0.498 | -0.058 | [-0.143, +0.025] |
| Llama-3.2-1B-Instruct | QA | all | 0.185 | 0.060 | +0.125 | [+0.020, +0.229] |
| Llama-3.2-3B | QA | all | 0.471 | 0.572 | -0.101 | [-0.159, -0.042] |
| Llama-3.2-3B-Instruct | QA | all | -0.138 | 0.095 | -0.232 | [-0.329, -0.149] |
| Qwen2.5-14B | QA | all | 0.206 | 0.247 | -0.041 | [-0.088, +0.009] |
| Qwen2.5-14B-Instruct | QA | all | 0.578 | 0.482 | +0.096 | [-0.031, +0.228] |
| Qwen2.5-3B | QA | all | 0.998 | 0.999 | -0.001 | [-0.004, +0.001] |
| Qwen2.5-3B-Instruct | QA | all | 0.695 | 0.846 | -0.151 | [-0.280, -0.042] |
| Qwen2.5-7B | QA | all | 0.299 | 0.390 | -0.091 | [-0.186, +0.005] |
| Qwen2.5-7B-Instruct | QA | all | 0.120 | 0.210 | -0.090 | [-0.220, +0.043] |
| gemma-2b | QA | all | 0.993 | 0.892 | +0.102 | [-0.018, +0.225] |
| gemma-2b-it | QA | all | 0.258 | 0.175 | +0.083 | [-0.074, +0.249] |

Frame QA, mode all: located beats all 20 random size-10 sets on moral items in 10 of 14 models; median fraction removed 0.340 (random10 mean, median over models: 0.019).

## Files

* `necessity.csv` (98 rows)
* `necessity_moral_minus_norm.csv` (14 rows)
* `figures/` (14 figures)
