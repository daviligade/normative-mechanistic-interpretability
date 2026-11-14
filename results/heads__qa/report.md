# Head results (p2r_all, readout S, head set located, items: accepted, inclusion gap >= 0.02)

All options are at their defaults and the item file is the set of accepted pairs: the moral/norm rows for frames A1 and B are the two primary tests (97.5 % intervals).

## Pooled ratios (mean over models of the log ratio; item bootstrap shared across models)

| frame | contrast | models used | left out | pooled ratio | interval | reading |
|---|---|---|---|---|---|---|
| QA | moral/norm | 14 | - | 0.89 | 0.82 to 0.98 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25; it excludes 1, but the difference is within the margin) |
| QA | moral/descr | 13 | Qwen2.5-3B-Instruct | 1.08 | 0.99 to 1.17 (95.0 %) |  |
| QA | norm/descr | 13 | Qwen2.5-3B-Instruct | 1.24 | 1.14 to 1.34 (95.0 %) |  |
| QA | moral/prudential | 14 | - | 0.96 | 0.85 to 1.10 (95.0 %) |  |
| QA | moral/etiquette | 13 | Qwen2.5-3B-Instruct | 0.95 | 0.86 to 1.06 (95.0 %) |  |
| QA | moral/aesthetic | 13 | Qwen2.5-3B-Instruct | 0.98 | 0.89 to 1.08 (95.0 %) |  |
| QA | moral/epistemic | 14 | - | 0.85 | 0.74 to 0.98 (95.0 %) |  |

Other head sets, moral / norm: QA located_top5 0.90 (0.84 to 0.96); QA located_top1 0.91 (0.82 to 1.01); QA topshare10 0.88 (0.81 to 0.96); QA topshare_1pct 0.90 (0.82 to 0.98)

## Per model, moral / norm

| model | frame | n moral | n norm | share moral | share norm | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | 79 | 106 | 0.083 | 0.096 | 0.010 | 0.86 | 0.79 to 0.94 | 0.0008 | 0.0020 |
| Llama-3.1-8B-Instruct | QA | 79 | 106 | 0.091 | 0.115 | 0.010 | 0.79 | 0.69 to 0.91 | 0.0008 | 0.0020 |
| Llama-3.2-1B | QA | 72 | 89 | 0.066 | 0.070 | 0.020 | 0.94 | 0.87 to 1.03 | 0.1878 | 0.2023 |
| Llama-3.2-1B-Instruct | QA | 75 | 91 | 0.045 | 0.037 | 0.020 | 1.20 | 1.10 to 1.32 | 0.0001 | 0.0009 |
| Llama-3.2-3B | QA | 79 | 101 | 0.079 | 0.084 | 0.015 | 0.94 | 0.87 to 1.03 | 0.1855 | 0.2023 |
| Llama-3.2-3B-Instruct | QA | 75 | 104 | 0.060 | 0.104 | 0.015 | 0.58 | 0.49 to 0.70 | 0.0000 | 0.0007 |
| Qwen2.5-14B | QA | 80 | 107 | 0.038 | 0.042 | 0.005 | 0.89 | 0.81 to 0.99 | 0.0354 | 0.0551 |
| Qwen2.5-14B-Instruct | QA | 75 | 95 | 0.052 | 0.041 | 0.005 | 1.27 | 1.02 to 1.55 | 0.0280 | 0.0490 |
| Qwen2.5-3B | QA | 74 | 104 | 0.057 | 0.068 | 0.017 | 0.84 | 0.74 to 0.95 | 0.0053 | 0.0107 |
| Qwen2.5-3B-Instruct | QA | 70 | 68 | 0.131 | 0.103 | 0.017 | 1.27 | 1.12 to 1.44 | 0.0002 | 0.0009 |
| Qwen2.5-7B | QA | 80 | 105 | 0.048 | 0.070 | 0.013 | 0.68 | 0.54 to 0.85 | 0.0003 | 0.0012 |
| Qwen2.5-7B-Instruct | QA | 70 | 80 | 0.037 | 0.070 | 0.013 | 0.53 | 0.23 to 1.29 | 0.1403 | 0.1786 |
| gemma-2b | QA | 73 | 92 | 0.205 | 0.198 | 0.069 | 1.04 | 0.97 to 1.11 | 0.2904 | 0.2904 |
| gemma-2b-it | QA | 70 | 93 | 0.139 | 0.128 | 0.069 | 1.09 | 0.98 to 1.21 | 0.1311 | 0.1786 |

## Per model, moral / descr

