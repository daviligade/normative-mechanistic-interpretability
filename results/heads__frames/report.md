# Head results (p2r_all, readout S, head set located, items: accepted, inclusion gap >= 0.02)

All options are at their defaults and the item file is the set of accepted pairs: the moral/norm rows for frames A1 and B are the two primary tests (97.5 % intervals).

## Pooled ratios (mean over models of the log ratio; item bootstrap shared across models)

| frame | contrast | models used | left out | pooled ratio | interval | reading |
|---|---|---|---|---|---|---|
| A0s | moral/norm | 14 | - | 1.08 | 1.02 to 1.14 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25; it excludes 1, but the difference is within the margin) |
| A0s | moral/descr | 10 | Llama-3.2-1B, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B | 1.19 | 1.12 to 1.27 (95.0 %) |  |
| A0s | norm/descr | 10 | Llama-3.2-1B, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B | 1.11 | 1.05 to 1.18 (95.0 %) |  |
| A0s | moral/prudential | 9 | Llama-3.2-3B, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-7B-Instruct | 1.15 | 1.04 to 1.29 (95.0 %) |  |
| A0s | moral/etiquette | 13 | Qwen2.5-3B | 1.03 | 0.94 to 1.14 (95.0 %) |  |
| A0s | moral/aesthetic | 14 | - | 1.15 | 1.07 to 1.25 (95.0 %) |  |
| A0s | moral/epistemic | 13 | Qwen2.5-14B | 0.98 | 0.91 to 1.07 (95.0 %) |  |
| B0 | moral/norm | 4 | Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B-Instruct, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it | 0.84 | 0.76 to 0.94 (95.0 %) | the published heads carry a SMALLER share for moral than for norm content (interval below 1) |
| B0 | moral/etiquette | 2 | Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Llama-3.2-3B-Instruct, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it | 0.92 | 0.76 to 1.15 (95.0 %) |  |
| B0 | moral/epistemic | 4 | Llama-3.1-8B-Instruct, Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B-Instruct, Qwen2.5-14B-Instruct, Qwen2.5-3B, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, gemma-2b, gemma-2b-it | 0.82 | 0.71 to 0.96 (95.0 %) |  |

Other head sets, moral / norm: A0s located_top5 1.12 (1.04 to 1.20); A0s located_top1 1.31 (1.16 to 1.48); A0s topshare10 1.08 (1.02 to 1.14); A0s topshare_1pct 1.07 (0.99 to 1.16); B0 located_top5 0.85 (0.73 to 0.99); B0 located_top1 0.78 (0.61 to 1.01); B0 topshare10 0.86 (0.78 to 0.96); B0 topshare_1pct 0.87 (0.78 to 0.97)

## Per model, moral / norm

