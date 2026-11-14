# Head results (p2r_all, readout S, head set located, items: accepted, inclusion gap >= 0.1)

**Sensitivity run (an option differs from the default): nothing here is a primary test; all intervals are 95 %.**

## Pooled ratios (mean over models of the log ratio; item bootstrap shared across models)

| frame | contrast | models used | left out | pooled ratio | interval | reading |
|---|---|---|---|---|---|---|
| A0 | moral/norm | 14 | - | 1.10 | 1.04 to 1.17 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25; it excludes 1, but the difference is within the margin) |
| A0 | moral/prudential | 10 | Llama-3.2-1B, Llama-3.2-1B-Instruct, Qwen2.5-3B, Qwen2.5-7B-Instruct | 1.18 | 1.04 to 1.36 (95.0 %) |  |
| A0 | moral/etiquette | 9 | Llama-3.2-1B, Llama-3.2-1B-Instruct, Llama-3.2-3B, Qwen2.5-3B, gemma-2b | 1.02 | 0.90 to 1.18 (95.0 %) |  |
| A0 | moral/aesthetic | 14 | - | 1.23 | 1.13 to 1.34 (95.0 %) |  |
| A0 | moral/epistemic | 13 | Llama-3.2-1B-Instruct | 1.07 | 0.98 to 1.17 (95.0 %) |  |
| A1 | moral/norm | 14 | - | 0.99 | 0.93 to 1.05 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25) |
| A1 | moral/descr | 13 | Qwen2.5-14B-Instruct | 1.19 | 1.11 to 1.26 (95.0 %) |  |
| A1 | norm/descr | 13 | Qwen2.5-14B-Instruct | 1.20 | 1.14 to 1.27 (95.0 %) |  |
| A1 | moral/prudential | 14 | - | 1.04 | 0.94 to 1.17 (95.0 %) |  |
| A1 | moral/etiquette | 13 | Qwen2.5-3B | 0.95 | 0.86 to 1.06 (95.0 %) |  |
| A1 | moral/aesthetic | 14 | - | 1.07 | 0.97 to 1.17 (95.0 %) |  |
| A1 | moral/epistemic | 14 | - | 0.98 | 0.89 to 1.09 (95.0 %) |  |
| B | moral/norm | 14 | - | 0.89 | 0.83 to 0.94 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25; it excludes 1, but the difference is within the margin) |
| B | moral/descr | 14 | - | 1.09 | 1.02 to 1.16 (95.0 %) |  |
| B | norm/descr | 14 | - | 1.23 | 1.16 to 1.31 (95.0 %) |  |
| B | moral/prudential | 13 | Llama-3.2-1B | 0.92 | 0.83 to 1.06 (95.0 %) |  |
| B | moral/etiquette | 12 | Llama-3.2-1B, gemma-2b-it | 0.89 | 0.80 to 1.00 (95.0 %) |  |
| B | moral/aesthetic | 14 | - | 0.89 | 0.83 to 0.98 (95.0 %) |  |
| B | moral/epistemic | 14 | - | 0.90 | 0.83 to 0.99 (95.0 %) |  |

Other head sets, moral / norm: A0 located_top5 1.16 (1.08 to 1.24); A0 located_top1 1.31 (1.15 to 1.48); A0 topshare10 1.13 (1.06 to 1.20); A0 topshare_1pct 1.11 (1.03 to 1.19); A1 located_top5 1.01 (0.94 to 1.09); A1 located_top1 1.09 (0.96 to 1.22); A1 topshare10 1.04 (0.97 to 1.11); A1 topshare_1pct 1.02 (0.94 to 1.10); B located_top5 0.90 (0.84 to 0.96); B located_top1 0.94 (0.84 to 1.05); B topshare10 0.90 (0.84 to 0.96); B topshare_1pct 0.87 (0.81 to 0.93)

## Per model, moral / norm