| model | frame | n moral | n descr | share moral | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | 79 | 40 | 0.083 | 0.071 | 0.010 | 1.17 | 1.03 to 1.33 | 0.0164 | 0.0535 |
| Llama-3.1-8B-Instruct | QA | 79 | 40 | 0.091 | 0.097 | 0.010 | 0.93 | 0.79 to 1.12 | 0.4950 | 0.8044 |
| Llama-3.2-1B | QA | 72 | 37 | 0.066 | 0.066 | 0.020 | 1.00 | 0.89 to 1.11 | 0.9440 | 0.9955 |
| Llama-3.2-1B-Instruct | QA | 75 | 37 | 0.045 | 0.028 | 0.020 | 1.58 | 1.39 to 1.81 | 0.0000 | 0.0006 |
| Llama-3.2-3B | QA | 79 | 38 | 0.079 | 0.067 | 0.015 | 1.19 | 1.08 to 1.31 | 0.0011 | 0.0075 |
| Llama-3.2-3B-Instruct | QA | 75 | 40 | 0.060 | 0.076 | 0.015 | 0.80 | 0.66 to 0.96 | 0.0331 | 0.0718 |
| Qwen2.5-14B | QA | 80 | 39 | 0.038 | 0.040 | 0.005 | 0.95 | 0.86 to 1.06 | 0.4636 | 0.8044 |
| Qwen2.5-14B-Instruct | QA | 75 | 23 | 0.052 | 0.037 | 0.005 | 1.39 | 1.03 to 1.88 | 0.0283 | 0.0718 |
| Qwen2.5-3B | QA | 74 | 40 | 0.057 | 0.056 | 0.017 | 1.02 | 0.88 to 1.19 | 0.7793 | 0.9955 |
| Qwen2.5-3B-Instruct | QA | 70 | 8 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | QA | 80 | 40 | 0.048 | 0.046 | 0.013 | 1.03 | 0.83 to 1.30 | 0.8527 | 0.9955 |
| Qwen2.5-7B-Instruct | QA | 70 | 28 | 0.037 | 0.036 | 0.013 | 1.02 | 0.51 to 2.08 | 0.9955 | 0.9955 |
| gemma-2b | QA | 73 | 38 | 0.205 | 0.180 | 0.069 | 1.14 | 1.04 to 1.26 | 0.0047 | 0.0206 |
| gemma-2b-it | QA | 70 | 35 | 0.139 | 0.141 | 0.069 | 0.98 | 0.87 to 1.11 | 0.8341 | 0.9955 |

## Per model, norm / descr

| model | frame | n norm | n descr | share norm | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | 106 | 40 | 0.096 | 0.071 | 0.010 | 1.35 | 1.20 to 1.53 | 0.0000 | 0.0003 |
| Llama-3.1-8B-Instruct | QA | 106 | 40 | 0.115 | 0.097 | 0.010 | 1.18 | 1.02 to 1.37 | 0.0331 | 0.0538 |
| Llama-3.2-1B | QA | 89 | 37 | 0.070 | 0.066 | 0.020 | 1.06 | 0.95 to 1.18 | 0.3259 | 0.3852 |
| Llama-3.2-1B-Instruct | QA | 91 | 37 | 0.037 | 0.028 | 0.020 | 1.31 | 1.16 to 1.49 | 0.0001 | 0.0004 |
| Llama-3.2-3B | QA | 101 | 38 | 0.084 | 0.067 | 0.015 | 1.26 | 1.15 to 1.40 | 0.0000 | 0.0003 |
| Llama-3.2-3B-Instruct | QA | 104 | 40 | 0.104 | 0.076 | 0.015 | 1.37 | 1.18 to 1.59 | 0.0005 | 0.0014 |
| Qwen2.5-14B | QA | 107 | 39 | 0.042 | 0.040 | 0.005 | 1.07 | 0.97 to 1.17 | 0.2868 | 0.3728 |
| Qwen2.5-14B-Instruct | QA | 95 | 23 | 0.041 | 0.037 | 0.005 | 1.10 | 0.81 to 1.50 | 0.6969 | 0.6969 |
| Qwen2.5-3B | QA | 104 | 40 | 0.068 | 0.056 | 0.017 | 1.22 | 1.06 to 1.41 | 0.0078 | 0.0169 |
| Qwen2.5-3B-Instruct | QA | 68 | 8 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | QA | 105 | 40 | 0.070 | 0.046 | 0.013 | 1.52 | 1.25 to 1.83 | 0.0005 | 0.0014 |
| Qwen2.5-7B-Instruct | QA | 80 | 28 | 0.070 | 0.036 | 0.013 | 1.93 | 0.96 to 3.48 | 0.3621 | 0.3923 |
| gemma-2b | QA | 92 | 38 | 0.198 | 0.180 | 0.069 | 1.10 | 1.01 to 1.21 | 0.0250 | 0.0464 |
| gemma-2b-it | QA | 93 | 35 | 0.128 | 0.141 | 0.069 | 0.91 | 0.82 to 1.00 | 0.0871 | 0.1258 |

## Base to instruct (moral items)

