# The located feature sets with "is ethically" (frame A1e), next to "is morally" (A1) and no cue (B)

Exploratory. Items: the item file is the set of accepted pairs; 227 items.

Primary (moral-versus-neutral sets, moral pairs, A1e over A1): at layer 7 or deeper 10 of 10 follow a moral cue in either wording, 0 follow the word 'morally', 0 inconclusive; at layer 0 to 3: 1 / 3 / 0 of 4.
H6 (moral vs norm yields more features than every split of the norm kinds): A1 12 of 14, A1e 7 of 14, B 3 of 14.

| condition | layer | moral: A1e/A1 [95 % CI] reading | norm: A1e/A1 | descr: A1e/A1 | moral: B/A1 | A1e descr/moral [CI] | H6 A1 / A1e / B (moral vs norm; best split) | answer-word mass A1 / A1e / B | capture R2 A1 / A1e |
|---|---|---|---|---|---|---|---|---|---|
| llama-3.1-8B-base | L12 | 0.75 [0.74, 0.76] moral cue in either wording | 0.75 | 0.74 | 0.11 | 0.85 [0.82, 0.88] | 7.3; 6.5 / 8.3; 2.0 / 10.7; 18.1 | 0.33 / 0.29 / 0.46 | -0.09 / -0.09 |
| llama-3.2-1B-IT | L7 | 0.64 [0.63, 0.65] moral cue in either wording | 0.61 | 0.56 | 0.09 | 0.70 [0.66, 0.74] | 15.0; 0.7 / 16.2; 2.8 / 14.3; 13.3 | 0.52 / 0.43 / 0.52 | -0.23 / -0.23 |
| llama-3.2-1B-IT-k128 | L7 | 0.69 [0.68, 0.70] moral cue in either wording | 0.71 | 0.68 | 0.14 | 0.76 [0.73, 0.80] | 30.9; 6.8 / 23.2; 7.3 / 16.9; 20.0 | 0.52 / 0.43 / 0.52 | -0.22 / -0.14 |
| llama-3.2-1B-base | L7 | 0.75 [0.74, 0.76] moral cue in either wording | 0.78 | 0.75 | 0.23 | 0.69 [0.66, 0.72] | 14.3; 6.0 / 11.2; 12.3 / 6.2; 9.7 | 0.58 / 0.40 / 0.52 | -0.23 / -0.29 |
| llama-3.2-1B-base-MLP0 | MLP0 | 0.09 [0.09, 0.09] the word 'morally' | 0.09 | 0.09 | 0.01 | 1.01 [1.00, 1.01] | 0.2; 0.9 / 0.1; 0.5 / 0.1; 0.8 | 0.58 / 0.40 / 0.52 | -1.66 / -4.53 |
| llama-3.2-1B-base-k128 | L7 | 0.79 [0.78, 0.80] moral cue in either wording | 0.81 | 0.80 | 0.17 | 0.74 [0.71, 0.77] | 23.4; 11.6 / 9.9; 10.2 / 16.4; 18.6 | 0.58 / 0.40 / 0.52 | -0.19 / -0.26 |
| llama-3.2-3B-IT-L19 | L19 | 0.80 [0.79, 0.81] moral cue in either wording | 0.80 | 0.85 | 0.33 | 0.98 [0.96, 1.01] | 54.9; 39.2 / 43.0; 20.4 / 77.4; 81.8 | 0.63 / 0.38 / 0.53 | 0.38 / 0.37 |
| llama-3.2-3B-IT-L3 | L3 | 0.77 [0.77, 0.78] moral cue in either wording | 0.78 | 0.82 | 0.12 | 0.91 [0.89, 0.92] | 0.9; 3.4 / 0.2; 4.8 / 4.4; 3.4 | 0.63 / 0.38 / 0.53 | -0.03 / -0.29 |
| llama-3.2-3B-IT-L7 | L7 | 0.90 [0.89, 0.91] moral cue in either wording | 0.92 | 0.98 | 0.03 | 0.83 [0.80, 0.86] | 15.1; 13.3 / 14.5; 15.3 / 19.8; 27.4 | 0.63 / 0.38 / 0.53 | -0.16 / -0.16 |
| llama-3.2-3B-IT-k128 | L11 | 0.86 [0.85, 0.87] moral cue in either wording | 0.87 | 0.94 | 0.19 | 0.89 [0.87, 0.91] | 59.5; 19.4 / 79.0; 13.1 / 32.0; 49.1 | 0.63 / 0.38 / 0.53 | -0.04 / 0.01 |
| llama-3.2-3B-base | L11 | 0.84 [0.82, 0.85] moral cue in either wording | 0.85 | 1.00 | 0.15 | 0.90 [0.86, 0.94] | 21.9; 9.2 / 18.9; 7.9 / 17.6; 17.7 | 0.52 / 0.35 / 0.48 | -0.12 / -0.08 |
| llama-3.2-3B-base-k128 | L11 | 0.86 [0.85, 0.87] moral cue in either wording | 0.85 | 0.96 | 0.18 | 0.82 [0.79, 0.85] | 52.4; 20.6 / 53.0; 10.8 / 24.6; 34.0 | 0.52 / 0.35 / 0.48 | -0.02 / -0.01 |
| qwen-2.5-7b-IT | L0 | 0.11 [0.11, 0.12] the word 'morally' | 0.12 | 0.12 | 0.06 | 1.00 [0.99, 1.02] | 0.3; 0.1 / 0.0; 2.1 / 0.2; 0.1 | 0.65 / 0.44 / 0.74 | -0.11 / 0.04 |
| qwen-2.5-7b-base | L0 | 0.08 [0.08, 0.08] the word 'morally' | 0.08 | 0.08 | 0.04 | 0.98 [0.97, 0.99] | 0.2; 0.1 / 0.0; 0.2 / 0.1; 0.3 | 0.65 / 0.50 / 0.75 | -0.06 / -0.03 |

