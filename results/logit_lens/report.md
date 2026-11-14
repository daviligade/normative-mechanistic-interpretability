# Pre-commitment dip on the new pairs (exploratory)

Items: the item file is the set of accepted pairs; 227 accepted pairs; inclusion gap >= 0.02; readout S; dip on the permissive prompt.

## Llama-3.1-8B

* A1 moral: 78 of 80 included; mean gap 0.778; dip mean 0.036 [0.019, 0.055], median 0.002; dip / gap 0.05 [0.03, 0.07]; sign reversals 0.01; late minimum at depth 0.50
* A1 norm: 104 of 107 included; mean gap 0.446; dip mean 0.027 [0.018, 0.037], median 0.002; dip / gap 0.06 [0.04, 0.09]; sign reversals 0.04; late minimum at depth 0.50
* A1 descr: 38 of 40 included; mean gap 0.241; dip mean 0.013 [0.006, 0.021], median 0.001; dip / gap 0.05 [0.02, 0.09]; sign reversals 0.00; late minimum at depth 0.50
* B moral: 77 of 80 included; mean gap 0.639; dip mean 0.243 [0.152, 0.342], median 0.003; dip / gap 0.38 [0.24, 0.54]; sign reversals 0.30; late minimum at depth 0.53
* B norm: 104 of 107 included; mean gap 0.621; dip mean 0.126 [0.072, 0.189], median 0.001; dip / gap 0.20 [0.12, 0.31]; sign reversals 0.18; late minimum at depth 0.53
* B descr: 40 of 40 included; mean gap 0.605; dip mean 0.039 [0.006, 0.088], median 0.001; dip / gap 0.06 [0.01, 0.15]; sign reversals 0.17; late minimum at depth 0.56
* moral: dip B / dip A1: 6.80 [3.62, 13.24]
* norm: dip B / dip A1: 4.64 [2.46, 8.15]
* A1: dip moral / dip norm: 1.31 [0.64, 2.35]
* A1: (dip/gap) moral / (dip/gap) norm: 0.75
* B: dip moral / dip norm: 1.92 [1.07, 3.64]
* B: (dip/gap) moral / (dip/gap) norm: 1.86

## Llama-3.1-8B-Instruct

* A1 moral: 78 of 80 included; mean gap 1.088; dip mean 0.031 [0.014, 0.052], median 0.001; dip / gap 0.03 [0.01, 0.05]; sign reversals 0.06; late minimum at depth 0.50
* A1 norm: 107 of 107 included; mean gap 0.625; dip mean 0.026 [0.016, 0.039], median 0.001; dip / gap 0.04 [0.03, 0.06]; sign reversals 0.03; late minimum at depth 0.50
* A1 descr: 37 of 40 included; mean gap 0.275; dip mean 0.017 [0.010, 0.025], median 0.006; dip / gap 0.06 [0.04, 0.10]; sign reversals 0.00; late minimum at depth 0.72
* B moral: 78 of 80 included; mean gap 0.846; dip mean 0.182 [0.108, 0.269], median 0.001; dip / gap 0.21 [0.12, 0.32]; sign reversals 0.18; late minimum at depth 0.53
* B norm: 103 of 107 included; mean gap 0.822; dip mean 0.062 [0.027, 0.102], median 0.000; dip / gap 0.08 [0.03, 0.13]; sign reversals 0.10; late minimum at depth 0.53
* B descr: 40 of 40 included; mean gap 0.755; dip mean 0.017 [0.000, 0.046], median 0.000; dip / gap 0.02 [0.00, 0.07]; sign reversals 0.12; late minimum at depth 0.53
* moral: dip B / dip A1: 5.81 [2.78, 13.63]
* norm: dip B / dip A1: 2.33 [0.95, 4.78]
* A1: dip moral / dip norm: 1.18 [0.51, 2.44]
* A1: (dip/gap) moral / (dip/gap) norm: 0.68
* B: dip moral / dip norm: 2.95 [1.41, 6.99]
* B: (dip/gap) moral / (dip/gap) norm: 2.86

## Llama-3.2-1B

