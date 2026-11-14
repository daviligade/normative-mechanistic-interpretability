# The choice frame: what the models answer

LD = logit(A) - logit(B). Gap of a pair = LD(prompt whose expected answer is A) - LD(prompt whose expected answer is B).
Choice (CH): the expected answer is the better version. Control (CW): the expected answer is the option that holds the word, which is the worse version. A pair is included in the removal analysis when its gap is at least 0.1.

## CH: choice

### All pairs

| model | pairs | probability on A and B | answers A | gap above 0 | gap at least 0.1 | expected label in both orders | median gap |
|---|---|---|---|---|---|---|---|
| Llama-3.2-1B | 227 | 0.96 | 36 % | 83 % | 69 % | 41 % | +0.24 |
| Llama-3.2-1B-Instruct | 227 | 0.99 | 51 % | 90 % | 89 % | 68 % | +1.48 |
| gemma-2b | 227 | 0.93 | 84 % | 88 % | 81 % | 31 % | +0.60 |
| gemma-2b-it | 227 | 0.99 | 48 % | 89 % | 89 % | 67 % | +6.35 |
| Llama-3.2-3B | 227 | 0.97 | 48 % | 94 % | 91 % | 73 % | +0.79 |
| Llama-3.2-3B-Instruct | 227 | 0.99 | 39 % | 98 % | 98 % | 77 % | +5.03 |
| Qwen2.5-3B | 227 | 1.00 | 33 % | 83 % | 81 % | 44 % | +0.98 |
| Qwen2.5-3B-Instruct | 227 | 1.00 | 30 % | 93 % | 93 % | 58 % | +4.93 |
| Qwen2.5-7B | 227 | 0.99 | 45 % | 87 % | 86 % | 78 % | +3.20 |
| Qwen2.5-7B-Instruct | 227 | 0.99 | 41 % | 74 % | 74 % | 58 % | +6.43 |
| Llama-3.1-8B | 227 | 0.97 | 60 % | 90 % | 85 % | 66 % | +0.68 |
| Llama-3.1-8B-Instruct | 227 | 0.98 | 50 % | 99 % | 98 % | 95 % | +3.31 |
| Qwen2.5-14B | 227 | 0.99 | 44 % | 98 % | 98 % | 88 % | +4.39 |
| Qwen2.5-14B-Instruct | 227 | 1.00 | 48 % | 99 % | 99 % | 96 % | +19.39 |

Median over the 14 models: gap above 0 in 90 % of the pairs, expected label in both orders in 68 %, probability on the two labels 0.99; gap above 0 in more than half of the pairs in 14 of 14 models.

### By kind of pair (share of pairs with a gap above 0; median gap)

| model | moral | normative | descriptive |
|---|---|---|---|
| Llama-3.2-1B | 86 % (+0.38; n = 80) | 79 % (+0.21; n = 107) | 85 % (+0.15; n = 40) |
| Llama-3.2-1B-Instruct | 95 % (+2.50; n = 80) | 95 % (+1.44; n = 107) | 68 % (+0.59; n = 40) |
| gemma-2b | 92 % (+0.84; n = 80) | 89 % (+0.69; n = 107) | 78 % (+0.17; n = 40) |
| gemma-2b-it | 96 % (+7.58; n = 80) | 92 % (+7.66; n = 107) | 70 % (+2.29; n = 40) |
| Llama-3.2-3B | 96 % (+1.12; n = 80) | 93 % (+0.71; n = 107) | 95 % (+0.56; n = 40) |
| Llama-3.2-3B-Instruct | 100 % (+7.97; n = 80) | 100 % (+5.18; n = 107) | 88 % (+1.67; n = 40) |
| Qwen2.5-3B | 82 % (+0.94; n = 80) | 96 % (+1.38; n = 107) | 50 % (+0.00; n = 40) |
| Qwen2.5-3B-Instruct | 91 % (+4.83; n = 80) | 97 % (+5.64; n = 107) | 85 % (+2.05; n = 40) |
| Qwen2.5-7B | 82 % (+3.76; n = 80) | 98 % (+4.04; n = 107) | 68 % (+0.46; n = 40) |
| Qwen2.5-7B-Instruct | 76 % (+8.10; n = 80) | 89 % (+8.25; n = 107) | 28 % (-3.42; n = 40) |
| Llama-3.1-8B | 90 % (+0.83; n = 80) | 87 % (+0.66; n = 107) | 98 % (+0.55; n = 40) |
| Llama-3.1-8B-Instruct | 99 % (+4.02; n = 80) | 100 % (+3.31; n = 107) | 98 % (+1.44; n = 40) |
| Qwen2.5-14B | 98 % (+4.75; n = 80) | 100 % (+5.02; n = 107) | 92 % (+1.81; n = 40) |
| Qwen2.5-14B-Instruct | 100 % (+20.81; n = 80) | 100 % (+19.68; n = 107) | 95 % (+10.11; n = 40) |

