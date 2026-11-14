# The located heads on the control pairs about a person

Pairs: moral 80, norm 107, thing 40, person 66. Control pairs: 66 candidates, 58 accepted by the screen (llm); used here: 66 (all). Runs: runs/heads, runs/heads_followup_person. Head set located, condition p2r_all, effects read on S, a pair is included when its gap in S is at least 0.02, 10000 bootstrap resamples.

Check against results/heads: the study's contrasts recomputed here are the same (122 per-model and 9 pooled ratios; largest difference 0.0e+00).

## Reading

- Frame A1: norm/person 1.13 [1.06, 1.21] (above 1); person/thing 1.06 [1.00, 1.13] (includes 1): the fifth comes with the standard: the located heads carry more when conduct is judged than when something good or bad happens to a person
- Frame B: norm/person 1.02 [0.94, 1.11] (includes 1); person/thing 1.19 [1.09, 1.29] (above 1): the fifth comes from the form of the phrase, not from the standard: on the control pairs the located heads carry what they carry on normative pairs
- Frame A0: not available (a group is missing or has too few included pairs)

## Pooled ratios of the located heads' share (geometric mean over models; 95 % interval from the item bootstrap)

| frame | contrast | models | ratio | 95 % interval | within template types | models with interval above 1 / below 1 | left out |
|---|---|---|---|---|---|---|---|
| A1 | norm/person | 14 | 1.13 | [1.06, 1.21] | 1.13 [1.07, 1.19] | 8 / 2 | - |
| A1 | moral/person | 14 | 1.13 | [1.05, 1.21] | 1.13 [1.06, 1.20] | 6 / 2 | - |
| A1 | person/thing | 13 | 1.06 | [1.00, 1.13] |  | 5 / 1 | Qwen2.5-14B-Instruct |
| A1 | norm/thing | 13 | 1.19 | [1.13, 1.26] |  | 9 / 0 | Qwen2.5-14B-Instruct |
| A1 | moral/thing | 13 | 1.19 | [1.11, 1.26] |  | 6 / 1 | Qwen2.5-14B-Instruct |
| A1 | moral/norm | 14 | 1.00 | [0.93, 1.06] |  | 2 / 2 | - |
| B | norm/person | 14 | 1.02 | [0.94, 1.11] | 1.01 [0.94, 1.07] | 4 / 3 | - |
| B | moral/person | 14 | 0.91 | [0.84, 0.99] | 0.91 [0.85, 0.98] | 1 / 5 | - |
| B | person/thing | 14 | 1.19 | [1.09, 1.29] |  | 8 / 0 | - |
| B | norm/thing | 14 | 1.21 | [1.14, 1.28] |  | 10 / 0 | - |
| B | moral/thing | 14 | 1.09 | [1.02, 1.16] |  | 5 / 1 | - |
| B | moral/norm | 14 | 0.90 | [0.85, 0.95] |  | 0 / 6 | - |
| A0 | norm/thing | 13 | 1.14 | [1.08, 1.21] |  | 5 / 0 | Qwen2.5-3B |
| A0 | moral/thing | 13 | 1.27 | [1.19, 1.35] |  | 11 / 0 | Qwen2.5-3B |
| A0 | moral/norm | 14 | 1.12 | [1.05, 1.18] |  | 5 / 0 | - |

## The share as a multiple of the share of ten heads chosen at random (geometric mean over models)

| frame | models | moral | norm | person | thing |
|---|---|---|---|---|---|
| A1 | 13 (all groups) | 5.44 | 5.47 | 4.89 | 4.59 |
| A1 | 13 (study groups) | 5.44 | 5.47 | n/a | 4.59 |
| B | 14 (all groups) | 4.36 | 4.86 | 4.78 | 4.01 |
| B | 14 (study groups) | 4.36 | 4.86 | n/a | 4.01 |
| A0 | 13 (study groups) | 5.44 | 4.89 | n/a | 4.29 |

