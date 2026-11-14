# Circuit-level results

Item set: the item file is the set of accepted pairs (the accepted pairs).

Items: 227 (moral 80, norm 107, descr 40, prudential 15, etiquette 18, aesthetic 22, epistemic 24); inclusion S(perm) - S(rest) >= 0.02; subset: accepted; bootstrap 2000 item resamples.
These analyses are exploratory.

## Necessity (mean-ablation of head sets against size-matched random sets)

Fraction of the clean gap removed = 1 - mean(gap after ablation) / mean(clean gap) over the included items of a group (ratio of means). Rank = number of random sets of the same size that remove at least as much as the located set (0 means the located set beats all of them; with 20 random sets, a rank of 0 corresponds to the 95th percentile). Mode `all`: every non-BOS position ablated; `final`: the final position only (the cleaner test).

| model | frame | mode | group | n | located removes | 95 % CI | rank among 20 random10 | random10 mean | topshare10 | located_top5 (rank/20) | located_top1 (rank/20) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | all | moral | 78 | 0.306 | [0.249, 0.367] | 0 | 0.005 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B | A1 | all | norm | 104 | 0.249 | [0.199, 0.301] | 0 | -0.023 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B | A1 | all | descr | 38 | 0.192 | [0.133, 0.251] | 0 | -0.019 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B | B | all | moral | 77 | 0.204 | [0.142, 0.269] | 0 | 0.027 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B | B | all | norm | 104 | 0.263 | [0.230, 0.298] | 0 | 0.028 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B | B | all | descr | 40 | 0.234 | [0.186, 0.287] | 0 | 0.021 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B-Instruct | A1 | all | moral | 78 | 0.256 | [0.216, 0.300] | 0 | 0.007 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B-Instruct | A1 | all | norm | 107 | 0.350 | [0.315, 0.387] | 0 | 0.026 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B-Instruct | A1 | all | descr | 37 | 0.287 | [0.213, 0.354] | 1 | 0.069 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B-Instruct | B | all | moral | 78 | 0.156 | [0.104, 0.213] | 0 | -0.009 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B-Instruct | B | all | norm | 103 | 0.205 | [0.174, 0.241] | 0 | 0.021 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.1-8B-Instruct | B | all | descr | 40 | 0.150 | [0.106, 0.199] | 2 | 0.035 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B | A1 | all | moral | 78 | 0.262 | [0.204, 0.320] | 2 | 0.118 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B | A1 | all | norm | 97 | 0.357 | [0.309, 0.408] | 0 | 0.094 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B | A1 | all | descr | 39 | 0.344 | [0.302, 0.381] | 1 | 0.057 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B | B | all | moral | 73 | 0.295 | [0.230, 0.361] | 1 | 0.039 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B | B | all | norm | 91 | 0.374 | [0.328, 0.420] | 0 | 0.037 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B | B | all | descr | 35 | 0.264 | [0.220, 0.309] | 2 | 0.033 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B-Instruct | A1 | all | moral | 69 | 0.203 | [0.136, 0.273] | 1 | 0.093 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B-Instruct | A1 | all | norm | 92 | 0.160 | [0.107, 0.213] | 3 | 0.081 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B-Instruct | A1 | all | descr | 38 | 0.214 | [0.147, 0.274] | 4 | 0.047 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B-Instruct | B | all | moral | 72 | 0.107 | [0.046, 0.169] | 5 | 0.026 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B-Instruct | B | all | norm | 95 | 0.099 | [0.033, 0.168] | 7 | 0.029 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-1B-Instruct | B | all | descr | 37 | 0.033 | [-0.044, 0.112] | 8 | -0.031 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B | A1 | all | moral | 79 | 0.372 | [0.329, 0.416] | 0 | -0.001 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B | A1 | all | norm | 104 | 0.544 | [0.515, 0.575] | 0 | 0.012 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B | A1 | all | descr | 40 | 0.420 | [0.357, 0.479] | 0 | 0.028 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B | B | all | moral | 78 | 0.275 | [0.221, 0.328] | 0 | 0.034 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B | B | all | norm | 100 | 0.399 | [0.366, 0.434] | 0 | 0.032 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B | B | all | descr | 40 | 0.174 | [0.119, 0.231] | 1 | 0.031 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B-Instruct | A1 | all | moral | 72 | 0.064 | [0.031, 0.099] | 4 | 0.045 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B-Instruct | A1 | all | norm | 103 | 0.188 | [0.151, 0.227] | 0 | 0.063 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B-Instruct | A1 | all | descr | 39 | -0.012 | [-0.071, 0.048] | 18 | 0.074 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B-Instruct | B | all | moral | 69 | -0.082 | [-0.127, -0.038] | 19 | 0.020 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B-Instruct | B | all | norm | 103 | 0.076 | [0.026, 0.124] | 4 | 0.021 | n/a (None) | n/a (None) | n/a (None) |
| Llama-3.2-3B-Instruct | B | all | descr | 39 | -0.032 | [-0.088, 0.024] | 13 | -0.001 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B | A1 | all | moral | 79 | 0.096 | [0.061, 0.134] | 0 | 0.028 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B | A1 | all | norm | 99 | 0.064 | [-0.005, 0.131] | 0 | -0.005 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B | A1 | all | descr | 36 | -0.225 | [-0.458, -0.027] | 12 | -0.213 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B | B | all | moral | 79 | 0.039 | [0.006, 0.078] | 2 | 0.007 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B | B | all | norm | 106 | 0.056 | [0.015, 0.096] | 0 | -0.008 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B | B | all | descr | 40 | -0.031 | [-0.067, -0.001] | 9 | -0.049 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B-Instruct | A1 | all | moral | 79 | 0.147 | [0.102, 0.195] | 0 | 0.011 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B-Instruct | A1 | all | norm | 99 | 0.343 | [0.269, 0.419] | 1 | 0.006 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B-Instruct | A1 | all | descr | 18* | 0.482 | [0.172, 0.811] | 1 | -0.150 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B-Instruct | B | all | moral | 78 | 0.081 | [0.033, 0.131] | 1 | 0.010 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B-Instruct | B | all | norm | 104 | -0.065 | [-0.120, -0.011] | 16 | -0.032 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-14B-Instruct | B | all | descr | 40 | 0.039 | [-0.043, 0.135] | 0 | -0.039 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B | A1 | all | moral | 78 | 1.000 | [0.999, 1.001] | 0 | 0.026 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B | A1 | all | norm | 98 | 0.999 | [0.998, 1.001] | 0 | -0.091 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B | A1 | all | descr | 39 | 0.999 | [0.996, 1.002] | 0 | 0.030 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B | B | all | moral | 75 | 1.000 | [0.998, 1.003] | 0 | -0.095 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B | B | all | norm | 101 | 0.997 | [0.995, 1.000] | 0 | -0.105 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B | B | all | descr | 40 | 0.993 | [0.984, 1.000] | 0 | -0.092 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B-Instruct | A1 | all | moral | 76 | 0.165 | [0.109, 0.224] | 0 | 0.026 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B-Instruct | A1 | all | norm | 103 | 0.242 | [0.194, 0.292] | 0 | 0.026 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B-Instruct | A1 | all | descr | 40 | 0.108 | [0.025, 0.190] | 3 | 0.015 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B-Instruct | B | all | moral | 76 | 0.130 | [0.064, 0.201] | 4 | 0.057 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B-Instruct | B | all | norm | 104 | 0.222 | [0.174, 0.272] | 1 | 0.063 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-3B-Instruct | B | all | descr | 40 | 0.047 | [-0.045, 0.133] | 9 | 0.040 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B | A1 | all | moral | 79 | 0.175 | [0.126, 0.231] | 0 | 0.011 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B | A1 | all | norm | 104 | 0.318 | [0.269, 0.374] | 0 | -0.003 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B | A1 | all | descr | 40 | 0.085 | [0.015, 0.146] | 3 | -0.031 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B | B | all | moral | 77 | 0.160 | [0.105, 0.222] | 0 | 0.003 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B | B | all | norm | 107 | 0.278 | [0.228, 0.336] | 0 | 0.034 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B | B | all | descr | 40 | 0.137 | [0.076, 0.199] | 0 | 0.019 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B-Instruct | A1 | all | moral | 75 | 0.040 | [-0.021, 0.104] | 4 | 0.005 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B-Instruct | A1 | all | norm | 106 | 0.133 | [0.053, 0.216] | 1 | 0.004 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B-Instruct | A1 | all | descr | 40 | -0.261 | [-0.439, -0.104] | 16 | -0.098 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B-Instruct | B | all | moral | 77 | 0.244 | [0.194, 0.304] | 0 | -0.013 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B-Instruct | B | all | norm | 104 | 0.186 | [0.119, 0.250] | 0 | -0.004 | n/a (None) | n/a (None) | n/a (None) |
| Qwen2.5-7B-Instruct | B | all | descr | 40 | 0.020 | [-0.077, 0.107] | 1 | -0.076 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b | A1 | all | moral | 74 | 0.941 | [0.900, 0.983] | 0 | 0.121 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b | A1 | all | norm | 99 | 0.941 | [0.884, 0.994] | 0 | 0.151 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b | A1 | all | descr | 39 | 0.863 | [0.753, 0.964] | 0 | -0.050 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b | B | all | moral | 72 | 0.932 | [0.832, 1.033] | 0 | -0.008 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b | B | all | norm | 95 | 0.834 | [0.760, 0.906] | 0 | 0.142 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b | B | all | descr | 40 | 0.772 | [0.666, 0.874] | 0 | 0.033 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b-it | A1 | all | moral | 73 | 0.257 | [0.177, 0.334] | 0 | 0.108 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b-it | A1 | all | norm | 98 | 0.163 | [0.060, 0.261] | 1 | 0.049 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b-it | A1 | all | descr | 37 | 0.323 | [0.232, 0.409] | 0 | 0.006 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b-it | B | all | moral | 67 | 0.344 | [0.222, 0.467] | 0 | 0.027 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b-it | B | all | norm | 88 | 0.155 | [0.013, 0.287] | 4 | 0.058 | n/a (None) | n/a (None) | n/a (None) |
| gemma-2b-it | B | all | descr | 34 | 0.412 | [0.235, 0.569] | 0 | 0.013 | n/a (None) | n/a (None) | n/a (None) |

