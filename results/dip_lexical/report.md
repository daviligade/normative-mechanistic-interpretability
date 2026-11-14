# The dip and the words (exploratory)

Items: the item file is the set of accepted pairs. Inclusion gap >= 0.02. Word valence: frame B, run alone.

## Llama-3.1-8B

* A1: dip means moral 0.036, norm 0.027; word negativity (minS) moral -0.014, norm +0.042, descr +0.040
  moral - norm dip: unadjusted +0.008 [-0.011, +0.030]; adjusted for minS +0.014 [-0.008, +0.039]; adjusted for minS and meanS +0.015 -> mixed
  rank correlation of the dip with minS: moral +0.13, norm +0.07, all +0.12
  timing (moral, n=15): dip minimum at depth 0.91 (median), edit arrives at 0.53; minimum before arrival in 0% of pairs; arrival at or before half depth in 47% (there the dip window starts after the arrival by construction); rank corr. -0.09
  timing (norm, n=31): dip minimum at depth 0.91 (median), edit arrives at 0.56; minimum before arrival in 0% of pairs; arrival at or before half depth in 45% (there the dip window starts after the arrival by construction); rank corr. 0.06
* B: dip means moral 0.243, norm 0.126; word negativity (minS) moral -0.016, norm +0.044, descr +0.039
  moral - norm dip: unadjusted +0.116 [+0.010, +0.229]; adjusted for minS +0.054 [-0.057, +0.166]; adjusted for minS and meanS +0.054 -> lexical
  rank correlation of the dip with minS: moral -0.04, norm -0.19, all -0.19
  timing (moral, n=28): dip minimum at depth 0.78 (median), edit arrives at 0.42; minimum before arrival in 0% of pairs; arrival at or before half depth in 96% (there the dip window starts after the arrival by construction); rank corr. 0.47
  timing (norm, n=22): dip minimum at depth 0.78 (median), edit arrives at 0.44; minimum before arrival in 0% of pairs; arrival at or before half depth in 95% (there the dip window starts after the arrival by construction); rank corr. 0.44

## Llama-3.1-8B-Instruct

* A1: dip means moral 0.031, norm 0.026; word negativity (minS) moral -0.066, norm +0.016, descr +0.056
  moral - norm dip: unadjusted +0.005 [-0.016, +0.028]; adjusted for minS -0.001 [-0.022, +0.018]; adjusted for minS and meanS -0.002 -> lexical
  rank correlation of the dip with minS: moral +0.19, norm +0.05, all +0.24
  timing (moral, n=12): dip minimum at depth 0.97 (median), edit arrives at 0.58; minimum before arrival in 0% of pairs; arrival at or before half depth in 33% (there the dip window starts after the arrival by construction); rank corr. 0.05
  timing (norm, n=28): dip minimum at depth 0.91 (median), edit arrives at 0.52; minimum before arrival in 0% of pairs; arrival at or before half depth in 50% (there the dip window starts after the arrival by construction); rank corr. 0.39
* B: dip means moral 0.182, norm 0.062; word negativity (minS) moral -0.066, norm +0.020, descr +0.043
  moral - norm dip: unadjusted +0.120 [+0.035, +0.212]; adjusted for minS +0.068 [-0.019, +0.159]; adjusted for minS and meanS +0.069 -> mixed
  rank correlation of the dip with minS: moral +0.07, norm -0.24, all -0.14
  timing (moral, n=18): dip minimum at depth 0.81 (median), edit arrives at 0.44; minimum before arrival in 0% of pairs; arrival at or before half depth in 89% (there the dip window starts after the arrival by construction); rank corr. -0.18
  timing (norm, n=12): dip minimum at depth 0.81 (median), edit arrives at 0.42; minimum before arrival in 0% of pairs; arrival at or before half depth in 92% (there the dip window starts after the arrival by construction); rank corr. 0.57

## Llama-3.2-1B

* A1: dip means moral 0.186, norm 0.103; word negativity (minS) moral +0.008, norm +0.048, descr +0.058
  moral - norm dip: unadjusted +0.083 [+0.029, +0.141]; adjusted for minS +0.076 [+0.019, +0.135]; adjusted for minS and meanS +0.076 -> moral content
  rank correlation of the dip with minS: moral +0.03, norm -0.31, all -0.19
  timing (moral, n=78): dip minimum at depth 0.56 (median), edit arrives at 0.62; minimum before arrival in 58% of pairs; arrival at or before half depth in 5% (there the dip window starts after the arrival by construction); rank corr. 0.16
  timing (norm, n=97): dip minimum at depth 0.56 (median), edit arrives at 0.69; minimum before arrival in 66% of pairs; arrival at or before half depth in 2% (there the dip window starts after the arrival by construction); rank corr. 0.08
