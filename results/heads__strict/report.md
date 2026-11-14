# Head results (p2r_all, readout S, head set located, items: strict, inclusion gap >= 0.02)

**Sensitivity run (an option differs from the default): nothing here is a primary test; all intervals are 95 %.**

## Pooled ratios (mean over models of the log ratio; item bootstrap shared across models)

| frame | contrast | models used | left out | pooled ratio | interval | reading |
|---|---|---|---|---|---|---|
| A0 | moral/norm | 14 | - | 1.11 | 1.04 to 1.18 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25; it excludes 1, but the difference is within the margin) |
| A0 | moral/etiquette | 14 | - | 1.08 | 0.98 to 1.20 (95.0 %) |  |
| A0 | moral/aesthetic | 14 | - | 1.21 | 1.11 to 1.32 (95.0 %) |  |
| A0 | moral/epistemic | 14 | - | 1.05 | 0.96 to 1.16 (95.0 %) |  |
| A1 | moral/norm | 14 | - | 0.96 | 0.90 to 1.02 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25) |
| A1 | moral/etiquette | 14 | - | 0.91 | 0.82 to 1.01 (95.0 %) |  |
| A1 | moral/aesthetic | 14 | - | 1.03 | 0.94 to 1.14 (95.0 %) |  |
| A1 | moral/epistemic | 14 | - | 0.94 | 0.85 to 1.06 (95.0 %) |  |
| B | moral/norm | 14 | - | 0.88 | 0.83 to 0.94 (95.0 %) | no meaningful content specificity (interval inside 0.8 to 1.25; it excludes 1, but the difference is within the margin) |
| B | moral/etiquette | 14 | - | 0.90 | 0.82 to 1.00 (95.0 %) |  |
| B | moral/aesthetic | 14 | - | 0.88 | 0.81 to 0.97 (95.0 %) |  |
| B | moral/epistemic | 14 | - | 0.90 | 0.82 to 0.99 (95.0 %) |  |

Other head sets, moral / norm: A0 located_top5 1.15 (1.06 to 1.24); A0 located_top1 1.29 (1.13 to 1.47); A0 topshare10 1.13 (1.05 to 1.20); A0 topshare_1pct 1.09 (1.01 to 1.18); A1 located_top5 0.98 (0.90 to 1.07); A1 located_top1 1.09 (0.95 to 1.25); A1 topshare10 1.00 (0.94 to 1.08); A1 topshare_1pct 0.97 (0.89 to 1.05); B located_top5 0.89 (0.82 to 0.96); B located_top1 0.94 (0.83 to 1.06); B topshare10 0.89 (0.82 to 0.96); B topshare_1pct 0.85 (0.79 to 0.93)

## Per model, moral / norm

