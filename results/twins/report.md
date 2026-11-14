# Twin test: the same scenario and edit, moral member against its prudential/epistemic twin (exploratory)

23 complete twins.

* Llama-3.1-8B, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.546 vs twin 0.485 (paired +0.061 [-0.000, +0.126])
    selA_all: relative fall moral +1.1% vs twin +0.8%; paired +1.4% [-0.1, +3.5] -> not specific
    selB_all: relative fall moral +0.5% vs twin +0.0%; paired +0.6% [-1.0, +2.4] -> not specific
* Llama-3.1-8B, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.628 vs twin 0.535 (paired +0.092 [+0.030, +0.155])
    selA_all: relative fall moral -2.8% vs twin -2.2%; paired -0.5% [-2.2, +1.1] -> not specific
    selB_all: relative fall moral -0.1% vs twin +1.2%; paired -1.3% [-2.3, -0.2] -> MORAL-SPECIFIC across twins
* Llama-3.1-8B-Instruct, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.868 vs twin 0.719 (paired +0.149 [+0.079, +0.221])
    selA_all: relative fall moral -2.4% vs twin -2.2%; paired -0.2% [-1.1, +0.9] -> not specific
    selB_all: relative fall moral -1.4% vs twin -1.0%; paired -0.3% [-1.2, +0.6] -> not specific
* Llama-3.1-8B-Instruct, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.792 vs twin 0.736 (paired +0.056 [-0.014, +0.132])
    selA_all: relative fall moral -1.9% vs twin -0.2%; paired -1.8% [-3.9, -0.2] -> MORAL-SPECIFIC across twins
    selB_all: relative fall moral +0.2% vs twin +2.6%; paired -2.3% [-3.6, -1.1] -> MORAL-SPECIFIC across twins
* Llama-3.2-1B, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.443 vs twin 0.394 (paired +0.049 [+0.008, +0.086])
    selA_all: relative fall moral +0.3% vs twin -0.1%; paired +0.4% [-0.9, +1.8] -> not specific
    selB_all: relative fall moral +3.4% vs twin +3.1%; paired +0.4% [-0.8, +1.5] -> not specific
* Llama-3.2-1B, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.295 vs twin 0.283 (paired +0.013 [-0.024, +0.052])
    selA_all: relative fall moral -3.9% vs twin -5.4%; paired -0.3% [-2.7, +2.4] -> not specific
    selB_all: relative fall moral -5.1% vs twin -6.2%; paired +0.8% [-2.6, +4.7] -> not specific
* Llama-3.2-1B-Instruct, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.332 vs twin 0.271 (paired +0.061 [+0.004, +0.117])
    selA_all: relative fall moral -4.6% vs twin -5.2%; paired +0.7% [-1.0, +2.4] -> not specific
    selB_all: relative fall moral -4.0% vs twin -4.6%; paired +0.6% [-0.3, +1.7] -> not specific
* Llama-3.2-1B-Instruct, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.634 vs twin 0.524 (paired +0.110 [+0.025, +0.192])
    selA_all: relative fall moral -0.2% vs twin +1.1%; paired -1.7% [-4.4, +1.1] -> not specific
    selB_all: relative fall moral -12.3% vs twin -11.6%; paired -0.3% [-4.7, +4.6] -> not specific
* Llama-3.2-3B, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.614 vs twin 0.590 (paired +0.024 [-0.062, +0.104])
    selA_all: relative fall moral +1.5% vs twin -1.0%; paired +2.5% [+1.0, +4.3] -> not specific
    selB_all: relative fall moral +2.4% vs twin +3.2%; paired -0.7% [-1.6, +0.1] -> not specific
* Llama-3.2-3B, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.537 vs twin 0.526 (paired +0.011 [-0.053, +0.072])
    selA_all: relative fall moral +0.7% vs twin +0.8%; paired -0.2% [-2.6, +2.1] -> not specific
    selB_all: relative fall moral -8.2% vs twin -8.0%; paired -0.2% [-2.1, +1.8] -> not specific