| model | frame | n moral | n norm | share moral | share norm | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0s | 73 | 78 | 0.084 | 0.075 | 0.010 | 1.12 | 1.00 to 1.26 | 0.0513 | 0.1797 |
| Llama-3.1-8B-Instruct | A0s | 75 | 73 | 0.097 | 0.087 | 0.010 | 1.12 | 0.99 to 1.27 | 0.0753 | 0.1815 |
| Llama-3.2-1B | A0s | 68 | 79 | 0.074 | 0.075 | 0.020 | 0.98 | 0.91 to 1.06 | 0.6418 | 0.6911 |
| Llama-3.2-1B-Instruct | A0s | 74 | 79 | 0.051 | 0.041 | 0.020 | 1.22 | 1.09 to 1.36 | 0.0009 | 0.0126 |
| Llama-3.2-3B | A0s | 67 | 70 | 0.111 | 0.101 | 0.015 | 1.10 | 0.98 to 1.23 | 0.0907 | 0.1815 |
| Llama-3.2-3B-Instruct | A0s | 79 | 85 | 0.131 | 0.120 | 0.015 | 1.09 | 0.97 to 1.22 | 0.1635 | 0.2862 |
| Qwen2.5-14B | A0s | 78 | 67 | 0.046 | 0.038 | 0.005 | 1.20 | 1.01 to 1.40 | 0.0345 | 0.1797 |
| Qwen2.5-14B-Instruct | A0s | 75 | 53 | 0.040 | 0.034 | 0.005 | 1.19 | 0.99 to 1.41 | 0.0848 | 0.1815 |
| Qwen2.5-3B | A0s | 54 | 59 | 0.075 | 0.071 | 0.017 | 1.06 | 0.88 to 1.27 | 0.5749 | 0.6911 |
| Qwen2.5-3B-Instruct | A0s | 76 | 86 | 0.094 | 0.082 | 0.017 | 1.15 | 1.00 to 1.30 | 0.0490 | 0.1797 |
| Qwen2.5-7B | A0s | 77 | 74 | 0.062 | 0.065 | 0.013 | 0.95 | 0.82 to 1.09 | 0.4343 | 0.6755 |
| Qwen2.5-7B-Instruct | A0s | 72 | 71 | 0.052 | 0.052 | 0.013 | 0.99 | 0.82 to 1.20 | 0.9548 | 0.9548 |
| gemma-2b | A0s | 59 | 72 | 0.200 | 0.195 | 0.069 | 1.02 | 0.93 to 1.13 | 0.6327 | 0.6911 |
| gemma-2b-it | A0s | 74 | 82 | 0.154 | 0.159 | 0.069 | 0.97 | 0.89 to 1.07 | 0.5883 | 0.6911 |
| Llama-3.1-8B | B0 | 62 | 39 | 0.052 | 0.059 | 0.010 | 0.88 | 0.75 to 1.03 | 0.1273 | 0.1697 |
| Llama-3.1-8B-Instruct | B0 | 54 | 27 | insufficient behavioural contrast: norm | | | | | | |
| Llama-3.2-1B | B0 | 38 | 14 | insufficient behavioural contrast: norm | | | | | | |
| Llama-3.2-1B-Instruct | B0 | 34 | 11 | insufficient behavioural contrast: norm | | | | | | |
| Llama-3.2-3B | B0 | 54 | 32 | 0.067 | 0.089 | 0.015 | 0.75 | 0.65 to 0.88 | 0.0006 | 0.0026 |
| Llama-3.2-3B-Instruct | B0 | 40 | 16 | insufficient behavioural contrast: norm | | | | | | |
| Qwen2.5-14B | B0 | 64 | 33 | 0.025 | 0.030 | 0.005 | 0.85 | 0.69 to 1.04 | 0.1146 | 0.1697 |
| Qwen2.5-14B-Instruct | B0 | 42 | 21 | insufficient behavioural contrast: norm | | | | | | |
| Qwen2.5-3B | B0 | 26 | 13 | insufficient behavioural contrast: moral, norm | | | | | | |
| Qwen2.5-3B-Instruct | B0 | 49 | 23 | insufficient behavioural contrast: norm | | | | | | |
| Qwen2.5-7B | B0 | 58 | 37 | 0.062 | 0.070 | 0.013 | 0.88 | 0.69 to 1.14 | 0.3605 | 0.3605 |
| Qwen2.5-7B-Instruct | B0 | 25 | 15 | insufficient behavioural contrast: moral, norm | | | | | | |
| gemma-2b | B0 | 40 | 22 | insufficient behavioural contrast: norm | | | | | | |
| gemma-2b-it | B0 | 49 | 22 | insufficient behavioural contrast: norm | | | | | | |

## Per model, moral / descr