| model | frame | n moral | n norm | share moral | share norm | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 66 | 75 | 0.078 | 0.062 | 0.010 | 1.25 | 1.08 to 1.44 | 0.0024 | 0.0112 |
| Llama-3.1-8B-Instruct | A0 | 65 | 81 | 0.098 | 0.080 | 0.010 | 1.23 | 1.08 to 1.40 | 0.0020 | 0.0112 |
| Llama-3.2-1B | A0 | 62 | 63 | 0.072 | 0.072 | 0.020 | 1.00 | 0.92 to 1.09 | 0.9798 | 0.9798 |
| Llama-3.2-1B-Instruct | A0 | 60 | 67 | 0.063 | 0.051 | 0.020 | 1.25 | 1.13 to 1.38 | 0.0000 | 0.0007 |
| Llama-3.2-3B | A0 | 66 | 67 | 0.103 | 0.094 | 0.015 | 1.09 | 0.95 to 1.23 | 0.1995 | 0.3991 |
| Llama-3.2-3B-Instruct | A0 | 65 | 73 | 0.101 | 0.100 | 0.015 | 1.02 | 0.91 to 1.13 | 0.7632 | 0.8219 |
| Qwen2.5-14B | A0 | 68 | 78 | 0.045 | 0.037 | 0.005 | 1.23 | 1.04 to 1.46 | 0.0192 | 0.0674 |
| Qwen2.5-14B-Instruct | A0 | 68 | 74 | 0.040 | 0.033 | 0.005 | 1.19 | 0.98 to 1.43 | 0.0744 | 0.1737 |
| Qwen2.5-3B | A0 | 45 | 63 | 0.073 | 0.062 | 0.017 | 1.18 | 1.00 to 1.41 | 0.0629 | 0.1737 |
| Qwen2.5-3B-Instruct | A0 | 66 | 78 | 0.083 | 0.077 | 0.017 | 1.07 | 0.92 to 1.25 | 0.3671 | 0.5402 |
| Qwen2.5-7B | A0 | 67 | 75 | 0.070 | 0.078 | 0.013 | 0.89 | 0.73 to 1.09 | 0.2997 | 0.5245 |
| Qwen2.5-7B-Instruct | A0 | 66 | 71 | 0.065 | 0.059 | 0.013 | 1.10 | 0.89 to 1.37 | 0.3859 | 0.5402 |
| gemma-2b | A0 | 63 | 72 | 0.213 | 0.208 | 0.069 | 1.02 | 0.94 to 1.11 | 0.5704 | 0.6654 |
| gemma-2b-it | A0 | 61 | 70 | 0.170 | 0.163 | 0.069 | 1.04 | 0.93 to 1.15 | 0.4894 | 0.6228 |
| Llama-3.1-8B | A1 | 66 | 80 | 0.066 | 0.080 | 0.010 | 0.83 | 0.74 to 0.93 | 0.0009 | 0.0126 |
| Llama-3.1-8B-Instruct | A1 | 66 | 83 | 0.086 | 0.100 | 0.010 | 0.86 | 0.76 to 0.96 | 0.0105 | 0.0369 |
| Llama-3.2-1B | A1 | 67 | 75 | 0.085 | 0.082 | 0.020 | 1.03 | 0.95 to 1.12 | 0.4160 | 0.4853 |
| Llama-3.2-1B-Instruct | A1 | 58 | 74 | 0.049 | 0.042 | 0.020 | 1.17 | 1.04 to 1.33 | 0.0103 | 0.0369 |
| Llama-3.2-3B | A1 | 67 | 81 | 0.115 | 0.131 | 0.015 | 0.88 | 0.78 to 0.99 | 0.0402 | 0.1126 |
| Llama-3.2-3B-Instruct | A1 | 60 | 80 | 0.107 | 0.114 | 0.015 | 0.94 | 0.83 to 1.06 | 0.3125 | 0.4177 |
| Qwen2.5-14B | A1 | 67 | 78 | 0.072 | 0.059 | 0.005 | 1.22 | 1.06 to 1.39 | 0.0053 | 0.0369 |
| Qwen2.5-14B-Instruct | A1 | 67 | 77 | 0.053 | 0.053 | 0.005 | 1.00 | 0.85 to 1.18 | 0.9914 | 0.9914 |
| Qwen2.5-3B | A1 | 66 | 78 | 0.066 | 0.062 | 0.017 | 1.07 | 0.94 to 1.21 | 0.3282 | 0.4177 |
| Qwen2.5-3B-Instruct | A1 | 65 | 80 | 0.118 | 0.118 | 0.017 | 1.01 | 0.85 to 1.17 | 0.9516 | 0.9914 |
| Qwen2.5-7B | A1 | 67 | 81 | 0.076 | 0.093 | 0.013 | 0.82 | 0.64 to 1.06 | 0.1495 | 0.2326 |
| Qwen2.5-7B-Instruct | A1 | 63 | 83 | 0.054 | 0.074 | 0.013 | 0.73 | 0.53 to 1.01 | 0.0644 | 0.1152 |
| gemma-2b | A1 | 63 | 78 | 0.192 | 0.208 | 0.069 | 0.92 | 0.85 to 1.00 | 0.0578 | 0.1152 |
| gemma-2b-it | A1 | 62 | 77 | 0.160 | 0.146 | 0.069 | 1.10 | 0.99 to 1.22 | 0.0658 | 0.1152 |
| Llama-3.1-8B | B | 65 | 80 | 0.056 | 0.066 | 0.010 | 0.85 | 0.73 to 0.98 | 0.0255 | 0.0595 |
| Llama-3.1-8B-Instruct | B | 66 | 79 | 0.054 | 0.063 | 0.010 | 0.85 | 0.74 to 0.97 | 0.0172 | 0.0482 |
| Llama-3.2-1B | B | 61 | 71 | 0.080 | 0.076 | 0.020 | 1.06 | 0.96 to 1.17 | 0.2794 | 0.4346 |
| Llama-3.2-1B-Instruct | B | 61 | 73 | 0.044 | 0.041 | 0.020 | 1.07 | 0.93 to 1.24 | 0.3244 | 0.4542 |
| Llama-3.2-3B | B | 66 | 77 | 0.078 | 0.094 | 0.015 | 0.83 | 0.72 to 0.96 | 0.0170 | 0.0482 |
| Llama-3.2-3B-Instruct | B | 57 | 80 | 0.062 | 0.081 | 0.015 | 0.76 | 0.67 to 0.87 | 0.0002 | 0.0017 |
| Qwen2.5-14B | B | 67 | 82 | 0.036 | 0.038 | 0.005 | 0.94 | 0.79 to 1.11 | 0.4443 | 0.5184 |
| Qwen2.5-14B-Instruct | B | 66 | 80 | 0.029 | 0.033 | 0.005 | 0.88 | 0.74 to 1.05 | 0.1482 | 0.2593 |
| Qwen2.5-3B | B | 63 | 79 | 0.057 | 0.071 | 0.017 | 0.81 | 0.71 to 0.92 | 0.0026 | 0.0124 |
| Qwen2.5-3B-Instruct | B | 65 | 81 | 0.107 | 0.109 | 0.017 | 0.98 | 0.86 to 1.13 | 0.8297 | 0.8297 |
| Qwen2.5-7B | B | 66 | 83 | 0.063 | 0.098 | 0.013 | 0.65 | 0.53 to 0.78 | 0.0001 | 0.0014 |
| Qwen2.5-7B-Instruct | B | 65 | 80 | 0.053 | 0.061 | 0.013 | 0.88 | 0.64 to 1.21 | 0.4207 | 0.5184 |
| gemma-2b | B | 60 | 74 | 0.193 | 0.212 | 0.069 | 0.91 | 0.83 to 1.01 | 0.0523 | 0.1046 |
| gemma-2b-it | B | 56 | 68 | 0.159 | 0.165 | 0.069 | 0.97 | 0.87 to 1.07 | 0.5196 | 0.5595 |

