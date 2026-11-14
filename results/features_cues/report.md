# Cue frames for the features: "is logically" (A1l) and "Morally speaking, ... is" (A1p), next to "is morally" (A1), no cue (B) and "is ethically" (A1e)

Exploratory. Items: the item file is the set of accepted pairs; 227 items.

## Checks of the manipulation (per model; behavioural gap ratios)

* 'logically' fits the epistemic pairs (epistemic fit ratio higher in A1l than in B): 0 of 7 models -> FAILED
* 'Morally speaking' works as a moral question (moral fit ratio higher in A1p than in B): 5 of 7 models -> passed
* reference, 'morally' (moral fit ratio higher in A1 than in B): 7 of 7 models

| model | moral fit ratio B / A1 / A1p / A1l | epistemic fit ratio B / A1 / A1l | answer-word mass, moral pairs, B / A1 / A1p / A1l |
|---|---|---|---|
| meta-llama/Llama-3.1-8B | 1.02 / 1.75 / 1.33 / 0.94 | 0.93 / 1.45 / 0.89 | 0.46 / 0.50 / 0.48 / 0.33 |
| meta-llama/Llama-3.2-1B-Instruct | 1.51 / 1.67 / 1.42 / 1.15 | 1.09 / 0.74 / 1.01 | 0.60 / 0.67 / 0.67 / 0.55 |
| meta-llama/Llama-3.2-1B | 1.29 / 1.42 / 1.19 / 1.12 | 1.39 / 0.98 / 0.78 | 0.56 / 0.69 / 0.71 / 0.51 |
| meta-llama/Llama-3.2-3B-Instruct | 1.02 / 1.22 / 1.33 / 1.14 | 1.18 / 0.94 / 0.83 | 0.57 / 0.75 / 0.65 / 0.53 |
| meta-llama/Llama-3.2-3B | 1.11 / 1.33 / 1.35 / 0.93 | 1.22 / 1.16 / 0.70 | 0.44 / 0.63 / 0.60 / 0.44 |
| Qwen/Qwen2.5-7B-Instruct | 1.07 / 1.21 / 1.40 / 1.13 | 0.89 / 0.66 / 0.50 | 0.80 / 0.79 / 0.80 / 0.51 |
| Qwen/Qwen2.5-7B | 1.01 / 1.31 / 1.33 / 0.98 | 0.87 / 0.88 / 0.75 | 0.78 / 0.80 / 0.74 / 0.47 |

## Readings

* Fit test (moral and epistemic pairs against the other norms, A1 / B / A1l): moral stands apart in 11 / 3 / 4 of 14 conditions, epistemic in 13 / 11 / 12 -> **not read: 'logically' did not fit the epistemic pairs better than the other kinds (check of the manipulation failed)**
* H6 (moral vs norm yields more features than every split of the norm kinds): A1 12 of 14, B 3 of 14, A1l 0 of 14, A1p 9 of 14 -> A1p: **the separation follows the moral question in context**
* located moral-versus-neutral sets, moral pairs, A1e/A1, layer 7 or deeper (10 conditions): 10 moral cue in either wording; 0 the word 'morally'; 0 inconclusive
* located moral-versus-neutral sets, moral pairs, A1e/A1, layer 0 to 3 (4 conditions): 1 moral cue in either wording; 3 the word 'morally'; 0 inconclusive
* located moral-versus-neutral sets, moral pairs, A1l/A1, layer 7 or deeper (10 conditions): 0 a non-moral adverb turns it on too; 10 not turned on by a non-moral adverb; 0 inconclusive
* located moral-versus-neutral sets, moral pairs, A1l/A1, layer 0 to 3 (4 conditions): 0 a non-moral adverb turns it on too; 4 not turned on by a non-moral adverb; 0 inconclusive
* located moral-versus-neutral sets, moral pairs, A1p/A1, layer 7 or deeper (10 conditions): 0 the moral question in context; 9 tied to the word at the final position; 1 inconclusive
* located moral-versus-neutral sets, moral pairs, A1p/A1, layer 0 to 3 (4 conditions): 0 the moral question in context; 4 tied to the word at the final position; 0 inconclusive

## The located moral-versus-neutral sets per condition (moral pairs)