## CW: control (word)

### All pairs

| model | pairs | probability on A and B | answers A | gap above 0 | gap at least 0.1 | expected label in both orders | median gap |
|---|---|---|---|---|---|---|---|
| Llama-3.2-1B | 227 | 0.96 | 50 % | 100 % | 99 % | 99 % | +5.10 |
| Llama-3.2-1B-Instruct | 227 | 0.99 | 50 % | 100 % | 100 % | 99 % | +7.61 |
| gemma-2b | 227 | 0.95 | 50 % | 99 % | 99 % | 99 % | +6.40 |
| gemma-2b-it | 227 | 1.00 | 50 % | 99 % | 99 % | 98 % | +21.13 |
| Llama-3.2-3B | 227 | 0.99 | 50 % | 99 % | 99 % | 98 % | +5.95 |
| Llama-3.2-3B-Instruct | 227 | 1.00 | 50 % | 99 % | 99 % | 99 % | +13.29 |
| Qwen2.5-3B | 227 | 1.00 | 50 % | 100 % | 100 % | 99 % | +6.21 |
| Qwen2.5-3B-Instruct | 227 | 1.00 | 50 % | 100 % | 100 % | 99 % | +13.38 |
| Qwen2.5-7B | 227 | 0.96 | 50 % | 100 % | 100 % | 99 % | +9.26 |
| Qwen2.5-7B-Instruct | 227 | 0.90 | 50 % | 100 % | 100 % | 100 % | +19.64 |
| Llama-3.1-8B | 227 | 0.98 | 51 % | 99 % | 99 % | 99 % | +6.46 |
| Llama-3.1-8B-Instruct | 227 | 1.00 | 50 % | 100 % | 100 % | 99 % | +10.61 |
| Qwen2.5-14B | 227 | 0.99 | 50 % | 100 % | 100 % | 100 % | +10.85 |
| Qwen2.5-14B-Instruct | 227 | 1.00 | 50 % | 100 % | 100 % | 100 % | +19.88 |

Median over the 14 models: gap above 0 in 100 % of the pairs, expected label in both orders in 99 %, probability on the two labels 0.99; gap above 0 in more than half of the pairs in 14 of 14 models.

### By kind of pair (share of pairs with a gap above 0; median gap)

| model | moral | normative | descriptive |
|---|---|---|---|
| Llama-3.2-1B | 100 % (+5.22; n = 80) | 99 % (+5.08; n = 107) | 100 % (+4.81; n = 40) |
| Llama-3.2-1B-Instruct | 100 % (+6.98; n = 80) | 100 % (+7.57; n = 107) | 100 % (+8.01; n = 40) |
| gemma-2b | 99 % (+6.60; n = 80) | 99 % (+6.00; n = 107) | 100 % (+6.74; n = 40) |
| gemma-2b-it | 99 % (+21.79; n = 80) | 98 % (+20.73; n = 107) | 100 % (+20.85; n = 40) |
| Llama-3.2-3B | 99 % (+6.57; n = 80) | 98 % (+6.53; n = 107) | 100 % (+4.87; n = 40) |
| Llama-3.2-3B-Instruct | 99 % (+14.35; n = 80) | 98 % (+12.49; n = 107) | 100 % (+13.43; n = 40) |
| Qwen2.5-3B | 100 % (+6.33; n = 80) | 99 % (+5.75; n = 107) | 100 % (+6.14; n = 40) |
| Qwen2.5-3B-Instruct | 100 % (+13.14; n = 80) | 100 % (+13.35; n = 107) | 100 % (+13.89; n = 40) |
| Qwen2.5-7B | 100 % (+9.78; n = 80) | 99 % (+9.03; n = 107) | 100 % (+9.06; n = 40) |
| Qwen2.5-7B-Instruct | 100 % (+20.03; n = 80) | 99 % (+19.31; n = 107) | 100 % (+19.56; n = 40) |
| Llama-3.1-8B | 100 % (+6.69; n = 80) | 98 % (+6.45; n = 107) | 100 % (+6.38; n = 40) |
| Llama-3.1-8B-Instruct | 100 % (+10.79; n = 80) | 99 % (+10.43; n = 107) | 100 % (+10.58; n = 40) |
| Qwen2.5-14B | 100 % (+11.31; n = 80) | 99 % (+10.55; n = 107) | 100 % (+10.85; n = 40) |
| Qwen2.5-14B-Instruct | 100 % (+19.88; n = 80) | 100 % (+19.50; n = 107) | 100 % (+20.51; n = 40) |