## Per model, moral / descr

| model | frame | n moral | n descr | share moral | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 66 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | A0 | 65 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | A0 | 62 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A0 | 60 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | A0 | 66 | 9 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | A0 | 65 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | A0 | 68 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A0 | 68 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A0 | 45 | 2 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A0 | 66 | 16 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | A0 | 67 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | A0 | 66 | 13 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | A0 | 63 | 16 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | A0 | 61 | 9 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B | A1 | 66 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | A1 | 66 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | A1 | 67 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A1 | 58 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | A1 | 67 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | A1 | 60 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | A1 | 67 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A1 | 67 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A1 | 66 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A1 | 65 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | A1 | 67 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | A1 | 63 | 19 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | A1 | 63 | 18 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | A1 | 62 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B | B | 65 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | B | 66 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | B | 61 | 15 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | B | 61 | 16 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | B | 66 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | B | 57 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | B | 67 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | B | 66 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | B | 63 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | B | 65 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | B | 66 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | B | 65 | 19 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | B | 60 | 19 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | B | 56 | 17 | insufficient behavioural contrast: descr | | | | | | |

## Per model, norm / descr

| model | frame | n norm | n descr | share norm | share descr | uniform | ratio | 95 % CI | p | q (BH over models) |
|---|---|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | 75 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | A0 | 81 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | A0 | 63 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A0 | 67 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | A0 | 67 | 9 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | A0 | 73 | 14 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | A0 | 78 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A0 | 74 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A0 | 63 | 2 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A0 | 78 | 16 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | A0 | 75 | 13 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | A0 | 71 | 13 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | A0 | 72 | 16 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | A0 | 70 | 9 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B | A1 | 80 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | A1 | 83 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | A1 | 75 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | A1 | 74 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | A1 | 81 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | A1 | 80 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | A1 | 78 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | A1 | 77 | 12 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | A1 | 78 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | A1 | 80 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | A1 | 81 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | A1 | 83 | 19 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | A1 | 78 | 18 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | A1 | 77 | 17 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B | B | 80 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.1-8B-Instruct | B | 79 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B | B | 71 | 15 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-1B-Instruct | B | 73 | 16 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B | B | 77 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Llama-3.2-3B-Instruct | B | 80 | 18 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B | B | 82 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-14B-Instruct | B | 80 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B | B | 79 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-3B-Instruct | B | 81 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B | B | 83 | 19 | insufficient behavioural contrast: descr | | | | | | |
| Qwen2.5-7B-Instruct | B | 80 | 19 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b | B | 74 | 19 | insufficient behavioural contrast: descr | | | | | | |
| gemma-2b-it | B | 68 | 17 | insufficient behavioural contrast: descr | | | | | | |

## Base to instruct (moral items)

| frame | pair | r | reliability base / instruct | rank of base top head | prediction met |
|---|---|---|---|---|---|
| A0 | Llama-3.2-1B | 0.879 | 0.978 / 0.972 | 26 | False |
| A0 | Llama-3.2-3B | 0.938 | 0.983 / 0.986 | 3 | True |
| A0 | Llama-3.1-8B | 0.960 | 0.978 / 0.982 | 4 | True |
| A0 | gemma-2b | 0.900 | 0.974 / 0.967 | 2 | True |
| A0 | Qwen2.5-3B | 0.809 | 0.918 / 0.956 | 7 | True |
| A0 | Qwen2.5-7B | 0.873 | 0.965 / 0.957 | 9 | True |
| A0 | Qwen2.5-14B | 0.937 | 0.960 / 0.957 | 1 | True |
| A1 | Llama-3.2-1B | 0.892 | 0.986 / 0.970 | 11 | False |
| A1 | Llama-3.2-3B | 0.910 | 0.990 / 0.988 | 4 | True |
| A1 | Llama-3.1-8B | 0.942 | 0.980 / 0.985 | 5 | True |
| A1 | gemma-2b | 0.891 | 0.981 / 0.977 | 19 | False |
| A1 | Qwen2.5-3B | 0.892 | 0.984 / 0.982 | 2 | True |
| A1 | Qwen2.5-7B | 0.785 | 0.973 / 0.941 | 63 | False |
| A1 | Qwen2.5-14B | 0.961 | 0.987 / 0.979 | 1 | True |
| B | Llama-3.2-1B | 0.929 | 0.984 / 0.975 | 9 | True |
| B | Llama-3.2-3B | 0.921 | 0.981 / 0.972 | 1 | True |
| B | Llama-3.1-8B | 0.956 | 0.982 / 0.980 | 3 | True |
| B | gemma-2b | 0.869 | 0.974 / 0.973 | 14 | False |
| B | Qwen2.5-3B | 0.904 | 0.973 / 0.980 | 1 | True |
| B | Qwen2.5-7B | 0.879 | 0.956 / 0.950 | 118 | False |
| B | Qwen2.5-14B | 0.941 | 0.979 / 0.976 | 2 | True |