* A1 moral: 78 of 80 included; mean gap 0.505; dip mean 0.186 [0.142, 0.232], median 0.053; dip / gap 0.37 [0.27, 0.49]; sign reversals 0.18; late minimum at depth 0.56
* A1 norm: 97 of 107 included; mean gap 0.389; dip mean 0.103 [0.073, 0.135], median 0.034; dip / gap 0.26 [0.19, 0.36]; sign reversals 0.18; late minimum at depth 0.56
* A1 descr: 39 of 40 included; mean gap 0.358; dip mean 0.029 [0.026, 0.032], median 0.027; dip / gap 0.08 [0.06, 0.10]; sign reversals 0.36; late minimum at depth 0.56
* B moral: 73 of 80 included; mean gap 0.348; dip mean 0.001 [0.000, 0.003], median 0.000; dip / gap 0.00 [0.00, 0.01]; sign reversals 0.16; late minimum at depth 0.50
* B norm: 91 of 107 included; mean gap 0.292; dip mean 0.006 [0.000, 0.018], median 0.000; dip / gap 0.02 [0.00, 0.06]; sign reversals 0.19; late minimum at depth 0.50
* B descr: 35 of 40 included; mean gap 0.336; dip mean 0.000 [0.000, 0.000], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 0.06; late minimum at depth 0.50
* moral: dip B / dip A1: 0.01 [0.00, 0.02]
* norm: dip B / dip A1: 0.06 [0.00, 0.20]
* A1: dip moral / dip norm: 1.81 [1.22, 2.71]
* A1: (dip/gap) moral / (dip/gap) norm: 1.39
* B: dip moral / dip norm: 0.21 [0.02, 9.56]
* B: (dip/gap) moral / (dip/gap) norm: 0.17

## Llama-3.2-1B-Instruct

* A1 moral: 69 of 80 included; mean gap 0.541; dip mean 0.343 [0.287, 0.397], median 0.364; dip / gap 0.64 [0.51, 0.79]; sign reversals 0.16; late minimum at depth 0.94
* A1 norm: 92 of 107 included; mean gap 0.330; dip mean 0.233 [0.200, 0.268], median 0.221; dip / gap 0.71 [0.58, 0.85]; sign reversals 0.24; late minimum at depth 0.94
* A1 descr: 38 of 40 included; mean gap 0.325; dip mean 0.114 [0.082, 0.157], median 0.083; dip / gap 0.35 [0.24, 0.50]; sign reversals 0.34; late minimum at depth 0.84
* B moral: 72 of 80 included; mean gap 0.734; dip mean 0.048 [0.019, 0.086], median 0.000; dip / gap 0.07 [0.02, 0.12]; sign reversals 0.06; late minimum at depth 0.50
* B norm: 95 of 107 included; mean gap 0.492; dip mean 0.011 [0.001, 0.024], median 0.000; dip / gap 0.02 [0.00, 0.05]; sign reversals 0.11; late minimum at depth 0.50
* B descr: 37 of 40 included; mean gap 0.460; dip mean 0.001 [0.000, 0.001], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 0.16; late minimum at depth 0.62
* moral: dip B / dip A1: 0.14 [0.05, 0.26]
* norm: dip B / dip A1: 0.05 [0.00, 0.11]
* A1: dip moral / dip norm: 1.47 [1.18, 1.83]
* A1: (dip/gap) moral / (dip/gap) norm: 0.90
* B: dip moral / dip norm: 4.59 [1.38, 83.58]
* B: (dip/gap) moral / (dip/gap) norm: 3.08

## Llama-3.2-3B

* A1 moral: 79 of 80 included; mean gap 0.738; dip mean 0.411 [0.343, 0.485], median 0.246; dip / gap 0.56 [0.45, 0.68]; sign reversals 0.19; late minimum at depth 0.50
* A1 norm: 104 of 107 included; mean gap 0.568; dip mean 0.271 [0.230, 0.319], median 0.183; dip / gap 0.48 [0.39, 0.58]; sign reversals 0.16; late minimum at depth 0.50
* A1 descr: 40 of 40 included; mean gap 0.389; dip mean 0.153 [0.117, 0.200], median 0.119; dip / gap 0.39 [0.28, 0.55]; sign reversals 0.10; late minimum at depth 0.50
* B moral: 78 of 80 included; mean gap 0.554; dip mean 0.089 [0.050, 0.135], median 0.000; dip / gap 0.16 [0.09, 0.24]; sign reversals 0.31; late minimum at depth 0.50
* B norm: 100 of 107 included; mean gap 0.520; dip mean 0.033 [0.010, 0.062], median 0.000; dip / gap 0.06 [0.02, 0.12]; sign reversals 0.29; late minimum at depth 0.50
* B descr: 40 of 40 included; mean gap 0.477; dip mean 0.014 [0.000, 0.041], median 0.000; dip / gap 0.03 [0.00, 0.09]; sign reversals 0.15; late minimum at depth 0.50
* moral: dip B / dip A1: 0.22 [0.11, 0.34]
* norm: dip B / dip A1: 0.12 [0.04, 0.24]
* A1: dip moral / dip norm: 1.52 [1.19, 1.94]
* A1: (dip/gap) moral / (dip/gap) norm: 1.17
* B: dip moral / dip norm: 2.67 [1.13, 8.88]
* B: (dip/gap) moral / (dip/gap) norm: 2.50