Moral-versus-norm sets (located; secondary), moral pairs A1e/A1 and the A1e descr/moral ratio:

* llama-3.1-8B-base: moral A1e/A1 2.01 [1.76, 2.31] (moral cue in either wording); A1e descr/moral 0.58 [0.47, 0.70] (inconclusive); A1e norm/moral 0.69
* llama-3.2-1B-IT: moral A1e/A1 0.74 [0.70, 0.78] (moral cue in either wording); A1e descr/moral 0.26 [0.18, 0.36] (follows the content); A1e norm/moral 0.43
* llama-3.2-1B-IT-k128: moral A1e/A1 0.82 [0.75, 0.89] (moral cue in either wording); A1e descr/moral 0.26 [0.22, 0.32] (follows the content); A1e norm/moral 0.34
* llama-3.2-1B-base: moral A1e/A1 1.39 [1.27, 1.52] (moral cue in either wording); A1e descr/moral 0.16 [0.13, 0.21] (follows the content); A1e norm/moral 0.52
* llama-3.2-1B-base-MLP0: moral A1e/A1 0.46 [0.42, 0.51] (inconclusive); A1e descr/moral 1.07 [1.05, 1.09] (follows the frame); A1e norm/moral 1.07
* llama-3.2-1B-base-k128: moral A1e/A1 1.10 [1.03, 1.18] (moral cue in either wording); A1e descr/moral 0.32 [0.26, 0.38] (follows the content); A1e norm/moral 0.49
* llama-3.2-3B-IT-L19: moral A1e/A1 1.04 [1.02, 1.07] (moral cue in either wording); A1e descr/moral 0.97 [0.92, 1.02] (follows the frame); A1e norm/moral 0.92
* llama-3.2-3B-IT-L3: moral A1e/A1 1.01 [0.88, 1.16] (moral cue in either wording); A1e descr/moral 0.70 [0.57, 0.85] (follows the frame); A1e norm/moral 0.49
* llama-3.2-3B-IT-L7: moral A1e/A1 1.71 [1.60, 1.84] (moral cue in either wording); A1e descr/moral 0.32 [0.27, 0.37] (follows the content); A1e norm/moral 0.51
* llama-3.2-3B-IT-k128: moral A1e/A1 1.23 [1.19, 1.27] (moral cue in either wording); A1e descr/moral 0.35 [0.33, 0.38] (follows the content); A1e norm/moral 0.55
* llama-3.2-3B-base: moral A1e/A1 1.35 [1.28, 1.43] (moral cue in either wording); A1e descr/moral 0.26 [0.21, 0.31] (follows the content); A1e norm/moral 0.48
* llama-3.2-3B-base-k128: moral A1e/A1 1.36 [1.31, 1.43] (moral cue in either wording); A1e descr/moral 0.32 [0.28, 0.37] (follows the content); A1e norm/moral 0.47
* qwen-2.5-7b-IT: moral A1e/A1 0.35 [0.30, 0.41] (the word 'morally'); A1e descr/moral 0.91 [0.81, 1.02] (follows the frame); A1e norm/moral 0.85
* qwen-2.5-7b-base: moral A1e/A1 0.15 [0.12, 0.19] (the word 'morally'); A1e descr/moral 0.17 [0.06, 0.31] (follows the content); A1e norm/moral 0.32