## Robustness (moral vs norm)

The last two columns select ten heads on half of the NEW items and test on the other half. If heads chosen on norm items show the same ratio in the other direction, a ratio above 1 only says that the two profiles differ.

| model | frame | adjusted logit difference (95 % CI) | unadjusted | gap-matched | rated-size-matched | raw ratio: head set / all heads | moral-selected: moral / norm | norm-selected: norm / moral |
|---|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | +0.105 (-0.043 to +0.250) | +0.194 | 1.07 | 1.20 | 1.64 / 1.26 | 1.34 (1.19 to 1.48) | 0.80 (0.74 to 0.87) |
| Llama-3.1-8B | A1 | -0.263 (-0.387 to -0.142) | -0.212 | 0.81 | 0.85 | 0.84 / 1.00 | 0.86 (0.78 to 0.94) | 1.29 (1.19 to 1.39) |
| Llama-3.1-8B | B | -0.129 (-0.276 to +0.014) | -0.152 | 0.84 | 0.83 | 0.67 / 0.77 | 0.97 (0.88 to 1.04) | 1.09 (0.99 to 1.16) |
| Llama-3.1-8B-Instruct | A0 | -0.005 (-0.164 to +0.142) | +0.184 | 0.93 | 1.17 | 1.62 / 1.29 | 1.24 (1.04 to 1.39) | 0.86 (0.81 to 0.93) |
| Llama-3.1-8B-Instruct | A1 | -0.320 (-0.446 to -0.195) | -0.175 | 0.80 | 0.87 | 0.83 / 0.96 | 0.87 (0.77 to 0.98) | 1.17 (1.08 to 1.25) |
| Llama-3.1-8B-Instruct | B | -0.170 (-0.301 to -0.043) | -0.188 | 0.84 | 0.87 | 0.81 / 0.89 | 0.91 (0.84 to 0.97) | 1.17 (1.09 to 1.25) |
| Llama-3.2-1B | A0 | -0.053 (-0.150 to +0.044) | +0.002 | 0.96 | 0.95 | 1.19 / 1.19 | 1.04 (0.93 to 1.16) | 0.99 (0.90 to 1.09) |
| Llama-3.2-1B | A1 | +0.028 (-0.052 to +0.110) | +0.050 | 1.03 | 0.98 | 1.12 / 1.07 | 0.97 (0.88 to 1.06) | 1.07 (0.98 to 1.15) |
| Llama-3.2-1B | B | +0.017 (-0.080 to +0.114) | +0.076 | 1.00 | 1.02 | 1.15 / 1.09 | 1.00 (0.90 to 1.08) | 1.03 (0.93 to 1.13) |
| Llama-3.2-1B-Instruct | A0 | +0.207 (+0.096 to +0.318) | +0.233 | 1.20 | 1.22 | 1.78 / 1.37 | 1.18 (1.04 to 1.31) | 1.11 (0.99 to 1.24) |
| Llama-3.2-1B-Instruct | A1 | +0.110 (+0.004 to +0.215) | +0.164 | 1.11 | 1.17 | 1.01 / 0.86 | 1.16 (0.99 to 1.33) | 1.03 (0.94 to 1.12) |
| Llama-3.2-1B-Instruct | B | -0.053 (-0.180 to +0.077) | +0.042 | 1.03 | 1.07 | 1.29 / 1.12 | 1.04 (0.91 to 1.16) | 1.00 (0.88 to 1.11) |
| Llama-3.2-3B | A0 | -0.019 (-0.154 to +0.117) | +0.078 | 0.94 | 1.02 | 1.43 / 1.26 | 1.17 (1.04 to 1.31) | 0.88 (0.81 to 0.95) |
| Llama-3.2-3B | A1 | -0.206 (-0.310 to -0.106) | -0.152 | 0.83 | 0.87 | 0.87 / 0.92 | 0.91 (0.83 to 1.00) | 1.12 (1.04 to 1.20) |
| Llama-3.2-3B | B | -0.097 (-0.258 to +0.069) | -0.147 | 0.85 | 0.80 | 0.56 / 0.64 | 0.90 (0.81 to 0.99) | 1.28 (1.10 to 1.42) |
| Llama-3.2-3B-Instruct | A0 | -0.133 (-0.266 to -0.004) | +0.034 | 0.93 | 1.00 | 1.55 / 1.48 | 1.13 (1.03 to 1.24) | 0.92 (0.84 to 0.99) |
| Llama-3.2-3B-Instruct | A1 | -0.080 (-0.209 to +0.044) | -0.072 | 0.93 | 0.91 | 0.54 / 0.55 | 0.95 (0.84 to 1.06) | 1.11 (1.00 to 1.20) |
| Llama-3.2-3B-Instruct | B | -0.223 (-0.367 to -0.080) | -0.236 | 0.75 | 0.77 | 0.52 / 0.66 | 0.80 (0.73 to 0.87) | 1.47 (1.34 to 1.60) |
| Qwen2.5-14B | A0 | +0.019 (-0.161 to +0.200) | +0.149 | 1.12 | 1.19 | 0.97 / 0.89 | 1.25 (1.09 to 1.42) | 0.89 (0.82 to 0.99) |
| Qwen2.5-14B | A1 | +0.041 (-0.122 to +0.184) | +0.207 | 1.03 | 1.23 | 0.61 / 0.51 | 1.16 (1.03 to 1.29) | 0.89 (0.80 to 1.00) |
| Qwen2.5-14B | B | -0.141 (-0.322 to +0.034) | -0.115 | 0.90 | 0.91 | 0.60 / 0.60 | 0.93 (0.80 to 1.04) | 1.19 (1.04 to 1.35) |
| Qwen2.5-14B-Instruct | A0 | +0.169 (-0.018 to +0.355) | +0.167 | 1.11 | 1.07 | 1.04 / 0.93 | 1.27 (1.11 to 1.43) | 0.82 (0.69 to 0.98) |
| Qwen2.5-14B-Instruct | A1 | -0.200 (-0.396 to -0.013) | -0.008 | 0.96 | 0.98 | 0.27 / 0.24 | 0.96 (0.84 to 1.06) | 1.10 (0.96 to 1.23) |
| Qwen2.5-14B-Instruct | B | -0.174 (-0.326 to -0.021) | -0.146 | 0.82 | 0.89 | 0.56 / 0.60 | 0.90 (0.79 to 1.02) | 1.38 (1.15 to 1.58) |
| Qwen2.5-3B | A0 | +0.122 (-0.057 to +0.307) | +0.163 | 1.14 | 1.27 | 1.70 / 1.67 | 1.14 (0.93 to 1.31) | 0.91 (0.75 to 1.05) |
| Qwen2.5-3B | A1 | +0.121 (+0.009 to +0.237) | +0.096 | 1.11 | 1.13 | 1.14 / 1.08 | 1.13 (1.00 to 1.26) | 0.91 (0.82 to 1.01) |
| Qwen2.5-3B | B | -0.172 (-0.301 to -0.047) | -0.207 | 0.82 | 0.88 | 0.58 / 0.75 | 0.91 (0.79 to 1.05) | 1.25 (1.11 to 1.38) |
| Qwen2.5-3B-Instruct | A0 | +0.014 (-0.126 to +0.155) | +0.004 | 1.02 | 1.07 | 1.10 / 1.09 | 1.21 (1.05 to 1.39) | 0.99 (0.89 to 1.11) |
| Qwen2.5-3B-Instruct | A1 | +0.042 (-0.103 to +0.200) | -0.023 | 0.99 | 1.00 | 0.60 / 0.61 | 1.05 (0.91 to 1.19) | 1.03 (0.93 to 1.12) |
| Qwen2.5-3B-Instruct | B | +0.064 (-0.059 to +0.188) | +0.043 | 0.94 | 0.95 | 0.62 / 0.61 | 0.99 (0.89 to 1.09) | 1.07 (0.96 to 1.19) |
| Qwen2.5-7B | A0 | -0.095 (-0.312 to +0.104) | -0.061 | 0.82 | 0.76 | 0.99 / 1.10 | 1.10 (0.97 to 1.24) | 0.98 (0.85 to 1.10) |
| Qwen2.5-7B | A1 | -0.197 (-0.401 to +0.004) | -0.209 | 0.85 | 0.79 | 0.78 / 0.85 | 0.95 (0.85 to 1.07) | 1.07 (0.95 to 1.21) |
| Qwen2.5-7B | B | -0.434 (-0.632 to -0.250) | -0.463 | 0.65 | 0.71 | 0.64 / 0.81 | 0.89 (0.75 to 1.03) | 1.19 (1.06 to 1.38) |
| Qwen2.5-7B-Instruct | A0 | +0.068 (-0.156 to +0.291) | +0.129 | 1.02 | 1.00 | 1.52 / 1.35 | 1.14 (1.00 to 1.28) | 0.92 (0.79 to 1.05) |
| Qwen2.5-7B-Instruct | A1 | -0.319 (-0.560 to -0.088) | -0.337 | 0.85 | 0.73 | 0.79 / 0.75 | 0.87 (0.73 to 1.02) | 1.30 (1.14 to 1.46) |
| Qwen2.5-7B-Instruct | B | -0.175 (-0.407 to +0.052) | -0.173 | 0.82 | 0.99 | 0.76 / 0.84 | 1.04 (0.89 to 1.19) | 1.03 (0.86 to 1.18) |
| gemma-2b | A0 | -0.007 (-0.108 to +0.094) | +0.029 | 1.02 | 1.02 | 1.00 / 1.02 | 1.03 (0.94 to 1.14) | 1.04 (0.99 to 1.11) |
| gemma-2b | A1 | -0.114 (-0.215 to -0.013) | -0.104 | 0.94 | 0.90 | 0.90 / 1.01 | 0.99 (0.92 to 1.06) | 1.02 (0.95 to 1.08) |
| gemma-2b | B | -0.131 (-0.247 to -0.013) | -0.132 | 0.91 | 0.91 | 0.88 / 0.98 | 1.01 (0.93 to 1.08) | 1.07 (1.01 to 1.15) |
| gemma-2b-it | A0 | +0.045 (-0.079 to +0.164) | +0.027 | 1.04 | 1.10 | 0.54 / 0.57 | 0.97 (0.88 to 1.06) | 1.15 (1.06 to 1.25) |
| gemma-2b-it | A1 | +0.110 (-0.011 to +0.232) | +0.106 | 1.09 | 1.13 | 0.61 / 0.56 | 1.01 (0.93 to 1.11) | 1.04 (0.97 to 1.11) |
| gemma-2b-it | B | -0.024 (-0.157 to +0.105) | -0.063 | 0.98 | 1.00 | 1.06 / 1.07 | 1.07 (0.99 to 1.17) | 0.97 (0.86 to 1.07) |

