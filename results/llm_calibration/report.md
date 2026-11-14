# AI annotators checked against the human panel (242 pairs of the main study)

Models: anthropic (claude-sonnet-5-5), openai (gpt-5.5), google (gemini-3.1-pro-preview); raters: R1, R2, R3, R4, R5. Pairs: 242 (89 moral, 113 norm, 40 descriptive). Answers parsed: anthropic 242, openai 242, google 242.

Checks: the rule as written here reproduces the panel's decisions on all 242 pairs, and llm_annotate.py's decisions for the models: identical on all pairs. Agreement of the raters on the main round, recomputed here (must equal the main rating report): better option (nominal) 0.975, class of standard, all letters incl. ties (nominal) 0.766, class M / non-moral norm / N, ties left out (nominal) 0.869, class as the rule reads it (M / norm / N / mixed; nominal) 0.822, moral rating (ordinal 0-3) 0.884.

## Primary: the alternative annotator test

eps = 0.1, one-sided paired t-tests, Benjamini-Yekutieli over the 5 raters at q = 0.05; a model passes a label when it wins against at least half of the raters (omega >= 0.5).

| model | label | omega (raters won) | passed | average advantage probability | per rater: rho_model / rho_rater (won?) |
|---|---|---|---|---|---|
| anthropic | class (primary) | 1.0 | yes | 1.000 | R1 1.00/0.98 (won); R2 1.00/0.97 (won); R3 1.00/0.91 (won); R4 1.00/0.97 (won); R5 1.00/0.82 (won) |
| anthropic | better (primary) | 1.0 | yes | 1.000 | R1 1.00/1.00 (won); R2 1.00/1.00 (won); R3 1.00/1.00 (won); R4 1.00/1.00 (won); R5 1.00/0.98 (won) |
| anthropic | class_fine | 1.0 | yes | 0.988 | R1 1.00/0.95 (won); R2 0.98/0.90 (won); R3 0.99/0.85 (won); R4 0.99/0.94 (won); R5 0.98/0.78 (won) |
| anthropic | moral_rating | 1.0 | yes | 0.988 | R1 0.98/0.95 (won); R2 0.99/0.75 (won); R3 1.00/0.95 (won); R4 0.99/0.94 (won); R5 0.99/0.88 (won) |
| anthropic | verdict (primary) | 1.0 | yes | 0.986 | R1 0.99/0.97 (won); R2 0.98/0.91 (won); R3 0.98/0.93 (won); R4 0.99/0.97 (won); R5 0.99/0.76 (won) |
| openai | class (primary) | 1.0 | yes | 0.984 | R1 0.98/0.98 (won); R2 0.98/0.97 (won); R3 0.98/0.92 (won); R4 0.98/0.97 (won); R5 0.99/0.83 (won) |
| openai | better (primary) | 1.0 | yes | 0.984 | R1 0.98/1.00 (won); R2 0.98/1.00 (won); R3 0.98/1.00 (won); R4 0.98/1.00 (won); R5 0.98/0.98 (won) |
| openai | class_fine | 1.0 | yes | 0.970 | R1 0.98/0.94 (won); R2 0.97/0.91 (won); R3 0.98/0.86 (won); R4 0.96/0.93 (won); R5 0.97/0.79 (won) |
| openai | moral_rating | 1.0 | yes | 0.962 | R1 0.96/0.95 (won); R2 0.96/0.76 (won); R3 0.97/0.95 (won); R4 0.96/0.95 (won); R5 0.96/0.88 (won) |
| openai | verdict (primary) | 1.0 | yes | 0.955 | R1 0.95/0.96 (won); R2 0.95/0.92 (won); R3 0.95/0.93 (won); R4 0.95/0.97 (won); R5 0.96/0.77 (won) |
| google | class (primary) | 1.0 | yes | 0.992 | R1 0.99/0.98 (won); R2 0.99/0.97 (won); R3 0.99/0.92 (won); R4 0.99/0.98 (won); R5 0.99/0.83 (won) |
| google | better (primary) | 1.0 | yes | 1.000 | R1 1.00/1.00 (won); R2 1.00/1.00 (won); R3 1.00/1.00 (won); R4 1.00/1.00 (won); R5 1.00/0.98 (won) |
| google | class_fine | 1.0 | yes | 0.979 | R1 0.99/0.95 (won); R2 0.98/0.91 (won); R3 0.98/0.86 (won); R4 0.98/0.95 (won); R5 0.98/0.78 (won) |
| google | moral_rating | 1.0 | yes | 0.969 | R1 0.97/0.96 (won); R2 0.97/0.76 (won); R3 0.97/0.95 (won); R4 0.97/0.94 (won); R5 0.97/0.88 (won) |
| google | verdict (primary) | 1.0 | yes | 0.986 | R1 0.98/0.98 (won); R2 0.98/0.91 (won); R3 0.98/0.94 (won); R4 0.99/0.98 (won); R5 0.99/0.77 (won) |

**Outcome: all three models pass all three primary labels.** The follow-up sets are reported as annotated by the three models, checked against the human panel by this test.

How one of our raters fares in the same test against the other four (context; omega with four raters):

| rater | class | better | class_fine | moral_rating | verdict |
|---|---|---|---|---|---|
| R1 | omega 1.00, AP 0.985 | omega 1.00, AP 0.996 | omega 1.00, AP 0.939 | omega 1.00, AP 0.954 | omega 1.00, AP 0.963 |
| R2 | omega 1.00, AP 0.975 | omega 1.00, AP 0.996 | omega 1.00, AP 0.939 | omega 0.00, AP 0.773 | omega 1.00, AP 0.918 |
| R3 | omega 1.00, AP 0.931 | omega 1.00, AP 1.000 | omega 0.25, AP 0.892 | omega 1.00, AP 0.942 | omega 1.00, AP 0.939 |
| R4 | omega 1.00, AP 0.974 | omega 1.00, AP 0.996 | omega 1.00, AP 0.947 | omega 1.00, AP 0.943 | omega 1.00, AP 0.966 |
| R5 | omega 0.00, AP 0.833 | omega 1.00, AP 0.983 | omega 0.00, AP 0.819 | omega 0.25, AP 0.894 | omega 0.00, AP 0.773 |

