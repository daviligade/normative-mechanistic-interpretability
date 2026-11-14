# The located heads' share by kind of pair, frames A0, A0s

Pairs: moral 80, norm 107, thing 40, etiquette 18, othernorm 85. No control pairs in this run (--no-controls). Runs: runs/heads, runs/heads_frames. Head set located, condition p2r_all, effects read on S, a pair is included when its gap in S is at least 0.02, 10000 bootstrap resamples.

No check against the study's output was asked for (--check).

## Pooled ratios of the located heads' share (geometric mean over models; 95 % interval from the item bootstrap)

| frame | contrast | models | ratio | 95 % interval | within template types | models with interval above 1 / below 1 | left out |
|---|---|---|---|---|---|---|---|
| A0 | norm/thing | 13 | 1.14 | [1.08, 1.21] |  | 5 / 0 | Qwen2.5-3B |
| A0 | moral/thing | 13 | 1.27 | [1.19, 1.35] |  | 11 / 0 | Qwen2.5-3B |
| A0 | moral/norm | 14 | 1.12 | [1.05, 1.18] |  | 5 / 0 | - |
| A0 | moral/etiquette | 14 | 1.10 | [1.00, 1.22] |  | 2 / 0 | - |
| A0 | etiquette/othernorm | 14 | 1.02 | [0.92, 1.12] |  | 1 / 0 | - |
| A0 | moral/othernorm | 14 | 1.13 | [1.06, 1.20] |  | 5 / 0 | - |
| A0s | norm/thing | 10 | 1.11 | [1.05, 1.18] |  | 3 / 0 | Llama-3.2-1B, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B |
| A0s | moral/thing | 10 | 1.19 | [1.12, 1.27] |  | 6 / 0 | Llama-3.2-1B, Qwen2.5-14B, Qwen2.5-14B-Instruct, Qwen2.5-3B |
| A0s | moral/norm | 14 | 1.08 | [1.02, 1.14] |  | 3 / 0 | - |
| A0s | moral/etiquette | 13 | 1.03 | [0.94, 1.14] |  | 2 / 1 | Qwen2.5-3B |
| A0s | etiquette/othernorm | 13 | 1.08 | [0.97, 1.18] |  | 2 / 0 | Qwen2.5-3B |
| A0s | moral/othernorm | 14 | 1.10 | [1.04, 1.17] |  | 4 / 0 | - |

## The share as a multiple of the share of ten heads chosen at random (geometric mean over models)

| frame | models | moral | norm | person | thing |
|---|---|---|---|---|---|
| A0 | 13 (all groups) | 5.44 | 4.89 | n/a | 4.29 |
| A0s | 10 (all groups) | 5.01 | 4.68 | n/a | 4.20 |