| model | frame | n moral | n norm | share moral | share norm | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 76 | 85 | 0.080 | 0.064 | 0.010 | 1.25 | 1.10 to 1.42 | 0.0011 | 0.0077 |
| Llama-3.1-8B-Instruct | A0 | 77 | 91 | 0.102 | 0.082 | 0.010 | 1.24 | 1.09 to 1.41 | 0.0009 | 0.0077 |
| Llama-3.2-1B | A0 | 65 | 59 | 0.074 | 0.073 | 0.020 | 1.01 | 0.93 to 1.11 | 0.7612 | 0.8198 |
| Llama-3.2-1B-Instruct | A0 | 61 | 47 | 0.063 | 0.053 | 0.020 | 1.18 | 1.06 to 1.32 | 0.0054 | 0.0252 |
| Llama-3.2-3B | A0 | 71 | 76 | 0.110 | 0.101 | 0.015 | 1.09 | 0.97 to 1.21 | 0.1626 | 0.2845 |
| Llama-3.2-3B-Instruct | A0 | 73 | 74 | 0.106 | 0.106 | 0.015 | 1.00 | 0.90 to 1.11 | 0.9978 | 0.9978 |
| Qwen2.5-14B | A0 | 75 | 91 | 0.046 | 0.038 | 0.005 | 1.19 | 1.01 to 1.39 | 0.0373 | 0.1044 |
| Qwen2.5-14B-Instruct | A0 | 73 | 87 | 0.043 | 0.034 | 0.005 | 1.25 | 1.04 to 1.48 | 0.0169 | 0.0593 |
| Qwen2.5-3B | A0 | 48 | 65 | 0.076 | 0.065 | 0.017 | 1.17 | 0.99 to 1.39 | 0.0734 | 0.1713 |
| Qwen2.5-3B-Instruct | A0 | 74 | 92 | 0.090 | 0.081 | 0.017 | 1.12 | 0.96 to 1.29 | 0.1508 | 0.2845 |
| Qwen2.5-7B | A0 | 75 | 89 | 0.069 | 0.077 | 0.013 | 0.89 | 0.75 to 1.07 | 0.2501 | 0.3891 |
| Qwen2.5-7B-Instruct | A0 | 73 | 76 | 0.066 | 0.060 | 0.013 | 1.09 | 0.89 to 1.33 | 0.4031 | 0.5643 |
| gemma-2b | A0 | 69 | 80 | 0.209 | 0.206 | 0.069 | 1.01 | 0.94 to 1.10 | 0.7298 | 0.8198 |
| gemma-2b-it | A0 | 65 | 83 | 0.167 | 0.163 | 0.069 | 1.03 | 0.93 to 1.13 | 0.6226 | 0.7924 |
| Llama-3.1-8B | A1 | 73 | 99 | 0.069 | 0.083 | 0.010 | 0.83 | 0.75 to 0.93 | 0.0022 | 0.0308 |
| Llama-3.1-8B-Instruct | A1 | 76 | 101 | 0.092 | 0.105 | 0.010 | 0.88 | 0.79 to 0.97 | 0.0130 | 0.0607 |
| Llama-3.2-1B | A1 | 69 | 86 | 0.090 | 0.084 | 0.020 | 1.07 | 0.99 to 1.15 | 0.0868 | 0.2148 |
| Llama-3.2-1B-Instruct | A1 | 65 | 77 | 0.048 | 0.044 | 0.020 | 1.11 | 0.98 to 1.25 | 0.0920 | 0.2148 |
| Llama-3.2-3B | A1 | 75 | 97 | 0.125 | 0.135 | 0.015 | 0.92 | 0.83 to 1.03 | 0.1378 | 0.2379 |
| Llama-3.2-3B-Instruct | A1 | 67 | 100 | 0.112 | 0.117 | 0.015 | 0.96 | 0.85 to 1.08 | 0.4832 | 0.5325 |
| Qwen2.5-14B | A1 | 78 | 96 | 0.073 | 0.061 | 0.005 | 1.20 | 1.06 to 1.35 | 0.0059 | 0.0413 |
| Qwen2.5-14B-Instruct | A1 | 78 | 93 | 0.055 | 0.054 | 0.005 | 1.01 | 0.87 to 1.16 | 0.9028 | 0.9028 |
| Qwen2.5-3B | A1 | 69 | 83 | 0.068 | 0.061 | 0.017 | 1.11 | 0.97 to 1.26 | 0.1268 | 0.2379 |
| Qwen2.5-3B-Instruct | A1 | 74 | 102 | 0.130 | 0.116 | 0.017 | 1.11 | 0.96 to 1.29 | 0.1529 | 0.2379 |
| Qwen2.5-7B | A1 | 78 | 102 | 0.083 | 0.091 | 0.013 | 0.91 | 0.70 to 1.19 | 0.4945 | 0.5325 |
| Qwen2.5-7B-Instruct | A1 | 73 | 102 | 0.065 | 0.075 | 0.013 | 0.87 | 0.59 to 1.27 | 0.4697 | 0.5325 |
| gemma-2b | A1 | 65 | 92 | 0.187 | 0.205 | 0.069 | 0.91 | 0.84 to 0.99 | 0.0242 | 0.0847 |
| gemma-2b-it | A1 | 71 | 88 | 0.155 | 0.149 | 0.069 | 1.04 | 0.94 to 1.15 | 0.4309 | 0.5325 |
| Llama-3.1-8B | B | 75 | 102 | 0.056 | 0.067 | 0.010 | 0.83 | 0.73 to 0.95 | 0.0062 | 0.0175 |
| Llama-3.1-8B-Instruct | B | 74 | 103 | 0.057 | 0.065 | 0.010 | 0.88 | 0.77 to 0.99 | 0.0400 | 0.0801 |
| Llama-3.2-1B | B | 65 | 74 | 0.084 | 0.080 | 0.020 | 1.06 | 0.97 to 1.15 | 0.2173 | 0.3042 |
| Llama-3.2-1B-Instruct | B | 69 | 85 | 0.044 | 0.043 | 0.020 | 1.01 | 0.88 to 1.16 | 0.8753 | 0.8753 |
| Llama-3.2-3B | B | 73 | 93 | 0.083 | 0.096 | 0.015 | 0.86 | 0.75 to 0.98 | 0.0235 | 0.0548 |
| Llama-3.2-3B-Instruct | B | 68 | 98 | 0.065 | 0.081 | 0.015 | 0.80 | 0.71 to 0.90 | 0.0006 | 0.0045 |
| Qwen2.5-14B | B | 79 | 102 | 0.036 | 0.040 | 0.005 | 0.90 | 0.77 to 1.04 | 0.1370 | 0.2132 |
| Qwen2.5-14B-Instruct | B | 78 | 102 | 0.029 | 0.034 | 0.005 | 0.87 | 0.75 to 1.01 | 0.0722 | 0.1263 |
| Qwen2.5-3B | B | 69 | 89 | 0.057 | 0.071 | 0.017 | 0.81 | 0.71 to 0.92 | 0.0017 | 0.0082 |
| Qwen2.5-3B-Instruct | B | 73 | 98 | 0.113 | 0.110 | 0.017 | 1.02 | 0.91 to 1.16 | 0.7126 | 0.7679 |
| Qwen2.5-7B | B | 75 | 104 | 0.068 | 0.098 | 0.013 | 0.70 | 0.58 to 0.85 | 0.0002 | 0.0028 |
| Qwen2.5-7B-Instruct | B | 73 | 102 | 0.056 | 0.064 | 0.013 | 0.87 | 0.64 to 1.17 | 0.3635 | 0.4627 |
| gemma-2b | B | 67 | 86 | 0.189 | 0.215 | 0.069 | 0.88 | 0.81 to 0.97 | 0.0043 | 0.0152 |
| gemma-2b-it | B | 61 | 75 | 0.157 | 0.160 | 0.069 | 0.98 | 0.88 to 1.09 | 0.7130 | 0.7679 |

## Per model, moral / descr