| model | frame | n moral | n descr | share moral | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0s | 73 | 29 | 0.084 | 0.068 | 0.010 | 1.24 | 1.08 to 1.43 | 0.0070 | 0.0140 |
| Llama-3.1-8B-Instruct | A0s | 75 | 23 | 0.097 | 0.073 | 0.010 | 1.33 | 1.13 to 1.59 | 0.0028 | 0.0071 |
| Llama-3.2-1B | A0s | 68 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A0s | 74 | 24 | 0.051 | 0.038 | 0.020 | 1.34 | 1.18 to 1.51 | 0.0004 | 0.0022 |
| Llama-3.2-3B | A0s | 67 | 30 | 0.111 | 0.090 | 0.015 | 1.24 | 1.10 to 1.39 | 0.0016 | 0.0055 |
| Llama-3.2-3B-Instruct | A0s | 79 | 39 | 0.131 | 0.094 | 0.015 | 1.38 | 1.22 to 1.57 | 0.0000 | 0.0005 |
| Qwen2.5-14B | A0s | 78 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A0s | 75 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A0s | 54 | 2 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A0s | 76 | 26 | 0.094 | 0.077 | 0.017 | 1.22 | 1.03 to 1.45 | 0.0475 | 0.0792 |
| Qwen2.5-7B | A0s | 77 | 29 | 0.062 | 0.061 | 0.013 | 1.01 | 0.85 to 1.22 | 0.9145 | 0.9841 |
| Qwen2.5-7B-Instruct | A0s | 72 | 28 | 0.052 | 0.043 | 0.013 | 1.20 | 0.99 to 1.48 | 0.1248 | 0.1783 |
| gemma-2b | A0s | 59 | 23 | 0.200 | 0.194 | 0.069 | 1.03 | 0.90 to 1.19 | 0.6361 | 0.7951 |
| gemma-2b-it | A0s | 74 | 32 | 0.154 | 0.155 | 0.069 | 1.00 | 0.89 to 1.13 | 0.9841 | 0.9841 |
| Llama-3.1-8B | B0 | 62 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | B0 | 54 | 10 | insufficient behavioural contrast: descr, norm | | | | | | |
| Llama-3.2-1B | B0 | 38 | 9 | insufficient behavioural contrast: descr, norm | | | | | | |
| Llama-3.2-1B-Instruct | B0 | 34 | 3 | insufficient behavioural contrast: descr, norm | | | | | | |
| Llama-3.2-3B | B0 | 54 | 10 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | B0 | 40 | 5 | insufficient behavioural contrast: descr, norm | | | | | | |
| Qwen2.5-14B | B0 | 64 | 15 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | B0 | 42 | 12 | insufficient behavioural contrast: descr, norm | | | | | | |
| Qwen2.5-3B | B0 | 26 | 0 | insufficient behavioural contrast: descr, moral, norm | | | | | | |
| Qwen2.5-3B-Instruct | B0 | 49 | 10 | insufficient behavioural contrast: descr, norm | | | | | | |
| Qwen2.5-7B | B0 | 58 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | B0 | 25 | 8 | insufficient behavioural contrast: descr, moral, norm | | | | | | |
| gemma-2b | B0 | 40 | 10 | insufficient behavioural contrast: descr, norm | | | | | | |
| gemma-2b-it | B0 | 49 | 9 | insufficient behavioural contrast: descr, norm | | | | | | |

## Per model, norm / descr

| model | frame | n norm | n descr | share norm | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0s | 78 | 29 | 0.075 | 0.068 | 0.010 | 1.10 | 0.96 to 1.28 | 0.2117 | 0.4106 |
| Llama-3.1-8B-Instruct | A0s | 73 | 23 | 0.087 | 0.073 | 0.010 | 1.19 | 1.01 to 1.42 | 0.0587 | 0.2935 |
| Llama-3.2-1B | A0s | 79 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A0s | 79 | 24 | 0.041 | 0.038 | 0.020 | 1.09 | 0.97 to 1.22 | 0.2464 | 0.4106 |
| Llama-3.2-3B | A0s | 70 | 30 | 0.101 | 0.090 | 0.015 | 1.13 | 1.00 to 1.27 | 0.0880 | 0.2935 |
| Llama-3.2-3B-Instruct | A0s | 85 | 39 | 0.120 | 0.094 | 0.015 | 1.27 | 1.13 to 1.44 | 0.0008 | 0.0085 |
| Qwen2.5-14B | A0s | 67 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A0s | 53 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A0s | 59 | 2 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A0s | 86 | 26 | 0.082 | 0.077 | 0.017 | 1.07 | 0.91 to 1.26 | 0.4725 | 0.6530 |
| Qwen2.5-7B | A0s | 74 | 29 | 0.065 | 0.061 | 0.013 | 1.07 | 0.89 to 1.30 | 0.5224 | 0.6530 |
| Qwen2.5-7B-Instruct | A0s | 71 | 28 | 0.052 | 0.043 | 0.013 | 1.21 | 0.99 to 1.50 | 0.1430 | 0.3575 |
| gemma-2b | A0s | 72 | 23 | 0.195 | 0.194 | 0.069 | 1.01 | 0.88 to 1.16 | 0.9340 | 0.9340 |
| gemma-2b-it | A0s | 82 | 32 | 0.159 | 0.155 | 0.069 | 1.02 | 0.92 to 1.14 | 0.6640 | 0.7377 |
| Llama-3.1-8B | B0 | 39 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | B0 | 27 | 10 | insufficient behavioural contrast: descr, norm | | | | | | |
| Llama-3.2-1B | B0 | 14 | 9 | insufficient behavioural contrast: descr, norm | | | | | | |
| Llama-3.2-1B-Instruct | B0 | 11 | 3 | insufficient behavioural contrast: descr, norm | | | | | | |
| Llama-3.2-3B | B0 | 32 | 10 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | B0 | 16 | 5 | insufficient behavioural contrast: descr, norm | | | | | | |
| Qwen2.5-14B | B0 | 33 | 15 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | B0 | 21 | 12 | insufficient behavioural contrast: descr, norm | | | | | | |
| Qwen2.5-3B | B0 | 13 | 0 | insufficient behavioural contrast: descr, moral, norm | | | | | | |
| Qwen2.5-3B-Instruct | B0 | 23 | 10 | insufficient behavioural contrast: descr, norm | | | | | | |
| Qwen2.5-7B | B0 | 37 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | B0 | 15 | 8 | insufficient behavioural contrast: descr, moral, norm | | | | | | |
| gemma-2b | B0 | 22 | 10 | insufficient behavioural contrast: descr, norm | | | | | | |
| gemma-2b-it | B0 | 22 | 9 | insufficient behavioural contrast: descr, norm | | | | | | |