* B: dip means moral 0.001, norm 0.006; word negativity (minS) moral +0.005, norm +0.049, descr +0.056
  moral - norm dip: unadjusted -0.005 [-0.017, +0.002]; adjusted for minS -0.003 [-0.012, +0.003]; adjusted for minS and meanS -0.002 -> no moral excess to explain
  rank correlation of the dip with minS: moral +0.20, norm -0.09, all +0.06

## Llama-3.2-1B-Instruct

* A1: dip means moral 0.343, norm 0.233; word negativity (minS) moral -0.036, norm +0.002, descr +0.027
  moral - norm dip: unadjusted +0.110 [+0.046, +0.175]; adjusted for minS +0.099 [+0.036, +0.162]; adjusted for minS and meanS +0.104 -> moral content
  rank correlation of the dip with minS: moral -0.16, norm -0.19, all -0.22
  timing (moral, n=69): dip minimum at depth 0.94 (median), edit arrives at 0.69; minimum before arrival in 25% of pairs; arrival at or before half depth in 1% (there the dip window starts after the arrival by construction); rank corr. 0.08
  timing (norm, n=92): dip minimum at depth 0.94 (median), edit arrives at 0.69; minimum before arrival in 25% of pairs; arrival at or before half depth in 1% (there the dip window starts after the arrival by construction); rank corr. 0.26
* B: dip means moral 0.048, norm 0.011; word negativity (minS) moral -0.052, norm -0.001, descr +0.029
  moral - norm dip: unadjusted +0.038 [+0.005, +0.077]; adjusted for minS +0.021 [-0.004, +0.047]; adjusted for minS and meanS +0.022 -> mixed
  rank correlation of the dip with minS: moral -0.05, norm -0.01, all +0.01
  timing (moral, n=11): dip minimum at depth 0.88 (median), edit arrives at 0.56; minimum before arrival in 0% of pairs; arrival at or before half depth in 45% (there the dip window starts after the arrival by construction); rank corr. -0.01

## Llama-3.2-3B

* A1: dip means moral 0.411, norm 0.271; word negativity (minS) moral -0.013, norm +0.033, descr +0.042
  moral - norm dip: unadjusted +0.140 [+0.058, +0.224]; adjusted for minS +0.126 [+0.043, +0.210]; adjusted for minS and meanS +0.128 -> moral content
  rank correlation of the dip with minS: moral -0.04, norm +0.09, all -0.08
  timing (moral, n=79): dip minimum at depth 0.50 (median), edit arrives at 0.61; minimum before arrival in 54% of pairs; arrival at or before half depth in 6% (there the dip window starts after the arrival by construction); rank corr. 0.35
  timing (norm, n=104): dip minimum at depth 0.50 (median), edit arrives at 0.61; minimum before arrival in 65% of pairs; arrival at or before half depth in 9% (there the dip window starts after the arrival by construction); rank corr. 0.14
* B: dip means moral 0.089, norm 0.033; word negativity (minS) moral -0.015, norm +0.034, descr +0.042
  moral - norm dip: unadjusted +0.056 [+0.008, +0.108]; adjusted for minS +0.028 [-0.020, +0.080]; adjusted for minS and meanS +0.029 -> mixed
  rank correlation of the dip with minS: moral -0.32, norm -0.02, all -0.20
  timing (moral, n=20): dip minimum at depth 0.93 (median), edit arrives at 0.45; minimum before arrival in 0% of pairs; arrival at or before half depth in 85% (there the dip window starts after the arrival by construction); rank corr. 0.45
  timing (norm, n=8): dip minimum at depth 0.93 (median), edit arrives at 0.46; minimum before arrival in 0% of pairs; arrival at or before half depth in 75% (there the dip window starts after the arrival by construction); rank corr. -0.14

## Llama-3.2-3B-Instruct