## Per model, norm/person

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | 104 | 65 | 0.082 | 0.073 | 1.13 | [1.02, 1.25] | 1.12 |
| Llama-3.1-8B-Instruct | A1 | 107 | 64 | 0.101 | 0.084 | 1.20 | [1.08, 1.33] | 1.19 |
| Llama-3.2-1B | A1 | 97 | 65 | 0.082 | 0.097 | 0.84 | [0.78, 0.91] | 0.84 |
| Llama-3.2-1B-Instruct | A1 | 92 | 64 | 0.043 | 0.037 | 1.15 | [1.04, 1.29] | 1.17 |
| Llama-3.2-3B | A1 | 104 | 65 | 0.131 | 0.154 | 0.85 | [0.77, 0.94] | 0.84 |
| Llama-3.2-3B-Instruct | A1 | 103 | 66 | 0.116 | 0.116 | 1.00 | [0.88, 1.14] | 0.98 |
| Qwen2.5-14B | A1 | 99 | 64 | 0.060 | 0.046 | 1.31 | [1.17, 1.47] | 1.30 |
| Qwen2.5-14B-Instruct | A1 | 99 | 61 | 0.053 | 0.041 | 1.29 | [1.13, 1.47] | 1.27 |
| Qwen2.5-3B | A1 | 98 | 65 | 0.062 | 0.056 | 1.10 | [0.97, 1.26] | 1.10 |
| Qwen2.5-3B-Instruct | A1 | 103 | 65 | 0.116 | 0.121 | 0.96 | [0.84, 1.10] | 0.95 |
| Qwen2.5-7B | A1 | 104 | 66 | 0.090 | 0.076 | 1.20 | [0.99, 1.44] | 1.20 |
| Qwen2.5-7B-Instruct | A1 | 106 | 65 | 0.075 | 0.053 | 1.42 | [1.07, 1.88] | 1.44 |
| gemma-2b | A1 | 99 | 66 | 0.206 | 0.159 | 1.29 | [1.19, 1.41] | 1.29 |
| gemma-2b-it | A1 | 98 | 66 | 0.149 | 0.116 | 1.28 | [1.16, 1.41] | 1.27 |
| Llama-3.1-8B | B | 104 | 66 | 0.066 | 0.082 | 0.81 | [0.70, 0.95] | 0.80 |
| Llama-3.1-8B-Instruct | B | 103 | 65 | 0.065 | 0.054 | 1.19 | [1.02, 1.38] | 1.17 |
| Llama-3.2-1B | B | 91 | 64 | 0.076 | 0.089 | 0.85 | [0.77, 0.93] | 0.84 |
| Llama-3.2-1B-Instruct | B | 95 | 66 | 0.042 | 0.041 | 1.04 | [0.92, 1.18] | 1.04 |
| Llama-3.2-3B | B | 100 | 66 | 0.092 | 0.114 | 0.81 | [0.71, 0.92] | 0.79 |
| Llama-3.2-3B-Instruct | B | 103 | 66 | 0.080 | 0.080 | 1.01 | [0.88, 1.15] | 0.99 |
| Qwen2.5-14B | B | 106 | 66 | 0.039 | 0.031 | 1.26 | [1.09, 1.47] | 1.24 |
| Qwen2.5-14B-Instruct | B | 104 | 65 | 0.034 | 0.029 | 1.14 | [1.00, 1.30] | 1.12 |
| Qwen2.5-3B | B | 101 | 65 | 0.070 | 0.068 | 1.03 | [0.91, 1.17] | 1.02 |
| Qwen2.5-3B-Instruct | B | 104 | 65 | 0.108 | 0.107 | 1.01 | [0.87, 1.18] | 0.98 |
| Qwen2.5-7B | B | 107 | 66 | 0.096 | 0.093 | 1.04 | [0.84, 1.30] | 1.03 |
| Qwen2.5-7B-Instruct | B | 104 | 65 | 0.064 | 0.070 | 0.92 | [0.67, 1.30] | 0.95 |
| gemma-2b | B | 95 | 65 | 0.212 | 0.170 | 1.25 | [1.14, 1.36] | 1.23 |
| gemma-2b-it | B | 88 | 65 | 0.164 | 0.159 | 1.03 | [0.93, 1.13] | 1.02 |
| Llama-3.1-8B | A0 | 98 | 0 | too few included pairs: person | | | | |
| Llama-3.1-8B-Instruct | A0 | 104 | 0 | too few included pairs: person | | | | |
| Llama-3.2-1B | A0 | 82 | 0 | too few included pairs: person | | | | |
| Llama-3.2-1B-Instruct | A0 | 86 | 0 | too few included pairs: person | | | | |
| Llama-3.2-3B | A0 | 90 | 0 | too few included pairs: person | | | | |
| Llama-3.2-3B-Instruct | A0 | 95 | 0 | too few included pairs: person | | | | |
| Qwen2.5-14B | A0 | 101 | 0 | too few included pairs: person | | | | |
| Qwen2.5-14B-Instruct | A0 | 95 | 0 | too few included pairs: person | | | | |
| Qwen2.5-3B | A0 | 80 | 0 | too few included pairs: person | | | | |
| Qwen2.5-3B-Instruct | A0 | 101 | 0 | too few included pairs: person | | | | |
| Qwen2.5-7B | A0 | 99 | 0 | too few included pairs: person | | | | |
| Qwen2.5-7B-Instruct | A0 | 92 | 0 | too few included pairs: person | | | | |
| gemma-2b | A0 | 93 | 0 | too few included pairs: person | | | | |
| gemma-2b-it | A0 | 92 | 0 | too few included pairs: person | | | | |

