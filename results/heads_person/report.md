# The located heads on the control pairs about a person

Pairs: moral 80, norm 107, thing 40, person 58. Control pairs: 66 candidates, 58 accepted by the screen (llm); used here: 58 (accepted). Runs: runs/heads, runs/heads_followup_person. Head set located, condition p2r_all, effects read on S, a pair is included when its gap in S is at least 0.02, 10000 bootstrap resamples.

Check against results/heads: the study's contrasts recomputed here are the same (122 per-model and 9 pooled ratios; largest difference 0.0e+00).

## Reading

- Frame A1: norm/person 1.11 [1.04, 1.19] (above 1); person/thing 1.08 [1.01, 1.15] (above 1): both contribute: the control pairs lie between the normative pairs and the descriptive pairs about a thing
- Frame B: norm/person 1.00 [0.92, 1.09] (includes 1); person/thing 1.22 [1.11, 1.32] (above 1): the fifth comes from the form of the phrase, not from the standard: on the control pairs the located heads carry what they carry on normative pairs
- Frame A0: not available (a group is missing or has too few included pairs)

## Pooled ratios of the located heads' share (geometric mean over models; 95 % interval from the item bootstrap)

| frame | contrast | models | ratio | 95 % interval | within template types | models with interval above 1 / below 1 | left out |
|---|---|---|---|---|---|---|---|
| A1 | norm/person | 14 | 1.11 | [1.04, 1.19] | 1.11 [1.05, 1.17] | 8 / 2 | - |
| A1 | moral/person | 14 | 1.11 | [1.03, 1.19] | 1.12 [1.05, 1.19] | 6 / 2 | - |
| A1 | person/thing | 13 | 1.08 | [1.01, 1.15] |  | 5 / 1 | Qwen2.5-14B-Instruct |
| A1 | norm/thing | 13 | 1.19 | [1.13, 1.26] |  | 9 / 0 | Qwen2.5-14B-Instruct |
| A1 | moral/thing | 13 | 1.19 | [1.11, 1.26] |  | 6 / 1 | Qwen2.5-14B-Instruct |
| A1 | moral/norm | 14 | 1.00 | [0.93, 1.06] |  | 2 / 2 | - |
| B | norm/person | 14 | 1.00 | [0.92, 1.09] | 0.99 [0.93, 1.07] | 2 / 3 | - |
| B | moral/person | 14 | 0.89 | [0.82, 0.98] | 0.89 [0.83, 0.97] | 0 / 6 | - |
| B | person/thing | 14 | 1.22 | [1.11, 1.32] |  | 8 / 0 | - |
| B | norm/thing | 14 | 1.21 | [1.14, 1.28] |  | 10 / 0 | - |
| B | moral/thing | 14 | 1.09 | [1.02, 1.16] |  | 5 / 1 | - |
| B | moral/norm | 14 | 0.90 | [0.85, 0.95] |  | 0 / 6 | - |
| A0 | norm/thing | 13 | 1.14 | [1.08, 1.21] |  | 5 / 0 | Qwen2.5-3B |
| A0 | moral/thing | 13 | 1.27 | [1.19, 1.35] |  | 11 / 0 | Qwen2.5-3B |
| A0 | moral/norm | 14 | 1.12 | [1.05, 1.18] |  | 5 / 0 | - |

## The share as a multiple of the share of ten heads chosen at random (geometric mean over models)

| frame | models | moral | norm | person | thing |
|---|---|---|---|---|---|
| A1 | 13 (all groups) | 5.44 | 5.47 | 4.97 | 4.59 |
| A1 | 13 (study groups) | 5.44 | 5.47 | n/a | 4.59 |
| B | 14 (all groups) | 4.36 | 4.86 | 4.88 | 4.01 |
| B | 14 (study groups) | 4.36 | 4.86 | n/a | 4.01 |
| A0 | 13 (study groups) | 5.44 | 4.89 | n/a | 4.29 |

## Per model, norm/person