* A1: dip means moral 0.391, norm 0.358; word negativity (minS) moral -0.089, norm -0.003, descr +0.021
  moral - norm dip: unadjusted +0.033 [-0.067, +0.132]; adjusted for minS -0.007 [-0.113, +0.097]; adjusted for minS and meanS -0.006 -> lexical
  rank correlation of the dip with minS: moral -0.25, norm -0.00, all -0.18
  timing (moral, n=72): dip minimum at depth 0.50 (median), edit arrives at 0.61; minimum before arrival in 64% of pairs; arrival at or before half depth in 3% (there the dip window starts after the arrival by construction); rank corr. 0.08
  timing (norm, n=103): dip minimum at depth 0.50 (median), edit arrives at 0.61; minimum before arrival in 57% of pairs; arrival at or before half depth in 8% (there the dip window starts after the arrival by construction); rank corr. 0.26
* B: dip means moral 0.124, norm 0.101; word negativity (minS) moral -0.078, norm -0.003, descr +0.021
  moral - norm dip: unadjusted +0.023 [-0.057, +0.102]; adjusted for minS +0.006 [-0.075, +0.084]; adjusted for minS and meanS +0.006 -> lexical
  rank correlation of the dip with minS: moral -0.01, norm -0.12, all -0.13
  timing (moral, n=15): dip minimum at depth 0.89 (median), edit arrives at 0.46; minimum before arrival in 0% of pairs; arrival at or before half depth in 87% (there the dip window starts after the arrival by construction); rank corr. 0.25
  timing (norm, n=18): dip minimum at depth 0.89 (median), edit arrives at 0.46; minimum before arrival in 0% of pairs; arrival at or before half depth in 78% (there the dip window starts after the arrival by construction); rank corr. 0.06

## Qwen2.5-14B

* A1: dip means moral 0.213, norm 0.090; word negativity (minS) moral -0.150, norm +0.017, descr +0.073
  moral - norm dip: unadjusted +0.123 [+0.023, +0.227]; adjusted for minS +0.072 [-0.046, +0.189]; adjusted for minS and meanS +0.074 -> mixed
  rank correlation of the dip with minS: moral +0.10, norm -0.05, all -0.21
  timing (moral, n=25): dip minimum at depth 0.85 (median), edit arrives at 0.69; minimum before arrival in 4% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. -0.23
  timing (norm, n=22): dip minimum at depth 0.85 (median), edit arrives at 0.69; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. -0.55
* B: dip means moral 0.211, norm 0.099; word negativity (minS) moral -0.150, norm +0.015, descr +0.071
  moral - norm dip: unadjusted +0.112 [-0.011, +0.242]; adjusted for minS +0.018 [-0.119, +0.157]; adjusted for minS and meanS +0.022 -> lexical
  rank correlation of the dip with minS: moral -0.03, norm +0.05, all +0.04
  timing (moral, n=12): dip minimum at depth 0.92 (median), edit arrives at 0.60; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.43
  timing (norm, n=9): dip minimum at depth 0.92 (median), edit arrives at 0.62; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.25

## Qwen2.5-14B-Instruct

* A1: dip means moral 0.113, norm 0.064; word negativity (minS) moral -0.099, norm +0.006, descr +0.037
  moral - norm dip: unadjusted +0.049 [-0.038, +0.143]; adjusted for minS -0.002 [-0.091, +0.090]; adjusted for minS and meanS -0.004 -> lexical
  rank correlation of the dip with minS: moral -0.06, norm -0.17, all -0.26
  timing (moral, n=11): dip minimum at depth 0.85 (median), edit arrives at 0.73; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. -0.05
  timing (norm, n=14): dip minimum at depth 0.85 (median), edit arrives at 0.68; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. -0.45
* B: dip means moral 0.097, norm 0.037; word negativity (minS) moral -0.092, norm +0.009, descr +0.037
  moral - norm dip: unadjusted +0.060 [-0.013, +0.139]; adjusted for minS +0.055 [-0.027, +0.148]; adjusted for minS and meanS +0.059 -> mixed
  rank correlation of the dip with minS: moral +0.06, norm -0.05, all +0.03
  timing (moral, n=8): dip minimum at depth 0.96 (median), edit arrives at 0.60; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.4
  timing (norm, n=7): dip minimum at depth 0.92 (median), edit arrives at 0.58; minimum before arrival in 14% of pairs; arrival at or before half depth in 29% (there the dip window starts after the arrival by construction); rank corr. 0.75

## Qwen2.5-3B