## Keep-or-drop decisions

The three models as a panel (two of three, the study's rule) against the five raters' decisions: agreement 0.942, Cohen's kappa 0.118. Both keep 227, only the raters keep 0, only the models keep 14, both drop 1 (the raters drop 15 of 242).

Three of the five raters as a panel, same rule, against the five raters' decisions (they are part of that panel, so this favours them):

| panel | agreement | kappa | keeps, of the 15 the five dropped | drops, of the 227 the five kept |
|---|---|---|---|---|
| raters 123 | 0.946 | 0.409 | 10 | 3 |
| raters 124 | 0.934 | 0.092 | 14 | 2 |
| raters 125 | 0.946 | 0.409 | 10 | 3 |
| raters 134 | 0.955 | 0.457 | 10 | 1 |
| raters 135 | 0.971 | 0.726 | 5 | 2 |
| raters 145 | 0.955 | 0.457 | 10 | 1 |
| raters 234 | 0.955 | 0.500 | 9 | 2 |
| raters 235 | 0.979 | 0.817 | 3 | 2 |
| raters 245 | 0.963 | 0.621 | 7 | 2 |
| raters 345 | 0.983 | 0.838 | 4 | 0 |
| the three models | 0.942 | 0.118 | 14 | 0 |

Models and raters judged against the same reference (each of the ten splits of the raters into three and two; the reference is the other two raters under the study's rule for two raters, i.e. both): mean agreement of the models 0.833, of the three raters 0.819; difference +0.013 (95 % bootstrap interval over pairs -0.002 to +0.028).

| split: panel / reference | reference keeps | models agree | three raters agree |
|---|---|---|---|
| 123 / 45 | 173 | 0.719 | 0.715 |
| 124 / 35 | 170 | 0.707 | 0.698 |
| 125 / 34 | 215 | 0.893 | 0.872 |
| 134 / 25 | 172 | 0.715 | 0.711 |
| 135 / 24 | 223 | 0.926 | 0.905 |
| 145 / 23 | 211 | 0.876 | 0.872 |
| 234 / 15 | 174 | 0.723 | 0.727 |
| 235 / 14 | 226 | 0.938 | 0.901 |
| 245 / 13 | 215 | 0.893 | 0.880 |
| 345 / 12 | 226 | 0.938 | 0.913 |

By category (kept by the raters / by the models): moral 80 / 89 of 89; norm 107 / 112 of 113; descr 40 / 40 of 40.

Pairs whose class the models read differently from a majority of the raters (at least three of five): anthropic 0; openai 4; google 5 (listed in pairs.csv).

## Answer profiles

| annotator | intended version | other version | no clear difference | unclear | Q3 = N, descriptive pairs | Q3 = N, other pairs | mean moral rating: moral / norm / descriptive pairs |
|---|---|---|---|---|---|---|---|
| R1 | 0.996 | 0.000 | 0.004 | 0.000 | 1.000 | 0.000 | 2.98 / 0.16 / 0.00 |
| R2 | 0.996 | 0.004 | 0.000 | 0.000 | 1.000 | 0.005 | 2.63 / 0.52 / 0.00 |
| R3 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.030 | 2.92 / 0.26 / 0.00 |
| R4 | 0.996 | 0.000 | 0.004 | 0.004 | 1.000 | 0.000 | 2.90 / 0.17 / 0.00 |
| R5 | 0.983 | 0.012 | 0.004 | 0.062 | 0.475 | 0.050 | 2.61 / 0.08 / 0.00 |
| anthropic | 1.000 | 0.000 | 0.000 | 0.004 | 1.000 | 0.000 | 3.00 / 0.13 / 0.00 |
| openai | 0.983 | 0.017 | 0.000 | 0.012 | 0.900 | 0.000 | 3.00 / 0.18 / 0.07 |
| google | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 3.00 / 0.18 / 0.00 |

## Agreement (Krippendorff's alpha)

| raters | better option (nominal) | class of standard, all letters incl. ties (nominal) | class M / non-moral norm / N, ties left out (nominal) | class as the rule reads it (M / norm / N / mixed; nominal) | moral rating (ordinal 0-3) |
|---|---|---|---|---|---|
| the five raters | 0.977 | 0.738 | 0.851 | 0.802 | 0.883 |
| the five raters + anthropic | 0.981 | 0.770 | 0.876 | 0.831 | 0.897 |
| the five raters + openai | 0.969 | 0.763 | 0.868 | 0.823 | 0.889 |
| the five raters + google | 0.981 | 0.765 | 0.876 | 0.826 | 0.892 |
| the five raters + all models | 0.977 | 0.806 | 0.901 | 0.859 | 0.908 |
| the models only | 0.978 | 0.949 | 0.982 | 0.956 | 0.963 |

Limits of the check: the raters chose the intended version in 1203 of 1210 answers and saw no clear difference in 3, so the check says little about how the models judge pairs without a better option (the follow-up's conduct controls). The five raters kept 227 of 242 pairs, and three of them, under the same rule, would have kept between 3 and 14 of the 15 they dropped: most drops come from one or two raters, so the check says little about whether the models drop the pairs that people would agree to drop; it shows whether they read the pairs as our raters do. The models' answers are sampled at each provider's default and are not deterministic; this is the one run that is compared.

