# Categorisation frame: behaviour (exploratory)

Items: the item file is the set of accepted pairs.

## Llama-3.1-8B

* fewshot: category words cover 10.7% of the distribution; P(moral set) moral 0.84, norm 0.10, descr 0.01; AUC moral vs norm 0.98; five-way argmax accuracy 0.89 (n=318, chance 0.20; mean rank of the true standard 1.14) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 147 7 2 0 4; prudential: 1 26 0 0 3; etiquette: 1 0 32 3 0; aesthetic: 2 0 0 39 3; epistemic: 7 2 0 0 39
* zeroshot: category words cover 4.6% of the distribution; P(moral set) moral 0.42, norm 0.05, descr 0.01; AUC moral vs norm 0.91; five-way argmax accuracy 0.69 (n=318, chance 0.20; mean rank of the true standard 1.44) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 107 31 3 10 9; prudential: 0 23 0 6 1; etiquette: 1 0 20 15 0; aesthetic: 0 0 0 43 1; epistemic: 11 2 0 9 26

## Llama-3.1-8B-Instruct

* fewshot: category words cover 11.4% of the distribution; P(moral set) moral 0.86, norm 0.08, descr 0.01; AUC moral vs norm 0.98; five-way argmax accuracy 0.89 (n=318, chance 0.20; mean rank of the true standard 1.13) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 146 6 2 0 6; prudential: 3 22 0 0 5; etiquette: 1 0 32 3 0; aesthetic: 0 0 0 44 0; epistemic: 7 1 0 0 40
* zeroshot: category words cover 3.2% of the distribution; P(moral set) moral 0.47, norm 0.06, descr 0.01; AUC moral vs norm 0.90; five-way argmax accuracy 0.72 (n=318, chance 0.20; mean rank of the true standard 1.41) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 114 27 2 9 8; prudential: 2 25 0 3 0; etiquette: 0 0 22 14 0; aesthetic: 0 2 0 41 1; epistemic: 14 2 0 6 26

## Llama-3.2-1B

* fewshot: category words cover 8.6% of the distribution; P(moral set) moral 0.70, norm 0.07, descr 0.03; AUC moral vs norm 0.97; five-way argmax accuracy 0.84 (n=318, chance 0.20; mean rank of the true standard 1.20) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 132 18 7 1 2; prudential: 1 26 2 1 0; etiquette: 0 0 27 9 0; aesthetic: 1 0 0 43 0; epistemic: 2 3 0 3 40
* zeroshot: category words cover 5.8% of the distribution; P(moral set) moral 0.33, norm 0.03, descr 0.00; AUC moral vs norm 0.93; five-way argmax accuracy 0.53 (n=318, chance 0.20; mean rank of the true standard 1.69) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 83 46 5 23 3; prudential: 1 18 0 9 2; etiquette: 1 0 11 24 0; aesthetic: 0 0 0 44 0; epistemic: 5 3 0 26 14

## Llama-3.2-1B-Instruct

* fewshot: category words cover 8.1% of the distribution; P(moral set) moral 0.81, norm 0.13, descr 0.09; AUC moral vs norm 0.95; five-way argmax accuracy 0.85 (n=318, chance 0.20; mean rank of the true standard 1.18) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 140 19 1 0 0; prudential: 1 28 1 0 0; etiquette: 3 0 28 5 0; aesthetic: 5 0 0 39 0; epistemic: 6 5 0 1 36
* zeroshot: category words cover 2.8% of the distribution; P(moral set) moral 0.46, norm 0.07, descr 0.03; AUC moral vs norm 0.91; five-way argmax accuracy 0.66 (n=318, chance 0.20; mean rank of the true standard 1.46) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 117 36 1 6 0; prudential: 3 18 0 8 1; etiquette: 2 2 11 21 0; aesthetic: 0 1 0 43 0; epistemic: 17 1 0 8 22

## Llama-3.2-3B

* fewshot: category words cover 8.6% of the distribution; P(moral set) moral 0.87, norm 0.13, descr 0.06; AUC moral vs norm 0.98; five-way argmax accuracy 0.90 (n=318, chance 0.20; mean rank of the true standard 1.13) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 152 5 2 0 1; prudential: 3 25 0 0 2; etiquette: 1 0 32 3 0; aesthetic: 2 0 0 42 0; epistemic: 11 2 0 0 35
* zeroshot: category words cover 4.6% of the distribution; P(moral set) moral 0.33, norm 0.04, descr 0.01; AUC moral vs norm 0.91; five-way argmax accuracy 0.60 (n=318, chance 0.20; mean rank of the true standard 1.62) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 92 38 3 19 8; prudential: 0 19 0 11 0; etiquette: 1 0 15 20 0; aesthetic: 0 0 0 42 2; epistemic: 10 2 0 14 22