## Behaviour

| model | frame | category | run | included | mean gap | correct sign | mean mass |
|---|---|---|---|---|---|---|---|
| Llama-3.1-8B | A0 | moral | 68 | 66 | +0.527 | 0.97 | 0.57 |
| Llama-3.1-8B | A0 | norm | 83 | 75 | +0.287 | 0.93 | 0.45 |
| Llama-3.1-8B | A0 | descr | 19 | 17 | +0.076 | 0.89 | 0.14 |
| Llama-3.1-8B | A1 | moral | 68 | 66 | +0.723 | 0.97 | 0.49 |
| Llama-3.1-8B | A1 | norm | 83 | 80 | +0.418 | 0.98 | 0.32 |
| Llama-3.1-8B | A1 | descr | 19 | 17 | +0.261 | 1.00 | 0.19 |
| Llama-3.1-8B | B | moral | 68 | 65 | +0.569 | 0.96 | 0.45 |
| Llama-3.1-8B | B | norm | 83 | 80 | +0.596 | 0.96 | 0.48 |
| Llama-3.1-8B | B | descr | 19 | 19 | +0.543 | 1.00 | 0.37 |
| Llama-3.1-8B-Instruct | A0 | moral | 68 | 65 | +0.581 | 0.97 | 0.45 |
| Llama-3.1-8B-Instruct | A0 | norm | 83 | 81 | +0.275 | 0.99 | 0.32 |
| Llama-3.1-8B-Instruct | A0 | descr | 19 | 14 | +0.058 | 0.89 | 0.11 |
| Llama-3.1-8B-Instruct | A1 | moral | 68 | 66 | +1.035 | 0.97 | 0.64 |
| Llama-3.1-8B-Instruct | A1 | norm | 83 | 83 | +0.624 | 1.00 | 0.40 |
| Llama-3.1-8B-Instruct | A1 | descr | 19 | 17 | +0.303 | 1.00 | 0.20 |
| Llama-3.1-8B-Instruct | B | moral | 68 | 66 | +0.781 | 0.97 | 0.55 |
| Llama-3.1-8B-Instruct | B | norm | 83 | 79 | +0.783 | 0.95 | 0.53 |
| Llama-3.1-8B-Instruct | B | descr | 19 | 19 | +0.692 | 1.00 | 0.41 |
| Llama-3.2-1B | A0 | moral | 68 | 62 | +0.319 | 0.91 | 0.56 |
| Llama-3.2-1B | A0 | norm | 83 | 63 | +0.165 | 0.81 | 0.38 |
| Llama-3.2-1B | A0 | descr | 19 | 12 | +0.055 | 0.79 | 0.16 |
| Llama-3.2-1B | A1 | moral | 68 | 67 | +0.462 | 1.00 | 0.68 |
| Llama-3.2-1B | A1 | norm | 83 | 75 | +0.363 | 0.94 | 0.60 |
| Llama-3.2-1B | A1 | descr | 19 | 18 | +0.305 | 1.00 | 0.44 |
| Llama-3.2-1B | B | moral | 68 | 61 | +0.305 | 0.91 | 0.56 |
| Llama-3.2-1B | B | norm | 83 | 71 | +0.250 | 0.92 | 0.54 |
| Llama-3.2-1B | B | descr | 19 | 15 | +0.250 | 0.84 | 0.48 |
| Llama-3.2-1B-Instruct | A0 | moral | 68 | 60 | +0.201 | 0.90 | 0.26 |
| Llama-3.2-1B-Instruct | A0 | norm | 83 | 67 | +0.107 | 0.93 | 0.18 |
| Llama-3.2-1B-Instruct | A0 | descr | 19 | 12 | +0.046 | 0.89 | 0.07 |
| Llama-3.2-1B-Instruct | A1 | moral | 68 | 58 | +0.420 | 0.91 | 0.66 |
| Llama-3.2-1B-Instruct | A1 | norm | 83 | 74 | +0.292 | 0.92 | 0.52 |
| Llama-3.2-1B-Instruct | A1 | descr | 19 | 17 | +0.240 | 0.95 | 0.33 |
| Llama-3.2-1B-Instruct | B | moral | 68 | 61 | +0.619 | 0.91 | 0.60 |
| Llama-3.2-1B-Instruct | B | norm | 83 | 73 | +0.448 | 0.92 | 0.56 |
| Llama-3.2-1B-Instruct | B | descr | 19 | 16 | +0.369 | 0.89 | 0.39 |
| Llama-3.2-3B | A0 | moral | 68 | 66 | +0.440 | 0.97 | 0.58 |
| Llama-3.2-3B | A0 | norm | 83 | 67 | +0.219 | 0.88 | 0.43 |
| Llama-3.2-3B | A0 | descr | 19 | 9 | +0.056 | 0.79 | 0.11 |
| Llama-3.2-3B | A1 | moral | 68 | 67 | +0.696 | 0.99 | 0.62 |
| Llama-3.2-3B | A1 | norm | 83 | 81 | +0.561 | 0.99 | 0.56 |
| Llama-3.2-3B | A1 | descr | 19 | 19 | +0.369 | 1.00 | 0.38 |
| Llama-3.2-3B | B | moral | 68 | 66 | +0.501 | 0.97 | 0.42 |
| Llama-3.2-3B | B | norm | 83 | 77 | +0.493 | 0.95 | 0.52 |
| Llama-3.2-3B | B | descr | 19 | 19 | +0.482 | 1.00 | 0.47 |
| Llama-3.2-3B-Instruct | A0 | moral | 68 | 65 | +0.387 | 0.97 | 0.32 |
| Llama-3.2-3B-Instruct | A0 | norm | 83 | 73 | +0.156 | 0.94 | 0.19 |
| Llama-3.2-3B-Instruct | A0 | descr | 19 | 14 | +0.052 | 0.95 | 0.09 |
| Llama-3.2-3B-Instruct | A1 | moral | 68 | 60 | +0.966 | 0.90 | 0.75 |
| Llama-3.2-3B-Instruct | A1 | norm | 83 | 80 | +0.840 | 0.98 | 0.63 |
| Llama-3.2-3B-Instruct | A1 | descr | 19 | 18 | +0.601 | 1.00 | 0.47 |
| Llama-3.2-3B-Instruct | B | moral | 68 | 57 | +0.730 | 0.84 | 0.56 |
| Llama-3.2-3B-Instruct | B | norm | 83 | 80 | +0.759 | 0.96 | 0.57 |
| Llama-3.2-3B-Instruct | B | descr | 19 | 18 | +0.654 | 1.00 | 0.45 |
| Qwen2.5-14B | A0 | moral | 68 | 68 | +0.741 | 1.00 | 0.69 |
| Qwen2.5-14B | A0 | norm | 83 | 78 | +0.372 | 0.96 | 0.62 |
| Qwen2.5-14B | A0 | descr | 19 | 13 | +0.051 | 0.89 | 0.11 |
| Qwen2.5-14B | A1 | moral | 68 | 67 | +1.332 | 0.99 | 0.80 |
| Qwen2.5-14B | A1 | norm | 83 | 78 | +0.744 | 0.96 | 0.52 |
| Qwen2.5-14B | A1 | descr | 19 | 17 | +0.187 | 1.00 | 0.15 |
| Qwen2.5-14B | B | moral | 68 | 67 | +1.246 | 0.99 | 0.77 |
| Qwen2.5-14B | B | norm | 83 | 82 | +1.052 | 0.99 | 0.68 |
| Qwen2.5-14B | B | descr | 19 | 19 | +0.967 | 1.00 | 0.60 |
| Qwen2.5-14B-Instruct | A0 | moral | 68 | 68 | +0.757 | 1.00 | 0.76 |
| Qwen2.5-14B-Instruct | A0 | norm | 83 | 74 | +0.486 | 0.92 | 0.70 |
| Qwen2.5-14B-Instruct | A0 | descr | 19 | 13 | +0.074 | 0.89 | 0.14 |
| Qwen2.5-14B-Instruct | A1 | moral | 68 | 67 | +1.475 | 1.00 | 0.84 |
| Qwen2.5-14B-Instruct | A1 | norm | 83 | 77 | +0.767 | 0.98 | 0.45 |
| Qwen2.5-14B-Instruct | A1 | descr | 19 | 12 | +0.180 | 0.95 | 0.11 |
| Qwen2.5-14B-Instruct | B | moral | 68 | 66 | +1.296 | 0.97 | 0.72 |
| Qwen2.5-14B-Instruct | B | norm | 83 | 80 | +1.029 | 0.98 | 0.60 |
| Qwen2.5-14B-Instruct | B | descr | 19 | 19 | +1.086 | 1.00 | 0.57 |
| Qwen2.5-3B | A0 | moral | 68 | 45 | +0.254 | 0.66 | 0.55 |
| Qwen2.5-3B | A0 | norm | 83 | 63 | +0.227 | 0.77 | 0.52 |
| Qwen2.5-3B | A0 | descr | 19 | 2 | +0.004 | 0.53 | 0.08 |
| Qwen2.5-3B | A1 | moral | 68 | 66 | +0.440 | 0.97 | 0.75 |
| Qwen2.5-3B | A1 | norm | 83 | 78 | +0.280 | 0.95 | 0.66 |
| Qwen2.5-3B | A1 | descr | 19 | 18 | +0.268 | 1.00 | 0.50 |
| Qwen2.5-3B | B | moral | 68 | 63 | +0.472 | 0.94 | 0.63 |
| Qwen2.5-3B | B | norm | 83 | 79 | +0.413 | 0.95 | 0.50 |
| Qwen2.5-3B | B | descr | 19 | 19 | +0.430 | 1.00 | 0.49 |
| Qwen2.5-3B-Instruct | A0 | moral | 68 | 66 | +0.583 | 0.99 | 0.71 |
| Qwen2.5-3B-Instruct | A0 | norm | 83 | 78 | +0.363 | 0.96 | 0.57 |
| Qwen2.5-3B-Instruct | A0 | descr | 19 | 16 | +0.091 | 0.95 | 0.17 |
| Qwen2.5-3B-Instruct | A1 | moral | 68 | 65 | +0.990 | 0.99 | 0.79 |
| Qwen2.5-3B-Instruct | A1 | norm | 83 | 80 | +0.928 | 0.96 | 0.69 |
| Qwen2.5-3B-Instruct | A1 | descr | 19 | 19 | +0.615 | 1.00 | 0.47 |
| Qwen2.5-3B-Instruct | B | moral | 68 | 65 | +1.004 | 0.97 | 0.69 |
| Qwen2.5-3B-Instruct | B | norm | 83 | 81 | +0.864 | 0.98 | 0.56 |
| Qwen2.5-3B-Instruct | B | descr | 19 | 19 | +0.721 | 1.00 | 0.50 |
| Qwen2.5-7B | A0 | moral | 68 | 67 | +0.624 | 0.99 | 0.62 |
| Qwen2.5-7B | A0 | norm | 83 | 75 | +0.323 | 0.93 | 0.48 |
| Qwen2.5-7B | A0 | descr | 19 | 13 | +0.062 | 0.89 | 0.13 |
| Qwen2.5-7B | A1 | moral | 68 | 67 | +1.095 | 0.99 | 0.80 |
| Qwen2.5-7B | A1 | norm | 83 | 81 | +0.873 | 0.99 | 0.68 |
| Qwen2.5-7B | A1 | descr | 19 | 19 | +0.480 | 1.00 | 0.49 |
| Qwen2.5-7B | B | moral | 68 | 66 | +1.035 | 0.97 | 0.78 |
| Qwen2.5-7B | B | norm | 83 | 83 | +1.046 | 1.00 | 0.74 |
| Qwen2.5-7B | B | descr | 19 | 19 | +0.967 | 1.00 | 0.70 |
| Qwen2.5-7B-Instruct | A0 | moral | 68 | 66 | +0.597 | 0.97 | 0.62 |
| Qwen2.5-7B-Instruct | A0 | norm | 83 | 71 | +0.308 | 0.86 | 0.51 |
| Qwen2.5-7B-Instruct | A0 | descr | 19 | 13 | +0.108 | 0.89 | 0.14 |
| Qwen2.5-7B-Instruct | A1 | moral | 68 | 63 | +1.116 | 0.94 | 0.78 |
| Qwen2.5-7B-Instruct | A1 | norm | 83 | 83 | +0.950 | 1.00 | 0.69 |
| Qwen2.5-7B-Instruct | A1 | descr | 19 | 19 | +0.664 | 1.00 | 0.46 |
| Qwen2.5-7B-Instruct | B | moral | 68 | 65 | +1.197 | 0.96 | 0.79 |
| Qwen2.5-7B-Instruct | B | norm | 83 | 80 | +1.128 | 0.96 | 0.73 |
| Qwen2.5-7B-Instruct | B | descr | 19 | 19 | +1.188 | 1.00 | 0.68 |
| gemma-2b | A0 | moral | 68 | 63 | +0.396 | 0.93 | 0.58 |
| gemma-2b | A0 | norm | 83 | 72 | +0.271 | 0.89 | 0.43 |
| gemma-2b | A0 | descr | 19 | 16 | +0.090 | 0.95 | 0.13 |
| gemma-2b | A1 | moral | 68 | 63 | +0.585 | 0.96 | 0.52 |
| gemma-2b | A1 | norm | 83 | 78 | +0.466 | 0.95 | 0.46 |
| gemma-2b | A1 | descr | 19 | 18 | +0.375 | 0.95 | 0.42 |
| gemma-2b | B | moral | 68 | 60 | +0.472 | 0.91 | 0.46 |
| gemma-2b | B | norm | 83 | 74 | +0.432 | 0.95 | 0.44 |
| gemma-2b | B | descr | 19 | 19 | +0.423 | 1.00 | 0.48 |
| gemma-2b-it | A0 | moral | 68 | 61 | +0.455 | 0.93 | 0.59 |
| gemma-2b-it | A0 | norm | 83 | 70 | +0.380 | 0.88 | 0.43 |
| gemma-2b-it | A0 | descr | 19 | 9 | +0.075 | 0.84 | 0.09 |
| gemma-2b-it | A1 | moral | 68 | 62 | +0.942 | 0.94 | 0.92 |
| gemma-2b-it | A1 | norm | 83 | 77 | +0.804 | 0.94 | 0.85 |
| gemma-2b-it | A1 | descr | 19 | 17 | +0.567 | 0.89 | 0.60 |
| gemma-2b-it | B | moral | 68 | 56 | +0.521 | 0.82 | 0.49 |
| gemma-2b-it | B | norm | 83 | 68 | +0.357 | 0.84 | 0.39 |
| gemma-2b-it | B | descr | 19 | 17 | +0.459 | 0.89 | 0.47 |