## Llama-3.2-3B-Instruct

* A1 moral: 72 of 80 included; mean gap 1.118; dip mean 0.391 [0.313, 0.473], median 0.210; dip / gap 0.35 [0.27, 0.44]; sign reversals 0.17; late minimum at depth 0.50
* A1 norm: 103 of 107 included; mean gap 0.852; dip mean 0.358 [0.300, 0.418], median 0.210; dip / gap 0.42 [0.34, 0.51]; sign reversals 0.17; late minimum at depth 0.50
* A1 descr: 39 of 40 included; mean gap 0.670; dip mean 0.201 [0.157, 0.253], median 0.144; dip / gap 0.30 [0.23, 0.40]; sign reversals 0.15; late minimum at depth 0.50
* B moral: 69 of 80 included; mean gap 0.916; dip mean 0.124 [0.068, 0.190], median 0.000; dip / gap 0.14 [0.07, 0.21]; sign reversals 0.25; late minimum at depth 0.50
* B norm: 103 of 107 included; mean gap 0.784; dip mean 0.101 [0.054, 0.152], median 0.001; dip / gap 0.13 [0.07, 0.20]; sign reversals 0.20; late minimum at depth 0.50
* B descr: 39 of 40 included; mean gap 0.686; dip mean 0.025 [0.000, 0.073], median 0.000; dip / gap 0.04 [0.00, 0.12]; sign reversals 0.18; late minimum at depth 0.50
* moral: dip B / dip A1: 0.32 [0.17, 0.51]
* norm: dip B / dip A1: 0.28 [0.15, 0.45]
* A1: dip moral / dip norm: 1.09 [0.83, 1.42]
* A1: (dip/gap) moral / (dip/gap) norm: 0.83
* B: dip moral / dip norm: 1.23 [0.60, 2.59]
* B: (dip/gap) moral / (dip/gap) norm: 1.05

## Qwen2.5-14B

* A1 moral: 79 of 80 included; mean gap 1.370; dip mean 0.213 [0.128, 0.306], median 0.003; dip / gap 0.16 [0.09, 0.22]; sign reversals 0.67; late minimum at depth 0.50
* A1 norm: 99 of 107 included; mean gap 0.806; dip mean 0.090 [0.044, 0.143], median 0.003; dip / gap 0.11 [0.05, 0.18]; sign reversals 0.57; late minimum at depth 0.50
* A1 descr: 36 of 40 included; mean gap 0.184; dip mean 0.001 [0.001, 0.002], median 0.001; dip / gap 0.01 [0.01, 0.01]; sign reversals 0.33; late minimum at depth 0.90
* B moral: 79 of 80 included; mean gap 1.287; dip mean 0.211 [0.110, 0.330], median 0.000; dip / gap 0.16 [0.08, 0.26]; sign reversals 0.37; late minimum at depth 0.50
* B norm: 106 of 107 included; mean gap 1.070; dip mean 0.099 [0.041, 0.168], median 0.000; dip / gap 0.09 [0.04, 0.16]; sign reversals 0.23; late minimum at depth 0.50
* B descr: 40 of 40 included; mean gap 1.078; dip mean 0.077 [0.000, 0.199], median 0.000; dip / gap 0.07 [0.00, 0.18]; sign reversals 0.28; late minimum at depth 0.50
* moral: dip B / dip A1: 0.99 [0.46, 1.98]
* norm: dip B / dip A1: 1.10 [0.40, 2.61]
* A1: dip moral / dip norm: 2.37 [1.19, 5.12]
* A1: (dip/gap) moral / (dip/gap) norm: 1.40
* B: dip moral / dip norm: 2.13 [0.93, 5.61]
* B: (dip/gap) moral / (dip/gap) norm: 1.77

## Qwen2.5-14B-Instruct