| model | frame | n | n | share | share | ratio | 95 % interval | within template types |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A1 | 104 | 57 | 0.082 | 0.074 | 1.12 | [1.01, 1.24] | 1.12 |
| Llama-3.1-8B-Instruct | A1 | 107 | 57 | 0.101 | 0.087 | 1.16 | [1.05, 1.29] | 1.16 |
| Llama-3.2-1B | A1 | 97 | 58 | 0.082 | 0.099 | 0.83 | [0.76, 0.90] | 0.83 |
| Llama-3.2-1B-Instruct | A1 | 92 | 57 | 0.043 | 0.037 | 1.16 | [1.04, 1.30] | 1.17 |
| Llama-3.2-3B | A1 | 104 | 57 | 0.131 | 0.157 | 0.83 | [0.75, 0.92] | 0.83 |
| Llama-3.2-3B-Instruct | A1 | 103 | 58 | 0.116 | 0.120 | 0.96 | [0.85, 1.10] | 0.96 |
| Qwen2.5-14B | A1 | 99 | 57 | 0.060 | 0.046 | 1.30 | [1.16, 1.45] | 1.29 |
| Qwen2.5-14B-Instruct | A1 | 99 | 54 | 0.053 | 0.042 | 1.25 | [1.10, 1.43] | 1.24 |
| Qwen2.5-3B | A1 | 98 | 57 | 0.062 | 0.056 | 1.10 | [0.97, 1.26] | 1.10 |
| Qwen2.5-3B-Instruct | A1 | 103 | 57 | 0.116 | 0.123 | 0.94 | [0.82, 1.08] | 0.94 |
| Qwen2.5-7B | A1 | 104 | 58 | 0.090 | 0.078 | 1.16 | [0.95, 1.40] | 1.16 |
| Qwen2.5-7B-Instruct | A1 | 106 | 57 | 0.075 | 0.054 | 1.38 | [1.03, 1.85] | 1.38 |
| gemma-2b | A1 | 99 | 58 | 0.206 | 0.159 | 1.29 | [1.19, 1.41] | 1.30 |
| gemma-2b-it | A1 | 98 | 58 | 0.149 | 0.117 | 1.27 | [1.15, 1.40] | 1.26 |
| Llama-3.1-8B | B | 104 | 58 | 0.066 | 0.084 | 0.79 | [0.67, 0.94] | 0.79 |
| Llama-3.1-8B-Instruct | B | 103 | 58 | 0.065 | 0.055 | 1.16 | [0.99, 1.38] | 1.16 |
| Llama-3.2-1B | B | 91 | 58 | 0.076 | 0.090 | 0.84 | [0.77, 0.93] | 0.85 |
| Llama-3.2-1B-Instruct | B | 95 | 58 | 0.042 | 0.041 | 1.03 | [0.91, 1.18] | 1.04 |
| Llama-3.2-3B | B | 100 | 58 | 0.092 | 0.118 | 0.78 | [0.68, 0.89] | 0.78 |
| Llama-3.2-3B-Instruct | B | 103 | 58 | 0.080 | 0.081 | 0.99 | [0.86, 1.13] | 0.99 |
| Qwen2.5-14B | B | 106 | 58 | 0.039 | 0.031 | 1.26 | [1.08, 1.47] | 1.25 |
| Qwen2.5-14B-Instruct | B | 104 | 58 | 0.034 | 0.030 | 1.11 | [0.97, 1.28] | 1.11 |
| Qwen2.5-3B | B | 101 | 57 | 0.070 | 0.067 | 1.04 | [0.92, 1.19] | 1.04 |
| Qwen2.5-3B-Instruct | B | 104 | 57 | 0.108 | 0.108 | 1.00 | [0.86, 1.17] | 0.99 |
| Qwen2.5-7B | B | 107 | 58 | 0.096 | 0.096 | 1.00 | [0.80, 1.26] | 0.99 |
| Qwen2.5-7B-Instruct | B | 104 | 57 | 0.064 | 0.074 | 0.87 | [0.62, 1.25] | 0.87 |
| gemma-2b | B | 95 | 57 | 0.212 | 0.174 | 1.22 | [1.11, 1.34] | 1.21 |
| gemma-2b-it | B | 88 | 57 | 0.164 | 0.163 | 1.01 | [0.91, 1.11] | 1.01 |
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
| Llama-3.1-8B | A1 | 57 | 38 | 0.074 | 0.078 | 0.94 | [0.84, 1.06] | n/a |
| Llama-3.1-8B-Instruct | A1 | 57 | 37 | 0.087 | 0.101 | 0.86 | [0.78, 0.96] | n/a |
| Llama-3.2-1B | A1 | 58 | 39 | 0.099 | 0.081 | 1.23 | [1.12, 1.35] | n/a |
| Llama-3.2-1B-Instruct | A1 | 57 | 38 | 0.037 | 0.031 | 1.19 | [1.03, 1.38] | n/a |
| Llama-3.2-3B | A1 | 57 | 40 | 0.157 | 0.115 | 1.36 | [1.21, 1.53] | n/a |
| Llama-3.2-3B-Instruct | A1 | 58 | 39 | 0.120 | 0.094 | 1.27 | [1.10, 1.46] | n/a |
| Qwen2.5-14B | A1 | 57 | 36 | 0.046 | 0.042 | 1.11 | [0.98, 1.25] | n/a |
| Qwen2.5-14B-Instruct | A1 | 54 | 18 | too few included pairs: thing | | | | |
| Qwen2.5-3B | A1 | 57 | 39 | 0.056 | 0.053 | 1.05 | [0.91, 1.21] | n/a |
| Qwen2.5-3B-Instruct | A1 | 57 | 40 | 0.123 | 0.126 | 0.98 | [0.85, 1.13] | n/a |
| Qwen2.5-7B | A1 | 58 | 40 | 0.078 | 0.062 | 1.25 | [1.05, 1.47] | n/a |
| Qwen2.5-7B-Instruct | A1 | 57 | 40 | 0.054 | 0.048 | 1.14 | [0.91, 1.46] | n/a |
| gemma-2b | A1 | 58 | 39 | 0.159 | 0.176 | 0.90 | [0.81, 1.01] | n/a |
| gemma-2b-it | A1 | 58 | 37 | 0.117 | 0.127 | 0.92 | [0.80, 1.07] | n/a |
| Llama-3.1-8B | B | 58 | 40 | 0.084 | 0.056 | 1.49 | [1.24, 1.77] | n/a |
| Llama-3.1-8B-Instruct | B | 58 | 40 | 0.055 | 0.054 | 1.02 | [0.85, 1.21] | n/a |
| Llama-3.2-1B | B | 58 | 35 | 0.090 | 0.066 | 1.35 | [1.20, 1.52] | n/a |
| Llama-3.2-1B-Instruct | B | 58 | 37 | 0.041 | 0.030 | 1.38 | [1.17, 1.63] | n/a |
| Llama-3.2-3B | B | 58 | 40 | 0.118 | 0.092 | 1.28 | [1.11, 1.48] | n/a |
| Llama-3.2-3B-Instruct | B | 58 | 39 | 0.081 | 0.076 | 1.07 | [0.92, 1.24] | n/a |
| Qwen2.5-14B | B | 58 | 40 | 0.031 | 0.030 | 1.05 | [0.89, 1.24] | n/a |
| Qwen2.5-14B-Instruct | B | 58 | 40 | 0.030 | 0.024 | 1.28 | [1.11, 1.46] | n/a |
| Qwen2.5-3B | B | 57 | 40 | 0.067 | 0.058 | 1.16 | [1.01, 1.33] | n/a |
| Qwen2.5-3B-Instruct | B | 57 | 40 | 0.108 | 0.104 | 1.04 | [0.87, 1.24] | n/a |
| Qwen2.5-7B | B | 58 | 40 | 0.096 | 0.071 | 1.37 | [1.07, 1.72] | n/a |
| Qwen2.5-7B-Instruct | B | 57 | 40 | 0.074 | 0.045 | 1.63 | [1.14, 2.25] | n/a |
| gemma-2b | B | 57 | 40 | 0.174 | 0.167 | 1.04 | [0.92, 1.18] | n/a |
| gemma-2b-it | B | 57 | 34 | 0.163 | 0.153 | 1.06 | [0.94, 1.20] | n/a |
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
| Llama-3.1-8B | A1 | 78 | 57 | 0.068 | 0.074 | 0.93 | [0.82, 1.05] | 0.93 |
| Llama-3.1-8B-Instruct | A1 | 78 | 57 | 0.091 | 0.087 | 1.04 | [0.93, 1.17] | 1.05 |
| Llama-3.2-1B | A1 | 78 | 58 | 0.087 | 0.099 | 0.88 | [0.82, 0.96] | 0.89 |
| Llama-3.2-1B-Instruct | A1 | 69 | 57 | 0.048 | 0.037 | 1.31 | [1.15, 1.51] | 1.29 |
| Llama-3.2-3B | A1 | 79 | 57 | 0.121 | 0.157 | 0.77 | [0.69, 0.86] | 0.78 |
| Llama-3.2-3B-Instruct | A1 | 72 | 58 | 0.112 | 0.120 | 0.94 | [0.81, 1.09] | 0.95 |
| Qwen2.5-14B | A1 | 79 | 57 | 0.073 | 0.046 | 1.59 | [1.40, 1.80] | 1.64 |
| Qwen2.5-14B-Instruct | A1 | 79 | 54 | 0.055 | 0.042 | 1.30 | [1.11, 1.50] | 1.33 |
| Qwen2.5-3B | A1 | 78 | 57 | 0.068 | 0.056 | 1.21 | [1.06, 1.38] | 1.22 |
| Qwen2.5-3B-Instruct | A1 | 76 | 57 | 0.128 | 0.123 | 1.04 | [0.88, 1.23] | 1.09 |
| Qwen2.5-7B | A1 | 79 | 58 | 0.082 | 0.078 | 1.05 | [0.83, 1.36] | 1.04 |
| Qwen2.5-7B-Instruct | A1 | 75 | 57 | 0.065 | 0.054 | 1.20 | [0.82, 1.75] | 1.17 |
| gemma-2b | A1 | 74 | 58 | 0.191 | 0.159 | 1.20 | [1.09, 1.32] | 1.20 |
| gemma-2b-it | A1 | 73 | 58 | 0.157 | 0.117 | 1.34 | [1.19, 1.50] | 1.34 |
| Llama-3.1-8B | B | 77 | 58 | 0.057 | 0.084 | 0.68 | [0.57, 0.81] | 0.68 |
| Llama-3.1-8B-Instruct | B | 78 | 58 | 0.055 | 0.055 | 1.00 | [0.84, 1.19] | 0.99 |
| Llama-3.2-1B | B | 73 | 58 | 0.082 | 0.090 | 0.91 | [0.83, 1.00] | 0.92 |
| Llama-3.2-1B-Instruct | B | 72 | 58 | 0.043 | 0.041 | 1.06 | [0.91, 1.25] | 1.02 |
| Llama-3.2-3B | B | 78 | 58 | 0.081 | 0.118 | 0.69 | [0.60, 0.78] | 0.69 |
| Llama-3.2-3B-Instruct | B | 69 | 58 | 0.065 | 0.081 | 0.80 | [0.70, 0.92] | 0.80 |
| Qwen2.5-14B | B | 79 | 58 | 0.036 | 0.031 | 1.15 | [0.96, 1.37] | 1.17 |
| Qwen2.5-14B-Instruct | B | 78 | 58 | 0.029 | 0.030 | 0.97 | [0.82, 1.15] | 0.98 |
| Qwen2.5-3B | B | 75 | 57 | 0.059 | 0.067 | 0.87 | [0.76, 0.99] | 0.88 |
| Qwen2.5-3B-Instruct | B | 76 | 57 | 0.111 | 0.108 | 1.03 | [0.89, 1.20] | 1.04 |
| Qwen2.5-7B | B | 77 | 58 | 0.068 | 0.096 | 0.70 | [0.56, 0.90] | 0.71 |
| Qwen2.5-7B-Instruct | B | 77 | 57 | 0.056 | 0.074 | 0.75 | [0.52, 1.13] | 0.74 |
| gemma-2b | B | 72 | 57 | 0.192 | 0.174 | 1.11 | [1.00, 1.23] | 1.11 |
| gemma-2b-it | B | 67 | 57 | 0.162 | 0.163 | 0.99 | [0.88, 1.12] | 1.00 |
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
| Llama-3.1-8B | A1 | person | 58 | 57 | +0.333 | 0.98 | 0.23 | 7.54 |
| Llama-3.1-8B | B | moral | 80 | 77 | +0.611 | 0.96 | 0.46 | 5.86 |
| Llama-3.1-8B | B | norm | 107 | 104 | +0.600 | 0.97 | 0.50 | 6.80 |
| Llama-3.1-8B | B | thing | 40 | 40 | +0.605 | 1.00 | 0.41 | 5.77 |
| Llama-3.1-8B | B | person | 58 | 58 | +0.710 | 1.00 | 0.44 | 8.61 |
| Llama-3.1-8B | A0 | moral | 80 | 78 | +0.553 | 0.97 | 0.58 | 8.13 |
| Llama-3.1-8B | A0 | norm | 107 | 98 | +0.291 | 0.93 | 0.46 | 6.41 |
| Llama-3.1-8B | A0 | thing | 40 | 31 | +0.068 | 0.88 | 0.12 | 5.58 |
| Llama-3.1-8B-Instruct | A1 | moral | 80 | 78 | +1.060 | 0.97 | 0.64 | 9.27 |
| Llama-3.1-8B-Instruct | A1 | norm | 107 | 107 | +0.625 | 1.00 | 0.40 | 10.35 |
| Llama-3.1-8B-Instruct | A1 | thing | 40 | 37 | +0.255 | 1.00 | 0.16 | 10.32 |
| Llama-3.1-8B-Instruct | A1 | person | 58 | 57 | +0.436 | 0.98 | 0.26 | 8.91 |
| Llama-3.1-8B-Instruct | B | moral | 80 | 78 | +0.819 | 0.97 | 0.56 | 5.66 |
| Llama-3.1-8B-Instruct | B | norm | 107 | 103 | +0.789 | 0.96 | 0.54 | 6.61 |
| Llama-3.1-8B-Instruct | B | thing | 40 | 40 | +0.755 | 1.00 | 0.44 | 5.58 |
| Llama-3.1-8B-Instruct | B | person | 58 | 58 | +0.835 | 1.00 | 0.48 | 5.67 |
| Llama-3.1-8B-Instruct | A0 | moral | 80 | 77 | +0.608 | 0.97 | 0.46 | 10.46 |
| Llama-3.1-8B-Instruct | A0 | norm | 107 | 104 | +0.281 | 0.99 | 0.32 | 8.21 |
| Llama-3.1-8B-Instruct | A0 | thing | 40 | 30 | +0.062 | 0.93 | 0.10 | 6.53 |
| Llama-3.2-1B | A1 | moral | 80 | 78 | +0.492 | 0.99 | 0.69 | 4.48 |
| Llama-3.2-1B | A1 | norm | 107 | 97 | +0.348 | 0.93 | 0.60 | 4.20 |
| Llama-3.2-1B | A1 | thing | 40 | 39 | +0.350 | 1.00 | 0.44 | 4.12 |
| Llama-3.2-1B | A1 | person | 58 | 58 | +0.551 | 1.00 | 0.62 | 5.06 |
| Llama-3.2-1B | B | moral | 80 | 73 | +0.314 | 0.93 | 0.56 | 4.19 |
| Llama-3.2-1B | B | norm | 107 | 91 | +0.243 | 0.91 | 0.55 | 3.88 |
| Llama-3.2-1B | B | thing | 40 | 35 | +0.290 | 0.90 | 0.46 | 3.40 |
| Llama-3.2-1B | B | person | 58 | 58 | +0.416 | 1.00 | 0.50 | 4.59 |
| Llama-3.2-1B | A0 | moral | 80 | 74 | +0.343 | 0.93 | 0.57 | 3.75 |
| Llama-3.2-1B | A0 | norm | 107 | 82 | +0.159 | 0.80 | 0.39 | 3.69 |
| Llama-3.2-1B | A0 | thing | 40 | 27 | +0.076 | 0.88 | 0.16 | 3.77 |
| Llama-3.2-1B-Instruct | A1 | moral | 80 | 69 | +0.463 | 0.91 | 0.67 | 2.47 |
| Llama-3.2-1B-Instruct | A1 | norm | 107 | 92 | +0.278 | 0.90 | 0.51 | 2.18 |
| Llama-3.2-1B-Instruct | A1 | thing | 40 | 38 | +0.309 | 0.97 | 0.39 | 1.59 |
| Llama-3.2-1B-Instruct | A1 | person | 58 | 57 | +0.469 | 1.00 | 0.53 | 1.88 |
| Llama-3.2-1B-Instruct | B | moral | 80 | 72 | +0.655 | 0.91 | 0.60 | 2.23 |
| Llama-3.2-1B-Instruct | B | norm | 107 | 95 | +0.434 | 0.92 | 0.57 | 2.15 |
| Llama-3.2-1B-Instruct | B | thing | 40 | 37 | +0.425 | 0.95 | 0.38 | 1.51 |
| Llama-3.2-1B-Instruct | B | person | 58 | 58 | +0.715 | 1.00 | 0.59 | 2.09 |
| Llama-3.2-1B-Instruct | A0 | moral | 80 | 72 | +0.224 | 0.91 | 0.27 | 3.22 |
| Llama-3.2-1B-Instruct | A0 | norm | 107 | 86 | +0.108 | 0.92 | 0.19 | 2.62 |
| Llama-3.2-1B-Instruct | A0 | thing | 40 | 24 | +0.040 | 0.93 | 0.07 | 2.35 |
| Llama-3.2-3B | A1 | moral | 80 | 79 | +0.728 | 0.99 | 0.63 | 8.12 |
| Llama-3.2-3B | A1 | norm | 107 | 104 | +0.548 | 0.98 | 0.57 | 8.77 |
| Llama-3.2-3B | A1 | thing | 40 | 40 | +0.389 | 1.00 | 0.36 | 7.76 |
| Llama-3.2-3B | A1 | person | 58 | 57 | +0.630 | 0.98 | 0.51 | 10.57 |
| Llama-3.2-3B | B | moral | 80 | 78 | +0.537 | 0.97 | 0.44 | 5.45 |
| Llama-3.2-3B | B | norm | 107 | 100 | +0.482 | 0.95 | 0.53 | 6.19 |
| Llama-3.2-3B | B | thing | 40 | 40 | +0.477 | 1.00 | 0.47 | 6.21 |
| Llama-3.2-3B | B | person | 58 | 58 | +0.614 | 1.00 | 0.41 | 7.95 |
| Llama-3.2-3B | A0 | moral | 80 | 78 | +0.465 | 0.97 | 0.59 | 7.17 |
| Llama-3.2-3B | A0 | norm | 107 | 90 | +0.227 | 0.91 | 0.44 | 6.44 |
| Llama-3.2-3B | A0 | thing | 40 | 25 | +0.050 | 0.82 | 0.10 | 5.67 |
| Llama-3.2-3B-Instruct | A1 | moral | 80 | 72 | +1.002 | 0.91 | 0.75 | 7.55 |
| Llama-3.2-3B-Instruct | A1 | norm | 107 | 103 | +0.819 | 0.97 | 0.64 | 7.77 |
| Llama-3.2-3B-Instruct | A1 | thing | 40 | 39 | +0.653 | 1.00 | 0.49 | 6.33 |
| Llama-3.2-3B-Instruct | A1 | person | 58 | 58 | +1.091 | 1.00 | 0.69 | 8.06 |
| Llama-3.2-3B-Instruct | B | moral | 80 | 69 | +0.766 | 0.86 | 0.57 | 4.36 |
| Llama-3.2-3B-Instruct | B | norm | 107 | 103 | +0.751 | 0.96 | 0.57 | 5.41 |
| Llama-3.2-3B-Instruct | B | thing | 40 | 39 | +0.669 | 1.00 | 0.45 | 5.12 |
| Llama-3.2-3B-Instruct | B | person | 58 | 58 | +0.976 | 1.00 | 0.58 | 5.48 |
| Llama-3.2-3B-Instruct | A0 | moral | 80 | 77 | +0.407 | 0.97 | 0.32 | 7.05 |
| Llama-3.2-3B-Instruct | A0 | norm | 107 | 95 | +0.167 | 0.93 | 0.20 | 6.88 |
| Llama-3.2-3B-Instruct | A0 | thing | 40 | 30 | +0.047 | 0.95 | 0.08 | 5.28 |
| Qwen2.5-14B | A1 | moral | 80 | 79 | +1.353 | 0.99 | 0.81 | 14.11 |
| Qwen2.5-14B | A1 | norm | 107 | 99 | +0.745 | 0.96 | 0.51 | 11.55 |
| Qwen2.5-14B | A1 | thing | 40 | 36 | +0.166 | 1.00 | 0.13 | 8.02 |
| Qwen2.5-14B | A1 | person | 58 | 57 | +0.533 | 0.98 | 0.36 | 8.87 |
| Qwen2.5-14B | B | moral | 80 | 79 | +1.270 | 0.99 | 0.77 | 6.82 |
| Qwen2.5-14B | B | norm | 107 | 106 | +1.059 | 0.99 | 0.69 | 7.46 |
| Qwen2.5-14B | B | thing | 40 | 40 | +1.078 | 1.00 | 0.64 | 5.69 |
| Qwen2.5-14B | B | person | 58 | 58 | +1.282 | 1.00 | 0.72 | 5.94 |
| Qwen2.5-14B | A0 | moral | 80 | 80 | +0.749 | 1.00 | 0.70 | 8.69 |
| Qwen2.5-14B | A0 | norm | 107 | 101 | +0.368 | 0.97 | 0.61 | 7.19 |
| Qwen2.5-14B | A0 | thing | 40 | 32 | +0.097 | 0.95 | 0.15 | 6.61 |
| Qwen2.5-14B-Instruct | A1 | moral | 80 | 79 | +1.488 | 1.00 | 0.84 | 10.51 |
| Qwen2.5-14B-Instruct | A1 | norm | 107 | 99 | +0.779 | 0.97 | 0.46 | 10.17 |
| Qwen2.5-14B-Instruct | A1 | thing | 40 | 18* | +0.120 | 0.97 | 0.07 | 6.65 |
| Qwen2.5-14B-Instruct | A1 | person | 58 | 54 | +0.603 | 0.98 | 0.36 | 8.11 |
| Qwen2.5-14B-Instruct | B | moral | 80 | 78 | +1.314 | 0.97 | 0.72 | 5.62 |
| Qwen2.5-14B-Instruct | B | norm | 107 | 104 | +1.035 | 0.98 | 0.61 | 6.44 |
| Qwen2.5-14B-Instruct | B | thing | 40 | 40 | +1.187 | 1.00 | 0.62 | 4.51 |
| Qwen2.5-14B-Instruct | B | person | 58 | 58 | +1.262 | 1.00 | 0.66 | 5.78 |
| Qwen2.5-14B-Instruct | A0 | moral | 80 | 80 | +0.777 | 1.00 | 0.77 | 8.06 |
| Qwen2.5-14B-Instruct | A0 | norm | 107 | 95 | +0.467 | 0.92 | 0.69 | 6.48 |
| Qwen2.5-14B-Instruct | A0 | thing | 40 | 32 | +0.123 | 0.93 | 0.15 | 5.89 |
| Qwen2.5-3B | A1 | moral | 80 | 78 | +0.465 | 0.97 | 0.75 | 3.90 |
| Qwen2.5-3B | A1 | norm | 107 | 98 | +0.259 | 0.94 | 0.65 | 3.55 |
| Qwen2.5-3B | A1 | thing | 40 | 39 | +0.293 | 1.00 | 0.52 | 3.08 |
| Qwen2.5-3B | A1 | person | 58 | 57 | +0.471 | 1.00 | 0.64 | 3.22 |
| Qwen2.5-3B | B | moral | 80 | 75 | +0.498 | 0.95 | 0.63 | 3.37 |
| Qwen2.5-3B | B | norm | 107 | 101 | +0.389 | 0.95 | 0.51 | 4.03 |
| Qwen2.5-3B | B | thing | 40 | 40 | +0.434 | 1.00 | 0.51 | 3.33 |
| Qwen2.5-3B | B | person | 58 | 57 | +0.666 | 0.98 | 0.59 | 3.87 |
| Qwen2.5-3B | A0 | moral | 80 | 57 | +0.284 | 0.71 | 0.55 | 4.19 |
| Qwen2.5-3B | A0 | norm | 107 | 80 | +0.202 | 0.77 | 0.50 | 3.64 |
| Qwen2.5-3B | A0 | thing | 40 | 3* | +0.001 | 0.55 | 0.07 | 3.29 |
| Qwen2.5-3B-Instruct | A1 | moral | 80 | 76 | +1.011 | 0.97 | 0.79 | 7.34 |
| Qwen2.5-3B-Instruct | A1 | norm | 107 | 103 | +0.892 | 0.96 | 0.69 | 6.68 |
| Qwen2.5-3B-Instruct | A1 | thing | 40 | 40 | +0.683 | 1.00 | 0.47 | 7.23 |
| Qwen2.5-3B-Instruct | A1 | person | 58 | 57 | +1.118 | 1.00 | 0.64 | 7.08 |
| Qwen2.5-3B-Instruct | B | moral | 80 | 76 | +1.015 | 0.96 | 0.70 | 6.42 |
| Qwen2.5-3B-Instruct | B | norm | 107 | 104 | +0.851 | 0.98 | 0.58 | 6.22 |
| Qwen2.5-3B-Instruct | B | thing | 40 | 40 | +0.869 | 1.00 | 0.54 | 6.01 |
| Qwen2.5-3B-Instruct | B | person | 58 | 57 | +1.393 | 1.00 | 0.74 | 6.23 |
| Qwen2.5-3B-Instruct | A0 | moral | 80 | 77 | +0.614 | 0.97 | 0.71 | 5.15 |
| Qwen2.5-3B-Instruct | A0 | norm | 107 | 101 | +0.350 | 0.96 | 0.57 | 4.58 |
| Qwen2.5-3B-Instruct | A0 | thing | 40 | 36 | +0.110 | 0.97 | 0.18 | 4.26 |
| Qwen2.5-7B | A1 | moral | 80 | 79 | +1.121 | 0.99 | 0.80 | 6.44 |
| Qwen2.5-7B | A1 | norm | 107 | 104 | +0.858 | 0.98 | 0.67 | 7.09 |
| Qwen2.5-7B | A1 | thing | 40 | 40 | +0.531 | 1.00 | 0.47 | 4.90 |
| Qwen2.5-7B | A1 | person | 58 | 58 | +0.904 | 1.00 | 0.62 | 6.12 |
| Qwen2.5-7B | B | moral | 80 | 77 | +1.055 | 0.96 | 0.78 | 5.31 |
| Qwen2.5-7B | B | norm | 107 | 107 | +1.044 | 1.00 | 0.75 | 7.56 |
| Qwen2.5-7B | B | thing | 40 | 40 | +1.077 | 1.00 | 0.72 | 5.53 |
| Qwen2.5-7B | B | person | 58 | 58 | +1.468 | 1.00 | 0.84 | 7.55 |
| Qwen2.5-7B | A0 | moral | 80 | 78 | +0.630 | 0.99 | 0.62 | 5.42 |
| Qwen2.5-7B | A0 | norm | 107 | 99 | +0.317 | 0.94 | 0.48 | 5.89 |
| Qwen2.5-7B | A0 | thing | 40 | 28 | +0.078 | 0.90 | 0.13 | 4.32 |
| Qwen2.5-7B-Instruct | A1 | moral | 80 | 75 | +1.163 | 0.95 | 0.79 | 5.12 |
| Qwen2.5-7B-Instruct | A1 | norm | 107 | 106 | +0.957 | 0.99 | 0.70 | 5.89 |
| Qwen2.5-7B-Instruct | A1 | thing | 40 | 40 | +0.715 | 1.00 | 0.46 | 3.72 |
| Qwen2.5-7B-Instruct | A1 | person | 58 | 57 | +1.095 | 0.98 | 0.70 | 4.26 |
| Qwen2.5-7B-Instruct | B | moral | 80 | 77 | +1.240 | 0.96 | 0.80 | 4.36 |
| Qwen2.5-7B-Instruct | B | norm | 107 | 104 | +1.160 | 0.97 | 0.75 | 5.03 |
| Qwen2.5-7B-Instruct | B | thing | 40 | 40 | +1.211 | 1.00 | 0.67 | 3.56 |
| Qwen2.5-7B-Instruct | B | person | 58 | 57 | +1.538 | 1.00 | 0.86 | 5.80 |
| Qwen2.5-7B-Instruct | A0 | moral | 80 | 77 | +0.629 | 0.96 | 0.62 | 5.08 |
| Qwen2.5-7B-Instruct | A0 | norm | 107 | 92 | +0.302 | 0.86 | 0.51 | 4.58 |
| Qwen2.5-7B-Instruct | A0 | thing | 40 | 28 | +0.132 | 0.90 | 0.14 | 4.00 |
| gemma-2b | A1 | moral | 80 | 74 | +0.602 | 0.96 | 0.52 | 2.75 |
| gemma-2b | A1 | norm | 107 | 99 | +0.453 | 0.95 | 0.47 | 2.97 |
| gemma-2b | A1 | thing | 40 | 39 | +0.420 | 0.97 | 0.41 | 2.54 |
| gemma-2b | A1 | person | 58 | 58 | +0.737 | 1.00 | 0.51 | 2.30 |
| gemma-2b | B | moral | 80 | 72 | +0.488 | 0.93 | 0.46 | 2.77 |
| gemma-2b | B | norm | 107 | 95 | +0.423 | 0.93 | 0.45 | 3.05 |
| gemma-2b | B | thing | 40 | 40 | +0.483 | 1.00 | 0.50 | 2.40 |
| gemma-2b | B | person | 58 | 57 | +0.662 | 0.98 | 0.46 | 2.50 |
| gemma-2b | A0 | moral | 80 | 75 | +0.409 | 0.94 | 0.59 | 3.02 |
| gemma-2b | A0 | norm | 107 | 93 | +0.262 | 0.89 | 0.43 | 2.99 |
| gemma-2b | A0 | thing | 40 | 34 | +0.095 | 0.95 | 0.14 | 2.83 |
| gemma-2b-it | A1 | moral | 80 | 73 | +1.007 | 0.94 | 0.92 | 2.26 |
| gemma-2b-it | A1 | norm | 107 | 98 | +0.758 | 0.93 | 0.84 | 2.14 |
| gemma-2b-it | A1 | thing | 40 | 37 | +0.680 | 0.93 | 0.66 | 1.83 |
| gemma-2b-it | A1 | person | 58 | 58 | +1.277 | 1.00 | 0.92 | 1.69 |
| gemma-2b-it | B | moral | 80 | 67 | +0.556 | 0.84 | 0.50 | 2.33 |
| gemma-2b-it | B | norm | 107 | 88 | +0.335 | 0.84 | 0.39 | 2.36 |
| gemma-2b-it | B | thing | 40 | 34 | +0.465 | 0.85 | 0.45 | 2.21 |
| gemma-2b-it | B | person | 58 | 57 | +0.617 | 0.98 | 0.39 | 2.34 |
| gemma-2b-it | A0 | moral | 80 | 73 | +0.464 | 0.94 | 0.60 | 2.38 |
| gemma-2b-it | A0 | norm | 107 | 92 | +0.367 | 0.90 | 0.43 | 2.33 |
| gemma-2b-it | A0 | thing | 40 | 21 | +0.096 | 0.85 | 0.13 | 2.11 |

\* fewer included pairs than the minimum; shown, not pooled.