* Llama-3.2-3B-Instruct, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.761 vs twin 0.778 (paired -0.017 [-0.113, +0.078])
    selA_all: relative fall moral +2.2% vs twin -0.1%; paired +1.4% [-0.6, +3.8] -> not specific
    selB_all: relative fall moral -3.4% vs twin -2.9%; paired -0.6% [-2.6, +1.1] -> not specific
* Llama-3.2-3B-Instruct, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.668 vs twin 0.754 (paired -0.087 [-0.210, +0.024])
    selA_all: relative fall moral +17.8% vs twin +9.1%; paired +8.3% [-12.9, +35.9] -> not specific
    selB_all: relative fall moral +8.6% vs twin -4.2%; paired +12.3% [+2.8, +26.1] -> not specific
* Qwen2.5-14B, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 1.085 vs twin 0.936 (paired +0.148 [+0.044, +0.260])
    selA_all: relative fall moral +0.2% vs twin +0.5%; paired -0.3% [-1.3, +0.7] -> not specific
    selB_all: relative fall moral -0.8% vs twin +0.1%; paired -0.9% [-2.6, +0.6] -> not specific
* Qwen2.5-14B, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 1.181 vs twin 1.019 (paired +0.162 [+0.058, +0.282])
    selA_all: relative fall moral +1.2% vs twin +0.5%; paired +0.7% [-2.6, +4.7] -> not specific
    selB_all: relative fall moral -0.1% vs twin -1.1%; paired +1.1% [-0.7, +3.3] -> not specific
* Qwen2.5-14B-Instruct, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 1.208 vs twin 1.060 (paired +0.148 [+0.043, +0.253])
    selA_all: relative fall moral +0.5% vs twin -0.9%; paired +1.4% [-0.3, +3.4] -> not specific
    selB_all: relative fall moral -1.9% vs twin -4.5%; paired +2.5% [-0.4, +5.7] -> not specific
* Qwen2.5-14B-Instruct, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 1.189 vs twin 0.993 (paired +0.196 [+0.114, +0.287])
    selA_all: relative fall moral -3.9% vs twin +0.2%; paired -4.6% [-13.9, +1.0] -> not specific
    selB_all: relative fall moral +0.4% vs twin -0.2%; paired +0.8% [-2.0, +4.1] -> not specific
* Qwen2.5-3B, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.324 vs twin 0.361 (paired -0.037 [-0.084, +0.014])
    selA_all: relative fall moral -2.0% vs twin -2.5%; paired +0.4% [-1.1, +1.8] -> not specific
    selB_all: relative fall moral -5.8% vs twin -5.8%; paired +0.0% [-1.4, +1.3] -> not specific
* Qwen2.5-3B, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.408 vs twin 0.394 (paired +0.014 [-0.051, +0.077])
    selA_all: relative fall moral -5.3% vs twin -5.8%; paired +0.7% [-2.7, +4.2] -> not specific
    selB_all: relative fall moral -8.0% vs twin -8.5%; paired +0.9% [-1.6, +3.4] -> not specific
* Qwen2.5-3B-Instruct, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.844 vs twin 0.833 (paired +0.012 [-0.096, +0.118])
    selA_all: relative fall moral -2.8% vs twin -2.1%; paired -0.7% [-2.0, +0.5] -> not specific
    selB_all: relative fall moral -1.9% vs twin -1.9%; paired -0.1% [-1.0, +1.0] -> not specific
* Qwen2.5-3B-Instruct, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.935 vs twin 0.848 (paired +0.087 [-0.018, +0.189])
    selA_all: relative fall moral -2.9% vs twin -3.1%; paired +0.2% [-1.5, +2.2] -> not specific
    selB_all: relative fall moral -1.6% vs twin -2.1%; paired +0.5% [-1.6, +3.1] -> not specific
* Qwen2.5-7B, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.917 vs twin 0.750 (paired +0.167 [+0.070, +0.264])
    selA_all: relative fall moral -4.8% vs twin -4.8%; paired +0.0% [-1.7, +1.7] -> not specific
    selB_all: relative fall moral +0.5% vs twin +0.6%; paired -0.1% [-1.5, +1.2] -> not specific