| frame | pair | r | reliability base / instruct | rank of base top head | prediction met |
|---|---|---|---|---|---|
| QA | Llama-3.2-1B | 0.885 | 0.991 / 0.989 | 8 | True |
| QA | Llama-3.2-3B | 0.867 | 0.994 / 0.972 | 3 | True |
| QA | Llama-3.1-8B | 0.932 | 0.994 / 0.987 | 3 | True |
| QA | gemma-2b | 0.837 | 0.992 / 0.976 | 16 | False |
| QA | Qwen2.5-3B | 0.770 | 0.991 / 0.987 | 12 | False |
| QA | Qwen2.5-7B | 0.875 | 0.982 / 0.922 | 214 | False |
| QA | Qwen2.5-14B | 0.868 | 0.990 / 0.985 | 4 | True |

## Robustness (moral vs norm)

The last two columns select ten heads on half of the NEW items and test on the other half. If heads chosen on norm items show the same ratio in the other direction, a ratio above 1 only says that the two profiles differ.

| model | frame | adjusted logit difference (95 % CI) | unadjusted | gap-matched | rated-size-matched | raw ratio: head set / all heads | moral-selected: moral / norm | norm-selected: norm / moral |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | -0.206 (-0.293 to -0.115) | -0.179 | 0.85 | 0.82 | 0.76 / 0.87 | 1.02 (0.95 to 1.09) | 1.04 (0.97 to 1.09) |
| Llama-3.1-8B-Instruct | QA | -0.279 (-0.409 to -0.148) | -0.279 | 0.80 | 0.74 | 0.49 / 0.55 | 0.85 (0.77 to 0.92) | 1.24 (1.14 to 1.34) |
| Llama-3.2-1B | QA | -0.109 (-0.198 to -0.019) | -0.065 | 0.91 | 0.90 | 1.07 / 1.10 | 1.08 (0.99 to 1.16) | 0.96 (0.88 to 1.04) |
| Llama-3.2-1B-Instruct | QA | +0.198 (+0.100 to +0.295) | +0.190 | 1.19 | 1.18 | 1.38 / 1.14 | 0.99 (0.91 to 1.06) | 1.05 (0.96 to 1.15) |
| Llama-3.2-3B | QA | -0.115 (-0.198 to -0.035) | -0.052 | 0.89 | 0.88 | 1.01 / 1.12 | 1.07 (0.98 to 1.14) | 0.96 (0.91 to 1.03) |
| Llama-3.2-3B-Instruct | QA | -0.591 (-0.747 to -0.432) | -0.603 | 0.56 | 0.57 | 0.40 / 0.59 | 0.79 (0.67 to 0.93) | 1.47 (1.33 to 1.64) |
| Qwen2.5-14B | QA | -0.122 (-0.225 to -0.021) | -0.116 | 0.90 | 0.93 | 0.97 / 1.08 | 0.98 (0.90 to 1.08) | 1.14 (1.07 to 1.20) |
| Qwen2.5-14B-Instruct | QA | +0.214 (+0.076 to +0.354) | +0.245 | 1.17 | 1.36 | 2.42 / 1.89 | 1.38 (1.26 to 1.50) | 0.99 (0.86 to 1.18) |
| Qwen2.5-3B | QA | -0.180 (-0.309 to -0.053) | -0.204 | 0.91 | 0.84 | 0.71 / 0.76 | 0.88 (0.80 to 0.96) | 1.26 (1.15 to 1.34) |
| Qwen2.5-3B-Instruct | QA | +0.343 (+0.212 to +0.466) | +0.298 | 1.28 | 1.20 | 2.95 / 2.30 | 1.28 (1.18 to 1.37) | 0.87 (0.79 to 0.94) |
| Qwen2.5-7B | QA | -0.429 (-0.599 to -0.254) | -0.444 | 0.70 | 0.67 | 0.56 / 0.81 | 1.14 (1.03 to 1.29) | 1.26 (1.13 to 1.41) |
| Qwen2.5-7B-Instruct | QA | -0.501 (-0.955 to -0.093) | -0.478 | 0.46 | 0.40 | 2.29 / 3.63 | 0.97 (0.77 to 1.28) | 1.25 (0.90 to 1.63) |
| gemma-2b | QA | +0.041 (-0.058 to +0.135) | +0.041 | 1.06 | 0.99 | 1.35 / 1.31 | 1.13 (1.07 to 1.20) | 0.91 (0.86 to 0.96) |
| gemma-2b-it | QA | +0.096 (-0.030 to +0.225) | +0.081 | 1.10 | 1.06 | 1.39 / 1.30 | 1.01 (0.92 to 1.11) | 1.08 (1.00 to 1.15) |

## Behaviour