## Per model, moral/etiquette

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 78 | 15 | 0.079 | 0.070 | 1.13 | [0.94, 1.35] | n/a |
| Llama-3.1-8B-Instruct | A0 | 77 | 18 | 0.102 | 0.092 | 1.11 | [0.96, 1.29] | n/a |
| Llama-3.2-1B | A0 | 74 | 11 | 0.073 | 0.065 | 1.13 | [0.99, 1.29] | n/a |
| Llama-3.2-1B-Instruct | A0 | 72 | 15 | 0.063 | 0.050 | 1.25 | [1.07, 1.45] | n/a |
| Llama-3.2-3B | A0 | 78 | 14 | 0.107 | 0.092 | 1.16 | [0.97, 1.41] | n/a |
| Llama-3.2-3B-Instruct | A0 | 77 | 17 | 0.105 | 0.104 | 1.01 | [0.83, 1.25] | n/a |
| Qwen2.5-14B | A0 | 80 | 17 | 0.045 | 0.042 | 1.07 | [0.86, 1.35] | n/a |
| Qwen2.5-14B-Instruct | A0 | 80 | 16 | 0.042 | 0.032 | 1.32 | [1.01, 1.81] | n/a |
| Qwen2.5-3B | A0 | 57 | 11 | 0.073 | 0.059 | 1.22 | [0.92, 1.73] | n/a |
| Qwen2.5-3B-Instruct | A0 | 77 | 17 | 0.089 | 0.076 | 1.18 | [0.96, 1.45] | n/a |
| Qwen2.5-7B | A0 | 78 | 16 | 0.069 | 0.070 | 0.98 | [0.72, 1.38] | n/a |
| Qwen2.5-7B-Instruct | A0 | 77 | 15 | 0.065 | 0.074 | 0.88 | [0.65, 1.25] | n/a |
| gemma-2b | A0 | 75 | 14 | 0.210 | 0.193 | 1.09 | [0.97, 1.21] | n/a |
| gemma-2b-it | A0 | 73 | 16 | 0.165 | 0.166 | 1.00 | [0.86, 1.15] | n/a |
| Llama-3.1-8B | A0s | 73 | 15 | 0.084 | 0.079 | 1.06 | [0.91, 1.26] | n/a |
| Llama-3.1-8B-Instruct | A0s | 75 | 16 | 0.097 | 0.099 | 0.99 | [0.85, 1.16] | n/a |
| Llama-3.2-1B | A0s | 68 | 14 | 0.074 | 0.069 | 1.08 | [0.95, 1.23] | n/a |
| Llama-3.2-1B-Instruct | A0s | 74 | 17 | 0.051 | 0.039 | 1.31 | [1.09, 1.57] | n/a |
| Llama-3.2-3B | A0s | 67 | 15 | 0.111 | 0.093 | 1.20 | [1.01, 1.45] | n/a |
| Llama-3.2-3B-Instruct | A0s | 79 | 15 | 0.131 | 0.132 | 0.99 | [0.85, 1.19] | n/a |
| Qwen2.5-14B | A0s | 78 | 16 | 0.046 | 0.047 | 0.97 | [0.71, 1.31] | n/a |
| Qwen2.5-14B-Instruct | A0s | 75 | 12 | 0.040 | 0.035 | 1.14 | [0.87, 1.57] | n/a |
| Qwen2.5-3B | A0s | 54 | 6 | too few included pairs: etiquette | | | | |
| Qwen2.5-3B-Instruct | A0s | 76 | 17 | 0.094 | 0.091 | 1.04 | [0.83, 1.32] | n/a |
| Qwen2.5-7B | A0s | 77 | 17 | 0.062 | 0.065 | 0.95 | [0.70, 1.30] | n/a |
| Qwen2.5-7B-Instruct | A0s | 72 | 15 | 0.052 | 0.068 | 0.76 | [0.60, 0.98] | n/a |
| gemma-2b | A0s | 59 | 16 | 0.200 | 0.202 | 0.99 | [0.85, 1.15] | n/a |
| gemma-2b-it | A0s | 74 | 18 | 0.154 | 0.159 | 0.97 | [0.85, 1.11] | n/a |