* Qwen2.5-7B, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 1.030 vs twin 0.914 (paired +0.116 [-0.008, +0.243])
    selA_all: relative fall moral +1.1% vs twin +1.1%; paired -0.5% [-3.1, +1.9] -> not specific
    selB_all: relative fall moral -0.3% vs twin -0.6%; paired -0.3% [-1.3, +0.6] -> not specific
* Qwen2.5-7B-Instruct, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 1.053 vs twin 0.787 (paired +0.265 [+0.084, +0.451])
    selA_all: relative fall moral -8.5% vs twin -10.4%; paired +2.5% [-0.5, +5.6] -> not specific
    selB_all: relative fall moral -4.8% vs twin -3.6%; paired -0.7% [-2.4, +1.0] -> not specific
* Qwen2.5-7B-Instruct, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 1.207 vs twin 1.113 (paired +0.094 [-0.083, +0.267])
    selA_all: relative fall moral -2.5% vs twin -4.6%; paired +2.0% [-5.9, +13.4] -> not specific
    selB_all: relative fall moral -2.1% vs twin -1.1%; paired -1.0% [-3.5, +1.5] -> not specific
* gemma-2b, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.405 vs twin 0.426 (paired -0.021 [-0.120, +0.076])
    selA_all: relative fall moral -6.3% vs twin -5.7%; paired -0.6% [-2.4, +1.2] -> not specific
    selB_all: relative fall moral +1.5% vs twin +0.7%; paired +0.8% [-0.0, +1.7] -> not specific
* gemma-2b, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.354 vs twin 0.342 (paired +0.012 [-0.052, +0.074])
    selA_all: relative fall moral +5.4% vs twin -0.3%; paired +7.3% [-1.6, +18.8] -> not specific
    selB_all: relative fall moral +6.8% vs twin +6.8%; paired +2.6% [-3.4, +9.7] -> not specific
* gemma-2b-it, units_ablation_mvn_followup_twins, A1: 23 twins; clean gap moral 0.984 vs twin 0.955 (paired +0.029 [-0.132, +0.201])
    selA_all: relative fall moral -1.4% vs twin -9.6%; paired +8.2% [-1.4, +26.3] -> not specific
    selB_all: relative fall moral -1.4% vs twin -14.0%; paired +12.5% [-2.4, +41.4] -> not specific
* gemma-2b-it, units_ablation_mvn_followup_twins, B: 23 twins; clean gap moral 0.462 vs twin 0.402 (paired +0.060 [-0.011, +0.139])
    selA_all: relative fall moral +5.1% vs twin +0.7%; paired +3.3% [-1.0, +7.6] -> not specific
    selB_all: relative fall moral -0.5% vs twin +0.3%; paired -0.3% [-3.7, +2.7] -> not specific
* Llama-3.1-8B, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.546 vs twin 0.485 (paired +0.061 [-0.001, +0.126])
    selA_all: relative fall moral -12.1% vs twin -12.4%; paired +0.6% [-0.9, +2.1] -> not specific
    selB_all: relative fall moral -14.6% vs twin -16.1%; paired +1.2% [-1.7, +4.0] -> not specific
* Llama-3.1-8B, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.628 vs twin 0.535 (paired +0.092 [+0.033, +0.153])
    selA_all: relative fall moral +15.1% vs twin +10.5%; paired +4.5% [-1.5, +10.9] -> not specific
    selB_all: relative fall moral +14.2% vs twin +14.8%; paired -0.6% [-7.4, +7.1] -> not specific
* Llama-3.1-8B-Instruct, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.868 vs twin 0.719 (paired +0.149 [+0.078, +0.219])
    selA_all: relative fall moral -5.4% vs twin -6.0%; paired +0.5% [-1.7, +2.7] -> not specific
    selB_all: relative fall moral -0.5% vs twin -1.3%; paired +0.8% [-0.9, +2.2] -> not specific
* Llama-3.1-8B-Instruct, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.792 vs twin 0.736 (paired +0.056 [-0.014, +0.131])
    selA_all: relative fall moral +23.2% vs twin +18.1%; paired +5.0% [-13.0, +32.5] -> not specific
    selB_all: relative fall moral +22.1% vs twin +18.9%; paired +3.2% [-11.5, +24.0] -> not specific