* A1: dip means moral 1.040, norm 0.992; word negativity (minS) moral -0.121, norm -0.072, descr -0.064
  moral - norm dip: unadjusted +0.048 [-0.047, +0.136]; adjusted for minS +0.018 [-0.080, +0.105]; adjusted for minS and meanS +0.016 -> lexical
  rank correlation of the dip with minS: moral -0.21, norm -0.20, all -0.26
  timing (moral, n=75): dip minimum at depth 0.92 (median), edit arrives at 0.78; minimum before arrival in 4% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. -0.16
  timing (norm, n=97): dip minimum at depth 0.92 (median), edit arrives at 0.81; minimum before arrival in 0% of pairs; arrival at or before half depth in 1% (there the dip window starts after the arrival by construction); rank corr. 0.12
* B: dip means moral 0.894, norm 0.714; word negativity (minS) moral -0.120, norm -0.071, descr -0.064
  moral - norm dip: unadjusted +0.181 [+0.009, +0.344]; adjusted for minS +0.150 [-0.025, +0.320]; adjusted for minS and meanS +0.146 -> mixed
  rank correlation of the dip with minS: moral -0.11, norm -0.10, all -0.21
  timing (moral, n=57): dip minimum at depth 0.94 (median), edit arrives at 0.61; minimum before arrival in 2% of pairs; arrival at or before half depth in 2% (there the dip window starts after the arrival by construction); rank corr. 0.01
  timing (norm, n=73): dip minimum at depth 0.94 (median), edit arrives at 0.61; minimum before arrival in 0% of pairs; arrival at or before half depth in 12% (there the dip window starts after the arrival by construction); rank corr. -0.21

## Qwen2.5-3B-Instruct

* A1: dip means moral 0.360, norm 0.302; word negativity (minS) moral -0.139, norm -0.011, descr -0.007
  moral - norm dip: unadjusted +0.058 [-0.085, +0.203]; adjusted for minS +0.038 [-0.123, +0.200]; adjusted for minS and meanS +0.051 -> mixed
  rank correlation of the dip with minS: moral +0.01, norm -0.21, all -0.19
  timing (moral, n=55): dip minimum at depth 0.75 (median), edit arrives at 0.81; minimum before arrival in 49% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.49
  timing (norm, n=49): dip minimum at depth 0.92 (median), edit arrives at 0.81; minimum before arrival in 22% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.19
* B: dip means moral 0.180, norm 0.082; word negativity (minS) moral -0.147, norm -0.012, descr -0.007
  moral - norm dip: unadjusted +0.099 [-0.006, +0.204]; adjusted for minS +0.047 [-0.060, +0.157]; adjusted for minS and meanS +0.053 -> lexical
  rank correlation of the dip with minS: moral -0.17, norm -0.01, all -0.16
  timing (moral, n=13): dip minimum at depth 0.94 (median), edit arrives at 0.61; minimum before arrival in 0% of pairs; arrival at or before half depth in 8% (there the dip window starts after the arrival by construction); rank corr. -0.32
  timing (norm, n=10): dip minimum at depth 0.94 (median), edit arrives at 0.65; minimum before arrival in 0% of pairs; arrival at or before half depth in 20% (there the dip window starts after the arrival by construction); rank corr. 0.53

## Qwen2.5-7B

* A1: dip means moral 0.116, norm 0.066; word negativity (minS) moral -0.198, norm -0.004, descr +0.030
  moral - norm dip: unadjusted +0.050 [-0.010, +0.114]; adjusted for minS +0.011 [-0.044, +0.071]; adjusted for minS and meanS +0.017 -> lexical
  rank correlation of the dip with minS: moral -0.04, norm -0.00, all -0.01
  timing (moral, n=27): dip minimum at depth 0.89 (median), edit arrives at 0.75; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.01
  timing (norm, n=29): dip minimum at depth 0.89 (median), edit arrives at 0.75; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.38
* B: dip means moral 0.213, norm 0.060; word negativity (minS) moral -0.188, norm -0.007, descr +0.030
  moral - norm dip: unadjusted +0.153 [+0.058, +0.253]; adjusted for minS +0.104 [+0.005, +0.204]; adjusted for minS and meanS +0.122 -> moral content
  rank correlation of the dip with minS: moral -0.22, norm -0.07, all -0.12
  timing (moral, n=19): dip minimum at depth 0.93 (median), edit arrives at 0.68; minimum before arrival in 0% of pairs; arrival at or before half depth in 16% (there the dip window starts after the arrival by construction); rank corr. -0.17
  timing (norm, n=7): dip minimum at depth 0.93 (median), edit arrives at 0.68; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.21