## Per model, etiquette/othernorm

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 15 | 79 | 0.070 | 0.061 | 1.16 | [0.98, 1.36] | n/a |
| Llama-3.1-8B-Instruct | A0 | 18 | 82 | 0.092 | 0.077 | 1.19 | [1.04, 1.36] | n/a |
| Llama-3.2-1B | A0 | 11 | 69 | 0.065 | 0.073 | 0.89 | [0.78, 1.01] | n/a |
| Llama-3.2-1B-Instruct | A0 | 15 | 68 | 0.050 | 0.051 | 0.98 | [0.85, 1.15] | n/a |
| Llama-3.2-3B | A0 | 14 | 72 | 0.092 | 0.095 | 0.96 | [0.79, 1.16] | n/a |
| Llama-3.2-3B-Instruct | A0 | 17 | 74 | 0.104 | 0.100 | 1.04 | [0.84, 1.26] | n/a |
| Qwen2.5-14B | A0 | 17 | 80 | 0.042 | 0.036 | 1.17 | [0.93, 1.43] | n/a |
| Qwen2.5-14B-Instruct | A0 | 16 | 75 | 0.032 | 0.034 | 0.94 | [0.69, 1.24] | n/a |
| Qwen2.5-3B | A0 | 11 | 67 | 0.059 | 0.064 | 0.92 | [0.66, 1.20] | n/a |
| Qwen2.5-3B-Instruct | A0 | 17 | 80 | 0.076 | 0.080 | 0.95 | [0.79, 1.13] | n/a |
| Qwen2.5-7B | A0 | 16 | 79 | 0.070 | 0.076 | 0.93 | [0.65, 1.30] | n/a |
| Qwen2.5-7B-Instruct | A0 | 15 | 73 | 0.074 | 0.056 | 1.33 | [0.94, 1.80] | n/a |
| gemma-2b | A0 | 14 | 75 | 0.193 | 0.212 | 0.91 | [0.81, 1.02] | n/a |
| gemma-2b-it | A0 | 16 | 72 | 0.166 | 0.161 | 1.03 | [0.89, 1.19] | n/a |
| Llama-3.1-8B | A0s | 15 | 59 | 0.079 | 0.074 | 1.07 | [0.89, 1.27] | n/a |
| Llama-3.1-8B-Instruct | A0s | 16 | 53 | 0.099 | 0.083 | 1.18 | [1.00, 1.39] | n/a |
| Llama-3.2-1B | A0s | 14 | 62 | 0.069 | 0.076 | 0.90 | [0.78, 1.02] | n/a |
| Llama-3.2-1B-Instruct | A0s | 17 | 58 | 0.039 | 0.043 | 0.91 | [0.76, 1.10] | n/a |
| Llama-3.2-3B | A0s | 15 | 51 | 0.093 | 0.103 | 0.90 | [0.74, 1.07] | n/a |
| Llama-3.2-3B-Instruct | A0s | 15 | 66 | 0.132 | 0.116 | 1.13 | [0.94, 1.33] | n/a |
| Qwen2.5-14B | A0s | 16 | 47 | 0.047 | 0.035 | 1.35 | [1.00, 1.82] | n/a |
| Qwen2.5-14B-Instruct | A0s | 12 | 38 | 0.035 | 0.034 | 1.05 | [0.77, 1.37] | n/a |
| Qwen2.5-3B | A0s | 6 | 51 | too few included pairs: etiquette | | | | |
| Qwen2.5-3B-Instruct | A0s | 17 | 65 | 0.091 | 0.079 | 1.15 | [0.91, 1.43] | n/a |
| Qwen2.5-7B | A0s | 17 | 53 | 0.065 | 0.065 | 1.00 | [0.72, 1.36] | n/a |
| Qwen2.5-7B-Instruct | A0s | 15 | 52 | 0.068 | 0.047 | 1.43 | [1.08, 1.84] | n/a |
| gemma-2b | A0s | 16 | 52 | 0.202 | 0.191 | 1.06 | [0.90, 1.24] | n/a |
| gemma-2b-it | A0s | 18 | 60 | 0.159 | 0.161 | 0.99 | [0.86, 1.13] | n/a |