* Llama-3.2-1B, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.443 vs twin 0.394 (paired +0.049 [+0.009, +0.088])
    selA_all: relative fall moral -4.6% vs twin -5.0%; paired +0.4% [-1.5, +2.8] -> not specific
    selB_all: relative fall moral -4.3% vs twin -5.3%; paired +1.0% [-0.9, +3.3] -> not specific
* Llama-3.2-1B, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.295 vs twin 0.283 (paired +0.013 [-0.026, +0.053])
    selA_all: relative fall moral -21.0% vs twin -24.2%; paired +3.4% [-9.2, +23.1] -> not specific
    selB_all: relative fall moral -9.0% vs twin -10.8%; paired +2.5% [-5.8, +11.1] -> not specific
* Llama-3.2-1B-Instruct, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.332 vs twin 0.271 (paired +0.061 [+0.003, +0.118])
    selA_all: relative fall moral -18.0% vs twin -22.7%; paired +3.4% [+0.5, +6.5] -> not specific
    selB_all: relative fall moral -6.8% vs twin -6.8%; paired -1.3% [-5.6, +2.7] -> not specific
* Llama-3.2-1B-Instruct, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.634 vs twin 0.524 (paired +0.110 [+0.025, +0.189])
    selA_all: relative fall moral -18.4% vs twin -28.6%; paired +10.1% [+5.0, +15.0] -> not specific
    selB_all: relative fall moral -11.9% vs twin -15.0%; paired +3.4% [-6.5, +11.6] -> not specific
* Llama-3.2-3B, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.614 vs twin 0.590 (paired +0.024 [-0.060, +0.104])
    selA_all: relative fall moral -11.5% vs twin -11.6%; paired +0.1% [-2.9, +3.5] -> not specific
    selB_all: relative fall moral -2.2% vs twin -4.6%; paired +2.4% [-1.6, +7.0] -> not specific
* Llama-3.2-3B, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.537 vs twin 0.526 (paired +0.011 [-0.053, +0.072])
    selA_all: relative fall moral -11.4% vs twin -7.3%; paired -4.2% [-10.0, +0.9] -> not specific
    selB_all: relative fall moral -8.7% vs twin -5.5%; paired -3.1% [-9.4, +2.9] -> not specific
* Llama-3.2-3B-Instruct, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.761 vs twin 0.778 (paired -0.017 [-0.110, +0.077])
    selA_all: relative fall moral -16.2% vs twin -22.2%; paired +5.2% [-2.2, +13.4] -> not specific
    selB_all: relative fall moral -16.4% vs twin -18.6%; paired +1.8% [-3.4, +7.0] -> not specific
* Llama-3.2-3B-Instruct, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.668 vs twin 0.754 (paired -0.087 [-0.210, +0.032])
    selA_all: relative fall moral -4.2% vs twin -1.2%; paired -2.7% [-29.8, +20.6] -> not specific
    selB_all: relative fall moral +3.3% vs twin +6.6%; paired +7.9% [-4.0, +27.0] -> not specific
* Qwen2.5-14B, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 1.085 vs twin 0.936 (paired +0.148 [+0.045, +0.254])
    selA_all: relative fall moral -4.1% vs twin -6.8%; paired +2.8% [-1.5, +6.7] -> not specific
    selB_all: relative fall moral +9.1% vs twin +10.3%; paired -1.3% [-5.4, +2.6] -> not specific
* Qwen2.5-14B, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 1.181 vs twin 1.019 (paired +0.162 [+0.055, +0.282])
    selA_all: relative fall moral +10.0% vs twin +14.4%; paired -4.3% [-22.0, +8.7] -> not specific
    selB_all: relative fall moral -11.4% vs twin +11.3%; paired -22.7% [-69.2, +3.8] -> not specific