\* fewer included items than the minimum of the plan; shown, not pooled.

Moral-specificity of the necessity: fraction removed by located on moral items minus on norm items (bootstrap interval, independent resamples).

| model | frame | mode | moral | norm | difference | 95 % CI |
|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | all | 0.306 | 0.249 | +0.057 | [-0.022, +0.136] |
| Llama-3.1-8B | B | all | 0.204 | 0.263 | -0.058 | [-0.131, +0.013] |
| Llama-3.1-8B-Instruct | A1 | all | 0.256 | 0.350 | -0.094 | [-0.147, -0.038] |
| Llama-3.1-8B-Instruct | B | all | 0.156 | 0.205 | -0.050 | [-0.113, +0.018] |
| Llama-3.2-1B | A1 | all | 0.262 | 0.357 | -0.095 | [-0.171, -0.018] |
| Llama-3.2-1B | B | all | 0.295 | 0.374 | -0.079 | [-0.159, -0.002] |
| Llama-3.2-1B-Instruct | A1 | all | 0.203 | 0.160 | +0.043 | [-0.046, +0.131] |
| Llama-3.2-1B-Instruct | B | all | 0.107 | 0.099 | +0.008 | [-0.089, +0.104] |
| Llama-3.2-3B | A1 | all | 0.372 | 0.544 | -0.172 | [-0.224, -0.121] |
| Llama-3.2-3B | B | all | 0.275 | 0.399 | -0.124 | [-0.188, -0.061] |
| Llama-3.2-3B-Instruct | A1 | all | 0.064 | 0.188 | -0.125 | [-0.175, -0.075] |
| Llama-3.2-3B-Instruct | B | all | -0.082 | 0.076 | -0.158 | [-0.224, -0.094] |
| Qwen2.5-14B | A1 | all | 0.096 | 0.064 | +0.032 | [-0.043, +0.111] |
| Qwen2.5-14B | B | all | 0.039 | 0.056 | -0.017 | [-0.069, +0.039] |
| Qwen2.5-14B-Instruct | A1 | all | 0.147 | 0.343 | -0.196 | [-0.285, -0.106] |
| Qwen2.5-14B-Instruct | B | all | 0.081 | -0.065 | +0.146 | [+0.072, +0.221] |
| Qwen2.5-3B | A1 | all | 1.000 | 0.999 | +0.000 | [-0.001, +0.002] |
| Qwen2.5-3B | B | all | 1.000 | 0.997 | +0.003 | [-0.001, +0.006] |
| Qwen2.5-3B-Instruct | A1 | all | 0.165 | 0.242 | -0.078 | [-0.153, -0.001] |
| Qwen2.5-3B-Instruct | B | all | 0.130 | 0.222 | -0.092 | [-0.171, -0.010] |
| Qwen2.5-7B | A1 | all | 0.175 | 0.318 | -0.143 | [-0.215, -0.071] |
| Qwen2.5-7B | B | all | 0.160 | 0.278 | -0.118 | [-0.196, -0.041] |
| Qwen2.5-7B-Instruct | A1 | all | 0.040 | 0.133 | -0.093 | [-0.196, +0.008] |
| Qwen2.5-7B-Instruct | B | all | 0.244 | 0.186 | +0.058 | [-0.021, +0.147] |
| gemma-2b | A1 | all | 0.941 | 0.941 | +0.000 | [-0.069, +0.071] |
| gemma-2b | B | all | 0.932 | 0.834 | +0.098 | [-0.026, +0.219] |
| gemma-2b-it | A1 | all | 0.257 | 0.163 | +0.093 | [-0.031, +0.217] |
| gemma-2b-it | B | all | 0.344 | 0.155 | +0.189 | [+0.006, +0.381] |

Frame A1, mode all: located beats all 20 random size-10 sets on moral items in 10 of 14 models; median fraction removed 0.230 (random10 mean, median over models: 0.026).

Frame B, mode all: located beats all 20 random size-10 sets on moral items in 8 of 14 models; median fraction removed 0.182 (random10 mean, median over models: 0.015).

## Files

* `necessity.csv` (196 rows)
* `necessity_moral_minus_norm.csv` (28 rows)
* `figures/` (28 figures)