| condition | layer | A1e/A1 [95 % CI] | A1l/A1 [95 % CI] | A1p/A1 [95 % CI] | B/A1 | descr in A1l / A1p (over moral) |
|---|---|---|---|---|---|---|
| llama-3.1-8B-base | L12 | 0.75 [0.74, 0.76] | 0.18 [0.16, 0.19] | 0.17 [0.17, 0.18] | 0.11 | 0.61 / 0.30 |
| llama-3.2-1B-IT | L7 | 0.64 [0.63, 0.65] | 0.33 [0.32, 0.33] | 0.13 [0.12, 0.14] | 0.09 | 0.75 / 0.21 |
| llama-3.2-1B-IT-k128 | L7 | 0.69 [0.68, 0.70] | 0.28 [0.28, 0.29] | 0.16 [0.15, 0.17] | 0.14 | 0.88 / 0.37 |
| llama-3.2-1B-base | L7 | 0.75 [0.74, 0.76] | 0.28 [0.27, 0.28] | 0.25 [0.24, 0.26] | 0.23 | 0.75 / 0.23 |
| llama-3.2-1B-base-MLP0 | MLP0 | 0.09 [0.09, 0.09] | 0.19 [0.18, 0.19] | 0.01 [0.01, 0.01] | 0.01 | 1.01 / 0.98 |
| llama-3.2-1B-base-k128 | L7 | 0.79 [0.78, 0.80] | 0.29 [0.29, 0.30] | 0.18 [0.17, 0.19] | 0.17 | 0.79 / 0.53 |
| llama-3.2-3B-IT-L19 | L19 | 0.80 [0.79, 0.81] | 0.44 [0.43, 0.45] | 0.49 [0.48, 0.50] | 0.33 | 0.60 / 0.66 |
| llama-3.2-3B-IT-L3 | L3 | 0.77 [0.77, 0.78] | 0.31 [0.30, 0.31] | 0.16 [0.15, 0.16] | 0.12 | 0.81 / 0.51 |
| llama-3.2-3B-IT-L7 | L7 | 0.90 [0.89, 0.92] | 0.29 [0.29, 0.30] | 0.10 [0.09, 0.10] | 0.03 | 0.74 / 0.36 |
| llama-3.2-3B-IT-k128 | L11 | 0.86 [0.85, 0.87] | 0.47 [0.46, 0.48] | 0.20 [0.19, 0.21] | 0.19 | 0.79 / 0.67 |
| llama-3.2-3B-base | L11 | 0.84 [0.82, 0.85] | 0.42 [0.41, 0.43] | 0.19 [0.18, 0.19] | 0.15 | 0.75 / 0.22 |
| llama-3.2-3B-base-k128 | L11 | 0.86 [0.85, 0.87] | 0.36 [0.35, 0.37] | 0.21 [0.20, 0.22] | 0.18 | 0.69 / 0.39 |
| qwen-2.5-7b-IT | L0 | 0.11 [0.11, 0.12] | 0.16 [0.16, 0.16] | 0.06 [0.06, 0.06] | 0.06 | 0.99 / 1.00 |
| qwen-2.5-7b-base | L0 | 0.08 [0.08, 0.08] | 0.20 [0.19, 0.20] | 0.04 [0.04, 0.04] | 0.04 | 0.95 / 1.01 |

## H6 and the fit test per condition

| condition | H6 moral vs norm; best split: A1 / B / A1l / A1p | fit test A1: moral, epistemic; best calibration | B | A1l |
|---|---|---|---|---|
| llama-3.1-8B-base | 7.3; 6.5 / 10.7; 18.1 / 1.9; 10.8 / 13.6; 15.1 | 1.7, 13.3; 0.2 | 0.8, 5.3; 2.1 | 0.1, 15.1; 0.7 |
| llama-3.2-1B-IT | 15.0; 0.7 / 14.3; 13.3 / 1.4; 7.0 / 23.4; 16.1 | 3.9, 1.4; 1.3 | 1.6, 3.8; 2.9 | 0.1, 10.6; 0.3 |
| llama-3.2-1B-IT-k128 | 30.9; 6.8 / 16.9; 20.0 / 2.3; 4.3 / 39.7; 27.2 | 9.2, 6.7; 1.2 | 3.6, 5.1; 4.1 | 0.3, 11.1; 0.2 |
| llama-3.2-1B-base | 14.3; 6.0 / 6.2; 9.7 / 5.0; 12.3 / 12.3; 8.2 | 2.3, 3.5; 0.6 | 0.7, 5.3; 1.1 | 0.2, 15.0; 0.7 |
| llama-3.2-1B-base-MLP0 | 0.2; 0.9 / 0.1; 0.8 / 0.3; 1.7 / 0.0; 0.1 | 0.1, 1.9; 0.1 | 0.0, 0.0; 0.6 | 0.1, 0.3; 0.1 |
| llama-3.2-1B-base-k128 | 23.4; 11.6 / 16.4; 18.6 / 3.8; 14.4 / 17.1; 17.5 | 4.5, 9.2; 0.2 | 1.4, 10.1; 3.1 | 0.3, 29.0; 0.6 |
| llama-3.2-3B-IT-L19 | 54.9; 39.2 / 77.4; 81.8 / 17.5; 40.8 / 72.0; 64.2 | 15.3, 9.7; 9.4 | 9.8, 13.3; 23.6 | 0.6, 45.9; 5.2 |
| llama-3.2-3B-IT-L3 | 0.9; 3.4 / 4.4; 3.4 / 0.6; 3.8 / 2.7; 3.2 | 1.2, 3.0; 0.8 | 0.4, 3.2; 0.5 | 0.2, 8.9; 0.1 |
| llama-3.2-3B-IT-L7 | 15.1; 13.3 / 19.8; 27.4 / 4.5; 12.3 / 31.3; 19.6 | 3.5, 18.4; 0.7 | 0.9, 10.6; 3.8 | 1.1, 29.6; 1.4 |
| llama-3.2-3B-IT-k128 | 59.5; 19.4 / 32.0; 49.1 / 5.6; 27.9 / 49.4; 28.9 | 12.8, 7.2; 8.2 | 5.8, 7.4; 5.7 | 0.8, 31.4; 1.6 |
| llama-3.2-3B-base | 21.9; 9.2 / 17.6; 17.7 / 4.8; 17.4 / 24.1; 8.4 | 4.3, 9.1; 1.0 | 1.1, 6.0; 0.8 | 2.3, 30.0; 0.7 |
| llama-3.2-3B-base-k128 | 52.4; 20.6 / 24.6; 34.0 / 5.7; 31.4 / 33.2; 31.7 | 10.4, 27.9; 1.2 | 3.5, 14.9; 3.1 | 1.9, 49.2; 1.4 |
| qwen-2.5-7b-IT | 0.3; 0.1 / 0.2; 0.1 / 0.1; 3.0 / 0.6; 0.2 | 0.0, 0.4; 0.1 | 0.0, 0.1; 0.1 | 0.0, 0.9; 1.4 |
| qwen-2.5-7b-base | 0.2; 0.1 / 0.1; 0.3 / 0.0; 0.5 / 0.2; 0.5 | 0.0, 1.1; 0.0 | 0.0, 0.1; 0.1 | 0.1, 0.1; 1.1 |
