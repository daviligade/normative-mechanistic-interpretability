# The located heads' share by kind of pair, frames QA

Pairs: moral 80, norm 107, thing 40. No control pairs in this run (--no-controls). Runs: runs/heads_qa. Head set located, condition p2r_all, effects read on S, a pair is included when its gap in S is at least 0.02, 10000 bootstrap resamples.

Check against results/heads__qa: the study's contrasts recomputed here are the same (40 per-model and 3 pooled ratios; largest difference 0.0e+00).

## Pooled ratios of the located heads' share (geometric mean over models; 95 % interval from the item bootstrap)

| frame | contrast | models | ratio | 95 % interval | within template types | models with interval above 1 / below 1 | left out |
|---|---|---|---|---|---|---|---|
| QA | norm/thing | 13 | 1.24 | [1.14, 1.34] |  | 8 / 0 | Qwen2.5-3B-Instruct |
| QA | moral/thing | 13 | 1.08 | [0.99, 1.17] |  | 5 / 1 | Qwen2.5-3B-Instruct |
| QA | moral/norm | 14 | 0.89 | [0.82, 0.98] |  | 3 / 6 | - |

## The share as a multiple of the share of ten heads chosen at random (geometric mean over models)

| frame | models | moral | norm | person | thing |
|---|---|---|---|---|---|
| QA | 13 (all groups) | 4.35 | 5.00 | n/a | 4.04 |

## Behaviour

| model | frame | group | run | included | mean gap | better version preferred | mean mass | multiple of random |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | QA | moral | 80 | 79 | +0.507 | 1.00 | 0.54 | 8.45 |
| Llama-3.1-8B | QA | norm | 107 | 106 | +0.468 | 0.99 | 0.58 | 9.79 |
| Llama-3.1-8B | QA | thing | 40 | 40 | +0.370 | 1.00 | 0.61 | 7.25 |
| Llama-3.1-8B-Instruct | QA | moral | 80 | 79 | +1.043 | 1.00 | 0.71 | 9.29 |
| Llama-3.1-8B-Instruct | QA | norm | 107 | 106 | +1.019 | 0.99 | 0.67 | 11.73 |
| Llama-3.1-8B-Instruct | QA | thing | 40 | 40 | +1.155 | 1.00 | 0.72 | 9.94 |
| Llama-3.2-1B | QA | moral | 80 | 72 | +0.182 | 0.95 | 0.65 | 3.39 |
| Llama-3.2-1B | QA | norm | 107 | 89 | +0.120 | 0.91 | 0.64 | 3.59 |
| Llama-3.2-1B | QA | thing | 40 | 37 | +0.174 | 0.97 | 0.61 | 3.40 |
| Llama-3.2-1B-Instruct | QA | moral | 80 | 75 | +0.269 | 0.96 | 0.53 | 2.29 |
| Llama-3.2-1B-Instruct | QA | norm | 107 | 91 | +0.199 | 0.86 | 0.56 | 1.90 |
| Llama-3.2-1B-Instruct | QA | thing | 40 | 37 | +0.333 | 0.93 | 0.62 | 1.45 |
| Llama-3.2-3B | QA | moral | 80 | 79 | +0.334 | 0.99 | 0.50 | 5.33 |
| Llama-3.2-3B | QA | norm | 107 | 101 | +0.230 | 0.95 | 0.48 | 5.65 |
| Llama-3.2-3B | QA | thing | 40 | 38 | +0.216 | 0.95 | 0.49 | 4.48 |
| Llama-3.2-3B-Instruct | QA | moral | 80 | 75 | +1.061 | 0.95 | 0.72 | 4.05 |
| Llama-3.2-3B-Instruct | QA | norm | 107 | 104 | +1.057 | 0.97 | 0.67 | 6.96 |
| Llama-3.2-3B-Instruct | QA | thing | 40 | 40 | +1.096 | 1.00 | 0.68 | 5.09 |
| Qwen2.5-14B | QA | moral | 80 | 80 | +0.779 | 1.00 | 0.44 | 7.24 |
| Qwen2.5-14B | QA | norm | 107 | 107 | +0.621 | 1.00 | 0.38 | 8.10 |
| Qwen2.5-14B | QA | thing | 40 | 39 | +0.317 | 1.00 | 0.20 | 7.59 |
| Qwen2.5-14B-Instruct | QA | moral | 80 | 75 | +0.839 | 0.99 | 0.43 | 9.97 |
| Qwen2.5-14B-Instruct | QA | norm | 107 | 95 | +0.565 | 1.00 | 0.30 | 7.88 |
| Qwen2.5-14B-Instruct | QA | thing | 40 | 23 | +0.189 | 1.00 | 0.09 | 7.17 |
| Qwen2.5-3B | QA | moral | 80 | 74 | +0.665 | 0.96 | 0.53 | 3.29 |
| Qwen2.5-3B | QA | norm | 107 | 104 | +0.570 | 0.97 | 0.44 | 3.91 |
| Qwen2.5-3B | QA | thing | 40 | 40 | +0.578 | 1.00 | 0.42 | 3.21 |
| Qwen2.5-3B-Instruct | QA | moral | 80 | 70 | +0.159 | 0.97 | 0.09 | 7.53 |
| Qwen2.5-3B-Instruct | QA | norm | 107 | 68 | +0.088 | 0.93 | 0.05 | 5.91 |
| Qwen2.5-3B-Instruct | QA | thing | 40 | 8* | +0.007 | 0.57 | 0.01 | 8.26 |
| Qwen2.5-7B | QA | moral | 80 | 80 | +0.432 | 1.00 | 0.30 | 3.74 |
| Qwen2.5-7B | QA | norm | 107 | 105 | +0.453 | 0.99 | 0.34 | 5.51 |
| Qwen2.5-7B | QA | thing | 40 | 40 | +0.574 | 1.00 | 0.40 | 3.63 |
| Qwen2.5-7B-Instruct | QA | moral | 80 | 70 | +0.465 | 0.97 | 0.25 | 2.88 |
| Qwen2.5-7B-Instruct | QA | norm | 107 | 80 | +0.266 | 0.96 | 0.15 | 5.45 |
| Qwen2.5-7B-Instruct | QA | thing | 40 | 28 | +0.237 | 1.00 | 0.12 | 2.82 |
| gemma-2b | QA | moral | 80 | 73 | +0.187 | 0.93 | 0.35 | 2.96 |
| gemma-2b | QA | norm | 107 | 92 | +0.108 | 0.96 | 0.33 | 2.85 |
| gemma-2b | QA | thing | 40 | 38 | +0.182 | 0.95 | 0.38 | 2.59 |
| gemma-2b-it | QA | moral | 80 | 70 | +0.647 | 0.91 | 0.54 | 2.01 |
| gemma-2b-it | QA | norm | 107 | 93 | +0.549 | 0.93 | 0.37 | 1.84 |
| gemma-2b-it | QA | thing | 40 | 35 | +0.653 | 0.97 | 0.37 | 2.04 |

\* fewer included pairs than the minimum; shown, not pooled.