## Per model, person/thing

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | 65 | 38 | 0.073 | 0.078 | 0.94 | [0.83, 1.05] | n/a |
| Llama-3.1-8B-Instruct | A1 | 64 | 37 | 0.084 | 0.101 | 0.84 | [0.75, 0.92] | n/a |
| Llama-3.2-1B | A1 | 65 | 39 | 0.097 | 0.081 | 1.21 | [1.10, 1.33] | n/a |
| Llama-3.2-1B-Instruct | A1 | 64 | 38 | 0.037 | 0.031 | 1.19 | [1.04, 1.37] | n/a |
| Llama-3.2-3B | A1 | 65 | 40 | 0.154 | 0.115 | 1.33 | [1.18, 1.50] | n/a |
| Llama-3.2-3B-Instruct | A1 | 66 | 39 | 0.116 | 0.094 | 1.23 | [1.07, 1.41] | n/a |
| Qwen2.5-14B | A1 | 64 | 36 | 0.046 | 0.042 | 1.10 | [0.98, 1.24] | n/a |
| Qwen2.5-14B-Instruct | A1 | 61 | 18 | too few included pairs: thing | | | | |
| Qwen2.5-3B | A1 | 65 | 39 | 0.056 | 0.053 | 1.04 | [0.91, 1.20] | n/a |
| Qwen2.5-3B-Instruct | A1 | 65 | 40 | 0.121 | 0.126 | 0.96 | [0.83, 1.10] | n/a |
| Qwen2.5-7B | A1 | 66 | 40 | 0.076 | 0.062 | 1.21 | [1.03, 1.42] | n/a |
| Qwen2.5-7B-Instruct | A1 | 65 | 40 | 0.053 | 0.048 | 1.11 | [0.90, 1.40] | n/a |
| gemma-2b | A1 | 66 | 39 | 0.159 | 0.176 | 0.90 | [0.81, 1.01] | n/a |
| gemma-2b-it | A1 | 66 | 37 | 0.116 | 0.127 | 0.92 | [0.80, 1.06] | n/a |
| Llama-3.1-8B | B | 66 | 40 | 0.082 | 0.056 | 1.45 | [1.21, 1.71] | n/a |
| Llama-3.1-8B-Instruct | B | 65 | 40 | 0.054 | 0.054 | 1.00 | [0.84, 1.18] | n/a |
| Llama-3.2-1B | B | 64 | 35 | 0.089 | 0.066 | 1.34 | [1.20, 1.51] | n/a |
| Llama-3.2-1B-Instruct | B | 66 | 37 | 0.041 | 0.030 | 1.37 | [1.17, 1.61] | n/a |
| Llama-3.2-3B | B | 66 | 40 | 0.114 | 0.092 | 1.23 | [1.07, 1.42] | n/a |
| Llama-3.2-3B-Instruct | B | 66 | 39 | 0.080 | 0.076 | 1.05 | [0.90, 1.21] | n/a |
| Qwen2.5-14B | B | 66 | 40 | 0.031 | 0.030 | 1.04 | [0.88, 1.21] | n/a |
| Qwen2.5-14B-Instruct | B | 65 | 40 | 0.029 | 0.024 | 1.25 | [1.09, 1.42] | n/a |
| Qwen2.5-3B | B | 65 | 40 | 0.068 | 0.058 | 1.18 | [1.03, 1.34] | n/a |
| Qwen2.5-3B-Instruct | B | 65 | 40 | 0.107 | 0.104 | 1.02 | [0.86, 1.22] | n/a |
| Qwen2.5-7B | B | 66 | 40 | 0.093 | 0.071 | 1.32 | [1.04, 1.65] | n/a |
| Qwen2.5-7B-Instruct | B | 65 | 40 | 0.070 | 0.045 | 1.53 | [1.10, 2.09] | n/a |
| gemma-2b | B | 65 | 40 | 0.170 | 0.167 | 1.02 | [0.90, 1.15] | n/a |
| gemma-2b-it | B | 65 | 34 | 0.159 | 0.153 | 1.04 | [0.92, 1.17] | n/a |
| Llama-3.1-8B | A0 | 0 | 31 | too few included pairs: person | | | | |
| Llama-3.1-8B-Instruct | A0 | 0 | 30 | too few included pairs: person | | | | |
| Llama-3.2-1B | A0 | 0 | 27 | too few included pairs: person | | | | |
| Llama-3.2-1B-Instruct | A0 | 0 | 24 | too few included pairs: person | | | | |
| Llama-3.2-3B | A0 | 0 | 25 | too few included pairs: person | | | | |
| Llama-3.2-3B-Instruct | A0 | 0 | 30 | too few included pairs: person | | | | |
| Qwen2.5-14B | A0 | 0 | 32 | too few included pairs: person | | | | |
| Qwen2.5-14B-Instruct | A0 | 0 | 32 | too few included pairs: person | | | | |
| Qwen2.5-3B | A0 | 0 | 3 | too few included pairs: person, thing | | | | |
| Qwen2.5-3B-Instruct | A0 | 0 | 36 | too few included pairs: person | | | | |
| Qwen2.5-7B | A0 | 0 | 28 | too few included pairs: person | | | | |
| Qwen2.5-7B-Instruct | A0 | 0 | 28 | too few included pairs: person | | | | |
| gemma-2b | A0 | 0 | 34 | too few included pairs: person | | | | |
| gemma-2b-it | A0 | 0 | 21 | too few included pairs: person | | | | |

