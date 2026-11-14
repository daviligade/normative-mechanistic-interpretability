# Jacobian-lens readout at the final token (exploratory)

Items: the item file is the set of accepted pairs.

## Llama-3.2-1B

* A1: moral readout AUC (moral vs norm) best 0.86 at layer 8 (depth 0.562), first >= 0.75 at layer 4 (depth 0.312), at the output 0.74; five-way accuracy best 0.50 at layer 0 (n = 159, chance 0.20), at the output 0.09; arrival depth of the judgment moral 0.62 / norm 0.62 / descr 0.69; dip minimum moral -0.01 / norm -0.01
* B: moral readout AUC (moral vs norm) best 0.95 at layer 12 (depth 0.812), first >= 0.75 at layer 4 (depth 0.312), at the output 0.93; five-way accuracy best 0.77 at layer 12 (n = 159, chance 0.20), at the output 0.42; arrival depth of the judgment moral 0.69 / norm 0.69 / descr 0.75; dip minimum moral 0.00 / norm -0.00

## Llama-3.2-1B-Instruct

* A1: moral readout AUC (moral vs norm) best 0.84 at layer 10 (depth 0.688), first >= 0.75 at layer 4 (depth 0.312), at the output 0.78; five-way accuracy best 0.50 at layer 0 (n = 159, chance 0.20), at the output 0.09; arrival depth of the judgment moral 0.81 / norm 0.69 / descr 0.81; dip minimum moral -0.02 / norm -0.00
* B: moral readout AUC (moral vs norm) best 0.95 at layer 14 (depth 0.938), first >= 0.75 at layer 4 (depth 0.312), at the output 0.94; five-way accuracy best 0.79 at layer 12 (n = 159, chance 0.20), at the output 0.46; arrival depth of the judgment moral 0.75 / norm 0.88 / descr 0.88; dip minimum moral -0.00 / norm -0.00

## Llama-3.2-3B

* A1: moral readout AUC (moral vs norm) best 0.91 at layer 12 (depth 0.464), first >= 0.75 at layer 3 (depth 0.143), at the output 0.66; five-way accuracy best 0.50 at layer 4 (n = 159, chance 0.20), at the output 0.09; arrival depth of the judgment moral 0.61 / norm 0.61 / descr 0.61; dip minimum moral -0.00 / norm -0.01
* B: moral readout AUC (moral vs norm) best 0.96 at layer 19 (depth 0.714), first >= 0.75 at layer 5 (depth 0.214), at the output 0.93; five-way accuracy best 0.84 at layer 19 (n = 159, chance 0.20), at the output 0.41; arrival depth of the judgment moral 0.71 / norm 0.68 / descr 0.68; dip minimum moral -0.04 / norm -0.00

## Llama-3.2-3B-Instruct

* A1: moral readout AUC (moral vs norm) best 0.90 at layer 12 (depth 0.464), first >= 0.75 at layer 7 (depth 0.286), at the output 0.68; five-way accuracy best 0.50 at layer 2 (n = 159, chance 0.20), at the output 0.09; arrival depth of the judgment moral 0.61 / norm 0.64 / descr 0.64; dip minimum moral -0.05 / norm -0.01
* B: moral readout AUC (moral vs norm) best 0.98 at layer 16 (depth 0.607), first >= 0.75 at layer 5 (depth 0.214), at the output 0.96; five-way accuracy best 0.82 at layer 19 (n = 159, chance 0.20), at the output 0.67; arrival depth of the judgment moral 0.71 / norm 0.61 / descr 0.79; dip minimum moral -0.00 / norm 0.00

## Qwen2.5-3B

* A1: moral readout AUC (moral vs norm) best 0.96 at layer 24 (depth 0.694), first >= 0.75 at layer 12 (depth 0.361), at the output 0.72; five-way accuracy best 0.52 at layer 12 (n = 159, chance 0.20), at the output 0.09; arrival depth of the judgment moral 0.69 / norm 0.69 / descr 0.75; dip minimum moral -0.00 / norm -0.00
* B: moral readout AUC (moral vs norm) best 0.96 at layer 32 (depth 0.917), first >= 0.75 at layer 18 (depth 0.528), at the output 0.92; five-way accuracy best 0.79 at layer 29 (n = 159, chance 0.20), at the output 0.41; arrival depth of the judgment moral 0.89 / norm 0.89 / descr 0.89; dip minimum moral -0.00 / norm -0.00

## Qwen2.5-3B-Instruct

* A1: moral readout AUC (moral vs norm) best 0.96 at layer 24 (depth 0.694), first >= 0.75 at layer 12 (depth 0.361), at the output 0.79; five-way accuracy best 0.50 at layer 11 (n = 159, chance 0.20), at the output 0.09; arrival depth of the judgment moral 0.78 / norm 0.81 / descr 0.83; dip minimum moral -0.01 / norm -0.00
* B: moral readout AUC (moral vs norm) best 0.99 at layer 32 (depth 0.917), first >= 0.75 at layer 16 (depth 0.472), at the output 0.99; five-way accuracy best 0.89 at layer 32 (n = 159, chance 0.20), at the output 0.31; arrival depth of the judgment moral 0.78 / norm 0.86 / descr 0.89; dip minimum moral -0.00 / norm -0.00

## gemma-2b

* A1: moral readout AUC (moral vs norm) best 0.89 at layer 12 (depth 0.722), first >= 0.75 at layer 2 (depth 0.167), at the output 0.85; five-way accuracy best 0.58 at layer 17 (n = 159, chance 0.20), at the output 0.58; arrival depth of the judgment moral 1.00 / norm 1.00 / descr 1.00; dip minimum moral -0.00 / norm -0.00
* B: moral readout AUC (moral vs norm) best 0.99 at layer 15 (depth 0.889), first >= 0.75 at layer 3 (depth 0.222), at the output 0.96; five-way accuracy best 0.47 at layer 17 (n = 159, chance 0.20), at the output 0.47; arrival depth of the judgment moral 1.00 / norm 1.00 / descr 1.00; dip minimum moral -0.00 / norm -0.00

## gemma-2b-it

* A1: moral readout AUC (moral vs norm) best 0.92 at layer 17 (depth 1.0), first >= 0.75 at layer 3 (depth 0.222), at the output 0.92; five-way accuracy best 0.55 at layer 17 (n = 159, chance 0.20), at the output 0.55; arrival depth of the judgment moral 0.94 / norm 1.00 / descr 1.00; dip minimum moral -0.00 / norm -0.00
* B: moral readout AUC (moral vs norm) best 0.97 at layer 11 (depth 0.667), first >= 0.75 at layer 3 (depth 0.222), at the output 0.95; five-way accuracy best 0.75 at layer 17 (n = 159, chance 0.20), at the output 0.75; arrival depth of the judgment moral 0.72 / norm 0.89 / descr 0.89; dip minimum moral -0.00 / norm -0.00