* A1 moral: 79 of 80 included; mean gap 1.507; dip mean 0.113 [0.041, 0.198], median 0.002; dip / gap 0.08 [0.03, 0.13]; sign reversals 0.77; late minimum at depth 0.50
* A1 norm: 99 of 107 included; mean gap 0.845; dip mean 0.064 [0.024, 0.115], median 0.002; dip / gap 0.08 [0.03, 0.14]; sign reversals 0.73; late minimum at depth 0.50
* A1 descr: 18 of 40 included; mean gap 0.256; dip mean 0.002 [0.001, 0.002], median 0.001; dip / gap 0.01 [0.00, 0.01]; sign reversals 0.72; late minimum at depth 0.58
* B moral: 78 of 80 included; mean gap 1.351; dip mean 0.097 [0.037, 0.171], median 0.001; dip / gap 0.07 [0.03, 0.13]; sign reversals 0.41; late minimum at depth 0.50
* B norm: 104 of 107 included; mean gap 1.068; dip mean 0.037 [0.010, 0.075], median 0.001; dip / gap 0.04 [0.01, 0.07]; sign reversals 0.17; late minimum at depth 0.52
* B descr: 40 of 40 included; mean gap 1.187; dip mean 0.055 [0.000, 0.150], median 0.000; dip / gap 0.05 [0.00, 0.13]; sign reversals 0.20; late minimum at depth 0.50
* moral: dip B / dip A1: 0.86 [0.27, 2.70]
* norm: dip B / dip A1: 0.58 [0.12, 1.84]
* A1: dip moral / dip norm: 1.76 [0.53, 5.45]
* A1: (dip/gap) moral / (dip/gap) norm: 0.99
* B: dip moral / dip norm: 2.59 [0.76, 13.18]
* B: (dip/gap) moral / (dip/gap) norm: 2.05

## Qwen2.5-3B

* A1 moral: 78 of 80 included; mean gap 0.479; dip mean 1.040 [0.956, 1.116], median 1.067; dip / gap 2.17 [1.83, 2.61]; sign reversals 0.26; late minimum at depth 0.92
* A1 norm: 98 of 107 included; mean gap 0.287; dip mean 0.992 [0.947, 1.035], median 0.999; dip / gap 3.45 [3.05, 3.96]; sign reversals 0.06; late minimum at depth 0.92
* A1 descr: 39 of 40 included; mean gap 0.300; dip mean 0.641 [0.554, 0.724], median 0.665; dip / gap 2.13 [1.76, 2.57]; sign reversals 0.33; late minimum at depth 0.94
* B moral: 75 of 80 included; mean gap 0.537; dip mean 0.894 [0.767, 1.017], median 1.021; dip / gap 1.67 [1.36, 2.04]; sign reversals 0.23; late minimum at depth 0.94
* B norm: 101 of 107 included; mean gap 0.414; dip mean 0.714 [0.604, 0.825], median 0.934; dip / gap 1.72 [1.41, 2.09]; sign reversals 0.29; late minimum at depth 0.94
* B descr: 40 of 40 included; mean gap 0.434; dip mean 0.452 [0.287, 0.626], median 0.106; dip / gap 1.04 [0.64, 1.52]; sign reversals 0.28; late minimum at depth 0.94
* moral: dip B / dip A1: 0.86 [0.72, 1.01]
* norm: dip B / dip A1: 0.72 [0.61, 0.83]
* A1: dip moral / dip norm: 1.05 [0.95, 1.14]
* A1: (dip/gap) moral / (dip/gap) norm: 0.63
* B: dip moral / dip norm: 1.25 [1.02, 1.56]
* B: (dip/gap) moral / (dip/gap) norm: 0.97

## Qwen2.5-3B-Instruct

* A1 moral: 76 of 80 included; mean gap 1.066; dip mean 0.360 [0.246, 0.482], median 0.017; dip / gap 0.34 [0.23, 0.46]; sign reversals 0.14; late minimum at depth 0.69
* A1 norm: 103 of 107 included; mean gap 0.929; dip mean 0.302 [0.215, 0.393], median 0.009; dip / gap 0.33 [0.23, 0.43]; sign reversals 0.22; late minimum at depth 0.69
* A1 descr: 40 of 40 included; mean gap 0.683; dip mean 0.053 [0.002, 0.114], median 0.002; dip / gap 0.08 [0.00, 0.17]; sign reversals 0.05; late minimum at depth 0.67
* B moral: 76 of 80 included; mean gap 1.075; dip mean 0.180 [0.094, 0.274], median 0.001; dip / gap 0.17 [0.09, 0.26]; sign reversals 0.18; late minimum at depth 0.56
* B norm: 104 of 107 included; mean gap 0.876; dip mean 0.082 [0.033, 0.140], median 0.000; dip / gap 0.09 [0.04, 0.16]; sign reversals 0.13; late minimum at depth 0.56
* B descr: 40 of 40 included; mean gap 0.869; dip mean 0.068 [0.002, 0.173], median 0.000; dip / gap 0.08 [0.00, 0.20]; sign reversals 0.12; late minimum at depth 0.53
* moral: dip B / dip A1: 0.50 [0.25, 0.88]
* norm: dip B / dip A1: 0.27 [0.11, 0.51]
* A1: dip moral / dip norm: 1.19 [0.76, 1.86]
* A1: (dip/gap) moral / (dip/gap) norm: 1.04
* B: dip moral / dip norm: 2.21 [0.99, 5.94]
* B: (dip/gap) moral / (dip/gap) norm: 1.80