## Base to instruct (moral items)

| frame | pair | r | reliability base / instruct | rank of base top head | prediction met |
|---|---|---|---|---|---|
| A0s | Llama-3.2-1B | 0.906 | 0.984 / 0.975 | 6 | True |
| A0s | Llama-3.2-3B | 0.945 | 0.988 / 0.992 | 3 | True |
| A0s | Llama-3.1-8B | 0.985 | 0.987 / 0.989 | 2 | True |
| A0s | gemma-2b | 0.716 | 0.978 / 0.988 | 7 | False |
| A0s | Qwen2.5-3B | 0.836 | 0.935 / 0.968 | 4 | True |
| A0s | Qwen2.5-7B | 0.917 | 0.977 / 0.962 | 14 | False |
| A0s | Qwen2.5-14B | 0.945 | 0.977 / 0.959 | 1 | True |
| B0 | Llama-3.2-1B | 0.932 | 0.960 / 0.952 | 8 | True |
| B0 | Llama-3.2-3B | 0.943 | 0.969 / 0.966 | 1 | True |
| B0 | Llama-3.1-8B | 0.976 | 0.974 / 0.966 | 1 | True |
| B0 | gemma-2b | 0.903 | 0.963 / 0.969 | 8 | True |
| B0 | Qwen2.5-14B | 0.924 | 0.971 / 0.929 | 2 | True |

## Robustness (moral vs norm)

The last two columns select ten heads on half of the NEW items and test on the other half. If heads chosen on norm items show the same ratio in the other direction, a ratio above 1 only says that the two profiles differ.