## Llama-3.2-3B-Instruct

* fewshot: category words cover 8.9% of the distribution; P(moral set) moral 0.84, norm 0.10, descr 0.04; AUC moral vs norm 0.98; five-way argmax accuracy 0.87 (n=318, chance 0.20; mean rank of the true standard 1.16) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 150 9 1 0 0; prudential: 1 27 0 0 2; etiquette: 1 0 27 8 0; aesthetic: 2 0 0 42 0; epistemic: 11 4 0 1 32
* zeroshot: category words cover 3.0% of the distribution; P(moral set) moral 0.49, norm 0.06, descr 0.02; AUC moral vs norm 0.91; five-way argmax accuracy 0.71 (n=318, chance 0.20; mean rank of the true standard 1.38) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 117 30 1 7 5; prudential: 4 24 0 2 0; etiquette: 0 0 18 18 0; aesthetic: 0 0 0 44 0; epistemic: 17 1 0 6 24

## Qwen2.5-14B

* fewshot: category words cover 9.1% of the distribution; P(moral set) moral 0.76, norm 0.04, descr 0.02; AUC moral vs norm 0.99; five-way argmax accuracy 0.89 (n=318, chance 0.20; mean rank of the true standard 1.12) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 143 4 3 1 9; prudential: 1 22 0 1 6; etiquette: 0 0 30 6 0; aesthetic: 0 0 0 43 1; epistemic: 2 0 0 0 46
* zeroshot: category words cover 4.1% of the distribution; P(moral set) moral 0.45, norm 0.03, descr 0.01; AUC moral vs norm 0.95; five-way argmax accuracy 0.66 (n=318, chance 0.20; mean rank of the true standard 1.53) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 96 33 4 22 5; prudential: 0 20 1 7 2; etiquette: 0 0 23 13 0; aesthetic: 0 0 0 42 2; epistemic: 6 3 0 10 29

## Qwen2.5-14B-Instruct

* fewshot: category words cover 7.9% of the distribution; P(moral set) moral 0.80, norm 0.04, descr 0.02; AUC moral vs norm 0.98; five-way argmax accuracy 0.89 (n=318, chance 0.20; mean rank of the true standard 1.13) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 141 6 5 1 7; prudential: 0 25 0 0 5; etiquette: 0 0 34 2 0; aesthetic: 2 1 0 38 3; epistemic: 2 2 0 0 44
* zeroshot: category words cover 3.2% of the distribution; P(moral set) moral 0.59, norm 0.03, descr 0.00; AUC moral vs norm 0.96; five-way argmax accuracy 0.71 (n=318, chance 0.20; mean rank of the true standard 1.43) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 113 26 6 11 4; prudential: 0 22 0 7 1; etiquette: 0 0 24 12 0; aesthetic: 0 2 0 40 2; epistemic: 6 6 0 8 28

## Qwen2.5-3B

* fewshot: category words cover 10.7% of the distribution; P(moral set) moral 0.81, norm 0.09, descr 0.10; AUC moral vs norm 0.98; five-way argmax accuracy 0.92 (n=318, chance 0.20; mean rank of the true standard 1.11) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 143 10 1 0 6; prudential: 1 29 0 0 0; etiquette: 0 0 32 4 0; aesthetic: 0 0 1 42 1; epistemic: 3 0 0 0 45
* zeroshot: category words cover 2.8% of the distribution; P(moral set) moral 0.37, norm 0.06, descr 0.02; AUC moral vs norm 0.88; five-way argmax accuracy 0.63 (n=318, chance 0.20; mean rank of the true standard 1.65) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 105 20 6 11 18; prudential: 3 14 0 5 8; etiquette: 0 4 12 18 2; aesthetic: 0 1 2 39 2; epistemic: 10 3 0 4 31

## Qwen2.5-3B-Instruct