## Qwen2.5-7B

* A1 moral: 79 of 80 included; mean gap 1.136; dip mean 0.116 [0.065, 0.172], median 0.000; dip / gap 0.10 [0.06, 0.15]; sign reversals 0.65; late minimum at depth 0.61
* A1 norm: 104 of 107 included; mean gap 0.883; dip mean 0.066 [0.038, 0.099], median 0.000; dip / gap 0.07 [0.04, 0.11]; sign reversals 0.81; late minimum at depth 0.61
* A1 descr: 40 of 40 included; mean gap 0.531; dip mean 0.000 [0.000, 0.000], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 0.85; late minimum at depth 0.61
* B moral: 77 of 80 included; mean gap 1.103; dip mean 0.213 [0.129, 0.304], median 0.000; dip / gap 0.19 [0.12, 0.28]; sign reversals 0.17; late minimum at depth 0.54
* B norm: 107 of 107 included; mean gap 1.044; dip mean 0.060 [0.022, 0.106], median 0.000; dip / gap 0.06 [0.02, 0.10]; sign reversals 0.07; late minimum at depth 0.50
* B descr: 40 of 40 included; mean gap 1.077; dip mean 0.018 [0.000, 0.053], median 0.000; dip / gap 0.02 [0.00, 0.05]; sign reversals 0.15; late minimum at depth 0.50
* moral: dip B / dip A1: 1.83 [0.98, 3.53]
* norm: dip B / dip A1: 0.90 [0.30, 2.00]
* A1: dip moral / dip norm: 1.75 [0.88, 3.50]
* A1: (dip/gap) moral / (dip/gap) norm: 1.36
* B: dip moral / dip norm: 3.56 [1.62, 10.96]
* B: (dip/gap) moral / (dip/gap) norm: 3.37

## Qwen2.5-7B-Instruct

* A1 moral: 75 of 80 included; mean gap 1.244; dip mean 0.155 [0.095, 0.225], median 0.000; dip / gap 0.12 [0.07, 0.18]; sign reversals 0.57; late minimum at depth 0.61
* A1 norm: 106 of 107 included; mean gap 0.967; dip mean 0.177 [0.127, 0.229], median 0.008; dip / gap 0.18 [0.13, 0.24]; sign reversals 0.72; late minimum at depth 0.89
* A1 descr: 40 of 40 included; mean gap 0.715; dip mean 0.002 [0.000, 0.006], median 0.000; dip / gap 0.00 [0.00, 0.01]; sign reversals 0.88; late minimum at depth 0.68
* B moral: 77 of 80 included; mean gap 1.291; dip mean 0.184 [0.103, 0.278], median 0.000; dip / gap 0.14 [0.08, 0.22]; sign reversals 0.12; late minimum at depth 0.54
* B norm: 104 of 107 included; mean gap 1.195; dip mean 0.043 [0.010, 0.084], median 0.000; dip / gap 0.04 [0.01, 0.07]; sign reversals 0.05; late minimum at depth 0.54
* B descr: 40 of 40 included; mean gap 1.211; dip mean 0.021 [0.000, 0.062], median 0.000; dip / gap 0.02 [0.00, 0.05]; sign reversals 0.25; late minimum at depth 0.50
* moral: dip B / dip A1: 1.19 [0.61, 2.27]
* norm: dip B / dip A1: 0.24 [0.05, 0.52]
* A1: dip moral / dip norm: 0.88 [0.50, 1.43]
* A1: (dip/gap) moral / (dip/gap) norm: 0.68
* B: dip moral / dip norm: 4.27 [1.77, 20.76]
* B: (dip/gap) moral / (dip/gap) norm: 3.95

## gemma-2b