| model | frame | n moral | n descr | share moral | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 76 | 11 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | A0 | 77 | 8 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | A0 | 65 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A0 | 61 | 4 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | A0 | 71 | 5 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | A0 | 73 | 2 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | A0 | 75 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A0 | 73 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A0 | 48 | 0 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A0 | 74 | 16 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | A0 | 75 | 10 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | A0 | 73 | 14 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | A0 | 69 | 17 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | A0 | 65 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B | A1 | 73 | 31 | 0.069 | 0.081 | 0.010 | 0.86 | 0.76 to 0.98 | 0.0499 | 0.1082 |
| Llama-3.1-8B-Instruct | A1 | 76 | 31 | 0.092 | 0.102 | 0.010 | 0.90 | 0.80 to 1.01 | 0.1348 | 0.1948 |
| Llama-3.2-1B | A1 | 69 | 33 | 0.090 | 0.083 | 0.020 | 1.09 | 1.00 to 1.18 | 0.0711 | 0.1321 |
| Llama-3.2-1B-Instruct | A1 | 65 | 32 | 0.048 | 0.030 | 0.020 | 1.62 | 1.38 to 1.92 | 0.0000 | 0.0003 |
| Llama-3.2-3B | A1 | 75 | 37 | 0.125 | 0.118 | 0.015 | 1.05 | 0.94 to 1.19 | 0.4313 | 0.4673 |
| Llama-3.2-3B-Instruct | A1 | 67 | 39 | 0.112 | 0.094 | 0.015 | 1.19 | 1.05 to 1.36 | 0.0240 | 0.0625 |
| Qwen2.5-14B | A1 | 78 | 22 | 0.073 | 0.043 | 0.005 | 1.70 | 1.48 to 1.95 | 0.0000 | 0.0003 |
| Qwen2.5-14B-Instruct | A1 | 78 | 10 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A1 | 69 | 36 | 0.068 | 0.054 | 0.017 | 1.26 | 1.10 to 1.44 | 0.0017 | 0.0055 |
| Qwen2.5-3B-Instruct | A1 | 74 | 39 | 0.130 | 0.127 | 0.017 | 1.02 | 0.87 to 1.19 | 0.8126 | 0.8126 |
| Qwen2.5-7B | A1 | 78 | 40 | 0.083 | 0.062 | 0.013 | 1.32 | 1.04 to 1.70 | 0.1055 | 0.1714 |
| Qwen2.5-7B-Instruct | A1 | 73 | 39 | 0.065 | 0.046 | 0.013 | 1.40 | 1.00 to 1.97 | 0.2301 | 0.2720 |
| gemma-2b | A1 | 65 | 37 | 0.187 | 0.175 | 0.069 | 1.07 | 0.96 to 1.19 | 0.2276 | 0.2720 |
| gemma-2b-it | A1 | 71 | 34 | 0.155 | 0.122 | 0.069 | 1.27 | 1.11 to 1.46 | 0.0006 | 0.0026 |
| Llama-3.1-8B | B | 75 | 39 | 0.056 | 0.057 | 0.010 | 0.98 | 0.85 to 1.14 | 0.8554 | 0.9212 |
| Llama-3.1-8B-Instruct | B | 74 | 40 | 0.057 | 0.054 | 0.010 | 1.04 | 0.90 to 1.20 | 0.6503 | 0.8276 |
| Llama-3.2-1B | B | 65 | 32 | 0.084 | 0.067 | 0.020 | 1.26 | 1.12 to 1.43 | 0.0002 | 0.0014 |
| Llama-3.2-1B-Instruct | B | 69 | 35 | 0.044 | 0.029 | 0.020 | 1.51 | 1.28 to 1.81 | 0.0000 | 0.0007 |
| Llama-3.2-3B | B | 73 | 39 | 0.083 | 0.093 | 0.015 | 0.89 | 0.77 to 1.02 | 0.1273 | 0.2547 |
| Llama-3.2-3B-Instruct | B | 68 | 39 | 0.065 | 0.076 | 0.015 | 0.86 | 0.75 to 0.98 | 0.0323 | 0.0904 |
| Qwen2.5-14B | B | 79 | 39 | 0.036 | 0.030 | 0.005 | 1.19 | 1.00 to 1.39 | 0.0949 | 0.2215 |
| Qwen2.5-14B-Instruct | B | 78 | 39 | 0.029 | 0.023 | 0.005 | 1.25 | 1.07 to 1.46 | 0.0313 | 0.0904 |
| Qwen2.5-3B | B | 69 | 37 | 0.057 | 0.057 | 0.017 | 1.00 | 0.87 to 1.14 | 0.9510 | 0.9510 |
| Qwen2.5-3B-Instruct | B | 73 | 38 | 0.113 | 0.106 | 0.017 | 1.06 | 0.91 to 1.25 | 0.4142 | 0.6444 |
| Qwen2.5-7B | B | 75 | 40 | 0.068 | 0.071 | 0.013 | 0.97 | 0.79 to 1.20 | 0.7896 | 0.9212 |
| Qwen2.5-7B-Instruct | B | 73 | 40 | 0.056 | 0.045 | 0.013 | 1.24 | 0.92 to 1.64 | 0.3011 | 0.5270 |
| gemma-2b | B | 67 | 38 | 0.189 | 0.161 | 0.069 | 1.18 | 1.06 to 1.32 | 0.0079 | 0.0371 |
| gemma-2b-it | B | 61 | 33 | 0.157 | 0.152 | 0.069 | 1.04 | 0.92 to 1.17 | 0.5837 | 0.8172 |

## Per model, norm / descr