## Qwen2.5-7B-Instruct

* A1: dip means moral 0.155, norm 0.177; word negativity (minS) moral -0.137, norm -0.019, descr +0.006
  moral - norm dip: unadjusted -0.022 [-0.100, +0.062]; adjusted for minS -0.037 [-0.122, +0.053]; adjusted for minS and meanS -0.034 -> no moral excess to explain
  rank correlation of the dip with minS: moral +0.17, norm -0.14, all +0.00
  timing (moral, n=29): dip minimum at depth 0.96 (median), edit arrives at 0.75; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.26
  timing (norm, n=52): dip minimum at depth 0.89 (median), edit arrives at 0.79; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.16
* B: dip means moral 0.184, norm 0.043; word negativity (minS) moral -0.149, norm -0.019, descr +0.006
  moral - norm dip: unadjusted +0.141 [+0.047, +0.238]; adjusted for minS +0.071 [-0.013, +0.158]; adjusted for minS and meanS +0.086 -> mixed
  rank correlation of the dip with minS: moral -0.24, norm -0.04, all -0.10
  timing (moral, n=16): dip minimum at depth 0.93 (median), edit arrives at 0.68; minimum before arrival in 0% of pairs; arrival at or before half depth in 31% (there the dip window starts after the arrival by construction); rank corr. 0.41
  timing (norm, n=5): dip minimum at depth 0.89 (median), edit arrives at 0.68; minimum before arrival in 0% of pairs; arrival at or before half depth in 20% (there the dip window starts after the arrival by construction); rank corr. 0.0

## gemma-2b

* A1: dip means moral 0.001, norm 0.000; word negativity (minS) moral -0.018, norm +0.052, descr +0.080
  moral - norm dip: unadjusted +0.001 [+0.000, +0.002]; adjusted for minS +0.001 [+0.000, +0.002]; adjusted for minS and meanS +0.001 -> moral content
  rank correlation of the dip with minS: moral -0.18, norm -0.20, all -0.17
* B: dip means moral 0.003, norm 0.004; word negativity (minS) moral -0.010, norm +0.046, descr +0.079
  moral - norm dip: unadjusted -0.002 [-0.011, +0.004]; adjusted for minS -0.004 [-0.017, +0.004]; adjusted for minS and meanS -0.004 -> no moral excess to explain
  rank correlation of the dip with minS: moral -0.32, norm -0.15, all -0.34

## gemma-2b-it

* A1: dip means moral 0.766, norm 0.661; word negativity (minS) moral -0.090, norm -0.083, descr -0.010
  moral - norm dip: unadjusted +0.105 [-0.081, +0.293]; adjusted for minS +0.097 [-0.084, +0.277]; adjusted for minS and meanS +0.081 -> mixed
  rank correlation of the dip with minS: moral -0.34, norm -0.16, all -0.23
  timing (moral, n=48): dip minimum at depth 0.89 (median), edit arrives at 0.78; minimum before arrival in 4% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.4
  timing (norm, n=60): dip minimum at depth 0.89 (median), edit arrives at 0.78; minimum before arrival in 3% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.24
* B: dip means moral 0.115, norm 0.039; word negativity (minS) moral -0.085, norm -0.081, descr -0.011
  moral - norm dip: unadjusted +0.076 [-0.004, +0.162]; adjusted for minS +0.074 [-0.003, +0.159]; adjusted for minS and meanS +0.069 -> mixed
  rank correlation of the dip with minS: moral -0.12, norm -0.06, all -0.15
  timing (moral, n=9): dip minimum at depth 0.94 (median), edit arrives at 0.72; minimum before arrival in 0% of pairs; arrival at or before half depth in 0% (there the dip window starts after the arrival by construction); rank corr. 0.5
  timing (norm, n=10): dip minimum at depth 0.92 (median), edit arrives at 0.58; minimum before arrival in 0% of pairs; arrival at or before half depth in 30% (there the dip window starts after the arrival by construction); rank corr. 0.78

## Count of models per reading

* frame A1: lexical 5, mixed 4, moral content 4, no moral excess to explain 1
* frame B: lexical 4, mixed 7, moral content 1, no moral excess to explain 2