| model | frame | adjusted logit difference (95 % CI) | unadjusted | gap-matched | rated-size-matched | raw ratio: head set / all heads | moral-selected: moral / norm | norm-selected: norm / moral |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0s | +0.092 (-0.020 to +0.206) | +0.126 | 1.09 | 0.98 | 1.25 / 1.13 | 1.09 (0.99 to 1.17) | 0.97 (0.91 to 1.03) |
| Llama-3.1-8B | B0 | -0.182 (-0.320 to -0.039) | -0.127 | 0.87 | 0.88 | 1.13 / 1.29 | 0.87 (0.81 to 0.95) | 1.15 (1.02 to 1.31) |
| Llama-3.1-8B-Instruct | A0s | -0.028 (-0.150 to +0.098) | +0.124 | 1.01 | 1.01 | 1.33 / 1.20 | 1.17 (1.05 to 1.29) | 0.92 (0.85 to 1.00) |
| Llama-3.2-1B | A0s | -0.029 (-0.113 to +0.053) | -0.013 | 0.97 | 0.98 | 1.08 / 1.11 | 1.12 (1.00 to 1.23) | 1.04 (0.93 to 1.15) |
| Llama-3.2-1B-Instruct | A0s | +0.191 (+0.069 to +0.310) | +0.206 | 1.23 | 1.19 | 1.15 / 0.87 | 0.96 (0.85 to 1.11) | 1.24 (1.13 to 1.34) |
| Llama-3.2-3B | A0s | +0.031 (-0.090 to +0.148) | +0.111 | 1.04 | 1.00 | 1.38 / 1.28 | 1.16 (1.07 to 1.26) | 0.90 (0.83 to 0.98) |
| Llama-3.2-3B | B0 | -0.398 (-0.570 to -0.215) | -0.302 | 0.74 | 0.68 | 1.00 / 1.27 | 0.83 (0.77 to 0.90) | 1.29 (1.14 to 1.44) |
| Llama-3.2-3B-Instruct | A0s | -0.061 (-0.187 to +0.060) | +0.085 | 0.93 | 0.98 | 0.97 / 0.93 | 1.19 (1.10 to 1.28) | 0.84 (0.77 to 0.90) |
| Qwen2.5-14B | A0s | -0.032 (-0.193 to +0.134) | +0.156 | 1.04 | 1.09 | 1.12 / 0.99 | 1.16 (1.01 to 1.35) | 1.03 (0.90 to 1.15) |
| Qwen2.5-14B | B0 | -0.214 (-0.411 to -0.026) | -0.180 | 0.84 | 0.92 | 1.34 / 1.38 | 0.89 (0.79 to 0.99) | 1.23 (1.06 to 1.41) |
| Qwen2.5-14B-Instruct | A0s | -0.064 (-0.248 to +0.129) | +0.083 | 1.01 | 1.15 | 1.36 / 1.25 | 1.16 (0.99 to 1.33) | 0.99 (0.83 to 1.13) |
| Qwen2.5-3B | A0s | -0.031 (-0.200 to +0.124) | +0.044 | 1.03 | 1.23 | 1.74 / 1.76 | 0.97 (0.83 to 1.12) | 0.96 (0.85 to 1.06) |
| Qwen2.5-3B-Instruct | A0s | +0.076 (-0.049 to +0.201) | +0.117 | 1.06 | 1.07 | 0.97 / 0.91 | 1.10 (0.96 to 1.23) | 1.01 (0.91 to 1.11) |
| Qwen2.5-7B | A0s | -0.020 (-0.160 to +0.125) | -0.034 | 0.95 | 0.91 | 0.99 / 1.03 | 0.99 (0.88 to 1.08) | 1.11 (0.99 to 1.21) |
| Qwen2.5-7B | B0 | -0.181 (-0.440 to +0.075) | -0.168 | 0.93 | 0.80 | 1.48 / 1.59 | 0.99 (0.81 to 1.13) | 1.46 (1.23 to 1.70) |
| Qwen2.5-7B-Instruct | A0s | -0.035 (-0.216 to +0.148) | -0.022 | 0.99 | 1.08 | 1.20 / 1.21 | 1.01 (0.90 to 1.12) | 0.97 (0.86 to 1.07) |
| gemma-2b | A0s | +0.042 (-0.089 to +0.170) | +0.043 | 1.03 | 1.03 | 1.24 / 1.24 | 0.98 (0.91 to 1.08) | 1.12 (1.04 to 1.23) |
| gemma-2b-it | A0s | -0.042 (-0.146 to +0.063) | -0.039 | 0.98 | 1.02 | 0.43 / 0.47 | 1.27 (1.16 to 1.41) | 0.81 (0.76 to 0.86) |

## Behaviour