## Per model, moral/person

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | 78 | 65 | 0.068 | 0.073 | 0.93 | [0.84, 1.06] | 0.93 |
| Llama-3.1-8B-Instruct | A1 | 78 | 64 | 0.091 | 0.084 | 1.08 | [0.96, 1.21] | 1.08 |
| Llama-3.2-1B | A1 | 78 | 65 | 0.087 | 0.097 | 0.90 | [0.83, 0.98] | 0.91 |
| Llama-3.2-1B-Instruct | A1 | 69 | 64 | 0.048 | 0.037 | 1.31 | [1.16, 1.49] | 1.29 |
| Llama-3.2-3B | A1 | 79 | 65 | 0.121 | 0.154 | 0.79 | [0.70, 0.88] | 0.80 |
| Llama-3.2-3B-Instruct | A1 | 72 | 66 | 0.112 | 0.116 | 0.97 | [0.84, 1.12] | 0.97 |
| Qwen2.5-14B | A1 | 79 | 64 | 0.073 | 0.046 | 1.60 | [1.41, 1.81] | 1.65 |
| Qwen2.5-14B-Instruct | A1 | 79 | 61 | 0.055 | 0.041 | 1.33 | [1.15, 1.54] | 1.36 |
| Qwen2.5-3B | A1 | 78 | 65 | 0.068 | 0.056 | 1.21 | [1.07, 1.37] | 1.21 |
| Qwen2.5-3B-Instruct | A1 | 76 | 65 | 0.128 | 0.121 | 1.06 | [0.90, 1.24] | 1.08 |
| Qwen2.5-7B | A1 | 79 | 66 | 0.082 | 0.076 | 1.08 | [0.85, 1.40] | 1.07 |
| Qwen2.5-7B-Instruct | A1 | 75 | 65 | 0.065 | 0.053 | 1.24 | [0.86, 1.79] | 1.24 |
| gemma-2b | A1 | 74 | 66 | 0.191 | 0.159 | 1.20 | [1.10, 1.31] | 1.19 |
| gemma-2b-it | A1 | 73 | 66 | 0.157 | 0.116 | 1.35 | [1.21, 1.50] | 1.34 |
| Llama-3.1-8B | B | 77 | 66 | 0.057 | 0.082 | 0.70 | [0.60, 0.83] | 0.69 |
| Llama-3.1-8B-Instruct | B | 78 | 65 | 0.055 | 0.054 | 1.02 | [0.87, 1.20] | 1.00 |
| Llama-3.2-1B | B | 73 | 64 | 0.082 | 0.089 | 0.92 | [0.84, 1.00] | 0.92 |
| Llama-3.2-1B-Instruct | B | 72 | 66 | 0.043 | 0.041 | 1.07 | [0.93, 1.25] | 1.06 |
| Llama-3.2-3B | B | 78 | 66 | 0.081 | 0.114 | 0.71 | [0.62, 0.81] | 0.71 |
| Llama-3.2-3B-Instruct | B | 69 | 66 | 0.065 | 0.080 | 0.81 | [0.71, 0.93] | 0.82 |
| Qwen2.5-14B | B | 79 | 66 | 0.036 | 0.031 | 1.16 | [0.97, 1.37] | 1.17 |
| Qwen2.5-14B-Instruct | B | 78 | 65 | 0.029 | 0.029 | 1.00 | [0.85, 1.17] | 1.00 |
| Qwen2.5-3B | B | 75 | 65 | 0.059 | 0.068 | 0.86 | [0.76, 0.97] | 0.86 |
| Qwen2.5-3B-Instruct | B | 76 | 65 | 0.111 | 0.107 | 1.04 | [0.91, 1.20] | 1.05 |
| Qwen2.5-7B | B | 77 | 66 | 0.068 | 0.093 | 0.73 | [0.59, 0.92] | 0.73 |
| Qwen2.5-7B-Instruct | B | 77 | 65 | 0.056 | 0.070 | 0.80 | [0.55, 1.18] | 0.79 |
| gemma-2b | B | 72 | 65 | 0.192 | 0.170 | 1.13 | [1.02, 1.25] | 1.12 |
| gemma-2b-it | B | 67 | 65 | 0.162 | 0.159 | 1.02 | [0.91, 1.14] | 1.02 |
| Llama-3.1-8B | A0 | 78 | 0 | too few included pairs: person | | | | |
| Llama-3.1-8B-Instruct | A0 | 77 | 0 | too few included pairs: person | | | | |
| Llama-3.2-1B | A0 | 74 | 0 | too few included pairs: person | | | | |
| Llama-3.2-1B-Instruct | A0 | 72 | 0 | too few included pairs: person | | | | |
| Llama-3.2-3B | A0 | 78 | 0 | too few included pairs: person | | | | |
| Llama-3.2-3B-Instruct | A0 | 77 | 0 | too few included pairs: person | | | | |
| Qwen2.5-14B | A0 | 80 | 0 | too few included pairs: person | | | | |
| Qwen2.5-14B-Instruct | A0 | 80 | 0 | too few included pairs: person | | | | |
| Qwen2.5-3B | A0 | 57 | 0 | too few included pairs: person | | | | |
| Qwen2.5-3B-Instruct | A0 | 77 | 0 | too few included pairs: person | | | | |
| Qwen2.5-7B | A0 | 78 | 0 | too few included pairs: person | | | | |
| Qwen2.5-7B-Instruct | A0 | 77 | 0 | too few included pairs: person | | | | |
| gemma-2b | A0 | 75 | 0 | too few included pairs: person | | | | |
| gemma-2b-it | A0 | 73 | 0 | too few included pairs: person | | | | |