## Per model, moral/othernorm

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 78 | 79 | 0.079 | 0.061 | 1.31 | [1.14, 1.49] | n/a |
| Llama-3.1-8B-Instruct | A0 | 77 | 82 | 0.102 | 0.077 | 1.32 | [1.16, 1.51] | n/a |
| Llama-3.2-1B | A0 | 74 | 69 | 0.073 | 0.073 | 1.00 | [0.92, 1.09] | n/a |
| Llama-3.2-1B-Instruct | A0 | 72 | 68 | 0.063 | 0.051 | 1.23 | [1.12, 1.35] | n/a |
| Llama-3.2-3B | A0 | 78 | 72 | 0.107 | 0.095 | 1.12 | [0.99, 1.26] | n/a |
| Llama-3.2-3B-Instruct | A0 | 77 | 74 | 0.105 | 0.100 | 1.05 | [0.95, 1.17] | n/a |
| Qwen2.5-14B | A0 | 80 | 80 | 0.045 | 0.036 | 1.25 | [1.06, 1.47] | n/a |
| Qwen2.5-14B-Instruct | A0 | 80 | 75 | 0.042 | 0.034 | 1.25 | [1.04, 1.49] | n/a |
| Qwen2.5-3B | A0 | 57 | 67 | 0.073 | 0.064 | 1.13 | [0.95, 1.33] | n/a |
| Qwen2.5-3B-Instruct | A0 | 77 | 80 | 0.089 | 0.080 | 1.12 | [0.96, 1.30] | n/a |
| Qwen2.5-7B | A0 | 78 | 79 | 0.069 | 0.076 | 0.91 | [0.76, 1.10] | n/a |
| Qwen2.5-7B-Instruct | A0 | 77 | 73 | 0.065 | 0.056 | 1.17 | [0.95, 1.44] | n/a |
| gemma-2b | A0 | 75 | 75 | 0.210 | 0.212 | 0.99 | [0.91, 1.07] | n/a |
| gemma-2b-it | A0 | 73 | 72 | 0.165 | 0.161 | 1.03 | [0.93, 1.13] | n/a |
| Llama-3.1-8B | A0s | 73 | 59 | 0.084 | 0.074 | 1.14 | [0.99, 1.30] | n/a |
| Llama-3.1-8B-Instruct | A0s | 75 | 53 | 0.097 | 0.083 | 1.17 | [1.01, 1.35] | n/a |
| Llama-3.2-1B | A0s | 68 | 62 | 0.074 | 0.076 | 0.97 | [0.89, 1.06] | n/a |
| Llama-3.2-1B-Instruct | A0s | 74 | 58 | 0.051 | 0.043 | 1.19 | [1.05, 1.35] | n/a |
| Llama-3.2-3B | A0s | 67 | 51 | 0.111 | 0.103 | 1.08 | [0.96, 1.22] | n/a |
| Llama-3.2-3B-Instruct | A0s | 79 | 66 | 0.131 | 0.116 | 1.13 | [0.99, 1.27] | n/a |
| Qwen2.5-14B | A0s | 78 | 47 | 0.046 | 0.035 | 1.31 | [1.11, 1.54] | n/a |
| Qwen2.5-14B-Instruct | A0s | 75 | 38 | 0.040 | 0.034 | 1.20 | [0.99, 1.44] | n/a |
| Qwen2.5-3B | A0s | 54 | 51 | 0.075 | 0.072 | 1.04 | [0.86, 1.27] | n/a |
| Qwen2.5-3B-Instruct | A0s | 76 | 65 | 0.094 | 0.079 | 1.19 | [1.04, 1.37] | n/a |
| Qwen2.5-7B | A0s | 77 | 53 | 0.062 | 0.065 | 0.94 | [0.82, 1.09] | n/a |
| Qwen2.5-7B-Instruct | A0s | 72 | 52 | 0.052 | 0.047 | 1.09 | [0.87, 1.34] | n/a |
| gemma-2b | A0s | 59 | 52 | 0.200 | 0.191 | 1.04 | [0.93, 1.17] | n/a |
| gemma-2b-it | A0s | 74 | 60 | 0.154 | 0.161 | 0.96 | [0.87, 1.06] | n/a |

## Behaviour