| model | frame | category | run | included | mean gap | correct sign | mean mass |
|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | moral | 80 | 79 | +0.507 | 1.00 | 0.54 |
| Llama-3.1-8B | QA | norm | 107 | 106 | +0.468 | 0.99 | 0.58 |
| Llama-3.1-8B | QA | descr | 40 | 40 | +0.370 | 1.00 | 0.61 |
| Llama-3.1-8B-Instruct | QA | moral | 80 | 79 | +1.043 | 1.00 | 0.71 |
| Llama-3.1-8B-Instruct | QA | norm | 107 | 106 | +1.019 | 0.99 | 0.67 |
| Llama-3.1-8B-Instruct | QA | descr | 40 | 40 | +1.155 | 1.00 | 0.72 |
| Llama-3.2-1B | QA | moral | 80 | 72 | +0.182 | 0.95 | 0.65 |
| Llama-3.2-1B | QA | norm | 107 | 89 | +0.120 | 0.91 | 0.64 |
| Llama-3.2-1B | QA | descr | 40 | 37 | +0.174 | 0.97 | 0.61 |
| Llama-3.2-1B-Instruct | QA | moral | 80 | 75 | +0.269 | 0.96 | 0.53 |
| Llama-3.2-1B-Instruct | QA | norm | 107 | 91 | +0.199 | 0.86 | 0.56 |
| Llama-3.2-1B-Instruct | QA | descr | 40 | 37 | +0.333 | 0.93 | 0.62 |
| Llama-3.2-3B | QA | moral | 80 | 79 | +0.334 | 0.99 | 0.50 |
| Llama-3.2-3B | QA | norm | 107 | 101 | +0.230 | 0.95 | 0.48 |
| Llama-3.2-3B | QA | descr | 40 | 38 | +0.216 | 0.95 | 0.49 |
| Llama-3.2-3B-Instruct | QA | moral | 80 | 75 | +1.061 | 0.95 | 0.72 |
| Llama-3.2-3B-Instruct | QA | norm | 107 | 104 | +1.057 | 0.97 | 0.67 |
| Llama-3.2-3B-Instruct | QA | descr | 40 | 40 | +1.096 | 1.00 | 0.68 |
| Qwen2.5-14B | QA | moral | 80 | 80 | +0.779 | 1.00 | 0.44 |
| Qwen2.5-14B | QA | norm | 107 | 107 | +0.621 | 1.00 | 0.38 |
| Qwen2.5-14B | QA | descr | 40 | 39 | +0.317 | 1.00 | 0.20 |
| Qwen2.5-14B-Instruct | QA | moral | 80 | 75 | +0.839 | 0.99 | 0.43 |
| Qwen2.5-14B-Instruct | QA | norm | 107 | 95 | +0.565 | 1.00 | 0.30 |
| Qwen2.5-14B-Instruct | QA | descr | 40 | 23 | +0.189 | 1.00 | 0.09 |
| Qwen2.5-3B | QA | moral | 80 | 74 | +0.665 | 0.96 | 0.53 |
| Qwen2.5-3B | QA | norm | 107 | 104 | +0.570 | 0.97 | 0.44 |
| Qwen2.5-3B | QA | descr | 40 | 40 | +0.578 | 1.00 | 0.42 |
| Qwen2.5-3B-Instruct | QA | moral | 80 | 70 | +0.159 | 0.97 | 0.09 |
| Qwen2.5-3B-Instruct | QA | norm | 107 | 68 | +0.088 | 0.93 | 0.05 |
| Qwen2.5-3B-Instruct | QA | descr | 40 | 8 | +0.007 | 0.57 | 0.01 |
| Qwen2.5-7B | QA | moral | 80 | 80 | +0.432 | 1.00 | 0.30 |
| Qwen2.5-7B | QA | norm | 107 | 105 | +0.453 | 0.99 | 0.34 |
| Qwen2.5-7B | QA | descr | 40 | 40 | +0.574 | 1.00 | 0.40 |
| Qwen2.5-7B-Instruct | QA | moral | 80 | 70 | +0.465 | 0.97 | 0.25 |
| Qwen2.5-7B-Instruct | QA | norm | 107 | 80 | +0.266 | 0.96 | 0.15 |
| Qwen2.5-7B-Instruct | QA | descr | 40 | 28 | +0.237 | 1.00 | 0.12 |
| gemma-2b | QA | moral | 80 | 73 | +0.187 | 0.93 | 0.35 |
| gemma-2b | QA | norm | 107 | 92 | +0.108 | 0.96 | 0.33 |
| gemma-2b | QA | descr | 40 | 38 | +0.182 | 0.95 | 0.38 |
| gemma-2b-it | QA | moral | 80 | 70 | +0.647 | 0.91 | 0.54 |
| gemma-2b-it | QA | norm | 107 | 93 | +0.549 | 0.93 | 0.37 |
| gemma-2b-it | QA | descr | 40 | 35 | +0.653 | 0.97 | 0.37 |