* A1 moral: 74 of 80 included; mean gap 0.653; dip mean 0.001 [0.001, 0.002], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 0.81; late minimum at depth 0.72
* A1 norm: 99 of 107 included; mean gap 0.495; dip mean 0.000 [0.000, 0.000], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 0.85; late minimum at depth 0.78
* A1 descr: 39 of 40 included; mean gap 0.432; dip mean 0.000 [0.000, 0.000], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 0.82; late minimum at depth 0.78
* B moral: 72 of 80 included; mean gap 0.549; dip mean 0.003 [0.000, 0.006], median 0.000; dip / gap 0.00 [0.00, 0.01]; sign reversals 0.86; late minimum at depth 0.72
* B norm: 95 of 107 included; mean gap 0.484; dip mean 0.004 [0.000, 0.013], median 0.000; dip / gap 0.01 [0.00, 0.03]; sign reversals 0.93; late minimum at depth 0.72
* B descr: 40 of 40 included; mean gap 0.483; dip mean 0.000 [0.000, 0.000], median 0.000; dip / gap 0.00 [0.00, 0.00]; sign reversals 1.00; late minimum at depth 0.67
* moral: dip B / dip A1: not reported (denominator mean dip 0.0012 below 0.005: ratio not reported)
* norm: dip B / dip A1: not reported (denominator mean dip 0.0002 below 0.005: ratio not reported)
* A1: dip moral / dip norm: not reported (denominator mean dip 0.0002 below 0.005: ratio not reported)
* A1: (dip/gap) moral / (dip/gap) norm: not reported (denominator near zero)
* B: dip moral / dip norm: not reported (denominator mean dip 0.0044 below 0.005: ratio not reported)
* B: (dip/gap) moral / (dip/gap) norm: 0.54

## gemma-2b-it

* A1 moral: 73 of 80 included; mean gap 1.111; dip mean 0.766 [0.628, 0.908], median 0.974; dip / gap 0.69 [0.54, 0.87]; sign reversals 0.37; late minimum at depth 0.89
* A1 norm: 98 of 107 included; mean gap 0.837; dip mean 0.661 [0.544, 0.779], median 0.681; dip / gap 0.79 [0.63, 0.98]; sign reversals 0.42; late minimum at depth 0.89
* A1 descr: 37 of 40 included; mean gap 0.739; dip mean 0.601 [0.442, 0.762], median 0.617; dip / gap 0.81 [0.57, 1.14]; sign reversals 0.46; late minimum at depth 0.89
* B moral: 67 of 80 included; mean gap 0.698; dip mean 0.115 [0.045, 0.194], median 0.000; dip / gap 0.16 [0.07, 0.28]; sign reversals 0.07; late minimum at depth 0.50
* B norm: 88 of 107 included; mean gap 0.434; dip mean 0.039 [0.008, 0.077], median 0.000; dip / gap 0.09 [0.02, 0.18]; sign reversals 0.06; late minimum at depth 0.50
* B descr: 34 of 40 included; mean gap 0.571; dip mean 0.052 [-0.000, 0.122], median 0.000; dip / gap 0.09 [-0.00, 0.22]; sign reversals 0.00; late minimum at depth 0.50
* moral: dip B / dip A1: 0.15 [0.06, 0.27]
* norm: dip B / dip A1: 0.06 [0.01, 0.12]
* A1: dip moral / dip norm: 1.16 [0.90, 1.51]
* A1: (dip/gap) moral / (dip/gap) norm: 0.87
* B: dip moral / dip norm: 2.96 [1.00, 14.06]
* B: (dip/gap) moral / (dip/gap) norm: 1.84

## Over models (medians)

* moral: dip B / dip A1: median 0.86 (range 0.01 to 6.80; 13 models)
* norm: dip B / dip A1: median 0.28 (range 0.05 to 4.64; 13 models)
* A1: dip moral / dip norm: median 1.31 (range 0.88 to 2.37; 13 models)
* B: dip moral / dip norm: median 2.59 (range 0.21 to 4.59; 13 models)
* A1 moral: dip / gap median over models 0.25 (range 0.00 to 2.17)
* A1 norm: dip / gap median over models 0.22 (range 0.00 to 3.45)
* A1 descr: dip / gap median over models 0.07 (range 0.00 to 2.13)
* B moral: dip / gap median over models 0.16 (range 0.00 to 1.67)
* B norm: dip / gap median over models 0.07 (range 0.01 to 1.72)
* B descr: dip / gap median over models 0.03 (range 0.00 to 1.04)