* fewshot: category words cover 13.1% of the distribution; P(moral set) moral 0.86, norm 0.11, descr 0.04; AUC moral vs norm 0.98; five-way argmax accuracy 0.88 (n=318, chance 0.20; mean rank of the true standard 1.15) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 149 9 0 0 2; prudential: 1 27 0 0 2; etiquette: 2 0 27 7 0; aesthetic: 2 0 1 39 2; epistemic: 7 2 0 1 38
* zeroshot: category words cover 5.3% of the distribution; P(moral set) moral 0.65, norm 0.07, descr 0.01; AUC moral vs norm 0.94; five-way argmax accuracy 0.74 (n=318, chance 0.20; mean rank of the true standard 1.37) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 123 27 2 3 5; prudential: 1 26 0 3 0; etiquette: 0 0 15 21 0; aesthetic: 0 0 0 44 0; epistemic: 15 2 0 4 27

## Qwen2.5-7B

* fewshot: category words cover 8.6% of the distribution; P(moral set) moral 0.71, norm 0.07, descr 0.02; AUC moral vs norm 0.96; five-way argmax accuracy 0.86 (n=318, chance 0.20; mean rank of the true standard 1.16) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 127 26 4 0 3; prudential: 1 28 0 0 1; etiquette: 0 0 34 2 0; aesthetic: 0 0 0 44 0; epistemic: 6 0 0 0 42
* zeroshot: category words cover 3.8% of the distribution; P(moral set) moral 0.32, norm 0.02, descr 0.00; AUC moral vs norm 0.94; five-way argmax accuracy 0.61 (n=318, chance 0.20; mean rank of the true standard 1.61) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 84 31 6 26 13; prudential: 0 20 0 6 4; etiquette: 0 0 18 18 0; aesthetic: 0 0 0 42 2; epistemic: 3 2 0 14 29

## Qwen2.5-7B-Instruct

* fewshot: category words cover 9.1% of the distribution; P(moral set) moral 0.76, norm 0.07, descr 0.02; AUC moral vs norm 0.96; five-way argmax accuracy 0.87 (n=318, chance 0.20; mean rank of the true standard 1.15) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 130 23 4 0 3; prudential: 0 29 0 0 1; etiquette: 0 0 34 2 0; aesthetic: 1 0 0 43 0; epistemic: 6 1 0 0 41
* zeroshot: category words cover 3.2% of the distribution; P(moral set) moral 0.42, norm 0.02, descr 0.00; AUC moral vs norm 0.95; five-way argmax accuracy 0.65 (n=318, chance 0.20; mean rank of the true standard 1.55) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 96 40 6 9 9; prudential: 1 25 0 4 0; etiquette: 0 0 19 17 0; aesthetic: 0 0 0 43 1; epistemic: 6 5 0 12 25

## gemma-2b

* fewshot: category words cover 9.1% of the distribution; P(moral set) moral 0.70, norm 0.05, descr 0.02; AUC moral vs norm 0.96; five-way argmax accuracy 0.86 (n=318, chance 0.20; mean rank of the true standard 1.18) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 126 19 7 1 7; prudential: 0 30 0 0 0; etiquette: 0 0 32 4 0; aesthetic: 2 0 0 42 0; epistemic: 2 2 0 2 42
* zeroshot: category words cover 5.0% of the distribution; P(moral set) moral 0.42, norm 0.06, descr 0.00; AUC moral vs norm 0.90; five-way argmax accuracy 0.61 (n=318, chance 0.20; mean rank of the true standard 1.63) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 97 50 1 8 4; prudential: 0 20 0 10 0; etiquette: 1 0 14 21 0; aesthetic: 0 0 0 44 0; epistemic: 8 2 0 19 19

## gemma-2b-it

* fewshot: category words cover 8.5% of the distribution; P(moral set) moral 0.94, norm 0.33, descr 0.44; AUC moral vs norm 0.94; five-way argmax accuracy 0.81 (n=318, chance 0.20; mean rank of the true standard 1.26) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 156 4 0 0 0; prudential: 3 25 0 0 2; etiquette: 12 0 23 1 0; aesthetic: 17 0 0 27 0; epistemic: 20 2 0 0 26
* zeroshot: category words cover 4.4% of the distribution; P(moral set) moral 0.67, norm 0.14, descr 0.02; AUC moral vs norm 0.89; five-way argmax accuracy 0.76 (n=318, chance 0.20; mean rank of the true standard 1.36) -> usable
  confusion (rows: annotators' standard; columns: model's argmax moral, prudential, etiquette, aesthetic, epistemic): moral: 131 24 0 0 5; prudential: 3 22 0 1 4; etiquette: 8 1 21 6 0; aesthetic: 4 1 0 38 1; epistemic: 12 2 0 3 31

## Usable models per preset

* fewshot: 14 of 14 models
* zeroshot: 14 of 14 models