| model | frame | n norm | n descr | share norm | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 85 | 11 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | A0 | 91 | 8 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | A0 | 59 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A0 | 47 | 4 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | A0 | 76 | 5 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | A0 | 74 | 2 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | A0 | 91 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A0 | 87 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A0 | 65 | 0 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A0 | 92 | 16 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | A0 | 89 | 10 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | A0 | 76 | 14 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | A0 | 80 | 17 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | A0 | 83 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B | A1 | 99 | 31 | 0.083 | 0.081 | 0.010 | 1.03 | 0.92 to 1.16 | 0.6575 | 0.7390 |
| Llama-3.1-8B-Instruct | A1 | 101 | 31 | 0.105 | 0.102 | 0.010 | 1.02 | 0.93 to 1.13 | 0.7195 | 0.7390 |
| Llama-3.2-1B | A1 | 86 | 33 | 0.084 | 0.083 | 0.020 | 1.02 | 0.93 to 1.11 | 0.7390 | 0.7390 |
| Llama-3.2-1B-Instruct | A1 | 77 | 32 | 0.044 | 0.030 | 0.020 | 1.46 | 1.27 to 1.70 | 0.0000 | 0.0006 |
| Llama-3.2-3B | A1 | 97 | 37 | 0.135 | 0.118 | 0.015 | 1.14 | 1.02 to 1.28 | 0.0395 | 0.0642 |
| Llama-3.2-3B-Instruct | A1 | 100 | 39 | 0.117 | 0.094 | 0.015 | 1.24 | 1.11 to 1.39 | 0.0009 | 0.0031 |
| Qwen2.5-14B | A1 | 96 | 22 | 0.061 | 0.043 | 0.005 | 1.42 | 1.25 to 1.61 | 0.0003 | 0.0023 |
| Qwen2.5-14B-Instruct | A1 | 93 | 10 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A1 | 83 | 36 | 0.061 | 0.054 | 0.017 | 1.13 | 0.98 to 1.32 | 0.1598 | 0.2309 |
| Qwen2.5-3B-Instruct | A1 | 102 | 39 | 0.116 | 0.127 | 0.017 | 0.92 | 0.81 to 1.04 | 0.2536 | 0.3297 |
| Qwen2.5-7B | A1 | 102 | 40 | 0.091 | 0.062 | 0.013 | 1.45 | 1.20 to 1.75 | 0.0053 | 0.0115 |
| Qwen2.5-7B-Instruct | A1 | 102 | 39 | 0.075 | 0.046 | 0.013 | 1.61 | 1.28 to 2.03 | 0.0092 | 0.0172 |
| gemma-2b | A1 | 92 | 37 | 0.205 | 0.175 | 0.069 | 1.17 | 1.06 to 1.29 | 0.0009 | 0.0031 |
| gemma-2b-it | A1 | 88 | 34 | 0.149 | 0.122 | 0.069 | 1.22 | 1.08 to 1.39 | 0.0014 | 0.0036 |
| Llama-3.1-8B | B | 102 | 39 | 0.067 | 0.057 | 0.010 | 1.18 | 1.03 to 1.35 | 0.0326 | 0.0456 |
| Llama-3.1-8B-Instruct | B | 103 | 40 | 0.065 | 0.054 | 0.010 | 1.19 | 1.03 to 1.35 | 0.0261 | 0.0406 |
| Llama-3.2-1B | B | 74 | 32 | 0.080 | 0.067 | 0.020 | 1.20 | 1.07 to 1.35 | 0.0026 | 0.0073 |
| Llama-3.2-1B-Instruct | B | 85 | 35 | 0.043 | 0.029 | 0.020 | 1.50 | 1.30 to 1.74 | 0.0000 | 0.0002 |
| Llama-3.2-3B | B | 93 | 39 | 0.096 | 0.093 | 0.015 | 1.03 | 0.90 to 1.19 | 0.6753 | 0.6885 |
| Llama-3.2-3B-Instruct | B | 98 | 39 | 0.081 | 0.076 | 0.015 | 1.07 | 0.94 to 1.22 | 0.3747 | 0.4371 |
| Qwen2.5-14B | B | 102 | 39 | 0.040 | 0.030 | 0.005 | 1.32 | 1.16 to 1.52 | 0.0011 | 0.0038 |
| Qwen2.5-14B-Instruct | B | 102 | 39 | 0.034 | 0.023 | 0.005 | 1.44 | 1.27 to 1.64 | 0.0000 | 0.0002 |
| Qwen2.5-3B | B | 89 | 37 | 0.071 | 0.057 | 0.017 | 1.23 | 1.08 to 1.41 | 0.0100 | 0.0200 |
| Qwen2.5-3B-Instruct | B | 98 | 38 | 0.110 | 0.106 | 0.017 | 1.04 | 0.88 to 1.23 | 0.6885 | 0.6885 |
| Qwen2.5-7B | B | 104 | 40 | 0.098 | 0.071 | 0.013 | 1.39 | 1.15 to 1.68 | 0.0036 | 0.0084 |
| Qwen2.5-7B-Instruct | B | 102 | 40 | 0.064 | 0.045 | 0.013 | 1.42 | 1.12 to 1.78 | 0.0248 | 0.0406 |
| gemma-2b | B | 86 | 38 | 0.215 | 0.161 | 0.069 | 1.34 | 1.22 to 1.47 | 0.0000 | 0.0002 |
| gemma-2b-it | B | 75 | 33 | 0.160 | 0.152 | 0.069 | 1.06 | 0.95 to 1.17 | 0.3099 | 0.3945 |

## Base to instruct (moral items)

| frame | pair | r | reliability base / instruct | rank of base top head | prediction met |
|---|---|---|---|---|---|
| A0 | Llama-3.2-1B | 0.873 | 0.979 / 0.976 | 21 | False |
| A0 | Llama-3.2-3B | 0.942 | 0.986 / 0.989 | 4 | True |
| A0 | Llama-3.1-8B | 0.960 | 0.981 / 0.985 | 4 | True |
| A0 | gemma-2b | 0.886 | 0.975 / 0.970 | 3 | True |
| A0 | Qwen2.5-3B | 0.851 | 0.934 / 0.964 | 3 | True |
| A0 | Qwen2.5-7B | 0.880 | 0.970 / 0.959 | 12 | False |
| A0 | Qwen2.5-14B | 0.943 | 0.968 / 0.962 | 1 | True |
| A1 | Llama-3.2-1B | 0.898 | 0.989 / 0.977 | 12 | False |
| A1 | Llama-3.2-3B | 0.915 | 0.991 / 0.990 | 4 | True |
| A1 | Llama-3.1-8B | 0.947 | 0.984 / 0.988 | 4 | True |
| A1 | gemma-2b | 0.892 | 0.984 / 0.980 | 20 | False |
| A1 | Qwen2.5-3B | 0.878 | 0.987 / 0.986 | 1 | True |
| A1 | Qwen2.5-7B | 0.776 | 0.971 / 0.933 | 99 | False |
| A1 | Qwen2.5-14B | 0.963 | 0.989 / 0.984 | 1 | True |
| B | Llama-3.2-1B | 0.928 | 0.988 / 0.981 | 7 | True |
| B | Llama-3.2-3B | 0.919 | 0.985 / 0.979 | 1 | True |
| B | Llama-3.1-8B | 0.960 | 0.985 / 0.983 | 3 | True |
| B | gemma-2b | 0.856 | 0.977 / 0.976 | 15 | False |
| B | Qwen2.5-3B | 0.911 | 0.975 / 0.984 | 1 | True |
| B | Qwen2.5-7B | 0.879 | 0.961 / 0.952 | 116 | False |
| B | Qwen2.5-14B | 0.943 | 0.983 / 0.979 | 2 | True |

## Robustness (moral vs norm)

The last two columns select ten heads on half of the NEW items and test on the other half. If heads chosen on norm items show the same ratio in the other direction, a ratio above 1 only says that the two profiles differ.