| model | frame | category | run | included | mean gap | correct sign | mean mass |
|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0s | moral | 80 | 73 | +0.378 | 0.91 | 0.50 |
| Llama-3.1-8B | A0s | norm | 107 | 78 | +0.222 | 0.76 | 0.48 |
| Llama-3.1-8B | A0s | descr | 40 | 29 | +0.118 | 0.95 | 0.18 |
| Llama-3.1-8B | B0 | moral | 80 | 62 | +0.051 | 0.96 | 0.04 |
| Llama-3.1-8B | B0 | norm | 107 | 39 | +0.022 | 0.82 | 0.02 |
| Llama-3.1-8B | B0 | descr | 40 | 13 | +0.024 | 0.93 | 0.02 |
| Llama-3.1-8B-Instruct | A0s | moral | 80 | 75 | +0.470 | 0.94 | 0.52 |
| Llama-3.1-8B-Instruct | A0s | norm | 107 | 73 | +0.180 | 0.71 | 0.46 |
| Llama-3.1-8B-Instruct | A0s | descr | 40 | 23 | +0.070 | 0.68 | 0.18 |
| Llama-3.1-8B-Instruct | B0 | moral | 80 | 54 | +0.038 | 0.96 | 0.03 |
| Llama-3.1-8B-Instruct | B0 | norm | 107 | 27 | +0.013 | 0.80 | 0.01 |
| Llama-3.1-8B-Instruct | B0 | descr | 40 | 10 | +0.022 | 0.97 | 0.02 |
| Llama-3.2-1B | A0s | moral | 80 | 68 | +0.243 | 0.86 | 0.49 |
| Llama-3.2-1B | A0s | norm | 107 | 79 | +0.164 | 0.77 | 0.49 |
| Llama-3.2-1B | A0s | descr | 40 | 19 | +0.083 | 0.72 | 0.20 |
| Llama-3.2-1B | B0 | moral | 80 | 38 | +0.029 | 0.84 | 0.03 |
| Llama-3.2-1B | B0 | norm | 107 | 14 | +0.008 | 0.78 | 0.02 |
| Llama-3.2-1B | B0 | descr | 40 | 9 | +0.012 | 0.90 | 0.02 |
| Llama-3.2-1B-Instruct | A0s | moral | 80 | 74 | +0.392 | 0.93 | 0.52 |
| Llama-3.2-1B-Instruct | A0s | norm | 107 | 79 | +0.215 | 0.80 | 0.45 |
| Llama-3.2-1B-Instruct | A0s | descr | 40 | 24 | +0.119 | 0.88 | 0.19 |
| Llama-3.2-1B-Instruct | B0 | moral | 80 | 34 | +0.024 | 0.86 | 0.02 |
| Llama-3.2-1B-Instruct | B0 | norm | 107 | 11 | +0.007 | 0.72 | 0.01 |
| Llama-3.2-1B-Instruct | B0 | descr | 40 | 3 | +0.005 | 0.90 | 0.01 |
| Llama-3.2-3B | A0s | moral | 80 | 67 | +0.304 | 0.84 | 0.53 |
| Llama-3.2-3B | A0s | norm | 107 | 70 | +0.139 | 0.68 | 0.56 |
| Llama-3.2-3B | A0s | descr | 40 | 30 | +0.144 | 0.88 | 0.25 |
| Llama-3.2-3B | B0 | moral | 80 | 54 | +0.039 | 0.95 | 0.04 |
| Llama-3.2-3B | B0 | norm | 107 | 32 | +0.015 | 0.80 | 0.02 |
| Llama-3.2-3B | B0 | descr | 40 | 10 | +0.019 | 0.90 | 0.02 |
| Llama-3.2-3B-Instruct | A0s | moral | 80 | 79 | +0.754 | 0.99 | 0.72 |
| Llama-3.2-3B-Instruct | A0s | norm | 107 | 85 | +0.355 | 0.80 | 0.66 |
| Llama-3.2-3B-Instruct | A0s | descr | 40 | 39 | +0.249 | 1.00 | 0.37 |
| Llama-3.2-3B-Instruct | B0 | moral | 80 | 40 | +0.035 | 0.96 | 0.02 |
| Llama-3.2-3B-Instruct | B0 | norm | 107 | 16 | +0.010 | 0.79 | 0.01 |
| Llama-3.2-3B-Instruct | B0 | descr | 40 | 5 | +0.012 | 0.88 | 0.01 |
| Qwen2.5-14B | A0s | moral | 80 | 78 | +0.544 | 0.97 | 0.47 |
| Qwen2.5-14B | A0s | norm | 107 | 67 | +0.176 | 0.65 | 0.43 |
| Qwen2.5-14B | A0s | descr | 40 | 18 | +0.026 | 0.72 | 0.12 |
| Qwen2.5-14B | B0 | moral | 80 | 64 | +0.049 | 0.96 | 0.04 |
| Qwen2.5-14B | B0 | norm | 107 | 33 | +0.018 | 0.77 | 0.02 |
| Qwen2.5-14B | B0 | descr | 40 | 15 | +0.029 | 0.97 | 0.03 |
| Qwen2.5-14B-Instruct | A0s | moral | 80 | 75 | +0.550 | 0.96 | 0.50 |
| Qwen2.5-14B-Instruct | A0s | norm | 107 | 53 | +0.113 | 0.54 | 0.43 |
| Qwen2.5-14B-Instruct | A0s | descr | 40 | 12 | +0.002 | 0.72 | 0.09 |
| Qwen2.5-14B-Instruct | B0 | moral | 80 | 42 | +0.038 | 0.95 | 0.03 |
| Qwen2.5-14B-Instruct | B0 | norm | 107 | 21 | +0.013 | 0.80 | 0.02 |
| Qwen2.5-14B-Instruct | B0 | descr | 40 | 12 | +0.029 | 0.88 | 0.02 |
| Qwen2.5-3B | A0s | moral | 80 | 54 | +0.258 | 0.79 | 0.33 |
| Qwen2.5-3B | A0s | norm | 107 | 59 | +0.140 | 0.69 | 0.27 |
| Qwen2.5-3B | A0s | descr | 40 | 2 | +0.003 | 0.62 | 0.01 |
| Qwen2.5-3B | B0 | moral | 80 | 26 | +0.025 | 0.71 | 0.02 |
| Qwen2.5-3B | B0 | norm | 107 | 13 | +0.008 | 0.70 | 0.01 |
| Qwen2.5-3B | B0 | descr | 40 | 0 | +0.001 | 0.65 | 0.00 |
| Qwen2.5-3B-Instruct | A0s | moral | 80 | 76 | +0.612 | 0.96 | 0.54 |
| Qwen2.5-3B-Instruct | A0s | norm | 107 | 86 | +0.307 | 0.83 | 0.49 |
| Qwen2.5-3B-Instruct | A0s | descr | 40 | 26 | +0.100 | 0.88 | 0.14 |
| Qwen2.5-3B-Instruct | B0 | moral | 80 | 49 | +0.042 | 0.91 | 0.03 |
| Qwen2.5-3B-Instruct | B0 | norm | 107 | 23 | +0.013 | 0.85 | 0.02 |
| Qwen2.5-3B-Instruct | B0 | descr | 40 | 10 | +0.012 | 0.93 | 0.01 |
| Qwen2.5-7B | A0s | moral | 80 | 77 | +0.448 | 0.96 | 0.49 |
| Qwen2.5-7B | A0s | norm | 107 | 74 | +0.231 | 0.78 | 0.47 |
| Qwen2.5-7B | A0s | descr | 40 | 29 | +0.116 | 0.88 | 0.20 |
| Qwen2.5-7B | B0 | moral | 80 | 58 | +0.049 | 0.99 | 0.04 |
| Qwen2.5-7B | B0 | norm | 107 | 37 | +0.019 | 0.79 | 0.02 |
| Qwen2.5-7B | B0 | descr | 40 | 14 | +0.031 | 0.97 | 0.03 |
| Qwen2.5-7B-Instruct | A0s | moral | 80 | 72 | +0.336 | 0.95 | 0.40 |
| Qwen2.5-7B-Instruct | A0s | norm | 107 | 71 | +0.185 | 0.71 | 0.37 |
| Qwen2.5-7B-Instruct | A0s | descr | 40 | 28 | +0.098 | 0.93 | 0.13 |
| Qwen2.5-7B-Instruct | B0 | moral | 80 | 25 | +0.023 | 0.74 | 0.02 |
| Qwen2.5-7B-Instruct | B0 | norm | 107 | 15 | +0.008 | 0.69 | 0.01 |
| Qwen2.5-7B-Instruct | B0 | descr | 40 | 8 | +0.033 | 0.93 | 0.02 |
| gemma-2b | A0s | moral | 80 | 59 | +0.228 | 0.76 | 0.51 |
| gemma-2b | A0s | norm | 107 | 72 | +0.150 | 0.69 | 0.52 |
| gemma-2b | A0s | descr | 40 | 23 | +0.065 | 0.70 | 0.16 |
| gemma-2b | B0 | moral | 80 | 40 | +0.026 | 0.88 | 0.03 |
| gemma-2b | B0 | norm | 107 | 22 | +0.011 | 0.76 | 0.02 |
| gemma-2b | B0 | descr | 40 | 10 | +0.018 | 0.90 | 0.02 |
| gemma-2b-it | A0s | moral | 80 | 74 | +0.493 | 0.93 | 0.61 |
| gemma-2b-it | A0s | norm | 107 | 82 | +0.358 | 0.80 | 0.56 |
| gemma-2b-it | A0s | descr | 40 | 32 | +0.446 | 0.88 | 0.55 |
| gemma-2b-it | B0 | moral | 80 | 49 | +0.087 | 0.80 | 0.08 |
| gemma-2b-it | B0 | norm | 107 | 22 | +0.014 | 0.65 | 0.02 |
| gemma-2b-it | B0 | descr | 40 | 9 | +0.030 | 0.90 | 0.02 |