| model | frame | group | run | included | mean gap | better version preferred | mean mass | multiple of random |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | moral | 80 | 78 | +0.553 | 0.97 | 0.58 | 8.13 |
| Llama-3.1-8B | A0 | norm | 107 | 98 | +0.291 | 0.93 | 0.46 | 6.41 |
| Llama-3.1-8B | A0 | thing | 40 | 31 | +0.068 | 0.88 | 0.12 | 5.58 |
| Llama-3.1-8B | A0 | etiquette | 18 | 15 | +0.223 | 0.89 | 0.58 | 7.21 |
| Llama-3.1-8B | A0 | othernorm | 85 | 79 | +0.310 | 0.94 | 0.43 | 6.22 |
| Llama-3.1-8B | A0s | moral | 80 | 73 | +0.378 | 0.91 | 0.50 | 8.59 |
| Llama-3.1-8B | A0s | norm | 107 | 78 | +0.222 | 0.76 | 0.48 | 7.64 |
| Llama-3.1-8B | A0s | thing | 40 | 29 | +0.118 | 0.95 | 0.18 | 6.92 |
| Llama-3.1-8B | A0s | etiquette | 18 | 15 | +0.435 | 0.83 | 0.73 | 8.10 |
| Llama-3.1-8B | A0s | othernorm | 85 | 59 | +0.164 | 0.73 | 0.41 | 7.56 |
| Llama-3.1-8B-Instruct | A0 | moral | 80 | 77 | +0.608 | 0.97 | 0.46 | 10.46 |
| Llama-3.1-8B-Instruct | A0 | norm | 107 | 104 | +0.281 | 0.99 | 0.32 | 8.21 |
| Llama-3.1-8B-Instruct | A0 | thing | 40 | 30 | +0.062 | 0.93 | 0.10 | 6.53 |
| Llama-3.1-8B-Instruct | A0 | etiquette | 18 | 18 | +0.283 | 1.00 | 0.44 | 9.38 |
| Llama-3.1-8B-Instruct | A0 | othernorm | 85 | 82 | +0.281 | 0.99 | 0.29 | 7.90 |
| Llama-3.1-8B-Instruct | A0s | moral | 80 | 75 | +0.470 | 0.94 | 0.52 | 9.98 |
| Llama-3.1-8B-Instruct | A0s | norm | 107 | 73 | +0.180 | 0.71 | 0.46 | 8.89 |
| Llama-3.1-8B-Instruct | A0s | thing | 40 | 23 | +0.070 | 0.68 | 0.18 | 7.47 |
| Llama-3.1-8B-Instruct | A0s | etiquette | 18 | 16 | +0.493 | 0.94 | 0.70 | 10.12 |
| Llama-3.1-8B-Instruct | A0s | othernorm | 85 | 53 | +0.102 | 0.65 | 0.40 | 8.54 |
| Llama-3.2-1B | A0 | moral | 80 | 74 | +0.343 | 0.93 | 0.57 | 3.75 |
| Llama-3.2-1B | A0 | norm | 107 | 82 | +0.159 | 0.80 | 0.39 | 3.69 |
| Llama-3.2-1B | A0 | thing | 40 | 27 | +0.076 | 0.88 | 0.16 | 3.77 |
| Llama-3.2-1B | A0 | etiquette | 18 | 11 | +0.104 | 0.72 | 0.51 | 3.32 |
| Llama-3.2-1B | A0 | othernorm | 85 | 69 | +0.173 | 0.84 | 0.36 | 3.75 |
| Llama-3.2-1B | A0s | moral | 80 | 68 | +0.243 | 0.86 | 0.49 | 3.78 |
| Llama-3.2-1B | A0s | norm | 107 | 79 | +0.164 | 0.77 | 0.49 | 3.86 |
| Llama-3.2-1B | A0s | thing | 40 | 19* | +0.083 | 0.72 | 0.20 | 3.81 |
| Llama-3.2-1B | A0s | etiquette | 18 | 14 | +0.200 | 0.78 | 0.66 | 3.51 |
| Llama-3.2-1B | A0s | othernorm | 85 | 62 | +0.148 | 0.75 | 0.44 | 3.90 |
| Llama-3.2-1B-Instruct | A0 | moral | 80 | 72 | +0.224 | 0.91 | 0.27 | 3.22 |
| Llama-3.2-1B-Instruct | A0 | norm | 107 | 86 | +0.108 | 0.92 | 0.19 | 2.62 |
| Llama-3.2-1B-Instruct | A0 | thing | 40 | 24 | +0.040 | 0.93 | 0.07 | 2.35 |
| Llama-3.2-1B-Instruct | A0 | etiquette | 18 | 15 | +0.104 | 0.89 | 0.27 | 2.58 |
| Llama-3.2-1B-Instruct | A0 | othernorm | 85 | 68 | +0.108 | 0.93 | 0.17 | 2.62 |
| Llama-3.2-1B-Instruct | A0s | moral | 80 | 74 | +0.392 | 0.93 | 0.52 | 2.60 |
| Llama-3.2-1B-Instruct | A0s | norm | 107 | 79 | +0.215 | 0.80 | 0.45 | 2.12 |
| Llama-3.2-1B-Instruct | A0s | thing | 40 | 24 | +0.119 | 0.88 | 0.19 | 1.94 |
| Llama-3.2-1B-Instruct | A0s | etiquette | 18 | 17 | +0.290 | 0.94 | 0.66 | 1.98 |
| Llama-3.2-1B-Instruct | A0s | othernorm | 85 | 58 | +0.186 | 0.76 | 0.40 | 2.18 |
| Llama-3.2-3B | A0 | moral | 80 | 78 | +0.465 | 0.97 | 0.59 | 7.17 |
| Llama-3.2-3B | A0 | norm | 107 | 90 | +0.227 | 0.91 | 0.44 | 6.44 |
| Llama-3.2-3B | A0 | thing | 40 | 25 | +0.050 | 0.82 | 0.10 | 5.67 |
| Llama-3.2-3B | A0 | etiquette | 18 | 14 | +0.160 | 0.89 | 0.54 | 6.16 |
| Llama-3.2-3B | A0 | othernorm | 85 | 72 | +0.239 | 0.91 | 0.41 | 6.39 |
| Llama-3.2-3B | A0s | moral | 80 | 67 | +0.304 | 0.84 | 0.53 | 7.47 |
| Llama-3.2-3B | A0s | norm | 107 | 70 | +0.139 | 0.68 | 0.56 | 6.79 |
| Llama-3.2-3B | A0s | thing | 40 | 30 | +0.144 | 0.88 | 0.25 | 6.03 |
| Llama-3.2-3B | A0s | etiquette | 18 | 15 | +0.235 | 0.89 | 0.73 | 6.23 |
| Llama-3.2-3B | A0s | othernorm | 85 | 51 | +0.108 | 0.62 | 0.51 | 6.93 |
| Llama-3.2-3B-Instruct | A0 | moral | 80 | 77 | +0.407 | 0.97 | 0.32 | 7.05 |
| Llama-3.2-3B-Instruct | A0 | norm | 107 | 95 | +0.167 | 0.93 | 0.20 | 6.88 |
| Llama-3.2-3B-Instruct | A0 | thing | 40 | 30 | +0.047 | 0.95 | 0.08 | 5.28 |
| Llama-3.2-3B-Instruct | A0 | etiquette | 18 | 17 | +0.176 | 1.00 | 0.28 | 6.99 |
| Llama-3.2-3B-Instruct | A0 | othernorm | 85 | 74 | +0.158 | 0.92 | 0.18 | 6.72 |
| Llama-3.2-3B-Instruct | A0s | moral | 80 | 79 | +0.754 | 0.99 | 0.72 | 8.77 |
| Llama-3.2-3B-Instruct | A0s | norm | 107 | 85 | +0.355 | 0.80 | 0.66 | 8.08 |
| Llama-3.2-3B-Instruct | A0s | thing | 40 | 39 | +0.249 | 1.00 | 0.37 | 6.34 |
| Llama-3.2-3B-Instruct | A0s | etiquette | 18 | 15 | +0.497 | 0.83 | 0.78 | 8.84 |
| Llama-3.2-3B-Instruct | A0s | othernorm | 85 | 66 | +0.301 | 0.79 | 0.62 | 7.79 |
| Qwen2.5-14B | A0 | moral | 80 | 80 | +0.749 | 1.00 | 0.70 | 8.69 |
| Qwen2.5-14B | A0 | norm | 107 | 101 | +0.368 | 0.97 | 0.61 | 7.19 |
| Qwen2.5-14B | A0 | thing | 40 | 32 | +0.097 | 0.95 | 0.15 | 6.61 |
| Qwen2.5-14B | A0 | etiquette | 18 | 17 | +0.451 | 1.00 | 0.74 | 8.15 |
| Qwen2.5-14B | A0 | othernorm | 85 | 80 | +0.345 | 0.96 | 0.57 | 6.95 |
| Qwen2.5-14B | A0s | moral | 80 | 78 | +0.544 | 0.97 | 0.47 | 8.84 |
| Qwen2.5-14B | A0s | norm | 107 | 67 | +0.176 | 0.65 | 0.43 | 7.38 |
| Qwen2.5-14B | A0s | thing | 40 | 18* | +0.026 | 0.72 | 0.12 | 6.29 |
| Qwen2.5-14B | A0s | etiquette | 18 | 16 | +0.487 | 1.00 | 0.63 | 9.10 |
| Qwen2.5-14B | A0s | othernorm | 85 | 47 | +0.080 | 0.56 | 0.37 | 6.77 |
| Qwen2.5-14B-Instruct | A0 | moral | 80 | 80 | +0.777 | 1.00 | 0.77 | 8.06 |
| Qwen2.5-14B-Instruct | A0 | norm | 107 | 95 | +0.467 | 0.92 | 0.69 | 6.48 |
| Qwen2.5-14B-Instruct | A0 | thing | 40 | 32 | +0.123 | 0.93 | 0.15 | 5.89 |
| Qwen2.5-14B-Instruct | A0 | etiquette | 18 | 16 | +0.545 | 0.89 | 0.85 | 6.09 |
| Qwen2.5-14B-Instruct | A0 | othernorm | 85 | 75 | +0.447 | 0.92 | 0.65 | 6.45 |
| Qwen2.5-14B-Instruct | A0s | moral | 80 | 75 | +0.550 | 0.96 | 0.50 | 7.75 |
| Qwen2.5-14B-Instruct | A0s | norm | 107 | 53 | +0.113 | 0.54 | 0.43 | 6.53 |
| Qwen2.5-14B-Instruct | A0s | thing | 40 | 12* | +0.002 | 0.72 | 0.09 | 5.96 |
| Qwen2.5-14B-Instruct | A0s | etiquette | 18 | 12 | +0.432 | 0.78 | 0.68 | 6.77 |
| Qwen2.5-14B-Instruct | A0s | othernorm | 85 | 38 | +0.038 | 0.48 | 0.37 | 6.46 |
| Qwen2.5-3B | A0 | moral | 80 | 57 | +0.284 | 0.71 | 0.55 | 4.19 |
| Qwen2.5-3B | A0 | norm | 107 | 80 | +0.202 | 0.77 | 0.50 | 3.64 |
| Qwen2.5-3B | A0 | thing | 40 | 3* | +0.001 | 0.55 | 0.07 | 3.29 |
| Qwen2.5-3B | A0 | etiquette | 18 | 11 | +0.082 | 0.61 | 0.50 | 3.42 |
| Qwen2.5-3B | A0 | othernorm | 85 | 67 | +0.232 | 0.81 | 0.50 | 3.71 |
| Qwen2.5-3B | A0s | moral | 80 | 54 | +0.258 | 0.79 | 0.33 | 4.34 |
| Qwen2.5-3B | A0s | norm | 107 | 59 | +0.140 | 0.69 | 0.27 | 4.10 |
| Qwen2.5-3B | A0s | thing | 40 | 2* | +0.003 | 0.62 | 0.01 | 3.24 |
| Qwen2.5-3B | A0s | etiquette | 18 | 6* | +0.027 | 0.56 | 0.30 | 3.75 |
| Qwen2.5-3B | A0s | othernorm | 85 | 51 | +0.157 | 0.73 | 0.25 | 4.16 |
| Qwen2.5-3B-Instruct | A0 | moral | 80 | 77 | +0.614 | 0.97 | 0.71 | 5.15 |
| Qwen2.5-3B-Instruct | A0 | norm | 107 | 101 | +0.350 | 0.96 | 0.57 | 4.58 |
| Qwen2.5-3B-Instruct | A0 | thing | 40 | 36 | +0.110 | 0.97 | 0.18 | 4.26 |
| Qwen2.5-3B-Instruct | A0 | etiquette | 18 | 17 | +0.257 | 0.94 | 0.69 | 4.37 |
| Qwen2.5-3B-Instruct | A0 | othernorm | 85 | 80 | +0.370 | 0.96 | 0.54 | 4.60 |
| Qwen2.5-3B-Instruct | A0s | moral | 80 | 76 | +0.612 | 0.96 | 0.54 | 5.44 |
| Qwen2.5-3B-Instruct | A0s | norm | 107 | 86 | +0.307 | 0.83 | 0.49 | 4.75 |
| Qwen2.5-3B-Instruct | A0s | thing | 40 | 26 | +0.100 | 0.88 | 0.14 | 4.45 |
| Qwen2.5-3B-Instruct | A0s | etiquette | 18 | 17 | +0.481 | 0.94 | 0.70 | 5.25 |
| Qwen2.5-3B-Instruct | A0s | othernorm | 85 | 65 | +0.249 | 0.80 | 0.43 | 4.56 |
| Qwen2.5-7B | A0 | moral | 80 | 78 | +0.630 | 0.99 | 0.62 | 5.42 |
| Qwen2.5-7B | A0 | norm | 107 | 99 | +0.317 | 0.94 | 0.48 | 5.89 |
| Qwen2.5-7B | A0 | thing | 40 | 28 | +0.078 | 0.90 | 0.13 | 4.32 |
| Qwen2.5-7B | A0 | etiquette | 18 | 16 | +0.419 | 1.00 | 0.64 | 5.52 |
| Qwen2.5-7B | A0 | othernorm | 85 | 79 | +0.285 | 0.93 | 0.43 | 5.93 |
| Qwen2.5-7B | A0s | moral | 80 | 77 | +0.448 | 0.96 | 0.49 | 4.83 |
| Qwen2.5-7B | A0s | norm | 107 | 74 | +0.231 | 0.78 | 0.47 | 5.11 |
| Qwen2.5-7B | A0s | thing | 40 | 29 | +0.116 | 0.88 | 0.20 | 4.78 |
| Qwen2.5-7B | A0s | etiquette | 18 | 17 | +0.552 | 0.94 | 0.66 | 5.11 |
| Qwen2.5-7B | A0s | othernorm | 85 | 53 | +0.133 | 0.73 | 0.42 | 5.12 |
| Qwen2.5-7B-Instruct | A0 | moral | 80 | 77 | +0.629 | 0.96 | 0.62 | 5.08 |
| Qwen2.5-7B-Instruct | A0 | norm | 107 | 92 | +0.302 | 0.86 | 0.51 | 4.58 |
| Qwen2.5-7B-Instruct | A0 | thing | 40 | 28 | +0.132 | 0.90 | 0.14 | 4.00 |
| Qwen2.5-7B-Instruct | A0 | etiquette | 18 | 15 | +0.296 | 0.83 | 0.66 | 5.79 |
| Qwen2.5-7B-Instruct | A0 | othernorm | 85 | 73 | +0.296 | 0.86 | 0.47 | 4.35 |
| Qwen2.5-7B-Instruct | A0s | moral | 80 | 72 | +0.336 | 0.95 | 0.40 | 4.04 |
| Qwen2.5-7B-Instruct | A0s | norm | 107 | 71 | +0.185 | 0.71 | 0.37 | 4.07 |
| Qwen2.5-7B-Instruct | A0s | thing | 40 | 28 | +0.098 | 0.93 | 0.13 | 3.36 |
| Qwen2.5-7B-Instruct | A0s | etiquette | 18 | 15 | +0.390 | 0.83 | 0.63 | 5.32 |
| Qwen2.5-7B-Instruct | A0s | othernorm | 85 | 52 | +0.099 | 0.67 | 0.31 | 3.72 |
| gemma-2b | A0 | moral | 80 | 75 | +0.409 | 0.94 | 0.59 | 3.02 |
| gemma-2b | A0 | norm | 107 | 93 | +0.262 | 0.89 | 0.43 | 2.99 |
| gemma-2b | A0 | thing | 40 | 34 | +0.095 | 0.95 | 0.14 | 2.83 |
| gemma-2b | A0 | etiquette | 18 | 14 | +0.201 | 0.83 | 0.57 | 2.78 |
| gemma-2b | A0 | othernorm | 85 | 75 | +0.269 | 0.89 | 0.40 | 3.05 |
| gemma-2b | A0s | moral | 80 | 59 | +0.228 | 0.76 | 0.51 | 2.88 |
| gemma-2b | A0s | norm | 107 | 72 | +0.150 | 0.69 | 0.52 | 2.81 |
| gemma-2b | A0s | thing | 40 | 23 | +0.065 | 0.70 | 0.16 | 2.79 |
| gemma-2b | A0s | etiquette | 18 | 16 | +0.275 | 0.89 | 0.74 | 2.91 |
| gemma-2b | A0s | othernorm | 85 | 52 | +0.107 | 0.64 | 0.47 | 2.75 |
| gemma-2b-it | A0 | moral | 80 | 73 | +0.464 | 0.94 | 0.60 | 2.38 |
| gemma-2b-it | A0 | norm | 107 | 92 | +0.367 | 0.90 | 0.43 | 2.33 |
| gemma-2b-it | A0 | thing | 40 | 21 | +0.096 | 0.85 | 0.13 | 2.11 |
| gemma-2b-it | A0 | etiquette | 18 | 16 | +0.325 | 0.89 | 0.62 | 2.39 |
| gemma-2b-it | A0 | othernorm | 85 | 72 | +0.368 | 0.89 | 0.37 | 2.32 |
| gemma-2b-it | A0s | moral | 80 | 74 | +0.493 | 0.93 | 0.61 | 2.22 |
| gemma-2b-it | A0s | norm | 107 | 82 | +0.358 | 0.80 | 0.56 | 2.28 |
| gemma-2b-it | A0s | thing | 40 | 32 | +0.446 | 0.88 | 0.55 | 2.23 |
| gemma-2b-it | A0s | etiquette | 18 | 18 | +0.630 | 1.00 | 0.91 | 2.29 |
| gemma-2b-it | A0s | othernorm | 85 | 60 | +0.283 | 0.75 | 0.47 | 2.32 |

\* fewer included pairs than the minimum; shown, not pooled.