| model | frame | adjusted logit difference (95 % CI) | unadjusted | gap-matched | rated-size-matched | raw ratio: head set / all heads | moral-selected: moral / norm | norm-selected: norm / moral |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | +0.045 (-0.091 to +0.178) | +0.196 | 1.00 | 1.20 | 1.65 / 1.26 | 1.32 (1.17 to 1.45) | 0.82 (0.76 to 0.89) |
| Llama-3.1-8B | A1 | -0.287 (-0.433 to -0.146) | -0.200 | 0.83 | 0.87 | 0.78 / 0.92 | 0.89 (0.79 to 0.98) | 1.24 (1.16 to 1.31) |
| Llama-3.1-8B | B | -0.184 (-0.310 to -0.064) | -0.185 | 0.84 | 0.81 | 0.60 / 0.69 | 1.01 (0.94 to 1.07) | 1.04 (0.96 to 1.12) |
| Llama-3.1-8B-Instruct | A0 | -0.041 (-0.193 to +0.096) | +0.191 | 0.92 | 1.16 | 1.50 / 1.17 | 1.24 (1.08 to 1.38) | 0.86 (0.80 to 0.92) |
| Llama-3.1-8B-Instruct | A1 | -0.260 (-0.398 to -0.121) | -0.171 | 0.86 | 0.88 | 0.83 / 0.94 | 0.88 (0.79 to 0.97) | 1.14 (1.08 to 1.21) |
| Llama-3.1-8B-Instruct | B | -0.140 (-0.264 to -0.017) | -0.142 | 0.86 | 0.87 | 0.77 / 0.85 | 0.97 (0.92 to 1.03) | 1.10 (1.03 to 1.17) |
| Llama-3.2-1B | A0 | -0.061 (-0.160 to +0.040) | +0.020 | 1.00 | 0.95 | 1.11 / 1.10 | 1.08 (0.98 to 1.19) | 0.99 (0.88 to 1.08) |
| Llama-3.2-1B | A1 | +0.043 (-0.028 to +0.115) | +0.085 | 1.03 | 1.00 | 1.24 / 1.13 | 1.05 (0.97 to 1.12) | 0.98 (0.91 to 1.05) |
| Llama-3.2-1B | B | +0.047 (-0.040 to +0.137) | +0.067 | 1.02 | 1.05 | 1.19 / 1.11 | 1.02 (0.93 to 1.10) | 1.03 (0.94 to 1.11) |
| Llama-3.2-1B-Instruct | A0 | +0.145 (+0.025 to +0.264) | +0.172 | 1.14 | 1.12 | 1.42 / 1.16 | 1.12 (1.00 to 1.25) | 1.18 (1.04 to 1.32) |
| Llama-3.2-1B-Instruct | A1 | +0.028 (-0.075 to +0.131) | +0.077 | 1.10 | 1.11 | 0.90 / 0.81 | 1.17 (0.99 to 1.37) | 0.99 (0.91 to 1.07) |
| Llama-3.2-1B-Instruct | B | -0.101 (-0.218 to +0.020) | -0.030 | 1.00 | 1.03 | 1.24 / 1.13 | 1.10 (0.97 to 1.21) | 0.98 (0.88 to 1.05) |
| Llama-3.2-3B | A0 | -0.118 (-0.250 to +0.018) | +0.080 | 0.92 | 1.06 | 1.37 / 1.20 | 1.18 (1.04 to 1.30) | 0.89 (0.81 to 0.96) |
| Llama-3.2-3B | A1 | -0.174 (-0.277 to -0.070) | -0.099 | 0.86 | 0.91 | 0.94 / 0.96 | 0.96 (0.88 to 1.04) | 1.06 (1.00 to 1.11) |
| Llama-3.2-3B | B | -0.177 (-0.295 to -0.060) | -0.160 | 0.82 | 0.81 | 0.63 / 0.67 | 0.93 (0.86 to 1.00) | 1.23 (1.11 to 1.33) |
| Llama-3.2-3B-Instruct | A0 | -0.166 (-0.306 to -0.026) | +0.007 | 0.92 | 1.00 | 1.30 / 1.28 | 1.12 (1.02 to 1.21) | 0.92 (0.85 to 0.99) |
| Llama-3.2-3B-Instruct | A1 | -0.131 (-0.257 to -0.013) | -0.058 | 0.93 | 0.90 | 0.59 / 0.58 | 1.01 (0.91 to 1.12) | 1.03 (0.95 to 1.11) |
| Llama-3.2-3B-Instruct | B | -0.181 (-0.311 to -0.051) | -0.197 | 0.79 | 0.78 | 0.53 / 0.64 | 0.83 (0.76 to 0.89) | 1.42 (1.28 to 1.54) |
| Qwen2.5-14B | A0 | +0.017 (-0.166 to +0.204) | +0.121 | 1.11 | 1.17 | 0.86 / 0.79 | 1.32 (1.17 to 1.47) | 0.87 (0.79 to 0.96) |
| Qwen2.5-14B | A1 | -0.021 (-0.174 to +0.129) | +0.182 | 1.05 | 1.23 | 0.59 / 0.50 | 1.20 (1.10 to 1.31) | 0.87 (0.79 to 0.97) |
| Qwen2.5-14B | B | -0.176 (-0.338 to -0.017) | -0.175 | 0.87 | 0.86 | 0.55 / 0.57 | 0.93 (0.81 to 1.03) | 1.29 (1.10 to 1.47) |
| Qwen2.5-14B-Instruct | A0 | +0.159 (-0.031 to +0.343) | +0.199 | 1.18 | 1.14 | 0.92 / 0.84 | 1.32 (1.10 to 1.51) | 0.83 (0.70 to 0.94) |
| Qwen2.5-14B-Instruct | A1 | -0.212 (-0.389 to -0.037) | -0.027 | 0.98 | 1.01 | 0.27 / 0.25 | 0.99 (0.88 to 1.10) | 1.11 (0.98 to 1.23) |
| Qwen2.5-14B-Instruct | B | -0.191 (-0.327 to -0.057) | -0.170 | 0.84 | 0.86 | 0.53 / 0.58 | 0.92 (0.82 to 1.05) | 1.44 (1.23 to 1.65) |
| Qwen2.5-3B | A0 | +0.070 (-0.127 to +0.265) | +0.139 | 1.14 | 1.26 | 1.50 / 1.53 | 1.18 (0.98 to 1.37) | 0.88 (0.75 to 1.01) |
| Qwen2.5-3B | A1 | +0.149 (+0.026 to +0.272) | +0.129 | 1.13 | 1.16 | 1.15 / 1.04 | 1.25 (1.11 to 1.38) | 0.83 (0.75 to 0.91) |
| Qwen2.5-3B | B | -0.188 (-0.310 to -0.065) | -0.221 | 0.83 | 0.87 | 0.55 / 0.71 | 0.92 (0.81 to 1.02) | 1.21 (1.06 to 1.33) |
| Qwen2.5-3B-Instruct | A0 | -0.029 (-0.165 to +0.110) | +0.035 | 1.01 | 1.13 | 1.06 / 1.02 | 1.25 (1.07 to 1.42) | 0.94 (0.85 to 1.05) |
| Qwen2.5-3B-Instruct | A1 | +0.100 (-0.043 to +0.250) | +0.082 | 1.09 | 1.06 | 0.69 / 0.63 | 1.16 (1.01 to 1.32) | 0.92 (0.84 to 1.00) |
| Qwen2.5-3B-Instruct | B | +0.059 (-0.056 to +0.174) | +0.076 | 0.97 | 0.97 | 0.65 / 0.61 | 1.05 (0.96 to 1.14) | 1.02 (0.93 to 1.12) |
| Qwen2.5-7B | A0 | -0.132 (-0.322 to +0.052) | -0.073 | 0.82 | 0.80 | 1.03 / 1.13 | 1.13 (1.01 to 1.26) | 0.97 (0.85 to 1.10) |
| Qwen2.5-7B | A1 | -0.154 (-0.351 to +0.040) | -0.141 | 0.90 | 0.91 | 0.79 / 0.80 | 1.01 (0.89 to 1.13) | 1.01 (0.92 to 1.11) |
| Qwen2.5-7B | B | -0.422 (-0.605 to -0.246) | -0.415 | 0.68 | 0.78 | 0.64 / 0.76 | 0.92 (0.81 to 1.05) | 1.16 (1.02 to 1.33) |
| Qwen2.5-7B-Instruct | A0 | +0.022 (-0.186 to +0.240) | +0.077 | 0.99 | 1.03 | 1.45 / 1.28 | 1.15 (1.00 to 1.30) | 0.91 (0.79 to 1.01) |
| Qwen2.5-7B-Instruct | A1 | -0.276 (-0.498 to -0.046) | -0.248 | 0.91 | 0.89 | 0.83 / 0.68 | 0.92 (0.77 to 1.09) | 1.18 (1.03 to 1.30) |
| Qwen2.5-7B-Instruct | B | -0.262 (-0.488 to -0.038) | -0.227 | 0.84 | 1.02 | 0.72 / 0.78 | 1.04 (0.90 to 1.18) | 1.07 (0.92 to 1.21) |
| gemma-2b | A0 | -0.037 (-0.131 to +0.058) | +0.014 | 1.00 | 1.00 | 0.95 / 0.97 | 1.01 (0.93 to 1.09) | 1.06 (1.00 to 1.11) |
| gemma-2b | A1 | -0.114 (-0.209 to -0.024) | -0.120 | 0.94 | 0.89 | 0.93 / 1.04 | 1.08 (1.01 to 1.15) | 0.96 (0.89 to 1.01) |
| gemma-2b | B | -0.157 (-0.267 to -0.047) | -0.172 | 0.89 | 0.87 | 0.83 / 0.94 | 1.03 (0.95 to 1.11) | 1.08 (1.01 to 1.15) |
| gemma-2b-it | A0 | +0.023 (-0.104 to +0.140) | +0.016 | 1.03 | 1.10 | 0.52 / 0.53 | 1.01 (0.94 to 1.09) | 1.12 (1.05 to 1.19) |
| gemma-2b-it | A1 | +0.046 (-0.071 to +0.164) | +0.038 | 1.04 | 1.05 | 0.55 / 0.53 | 1.06 (0.95 to 1.16) | 0.99 (0.93 to 1.04) |
| gemma-2b-it | B | -0.013 (-0.138 to +0.106) | -0.043 | 0.98 | 1.00 | 1.05 / 1.05 | 1.15 (1.06 to 1.26) | 0.95 (0.83 to 1.04) |