## Behaviour

| model | frame | group | run | included | mean gap | better version preferred | mean mass | multiple of random |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | moral | 80 | 78 | +0.756 | 0.97 | 0.50 | 6.99 |
| Llama-3.1-8B | A1 | norm | 107 | 104 | +0.431 | 0.98 | 0.33 | 8.42 |
| Llama-3.1-8B | A1 | thing | 40 | 38 | +0.230 | 1.00 | 0.16 | 7.98 |
| Llama-3.1-8B | A1 | person | 66 | 65 | +0.327 | 0.98 | 0.23 | 7.48 |
| Llama-3.1-8B | B | moral | 80 | 77 | +0.611 | 0.96 | 0.46 | 5.86 |
| Llama-3.1-8B | B | norm | 107 | 104 | +0.600 | 0.97 | 0.50 | 6.80 |
| Llama-3.1-8B | B | thing | 40 | 40 | +0.605 | 1.00 | 0.41 | 5.77 |
| Llama-3.1-8B | B | person | 66 | 66 | +0.684 | 1.00 | 0.45 | 8.35 |
| Llama-3.1-8B | A0 | moral | 80 | 78 | +0.553 | 0.97 | 0.58 | 8.13 |
| Llama-3.1-8B | A0 | norm | 107 | 98 | +0.291 | 0.93 | 0.46 | 6.41 |
| Llama-3.1-8B | A0 | thing | 40 | 31 | +0.068 | 0.88 | 0.12 | 5.58 |
| Llama-3.1-8B-Instruct | A1 | moral | 80 | 78 | +1.060 | 0.97 | 0.64 | 9.27 |
| Llama-3.1-8B-Instruct | A1 | norm | 107 | 107 | +0.625 | 1.00 | 0.40 | 10.35 |
| Llama-3.1-8B-Instruct | A1 | thing | 40 | 37 | +0.255 | 1.00 | 0.16 | 10.32 |
| Llama-3.1-8B-Instruct | A1 | person | 66 | 64 | +0.423 | 0.98 | 0.27 | 8.62 |
| Llama-3.1-8B-Instruct | B | moral | 80 | 78 | +0.819 | 0.97 | 0.56 | 5.66 |
| Llama-3.1-8B-Instruct | B | norm | 107 | 103 | +0.789 | 0.96 | 0.54 | 6.61 |
| Llama-3.1-8B-Instruct | B | thing | 40 | 40 | +0.755 | 1.00 | 0.44 | 5.58 |
| Llama-3.1-8B-Instruct | B | person | 66 | 65 | +0.802 | 1.00 | 0.49 | 5.57 |
| Llama-3.1-8B-Instruct | A0 | moral | 80 | 77 | +0.608 | 0.97 | 0.46 | 10.46 |
| Llama-3.1-8B-Instruct | A0 | norm | 107 | 104 | +0.281 | 0.99 | 0.32 | 8.21 |
| Llama-3.1-8B-Instruct | A0 | thing | 40 | 30 | +0.062 | 0.93 | 0.10 | 6.53 |
| Llama-3.2-1B | A1 | moral | 80 | 78 | +0.492 | 0.99 | 0.69 | 4.48 |
| Llama-3.2-1B | A1 | norm | 107 | 97 | +0.348 | 0.93 | 0.60 | 4.20 |
| Llama-3.2-1B | A1 | thing | 40 | 39 | +0.350 | 1.00 | 0.44 | 4.12 |
| Llama-3.2-1B | A1 | person | 66 | 65 | +0.519 | 0.98 | 0.62 | 4.98 |
| Llama-3.2-1B | B | moral | 80 | 73 | +0.314 | 0.93 | 0.56 | 4.19 |
| Llama-3.2-1B | B | norm | 107 | 91 | +0.243 | 0.91 | 0.55 | 3.88 |
| Llama-3.2-1B | B | thing | 40 | 35 | +0.290 | 0.90 | 0.46 | 3.40 |
| Llama-3.2-1B | B | person | 66 | 64 | +0.393 | 0.98 | 0.50 | 4.57 |
| Llama-3.2-1B | A0 | moral | 80 | 74 | +0.343 | 0.93 | 0.57 | 3.75 |
| Llama-3.2-1B | A0 | norm | 107 | 82 | +0.159 | 0.80 | 0.39 | 3.69 |
| Llama-3.2-1B | A0 | thing | 40 | 27 | +0.076 | 0.88 | 0.16 | 3.77 |
| Llama-3.2-1B-Instruct | A1 | moral | 80 | 69 | +0.463 | 0.91 | 0.67 | 2.47 |
| Llama-3.2-1B-Instruct | A1 | norm | 107 | 92 | +0.278 | 0.90 | 0.51 | 2.18 |
| Llama-3.2-1B-Instruct | A1 | thing | 40 | 38 | +0.309 | 0.97 | 0.39 | 1.59 |
| Llama-3.2-1B-Instruct | A1 | person | 66 | 64 | +0.450 | 1.00 | 0.53 | 1.89 |
| Llama-3.2-1B-Instruct | B | moral | 80 | 72 | +0.655 | 0.91 | 0.60 | 2.23 |
| Llama-3.2-1B-Instruct | B | norm | 107 | 95 | +0.434 | 0.92 | 0.57 | 2.15 |
| Llama-3.2-1B-Instruct | B | thing | 40 | 37 | +0.425 | 0.95 | 0.38 | 1.51 |
| Llama-3.2-1B-Instruct | B | person | 66 | 66 | +0.683 | 1.00 | 0.60 | 2.07 |
| Llama-3.2-1B-Instruct | A0 | moral | 80 | 72 | +0.224 | 0.91 | 0.27 | 3.22 |
| Llama-3.2-1B-Instruct | A0 | norm | 107 | 86 | +0.108 | 0.92 | 0.19 | 2.62 |
| Llama-3.2-1B-Instruct | A0 | thing | 40 | 24 | +0.040 | 0.93 | 0.07 | 2.35 |
| Llama-3.2-3B | A1 | moral | 80 | 79 | +0.728 | 0.99 | 0.63 | 8.12 |
| Llama-3.2-3B | A1 | norm | 107 | 104 | +0.548 | 0.98 | 0.57 | 8.77 |
| Llama-3.2-3B | A1 | thing | 40 | 40 | +0.389 | 1.00 | 0.36 | 7.76 |
| Llama-3.2-3B | A1 | person | 66 | 65 | +0.617 | 0.98 | 0.51 | 10.32 |
| Llama-3.2-3B | B | moral | 80 | 78 | +0.537 | 0.97 | 0.44 | 5.45 |
| Llama-3.2-3B | B | norm | 107 | 100 | +0.482 | 0.95 | 0.53 | 6.19 |
| Llama-3.2-3B | B | thing | 40 | 40 | +0.477 | 1.00 | 0.47 | 6.21 |
| Llama-3.2-3B | B | person | 66 | 66 | +0.590 | 1.00 | 0.41 | 7.65 |
| Llama-3.2-3B | A0 | moral | 80 | 78 | +0.465 | 0.97 | 0.59 | 7.17 |
| Llama-3.2-3B | A0 | norm | 107 | 90 | +0.227 | 0.91 | 0.44 | 6.44 |
| Llama-3.2-3B | A0 | thing | 40 | 25 | +0.050 | 0.82 | 0.10 | 5.67 |
| Llama-3.2-3B-Instruct | A1 | moral | 80 | 72 | +1.002 | 0.91 | 0.75 | 7.55 |
| Llama-3.2-3B-Instruct | A1 | norm | 107 | 103 | +0.819 | 0.97 | 0.64 | 7.77 |
| Llama-3.2-3B-Instruct | A1 | thing | 40 | 39 | +0.653 | 1.00 | 0.49 | 6.33 |
| Llama-3.2-3B-Instruct | A1 | person | 66 | 66 | +1.056 | 1.00 | 0.69 | 7.78 |
| Llama-3.2-3B-Instruct | B | moral | 80 | 69 | +0.766 | 0.86 | 0.57 | 4.36 |
| Llama-3.2-3B-Instruct | B | norm | 107 | 103 | +0.751 | 0.96 | 0.57 | 5.41 |
| Llama-3.2-3B-Instruct | B | thing | 40 | 39 | +0.669 | 1.00 | 0.45 | 5.12 |
| Llama-3.2-3B-Instruct | B | person | 66 | 66 | +0.929 | 1.00 | 0.58 | 5.36 |
| Llama-3.2-3B-Instruct | A0 | moral | 80 | 77 | +0.407 | 0.97 | 0.32 | 7.05 |
| Llama-3.2-3B-Instruct | A0 | norm | 107 | 95 | +0.167 | 0.93 | 0.20 | 6.88 |
| Llama-3.2-3B-Instruct | A0 | thing | 40 | 30 | +0.047 | 0.95 | 0.08 | 5.28 |
| Qwen2.5-14B | A1 | moral | 80 | 79 | +1.353 | 0.99 | 0.81 | 14.11 |
| Qwen2.5-14B | A1 | norm | 107 | 99 | +0.745 | 0.96 | 0.51 | 11.55 |
| Qwen2.5-14B | A1 | thing | 40 | 36 | +0.166 | 1.00 | 0.13 | 8.02 |
| Qwen2.5-14B | A1 | person | 66 | 64 | +0.519 | 0.97 | 0.37 | 8.82 |
| Qwen2.5-14B | B | moral | 80 | 79 | +1.270 | 0.99 | 0.77 | 6.82 |
| Qwen2.5-14B | B | norm | 107 | 106 | +1.059 | 0.99 | 0.69 | 7.46 |
| Qwen2.5-14B | B | thing | 40 | 40 | +1.078 | 1.00 | 0.64 | 5.69 |
| Qwen2.5-14B | B | person | 66 | 66 | +1.239 | 1.00 | 0.72 | 5.90 |
| Qwen2.5-14B | A0 | moral | 80 | 80 | +0.749 | 1.00 | 0.70 | 8.69 |
| Qwen2.5-14B | A0 | norm | 107 | 101 | +0.368 | 0.97 | 0.61 | 7.19 |
| Qwen2.5-14B | A0 | thing | 40 | 32 | +0.097 | 0.95 | 0.15 | 6.61 |
| Qwen2.5-14B-Instruct | A1 | moral | 80 | 79 | +1.488 | 1.00 | 0.84 | 10.51 |
| Qwen2.5-14B-Instruct | A1 | norm | 107 | 99 | +0.779 | 0.97 | 0.46 | 10.17 |
| Qwen2.5-14B-Instruct | A1 | thing | 40 | 18* | +0.120 | 0.97 | 0.07 | 6.65 |
| Qwen2.5-14B-Instruct | A1 | person | 66 | 61 | +0.590 | 0.97 | 0.37 | 7.88 |
| Qwen2.5-14B-Instruct | B | moral | 80 | 78 | +1.314 | 0.97 | 0.72 | 5.62 |
| Qwen2.5-14B-Instruct | B | norm | 107 | 104 | +1.035 | 0.98 | 0.61 | 6.44 |
| Qwen2.5-14B-Instruct | B | thing | 40 | 40 | +1.187 | 1.00 | 0.62 | 4.51 |
| Qwen2.5-14B-Instruct | B | person | 66 | 65 | +1.214 | 0.98 | 0.66 | 5.63 |
| Qwen2.5-14B-Instruct | A0 | moral | 80 | 80 | +0.777 | 1.00 | 0.77 | 8.06 |
| Qwen2.5-14B-Instruct | A0 | norm | 107 | 95 | +0.467 | 0.92 | 0.69 | 6.48 |
| Qwen2.5-14B-Instruct | A0 | thing | 40 | 32 | +0.123 | 0.93 | 0.15 | 5.89 |
| Qwen2.5-3B | A1 | moral | 80 | 78 | +0.465 | 0.97 | 0.75 | 3.90 |
| Qwen2.5-3B | A1 | norm | 107 | 98 | +0.259 | 0.94 | 0.65 | 3.55 |
| Qwen2.5-3B | A1 | thing | 40 | 39 | +0.293 | 1.00 | 0.52 | 3.08 |
| Qwen2.5-3B | A1 | person | 66 | 65 | +0.450 | 1.00 | 0.65 | 3.21 |
| Qwen2.5-3B | B | moral | 80 | 75 | +0.498 | 0.95 | 0.63 | 3.37 |
| Qwen2.5-3B | B | norm | 107 | 101 | +0.389 | 0.95 | 0.51 | 4.03 |
| Qwen2.5-3B | B | thing | 40 | 40 | +0.434 | 1.00 | 0.51 | 3.33 |
| Qwen2.5-3B | B | person | 66 | 65 | +0.639 | 0.98 | 0.59 | 3.93 |
| Qwen2.5-3B | A0 | moral | 80 | 57 | +0.284 | 0.71 | 0.55 | 4.19 |
| Qwen2.5-3B | A0 | norm | 107 | 80 | +0.202 | 0.77 | 0.50 | 3.64 |
| Qwen2.5-3B | A0 | thing | 40 | 3* | +0.001 | 0.55 | 0.07 | 3.29 |
| Qwen2.5-3B-Instruct | A1 | moral | 80 | 76 | +1.011 | 0.97 | 0.79 | 7.34 |
| Qwen2.5-3B-Instruct | A1 | norm | 107 | 103 | +0.892 | 0.96 | 0.69 | 6.68 |
| Qwen2.5-3B-Instruct | A1 | thing | 40 | 40 | +0.683 | 1.00 | 0.47 | 7.23 |
| Qwen2.5-3B-Instruct | A1 | person | 66 | 65 | +1.082 | 1.00 | 0.64 | 6.95 |
| Qwen2.5-3B-Instruct | B | moral | 80 | 76 | +1.015 | 0.96 | 0.70 | 6.42 |
| Qwen2.5-3B-Instruct | B | norm | 107 | 104 | +0.851 | 0.98 | 0.58 | 6.22 |
| Qwen2.5-3B-Instruct | B | thing | 40 | 40 | +0.869 | 1.00 | 0.54 | 6.01 |
| Qwen2.5-3B-Instruct | B | person | 66 | 65 | +1.329 | 1.00 | 0.73 | 6.15 |
| Qwen2.5-3B-Instruct | A0 | moral | 80 | 77 | +0.614 | 0.97 | 0.71 | 5.15 |
| Qwen2.5-3B-Instruct | A0 | norm | 107 | 101 | +0.350 | 0.96 | 0.57 | 4.58 |
| Qwen2.5-3B-Instruct | A0 | thing | 40 | 36 | +0.110 | 0.97 | 0.18 | 4.26 |
| Qwen2.5-7B | A1 | moral | 80 | 79 | +1.121 | 0.99 | 0.80 | 6.44 |
| Qwen2.5-7B | A1 | norm | 107 | 104 | +0.858 | 0.98 | 0.67 | 7.09 |
| Qwen2.5-7B | A1 | thing | 40 | 40 | +0.531 | 1.00 | 0.47 | 4.90 |
| Qwen2.5-7B | A1 | person | 66 | 66 | +0.865 | 1.00 | 0.63 | 5.94 |
| Qwen2.5-7B | B | moral | 80 | 77 | +1.055 | 0.96 | 0.78 | 5.31 |
| Qwen2.5-7B | B | norm | 107 | 107 | +1.044 | 1.00 | 0.75 | 7.56 |
| Qwen2.5-7B | B | thing | 40 | 40 | +1.077 | 1.00 | 0.72 | 5.53 |
| Qwen2.5-7B | B | person | 66 | 66 | +1.392 | 1.00 | 0.83 | 7.28 |
| Qwen2.5-7B | A0 | moral | 80 | 78 | +0.630 | 0.99 | 0.62 | 5.42 |
| Qwen2.5-7B | A0 | norm | 107 | 99 | +0.317 | 0.94 | 0.48 | 5.89 |
| Qwen2.5-7B | A0 | thing | 40 | 28 | +0.078 | 0.90 | 0.13 | 4.32 |
| Qwen2.5-7B-Instruct | A1 | moral | 80 | 75 | +1.163 | 0.95 | 0.79 | 5.12 |
| Qwen2.5-7B-Instruct | A1 | norm | 107 | 106 | +0.957 | 0.99 | 0.70 | 5.89 |
| Qwen2.5-7B-Instruct | A1 | thing | 40 | 40 | +0.715 | 1.00 | 0.46 | 3.72 |
| Qwen2.5-7B-Instruct | A1 | person | 66 | 65 | +1.046 | 0.98 | 0.70 | 4.13 |
| Qwen2.5-7B-Instruct | B | moral | 80 | 77 | +1.240 | 0.96 | 0.80 | 4.36 |
| Qwen2.5-7B-Instruct | B | norm | 107 | 104 | +1.160 | 0.97 | 0.75 | 5.03 |
| Qwen2.5-7B-Instruct | B | thing | 40 | 40 | +1.211 | 1.00 | 0.67 | 3.56 |
| Qwen2.5-7B-Instruct | B | person | 66 | 65 | +1.450 | 1.00 | 0.86 | 5.46 |
| Qwen2.5-7B-Instruct | A0 | moral | 80 | 77 | +0.629 | 0.96 | 0.62 | 5.08 |
| Qwen2.5-7B-Instruct | A0 | norm | 107 | 92 | +0.302 | 0.86 | 0.51 | 4.58 |
| Qwen2.5-7B-Instruct | A0 | thing | 40 | 28 | +0.132 | 0.90 | 0.14 | 4.00 |
| gemma-2b | A1 | moral | 80 | 74 | +0.602 | 0.96 | 0.52 | 2.75 |
| gemma-2b | A1 | norm | 107 | 99 | +0.453 | 0.95 | 0.47 | 2.97 |
| gemma-2b | A1 | thing | 40 | 39 | +0.420 | 0.97 | 0.41 | 2.54 |
| gemma-2b | A1 | person | 66 | 66 | +0.712 | 1.00 | 0.51 | 2.29 |
| gemma-2b | B | moral | 80 | 72 | +0.488 | 0.93 | 0.46 | 2.77 |
| gemma-2b | B | norm | 107 | 95 | +0.423 | 0.93 | 0.45 | 3.05 |
| gemma-2b | B | thing | 40 | 40 | +0.483 | 1.00 | 0.50 | 2.40 |
| gemma-2b | B | person | 66 | 65 | +0.644 | 0.98 | 0.46 | 2.45 |
| gemma-2b | A0 | moral | 80 | 75 | +0.409 | 0.94 | 0.59 | 3.02 |
| gemma-2b | A0 | norm | 107 | 93 | +0.262 | 0.89 | 0.43 | 2.99 |
| gemma-2b | A0 | thing | 40 | 34 | +0.095 | 0.95 | 0.14 | 2.83 |
| gemma-2b-it | A1 | moral | 80 | 73 | +1.007 | 0.94 | 0.92 | 2.26 |
| gemma-2b-it | A1 | norm | 107 | 98 | +0.758 | 0.93 | 0.84 | 2.14 |
| gemma-2b-it | A1 | thing | 40 | 37 | +0.680 | 0.93 | 0.66 | 1.83 |
| gemma-2b-it | A1 | person | 66 | 66 | +1.225 | 1.00 | 0.91 | 1.68 |
| gemma-2b-it | B | moral | 80 | 67 | +0.556 | 0.84 | 0.50 | 2.33 |
| gemma-2b-it | B | norm | 107 | 88 | +0.335 | 0.84 | 0.39 | 2.36 |
| gemma-2b-it | B | thing | 40 | 34 | +0.465 | 0.85 | 0.45 | 2.21 |
| gemma-2b-it | B | person | 66 | 65 | +0.599 | 0.98 | 0.39 | 2.29 |
| gemma-2b-it | A0 | moral | 80 | 73 | +0.464 | 0.94 | 0.60 | 2.38 |
| gemma-2b-it | A0 | norm | 107 | 92 | +0.367 | 0.90 | 0.43 | 2.33 |
| gemma-2b-it | A0 | thing | 40 | 21 | +0.096 | 0.85 | 0.13 | 2.11 |

\* fewer included pairs than the minimum; shown, not pooled.