* Qwen2.5-14B-Instruct, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 1.208 vs twin 1.060 (paired +0.148 [+0.040, +0.253])
    selA_all: relative fall moral -2.9% vs twin -4.0%; paired +1.1% [-2.7, +4.7] -> not specific
    selB_all: relative fall moral -0.1% vs twin -1.3%; paired +1.3% [-2.1, +4.1] -> not specific
* Qwen2.5-14B-Instruct, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 1.189 vs twin 0.993 (paired +0.196 [+0.114, +0.288])
    selA_all: relative fall moral +3.8% vs twin -1.6%; paired +3.1% [-3.5, +9.5] -> not specific
    selB_all: relative fall moral -5.1% vs twin -11.1%; paired +2.4% [-4.4, +9.7] -> not specific
* Qwen2.5-3B, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.324 vs twin 0.361 (paired -0.037 [-0.084, +0.017])
    selA_all: relative fall moral -4.2% vs twin -6.9%; paired +2.7% [+0.8, +4.9] -> not specific
    selB_all: relative fall moral -2.9% vs twin -4.6%; paired +1.7% [-1.2, +5.4] -> not specific
* Qwen2.5-3B, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.408 vs twin 0.394 (paired +0.014 [-0.049, +0.078])
    selA_all: relative fall moral -19.2% vs twin -23.7%; paired +5.4% [-1.1, +14.0] -> not specific
    selB_all: relative fall moral -1.7% vs twin -4.6%; paired +5.6% [-5.5, +15.2] -> not specific
* Qwen2.5-3B-Instruct, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.844 vs twin 0.833 (paired +0.012 [-0.096, +0.116])
    selA_all: relative fall moral -3.7% vs twin -4.3%; paired +0.6% [-2.0, +3.8] -> not specific
    selB_all: relative fall moral +1.1% vs twin -0.7%; paired +1.7% [-0.9, +5.0] -> not specific
* Qwen2.5-3B-Instruct, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.935 vs twin 0.848 (paired +0.087 [-0.019, +0.191])
    selA_all: relative fall moral +0.1% vs twin -5.1%; paired +5.5% [-9.9, +19.7] -> not specific
    selB_all: relative fall moral +0.2% vs twin -2.9%; paired +4.1% [-3.5, +13.5] -> not specific
* Qwen2.5-7B, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.917 vs twin 0.750 (paired +0.167 [+0.072, +0.267])
    selA_all: relative fall moral +3.4% vs twin +3.9%; paired -0.5% [-9.3, +5.6] -> not specific
    selB_all: relative fall moral +2.9% vs twin +6.8%; paired -3.9% [-8.1, -0.1] -> MORAL-SPECIFIC across twins
* Qwen2.5-7B, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 1.030 vs twin 0.914 (paired +0.116 [-0.008, +0.248])
    selA_all: relative fall moral +15.3% vs twin +15.4%; paired +1.3% [-6.6, +9.6] -> not specific
    selB_all: relative fall moral +23.9% vs twin +25.4%; paired -1.1% [-9.5, +7.1] -> not specific
* Qwen2.5-7B-Instruct, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 1.053 vs twin 0.787 (paired +0.265 [+0.090, +0.449])
    selA_all: relative fall moral -7.8% vs twin -13.4%; paired +3.6% [-0.2, +7.4] -> not specific
    selB_all: relative fall moral -8.9% vs twin -12.9%; paired +2.5% [-0.3, +5.3] -> not specific
* Qwen2.5-7B-Instruct, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 1.207 vs twin 1.113 (paired +0.094 [-0.077, +0.264])
    selA_all: relative fall moral +19.9% vs twin +19.4%; paired +0.5% [-12.4, +14.3] -> not specific
    selB_all: relative fall moral +29.3% vs twin +27.5%; paired +1.8% [-11.9, +17.5] -> not specific
* gemma-2b, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.405 vs twin 0.426 (paired -0.021 [-0.120, +0.077])
    selA_all: relative fall moral -8.7% vs twin -15.9%; paired +7.2% [+2.9, +12.3] -> not specific
    selB_all: relative fall moral -4.6% vs twin -14.8%; paired +10.2% [+2.2, +21.7] -> not specific