## Behaviour

| model | frame | category | run | included | mean gap | correct sign | mean mass |
|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | moral | 80 | 76 | +0.553 | 0.97 | 0.58 |
| Llama-3.1-8B | A0 | norm | 107 | 85 | +0.291 | 0.93 | 0.46 |
| Llama-3.1-8B | A0 | descr | 40 | 11 | +0.068 | 0.88 | 0.12 |
| Llama-3.1-8B | A1 | moral | 80 | 73 | +0.756 | 0.97 | 0.50 |
| Llama-3.1-8B | A1 | norm | 107 | 99 | +0.431 | 0.98 | 0.33 |
| Llama-3.1-8B | A1 | descr | 40 | 31 | +0.230 | 1.00 | 0.16 |
| Llama-3.1-8B | B | moral | 80 | 75 | +0.611 | 0.96 | 0.46 |
| Llama-3.1-8B | B | norm | 107 | 102 | +0.600 | 0.97 | 0.50 |
| Llama-3.1-8B | B | descr | 40 | 39 | +0.605 | 1.00 | 0.41 |
| Llama-3.1-8B-Instruct | A0 | moral | 80 | 77 | +0.608 | 0.97 | 0.46 |
| Llama-3.1-8B-Instruct | A0 | norm | 107 | 91 | +0.281 | 0.99 | 0.32 |
| Llama-3.1-8B-Instruct | A0 | descr | 40 | 8 | +0.062 | 0.93 | 0.10 |
| Llama-3.1-8B-Instruct | A1 | moral | 80 | 76 | +1.060 | 0.97 | 0.64 |
| Llama-3.1-8B-Instruct | A1 | norm | 107 | 101 | +0.625 | 1.00 | 0.40 |
| Llama-3.1-8B-Instruct | A1 | descr | 40 | 31 | +0.255 | 1.00 | 0.16 |
| Llama-3.1-8B-Instruct | B | moral | 80 | 74 | +0.819 | 0.97 | 0.56 |
| Llama-3.1-8B-Instruct | B | norm | 107 | 103 | +0.789 | 0.96 | 0.54 |
| Llama-3.1-8B-Instruct | B | descr | 40 | 40 | +0.755 | 1.00 | 0.44 |
| Llama-3.2-1B | A0 | moral | 80 | 65 | +0.343 | 0.93 | 0.57 |
| Llama-3.2-1B | A0 | norm | 107 | 59 | +0.159 | 0.80 | 0.39 |
| Llama-3.2-1B | A0 | descr | 40 | 14 | +0.076 | 0.88 | 0.16 |
| Llama-3.2-1B | A1 | moral | 80 | 69 | +0.492 | 0.99 | 0.69 |
| Llama-3.2-1B | A1 | norm | 107 | 86 | +0.348 | 0.93 | 0.60 |
| Llama-3.2-1B | A1 | descr | 40 | 33 | +0.350 | 1.00 | 0.44 |
| Llama-3.2-1B | B | moral | 80 | 65 | +0.314 | 0.93 | 0.56 |
| Llama-3.2-1B | B | norm | 107 | 74 | +0.243 | 0.91 | 0.55 |
| Llama-3.2-1B | B | descr | 40 | 32 | +0.290 | 0.90 | 0.46 |
| Llama-3.2-1B-Instruct | A0 | moral | 80 | 61 | +0.224 | 0.91 | 0.27 |
| Llama-3.2-1B-Instruct | A0 | norm | 107 | 47 | +0.108 | 0.92 | 0.19 |
| Llama-3.2-1B-Instruct | A0 | descr | 40 | 4 | +0.040 | 0.93 | 0.07 |
| Llama-3.2-1B-Instruct | A1 | moral | 80 | 65 | +0.463 | 0.91 | 0.67 |
| Llama-3.2-1B-Instruct | A1 | norm | 107 | 77 | +0.278 | 0.90 | 0.51 |
| Llama-3.2-1B-Instruct | A1 | descr | 40 | 32 | +0.309 | 0.97 | 0.39 |
| Llama-3.2-1B-Instruct | B | moral | 80 | 69 | +0.655 | 0.91 | 0.60 |
| Llama-3.2-1B-Instruct | B | norm | 107 | 85 | +0.434 | 0.92 | 0.57 |
| Llama-3.2-1B-Instruct | B | descr | 40 | 35 | +0.425 | 0.95 | 0.38 |
| Llama-3.2-3B | A0 | moral | 80 | 71 | +0.465 | 0.97 | 0.59 |
| Llama-3.2-3B | A0 | norm | 107 | 76 | +0.227 | 0.91 | 0.44 |
| Llama-3.2-3B | A0 | descr | 40 | 5 | +0.050 | 0.82 | 0.10 |
| Llama-3.2-3B | A1 | moral | 80 | 75 | +0.728 | 0.99 | 0.63 |
| Llama-3.2-3B | A1 | norm | 107 | 97 | +0.548 | 0.98 | 0.57 |
| Llama-3.2-3B | A1 | descr | 40 | 37 | +0.389 | 1.00 | 0.36 |
| Llama-3.2-3B | B | moral | 80 | 73 | +0.537 | 0.97 | 0.44 |
| Llama-3.2-3B | B | norm | 107 | 93 | +0.482 | 0.95 | 0.53 |
| Llama-3.2-3B | B | descr | 40 | 39 | +0.477 | 1.00 | 0.47 |
| Llama-3.2-3B-Instruct | A0 | moral | 80 | 73 | +0.407 | 0.97 | 0.32 |
| Llama-3.2-3B-Instruct | A0 | norm | 107 | 74 | +0.167 | 0.93 | 0.20 |
| Llama-3.2-3B-Instruct | A0 | descr | 40 | 2 | +0.047 | 0.95 | 0.08 |
| Llama-3.2-3B-Instruct | A1 | moral | 80 | 67 | +1.002 | 0.91 | 0.75 |
| Llama-3.2-3B-Instruct | A1 | norm | 107 | 100 | +0.819 | 0.97 | 0.64 |
| Llama-3.2-3B-Instruct | A1 | descr | 40 | 39 | +0.653 | 1.00 | 0.49 |
| Llama-3.2-3B-Instruct | B | moral | 80 | 68 | +0.766 | 0.86 | 0.57 |
| Llama-3.2-3B-Instruct | B | norm | 107 | 98 | +0.751 | 0.96 | 0.57 |
| Llama-3.2-3B-Instruct | B | descr | 40 | 39 | +0.669 | 1.00 | 0.45 |
| Qwen2.5-14B | A0 | moral | 80 | 75 | +0.749 | 1.00 | 0.70 |
| Qwen2.5-14B | A0 | norm | 107 | 91 | +0.368 | 0.97 | 0.61 |
| Qwen2.5-14B | A0 | descr | 40 | 13 | +0.097 | 0.95 | 0.15 |
| Qwen2.5-14B | A1 | moral | 80 | 78 | +1.353 | 0.99 | 0.81 |
| Qwen2.5-14B | A1 | norm | 107 | 96 | +0.745 | 0.96 | 0.51 |
| Qwen2.5-14B | A1 | descr | 40 | 22 | +0.166 | 1.00 | 0.13 |
| Qwen2.5-14B | B | moral | 80 | 79 | +1.270 | 0.99 | 0.77 |
| Qwen2.5-14B | B | norm | 107 | 102 | +1.059 | 0.99 | 0.69 |
| Qwen2.5-14B | B | descr | 40 | 39 | +1.078 | 1.00 | 0.64 |
| Qwen2.5-14B-Instruct | A0 | moral | 80 | 73 | +0.777 | 1.00 | 0.77 |
| Qwen2.5-14B-Instruct | A0 | norm | 107 | 87 | +0.467 | 0.92 | 0.69 |
| Qwen2.5-14B-Instruct | A0 | descr | 40 | 17 | +0.123 | 0.93 | 0.15 |
| Qwen2.5-14B-Instruct | A1 | moral | 80 | 78 | +1.488 | 1.00 | 0.84 |
| Qwen2.5-14B-Instruct | A1 | norm | 107 | 93 | +0.779 | 0.97 | 0.46 |
| Qwen2.5-14B-Instruct | A1 | descr | 40 | 10 | +0.120 | 0.97 | 0.07 |
| Qwen2.5-14B-Instruct | B | moral | 80 | 78 | +1.314 | 0.97 | 0.72 |
| Qwen2.5-14B-Instruct | B | norm | 107 | 102 | +1.035 | 0.98 | 0.61 |
| Qwen2.5-14B-Instruct | B | descr | 40 | 39 | +1.187 | 1.00 | 0.62 |
| Qwen2.5-3B | A0 | moral | 80 | 48 | +0.284 | 0.71 | 0.55 |
| Qwen2.5-3B | A0 | norm | 107 | 65 | +0.202 | 0.77 | 0.50 |
| Qwen2.5-3B | A0 | descr | 40 | 0 | +0.001 | 0.55 | 0.07 |
| Qwen2.5-3B | A1 | moral | 80 | 69 | +0.465 | 0.97 | 0.75 |
| Qwen2.5-3B | A1 | norm | 107 | 83 | +0.259 | 0.94 | 0.65 |
| Qwen2.5-3B | A1 | descr | 40 | 36 | +0.293 | 1.00 | 0.52 |
| Qwen2.5-3B | B | moral | 80 | 69 | +0.498 | 0.95 | 0.63 |
| Qwen2.5-3B | B | norm | 107 | 89 | +0.389 | 0.95 | 0.51 |
| Qwen2.5-3B | B | descr | 40 | 37 | +0.434 | 1.00 | 0.51 |
| Qwen2.5-3B-Instruct | A0 | moral | 80 | 74 | +0.614 | 0.97 | 0.71 |
| Qwen2.5-3B-Instruct | A0 | norm | 107 | 92 | +0.350 | 0.96 | 0.57 |
| Qwen2.5-3B-Instruct | A0 | descr | 40 | 16 | +0.110 | 0.97 | 0.18 |
| Qwen2.5-3B-Instruct | A1 | moral | 80 | 74 | +1.011 | 0.97 | 0.79 |
| Qwen2.5-3B-Instruct | A1 | norm | 107 | 102 | +0.892 | 0.96 | 0.69 |
| Qwen2.5-3B-Instruct | A1 | descr | 40 | 39 | +0.683 | 1.00 | 0.47 |
| Qwen2.5-3B-Instruct | B | moral | 80 | 73 | +1.015 | 0.96 | 0.70 |
| Qwen2.5-3B-Instruct | B | norm | 107 | 98 | +0.851 | 0.98 | 0.58 |
| Qwen2.5-3B-Instruct | B | descr | 40 | 38 | +0.869 | 1.00 | 0.54 |
| Qwen2.5-7B | A0 | moral | 80 | 75 | +0.630 | 0.99 | 0.62 |
| Qwen2.5-7B | A0 | norm | 107 | 89 | +0.317 | 0.94 | 0.48 |
| Qwen2.5-7B | A0 | descr | 40 | 10 | +0.078 | 0.90 | 0.13 |
| Qwen2.5-7B | A1 | moral | 80 | 78 | +1.121 | 0.99 | 0.80 |
| Qwen2.5-7B | A1 | norm | 107 | 102 | +0.858 | 0.98 | 0.67 |
| Qwen2.5-7B | A1 | descr | 40 | 40 | +0.531 | 1.00 | 0.47 |
| Qwen2.5-7B | B | moral | 80 | 75 | +1.055 | 0.96 | 0.78 |
| Qwen2.5-7B | B | norm | 107 | 104 | +1.044 | 1.00 | 0.75 |
| Qwen2.5-7B | B | descr | 40 | 40 | +1.077 | 1.00 | 0.72 |
| Qwen2.5-7B-Instruct | A0 | moral | 80 | 73 | +0.629 | 0.96 | 0.62 |
| Qwen2.5-7B-Instruct | A0 | norm | 107 | 76 | +0.302 | 0.86 | 0.51 |
| Qwen2.5-7B-Instruct | A0 | descr | 40 | 14 | +0.132 | 0.90 | 0.14 |
| Qwen2.5-7B-Instruct | A1 | moral | 80 | 73 | +1.163 | 0.95 | 0.79 |
| Qwen2.5-7B-Instruct | A1 | norm | 107 | 102 | +0.957 | 0.99 | 0.70 |
| Qwen2.5-7B-Instruct | A1 | descr | 40 | 39 | +0.715 | 1.00 | 0.46 |
| Qwen2.5-7B-Instruct | B | moral | 80 | 73 | +1.240 | 0.96 | 0.80 |
| Qwen2.5-7B-Instruct | B | norm | 107 | 102 | +1.160 | 0.97 | 0.75 |
| Qwen2.5-7B-Instruct | B | descr | 40 | 40 | +1.211 | 1.00 | 0.67 |
| gemma-2b | A0 | moral | 80 | 69 | +0.409 | 0.94 | 0.59 |
| gemma-2b | A0 | norm | 107 | 80 | +0.262 | 0.89 | 0.43 |
| gemma-2b | A0 | descr | 40 | 17 | +0.095 | 0.95 | 0.14 |
| gemma-2b | A1 | moral | 80 | 65 | +0.602 | 0.96 | 0.52 |
| gemma-2b | A1 | norm | 107 | 92 | +0.453 | 0.95 | 0.47 |
| gemma-2b | A1 | descr | 40 | 37 | +0.420 | 0.97 | 0.41 |
| gemma-2b | B | moral | 80 | 67 | +0.488 | 0.93 | 0.46 |
| gemma-2b | B | norm | 107 | 86 | +0.423 | 0.93 | 0.45 |
| gemma-2b | B | descr | 40 | 38 | +0.483 | 1.00 | 0.50 |
| gemma-2b-it | A0 | moral | 80 | 65 | +0.464 | 0.94 | 0.60 |
| gemma-2b-it | A0 | norm | 107 | 83 | +0.367 | 0.90 | 0.43 |
| gemma-2b-it | A0 | descr | 40 | 13 | +0.096 | 0.85 | 0.13 |
| gemma-2b-it | A1 | moral | 80 | 71 | +1.007 | 0.94 | 0.92 |
| gemma-2b-it | A1 | norm | 107 | 88 | +0.758 | 0.93 | 0.84 |
| gemma-2b-it | A1 | descr | 40 | 34 | +0.680 | 0.93 | 0.66 |
| gemma-2b-it | B | moral | 80 | 61 | +0.556 | 0.84 | 0.50 |
| gemma-2b-it | B | norm | 107 | 75 | +0.335 | 0.84 | 0.39 |
| gemma-2b-it | B | descr | 40 | 33 | +0.465 | 0.85 | 0.45 |
