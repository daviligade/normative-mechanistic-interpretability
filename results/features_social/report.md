# A non-moral cue that suits one kind of norm: "is socially" (A1s) and the etiquette pairs, next to "is morally" (A1), no cue (B) and "is logically" (A1l)

Exploratory. Items: the item file is the set of accepted pairs; 227 items.

## Check of the manipulation and strength of the fit (per model; behavioural gap ratios)

* 'socially' suits the etiquette pairs (etiquette fit ratio higher in A1s than in B): 7 of 7 models -> passed
* reference, 'morally' suits the moral pairs (moral fit ratio higher in A1 than in B): 7 of 7 models
* 'socially' also suits the moral pairs (moral fit ratio higher in A1s than in B): 6 of 7 models
* strength: median etiquette gain (A1s over B) 2.24, median moral gain (A1 over B) 1.19 -> comparable (gain E - 1 at least half of gain M - 1)

| model | etiquette fit ratio B / A1 / A1s | moral fit ratio B / A1 / A1s | answer-word mass, etiquette pairs, B / A1 / A1s |
|---|---|---|---|
| meta-llama/Llama-3.1-8B | 1.05 / 0.95 / 1.73 | 1.02 / 1.75 / 1.44 | 0.55 / 0.35 / 0.77 |
| meta-llama/Llama-3.2-1B-Instruct | 0.64 / 0.80 / 1.03 | 1.51 / 1.67 / 1.59 | 0.54 / 0.64 / 0.79 |
| meta-llama/Llama-3.2-1B | 0.37 / 0.37 / 0.82 | 1.29 / 1.42 / 1.18 | 0.51 / 0.65 / 0.80 |
| meta-llama/Llama-3.2-3B-Instruct | 0.92 / 0.92 / 1.45 | 1.02 / 1.22 / 1.40 | 0.56 / 0.73 / 0.79 |
| meta-llama/Llama-3.2-3B | 0.72 / 0.81 / 1.64 | 1.11 / 1.33 / 1.74 | 0.57 / 0.63 / 0.80 |
| Qwen/Qwen2.5-7B-Instruct | 0.92 / 0.93 / 2.16 | 1.07 / 1.21 / 1.41 | 0.73 / 0.79 / 0.77 |
| Qwen/Qwen2.5-7B | 0.77 / 0.96 / 2.28 | 1.01 / 1.31 / 1.62 | 0.73 / 0.79 / 0.81 |

## Readings

* Fit test (targets against the mix of prudential, aesthetic and epistemic pairs; A1, B, A1s, A1l): etiquette stands apart in 0 / 0 / 5 / 0 of 14 conditions, moral in 3 / 0 / 0 / 0 -> **not informative: in this comparison the moral pairs do not stand apart much more with 'morally' than without a cue**
* Margin (12 informative conditions): dE > 0 in 9, median dE 0.75, median dM 0.40 -> fit (secondary)
* H6 (moral vs norm yields more features than every split of the norm kinds): A1 12 of 14, B 3 of 14, A1s 2 of 14 (descriptive)
* located moral-versus-neutral sets, moral pairs, A1s/A1, layer 7 or deeper (10 conditions): 5 a non-moral adverb turns it on too; 4 not turned on by a non-moral adverb; 1 inconclusive
* located moral-versus-neutral sets, moral pairs, A1s/A1, layer 0 to 3 (4 conditions): 0 a non-moral adverb turns it on too; 4 not turned on by a non-moral adverb; 0 inconclusive

## The located sets per condition

| condition | layer | vs-neutral set, moral pairs: A1s/A1 [95 % CI] | B/A1 | A1s descr/moral [CI] | vs-norm set: A1s descr/moral [CI] |
|---|---|---|---|---|---|
| llama-3.1-8B-base | L12 | 0.54 [0.53, 0.55] | 0.11 | 0.84 [0.82, 0.87] | 0.55 [0.37, 0.76] |
| llama-3.2-1B-IT | L7 | 0.33 [0.32, 0.34] | 0.09 | 0.82 [0.79, 0.85] | 0.33 [0.25, 0.41] |
| llama-3.2-1B-IT-k128 | L7 | 0.36 [0.35, 0.37] | 0.14 | 0.87 [0.84, 0.90] | 0.16 [0.08, 0.26] |
| llama-3.2-1B-base | L7 | 0.51 [0.50, 0.52] | 0.23 | 0.81 [0.79, 0.84] | 0.25 [0.18, 0.33] |
| llama-3.2-1B-base-MLP0 | MLP0 | 0.20 [0.20, 0.21] | 0.01 | 0.99 [0.97, 1.01] | 0.85 [0.77, 0.94] |
| llama-3.2-1B-base-k128 | L7 | 0.50 [0.49, 0.50] | 0.17 | 0.85 [0.83, 0.88] | 0.31 [0.21, 0.44] |
| llama-3.2-3B-IT-L19 | L19 | 0.48 [0.47, 0.48] | 0.33 | 0.76 [0.73, 0.79] | 0.61 [0.56, 0.67] |
| llama-3.2-3B-IT-L3 | L3 | 0.37 [0.37, 0.38] | 0.12 | 0.88 [0.86, 0.91] | 0.64 [0.39, 0.98] |
| llama-3.2-3B-IT-L7 | L7 | 0.46 [0.46, 0.47] | 0.03 | 0.83 [0.80, 0.85] | 0.33 [0.26, 0.40] |
| llama-3.2-3B-IT-k128 | L11 | 0.53 [0.53, 0.54] | 0.19 | 0.77 [0.74, 0.81] | 0.36 [0.32, 0.40] |
| llama-3.2-3B-base | L11 | 0.54 [0.53, 0.55] | 0.15 | 0.77 [0.74, 0.80] | 0.10 [0.06, 0.16] |
| llama-3.2-3B-base-k128 | L11 | 0.54 [0.53, 0.55] | 0.18 | 0.77 [0.74, 0.80] | 0.38 [0.32, 0.43] |
| qwen-2.5-7b-IT | L0 | 0.23 [0.23, 0.24] | 0.06 | 0.96 [0.95, 0.98] | 0.36 [0.20, 0.58] |
| qwen-2.5-7b-base | L0 | 0.18 [0.18, 0.18] | 0.04 | 0.91 [0.90, 0.93] | 0.45 [0.39, 0.52] |