* gemma-2b, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.354 vs twin 0.342 (paired +0.012 [-0.055, +0.071])
    selA_all: relative fall moral -12.4% vs twin -23.1%; paired +9.6% [+0.8, +19.8] -> not specific
    selB_all: relative fall moral -14.2% vs twin -19.8%; paired +5.2% [-1.0, +11.7] -> not specific
* gemma-2b-it, units_ablation_stance_followup_twins, A1: 23 twins; clean gap moral 0.984 vs twin 0.955 (paired +0.029 [-0.145, +0.198])
    selA_all: relative fall moral -12.7% vs twin +17.0%; paired -29.7% [-82.6, +0.3] -> not specific
    selB_all: relative fall moral +3.7% vs twin +32.7%; paired -29.0% [-86.3, +0.4] -> not specific
* gemma-2b-it, units_ablation_stance_followup_twins, B: 23 twins; clean gap moral 0.462 vs twin 0.402 (paired +0.060 [-0.014, +0.139])
    selA_all: relative fall moral -41.0% vs twin -44.4%; paired +4.3% [-4.6, +13.7] -> not specific
    selB_all: relative fall moral -9.8% vs twin -11.6%; paired +0.5% [-6.5, +9.9] -> not specific
* Llama-3.2-1B, located head share, A1: moral 0.087 vs twin 0.084 (ratio 1.04); paired +0.0031 [-0.0016, +0.0081] -> not specific
* Llama-3.2-1B, located head share, B: moral 0.079 vs twin 0.086 (ratio 0.92); paired -0.0050 [-0.0103, +0.0001] -> not specific
* Llama-3.2-1B-Instruct, located head share, A1: moral 0.043 vs twin 0.039 (ratio 1.10); paired +0.0037 [-0.0010, +0.0082] -> not specific
* Llama-3.2-1B-Instruct, located head share, B: moral 0.035 vs twin 0.034 (ratio 1.03); paired +0.0006 [-0.0042, +0.0058] -> not specific
* Llama-3.2-3B, located head share, A1: moral 0.182 vs twin 0.170 (ratio 1.07); paired +0.0116 [-0.0092, +0.0325] -> not specific
* Llama-3.2-3B, located head share, B: moral 0.106 vs twin 0.114 (ratio 0.93); paired -0.0080 [-0.0248, +0.0080] -> not specific
* Llama-3.2-3B-Instruct, located head share, A1: moral 0.139 vs twin 0.142 (ratio 0.98); paired +0.0005 [-0.0156, +0.0175] -> not specific
* Llama-3.2-3B-Instruct, located head share, B: moral 0.067 vs twin 0.074 (ratio 0.91); paired -0.0094 [-0.0201, +0.0016] -> not specific
* Qwen2.5-3B, located head share, A1: moral 0.069 vs twin 0.073 (ratio 0.94); paired -0.0040 [-0.0148, +0.0056] -> not specific
* Qwen2.5-3B, located head share, B: moral 0.072 vs twin 0.064 (ratio 1.13); paired +0.0081 [-0.0016, +0.0177] -> not specific
* Qwen2.5-3B-Instruct, located head share, A1: moral 0.150 vs twin 0.155 (ratio 0.97); paired -0.0053 [-0.0315, +0.0188] -> not specific
* Qwen2.5-3B-Instruct, located head share, B: moral 0.112 vs twin 0.118 (ratio 0.94); paired -0.0088 [-0.0232, +0.0055] -> not specific
* gemma-2b, located head share, A1: moral 0.180 vs twin 0.161 (ratio 1.12); paired +0.0188 [+0.0039, +0.0339] -> MORAL-SPECIFIC across twins
* gemma-2b, located head share, B: moral 0.183 vs twin 0.158 (ratio 1.16); paired +0.0267 [+0.0157, +0.0384] -> MORAL-SPECIFIC across twins
* gemma-2b-it, located head share, A1: moral 0.149 vs twin 0.143 (ratio 1.04); paired +0.0061 [-0.0033, +0.0151] -> not specific
* gemma-2b-it, located head share, B: moral 0.180 vs twin 0.171 (ratio 1.05); paired +0.0084 [-0.0150, +0.0318] -> not specific