## Fit test and H6 per condition (mean counts over 20 subsamples)

| condition | A1: etiquette, moral; largest calibration | B: etiquette, moral; largest calibration | A1s: etiquette, moral; largest calibration | A1l: etiquette, moral; largest calibration | H6 A1s: moral vs norm; best split |
|---|---|---|---|---|---|
| llama-3.1-8B-base | 0.3, 1.1; 9.8 | 2.0, 1.4; 6.8 | 4.4, 1.5; 4.5 | 0.2, 0.1; 15.8 | 2.8; 11.7 |
| llama-3.2-1B-IT | 1.6, 4.5; 2.8 | 1.5, 2.0; 5.0 | 1.5, 1.8; 3.8 | 0.5, 0.6; 8.0 | 3.9; 8.6 |
| llama-3.2-1B-IT-k128 | 0.1, 7.7; 5.8 | 1.8, 4.1; 10.2 | 4.8, 2.5; 12.1 | 0.2, 0.2; 8.8 | 11.1; 16.6 |
| llama-3.2-1B-base | 0.6, 3.0; 3.9 | 0.1, 0.5; 6.0 | 2.5, 1.2; 7.9 | 0.0, 0.2; 17.0 | 8.8; 10.9 |
| llama-3.2-1B-base-MLP0 | 0.0, 0.1; 2.1 | 0.1, 0.0; 0.8 | 0.8, 0.1; 0.2 | 0.0, 0.7; 1.7 | 0.1; 1.6 |
| llama-3.2-1B-base-k128 | 0.1, 3.6; 12.9 | 3.7, 1.8; 11.4 | 4.8, 2.3; 15.8 | 0.9, 0.4; 29.6 | 11.8; 13.8 |
| llama-3.2-3B-IT-L19 | 1.5, 11.3; 18.9 | 20.6, 12.6; 31.2 | 14.8, 8.7; 11.2 | 1.9, 1.2; 44.8 | 41.3; 49.6 |
| llama-3.2-3B-IT-L3 | 0.1, 0.1; 4.5 | 0.4, 0.5; 3.4 | 0.7, 0.1; 4.8 | 0.1, 0.5; 9.8 | 2.8; 1.7 |
| llama-3.2-3B-IT-L7 | 0.1, 2.5; 19.5 | 4.0, 1.5; 6.5 | 6.8, 1.9; 16.6 | 0.9, 0.8; 30.4 | 11.0; 25.9 |
| llama-3.2-3B-IT-k128 | 1.0, 16.4; 14.9 | 3.5, 4.0; 12.6 | 13.2, 5.8; 7.1 | 0.7, 0.8; 30.6 | 35.4; 31.2 |
| llama-3.2-3B-base | 1.6, 6.2; 7.9 | 1.6, 1.6; 5.8 | 11.8, 1.3; 5.5 | 0.9, 1.9; 27.3 | 7.3; 22.2 |
| llama-3.2-3B-base-k128 | 1.4, 10.4; 26.6 | 2.8, 2.9; 12.8 | 18.6, 3.0; 8.7 | 3.0, 1.1; 49.1 | 15.2; 39.7 |
| qwen-2.5-7b-IT | 0.1, 0.2; 0.3 | 0.0, 0.0; 0.1 | 0.1, 0.1; 1.9 | 0.1, 0.1; 1.5 | 0.5; 2.1 |
| qwen-2.5-7b-base | 0.0, 0.1; 0.9 | 0.0, 0.1; 0.3 | 0.1, 0.1; 0.6 | 0.0, 0.0; 0.7 | 0.3; 0.3 |
