# Standard or topic? The twins

Paired accuracy: share of twins in which the moral member gets the larger moral score (chance 0.5); models at p < 0.05 by a one-sided sign test.

## Summary (medians over models)

| part | frame | subset | feature | models | median paired accuracy | models with p < 0.05 |
|---|---|---|---|---|---|---|
| category prompt | - | all twins | moral words | 14 | 0.843 | 13 |
| category prompt | - | all twins | words of the other standard | 14 | 0.686 | 11 |
| category prompt | - | both members passed | moral words | 14 | 0.804 | 12 |
| category prompt | - | both members passed | words of the other standard | 14 | 0.630 | 5 |
| transfer | A1 | all twins | hidden, after the located heads | 14 | 0.900 | 14 |
| transfer | A1 | all twins | hidden, last layer | 14 | 0.900 | 14 |
| transfer | A1 | all twins | located heads write | 14 | 0.886 | 13 |
| transfer | A1 | all twins | random sets (median of 20) | 14 | 0.886 | 14 (median set) |
| transfer | A1 | both members passed | hidden, after the located heads | 14 | 0.891 | 13 |
| transfer | A1 | both members passed | hidden, last layer | 14 | 0.891 | 13 |
| transfer | A1 | both members passed | located heads write | 14 | 0.870 | 11 |
| transfer | A1 | both members passed | random sets (median of 20) | 14 | 0.935 | 14 (median set) |
| transfer | B | all twins | hidden, after the located heads | 14 | 0.914 | 14 |
| transfer | B | all twins | hidden, last layer | 14 | 0.900 | 14 |
| transfer | B | all twins | located heads write | 14 | 0.786 | 12 |
| transfer | B | all twins | random sets (median of 20) | 14 | 0.829 | 14 (median set) |
| transfer | B | both members passed | hidden, after the located heads | 14 | 0.913 | 14 |
| transfer | B | both members passed | hidden, last layer | 14 | 0.913 | 14 |
| transfer | B | both members passed | located heads write | 14 | 0.804 | 10 |
| transfer | B | both members passed | random sets (median of 20) | 14 | 0.870 | 14 (median set) |

## Per model (not random sets)

| part | model | frame | subset | feature | twins | wins | paired accuracy | p |
|---|---|---|---|---|---|---|---|---|
| category prompt | Llama-3.1-8B | - | all twins | moral words | 35 | 31 | 0.886 | 0.000 |
| category prompt | Llama-3.1-8B | - | all twins | words of the other standard | 35 | 28 | 0.800 | 0.000 |
| category prompt | Llama-3.1-8B | - | both members passed | moral words | 23 | 20 | 0.870 | 0.000 |
| category prompt | Llama-3.1-8B | - | both members passed | words of the other standard | 23 | 18 | 0.783 | 0.005 |
| category prompt | Llama-3.1-8B-Instruct | - | all twins | moral words | 35 | 33 | 0.943 | 0.000 |
| category prompt | Llama-3.1-8B-Instruct | - | all twins | words of the other standard | 35 | 30 | 0.857 | 0.000 |
| category prompt | Llama-3.1-8B-Instruct | - | both members passed | moral words | 23 | 22 | 0.957 | 0.000 |
| category prompt | Llama-3.1-8B-Instruct | - | both members passed | words of the other standard | 23 | 20 | 0.870 | 0.000 |
| category prompt | Llama-3.2-1B | - | all twins | moral words | 35 | 27 | 0.771 | 0.001 |
| category prompt | Llama-3.2-1B | - | all twins | words of the other standard | 35 | 24 | 0.686 | 0.020 |
| category prompt | Llama-3.2-1B | - | both members passed | moral words | 23 | 16 | 0.696 | 0.047 |
| category prompt | Llama-3.2-1B | - | both members passed | words of the other standard | 23 | 13 | 0.565 | 0.339 |
| category prompt | Llama-3.2-1B-Instruct | - | all twins | moral words | 35 | 30 | 0.857 | 0.000 |
| category prompt | Llama-3.2-1B-Instruct | - | all twins | words of the other standard | 35 | 27 | 0.771 | 0.001 |
| category prompt | Llama-3.2-1B-Instruct | - | both members passed | moral words | 23 | 19 | 0.826 | 0.001 |
| category prompt | Llama-3.2-1B-Instruct | - | both members passed | words of the other standard | 23 | 17 | 0.739 | 0.017 |
| category prompt | Llama-3.2-3B | - | all twins | moral words | 35 | 30 | 0.857 | 0.000 |
| category prompt | Llama-3.2-3B | - | all twins | words of the other standard | 35 | 28 | 0.800 | 0.000 |
| category prompt | Llama-3.2-3B | - | both members passed | moral words | 23 | 18 | 0.783 | 0.005 |
| category prompt | Llama-3.2-3B | - | both members passed | words of the other standard | 23 | 17 | 0.739 | 0.017 |
| category prompt | Llama-3.2-3B-Instruct | - | all twins | moral words | 35 | 33 | 0.943 | 0.000 |
| category prompt | Llama-3.2-3B-Instruct | - | all twins | words of the other standard | 35 | 26 | 0.743 | 0.003 |
| category prompt | Llama-3.2-3B-Instruct | - | both members passed | moral words | 23 | 21 | 0.913 | 0.000 |
| category prompt | Llama-3.2-3B-Instruct | - | both members passed | words of the other standard | 23 | 15 | 0.652 | 0.105 |
| category prompt | Qwen2.5-14B | - | all twins | moral words | 35 | 33 | 0.943 | 0.000 |
| category prompt | Qwen2.5-14B | - | all twins | words of the other standard | 35 | 24 | 0.686 | 0.020 |
| category prompt | Qwen2.5-14B | - | both members passed | moral words | 23 | 22 | 0.957 | 0.000 |
| category prompt | Qwen2.5-14B | - | both members passed | words of the other standard | 23 | 15 | 0.652 | 0.105 |
| category prompt | Qwen2.5-14B-Instruct | - | all twins | moral words | 35 | 32 | 0.914 | 0.000 |
| category prompt | Qwen2.5-14B-Instruct | - | all twins | words of the other standard | 35 | 23 | 0.657 | 0.045 |
| category prompt | Qwen2.5-14B-Instruct | - | both members passed | moral words | 23 | 21 | 0.913 | 0.000 |
| category prompt | Qwen2.5-14B-Instruct | - | both members passed | words of the other standard | 23 | 13 | 0.565 | 0.339 |
| category prompt | Qwen2.5-3B | - | all twins | moral words | 35 | 21 | 0.600 | 0.155 |
| category prompt | Qwen2.5-3B | - | all twins | words of the other standard | 35 | 20 | 0.571 | 0.250 |
| category prompt | Qwen2.5-3B | - | both members passed | moral words | 23 | 12 | 0.522 | 0.500 |
| category prompt | Qwen2.5-3B | - | both members passed | words of the other standard | 23 | 12 | 0.522 | 0.500 |
| category prompt | Qwen2.5-3B-Instruct | - | all twins | moral words | 35 | 26 | 0.743 | 0.003 |
| category prompt | Qwen2.5-3B-Instruct | - | all twins | words of the other standard | 35 | 22 | 0.629 | 0.088 |
| category prompt | Qwen2.5-3B-Instruct | - | both members passed | moral words | 23 | 14 | 0.609 | 0.202 |
| category prompt | Qwen2.5-3B-Instruct | - | both members passed | words of the other standard | 23 | 12 | 0.522 | 0.500 |
| category prompt | Qwen2.5-7B | - | all twins | moral words | 35 | 29 | 0.829 | 0.000 |
| category prompt | Qwen2.5-7B | - | all twins | words of the other standard | 35 | 23 | 0.657 | 0.045 |
| category prompt | Qwen2.5-7B | - | both members passed | moral words | 23 | 19 | 0.826 | 0.001 |
| category prompt | Qwen2.5-7B | - | both members passed | words of the other standard | 23 | 12 | 0.522 | 0.500 |
| category prompt | Qwen2.5-7B-Instruct | - | all twins | moral words | 35 | 28 | 0.800 | 0.000 |
| category prompt | Qwen2.5-7B-Instruct | - | all twins | words of the other standard | 35 | 21 | 0.600 | 0.155 |
| category prompt | Qwen2.5-7B-Instruct | - | both members passed | moral words | 23 | 18 | 0.783 | 0.005 |
| category prompt | Qwen2.5-7B-Instruct | - | both members passed | words of the other standard | 23 | 12 | 0.522 | 0.500 |
| category prompt | gemma-2b | - | all twins | moral words | 35 | 26 | 0.743 | 0.003 |
| category prompt | gemma-2b | - | all twins | words of the other standard | 35 | 23 | 0.657 | 0.045 |
| category prompt | gemma-2b | - | both members passed | moral words | 23 | 17 | 0.739 | 0.017 |
| category prompt | gemma-2b | - | both members passed | words of the other standard | 23 | 14 | 0.609 | 0.202 |
| category prompt | gemma-2b-it | - | all twins | moral words | 35 | 29 | 0.829 | 0.000 |
| category prompt | gemma-2b-it | - | all twins | words of the other standard | 35 | 29 | 0.829 | 0.000 |
| category prompt | gemma-2b-it | - | both members passed | moral words | 23 | 18 | 0.783 | 0.005 |
| category prompt | gemma-2b-it | - | both members passed | words of the other standard | 23 | 18 | 0.783 | 0.005 |
| transfer | Llama-3.1-8B | A1 | all twins | located heads write | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.1-8B | A1 | both members passed | located heads write | 23 | 23 | 1.000 | 0.000 |
| transfer | Llama-3.1-8B | A1 | all twins | hidden, after the located heads | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.1-8B | A1 | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.1-8B | A1 | all twins | hidden, last layer | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.1-8B | A1 | both members passed | hidden, last layer | 23 | 23 | 1.000 | 0.000 |
| transfer | Llama-3.1-8B | B | all twins | located heads write | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.1-8B | B | both members passed | located heads write | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.1-8B | B | all twins | hidden, after the located heads | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.1-8B | B | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.1-8B | B | all twins | hidden, last layer | 35 | 31 | 0.886 | 0.000 |
| transfer | Llama-3.1-8B | B | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | A1 | all twins | located heads write | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | A1 | both members passed | located heads write | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | A1 | all twins | hidden, after the located heads | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | A1 | both members passed | hidden, after the located heads | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | A1 | all twins | hidden, last layer | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | A1 | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | B | all twins | located heads write | 35 | 31 | 0.886 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | B | both members passed | located heads write | 23 | 20 | 0.870 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | B | all twins | hidden, after the located heads | 35 | 35 | 1.000 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | B | both members passed | hidden, after the located heads | 23 | 23 | 1.000 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | B | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.1-8B-Instruct | B | both members passed | hidden, last layer | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.2-1B | A1 | all twins | located heads write | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.2-1B | A1 | both members passed | located heads write | 23 | 23 | 1.000 | 0.000 |
| transfer | Llama-3.2-1B | A1 | all twins | hidden, after the located heads | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-1B | A1 | both members passed | hidden, after the located heads | 23 | 23 | 1.000 | 0.000 |
| transfer | Llama-3.2-1B | A1 | all twins | hidden, last layer | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.2-1B | A1 | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B | B | all twins | located heads write | 35 | 31 | 0.886 | 0.000 |
| transfer | Llama-3.2-1B | B | both members passed | located heads write | 23 | 20 | 0.870 | 0.000 |
| transfer | Llama-3.2-1B | B | all twins | hidden, after the located heads | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-1B | B | both members passed | hidden, after the located heads | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B | B | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-1B | B | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | A1 | all twins | located heads write | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | A1 | both members passed | located heads write | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | A1 | all twins | hidden, after the located heads | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | A1 | both members passed | hidden, after the located heads | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | A1 | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | A1 | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | B | all twins | located heads write | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | B | both members passed | located heads write | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | B | all twins | hidden, after the located heads | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | B | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | B | all twins | hidden, last layer | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.2-1B-Instruct | B | both members passed | hidden, last layer | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.2-3B | A1 | all twins | located heads write | 35 | 32 | 0.914 | 0.000 |
| transfer | Llama-3.2-3B | A1 | both members passed | located heads write | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.2-3B | A1 | all twins | hidden, after the located heads | 35 | 31 | 0.886 | 0.000 |
| transfer | Llama-3.2-3B | A1 | both members passed | hidden, after the located heads | 23 | 20 | 0.870 | 0.000 |
| transfer | Llama-3.2-3B | A1 | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-3B | A1 | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-3B | B | all twins | located heads write | 35 | 31 | 0.886 | 0.000 |
| transfer | Llama-3.2-3B | B | both members passed | located heads write | 23 | 20 | 0.870 | 0.000 |
| transfer | Llama-3.2-3B | B | all twins | hidden, after the located heads | 35 | 31 | 0.886 | 0.000 |
| transfer | Llama-3.2-3B | B | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.2-3B | B | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-3B | B | both members passed | hidden, last layer | 23 | 21 | 0.913 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | A1 | all twins | located heads write | 35 | 30 | 0.857 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | A1 | both members passed | located heads write | 23 | 19 | 0.826 | 0.001 |
| transfer | Llama-3.2-3B-Instruct | A1 | all twins | hidden, after the located heads | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | A1 | both members passed | hidden, after the located heads | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | A1 | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | A1 | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | B | all twins | located heads write | 35 | 28 | 0.800 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | B | both members passed | located heads write | 23 | 18 | 0.783 | 0.005 |
| transfer | Llama-3.2-3B-Instruct | B | all twins | hidden, after the located heads | 35 | 35 | 1.000 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | B | both members passed | hidden, after the located heads | 23 | 23 | 1.000 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | B | all twins | hidden, last layer | 35 | 34 | 0.971 | 0.000 |
| transfer | Llama-3.2-3B-Instruct | B | both members passed | hidden, last layer | 23 | 23 | 1.000 | 0.000 |
| transfer | Qwen2.5-14B | A1 | all twins | located heads write | 35 | 23 | 0.657 | 0.045 |
| transfer | Qwen2.5-14B | A1 | both members passed | located heads write | 23 | 14 | 0.609 | 0.202 |
| transfer | Qwen2.5-14B | A1 | all twins | hidden, after the located heads | 35 | 30 | 0.857 | 0.000 |
| transfer | Qwen2.5-14B | A1 | both members passed | hidden, after the located heads | 23 | 19 | 0.826 | 0.001 |
| transfer | Qwen2.5-14B | A1 | all twins | hidden, last layer | 35 | 31 | 0.886 | 0.000 |
| transfer | Qwen2.5-14B | A1 | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-14B | B | all twins | located heads write | 35 | 20 | 0.571 | 0.250 |
| transfer | Qwen2.5-14B | B | both members passed | located heads write | 23 | 13 | 0.565 | 0.339 |
| transfer | Qwen2.5-14B | B | all twins | hidden, after the located heads | 35 | 33 | 0.943 | 0.000 |
| transfer | Qwen2.5-14B | B | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | Qwen2.5-14B | B | all twins | hidden, last layer | 35 | 31 | 0.886 | 0.000 |
| transfer | Qwen2.5-14B | B | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | A1 | all twins | located heads write | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | A1 | both members passed | located heads write | 23 | 18 | 0.783 | 0.005 |
| transfer | Qwen2.5-14B-Instruct | A1 | all twins | hidden, after the located heads | 35 | 32 | 0.914 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | A1 | both members passed | hidden, after the located heads | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | A1 | all twins | hidden, last layer | 35 | 32 | 0.914 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | A1 | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | B | all twins | located heads write | 35 | 25 | 0.714 | 0.008 |
| transfer | Qwen2.5-14B-Instruct | B | both members passed | located heads write | 23 | 16 | 0.696 | 0.047 |
| transfer | Qwen2.5-14B-Instruct | B | all twins | hidden, after the located heads | 35 | 32 | 0.914 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | B | both members passed | hidden, after the located heads | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | B | all twins | hidden, last layer | 35 | 33 | 0.943 | 0.000 |
| transfer | Qwen2.5-14B-Instruct | B | both members passed | hidden, last layer | 23 | 21 | 0.913 | 0.000 |
| transfer | Qwen2.5-3B | A1 | all twins | located heads write | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-3B | A1 | both members passed | located heads write | 23 | 18 | 0.783 | 0.005 |
| transfer | Qwen2.5-3B | A1 | all twins | hidden, after the located heads | 35 | 30 | 0.857 | 0.000 |
| transfer | Qwen2.5-3B | A1 | both members passed | hidden, after the located heads | 23 | 19 | 0.826 | 0.001 |
| transfer | Qwen2.5-3B | A1 | all twins | hidden, last layer | 35 | 28 | 0.800 | 0.000 |
| transfer | Qwen2.5-3B | A1 | both members passed | hidden, last layer | 23 | 18 | 0.783 | 0.005 |
| transfer | Qwen2.5-3B | B | all twins | located heads write | 35 | 24 | 0.686 | 0.020 |
| transfer | Qwen2.5-3B | B | both members passed | located heads write | 23 | 14 | 0.609 | 0.202 |
| transfer | Qwen2.5-3B | B | all twins | hidden, after the located heads | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-3B | B | both members passed | hidden, after the located heads | 23 | 19 | 0.826 | 0.001 |
| transfer | Qwen2.5-3B | B | all twins | hidden, last layer | 35 | 23 | 0.657 | 0.045 |
| transfer | Qwen2.5-3B | B | both members passed | hidden, last layer | 23 | 16 | 0.696 | 0.047 |
| transfer | Qwen2.5-3B-Instruct | A1 | all twins | located heads write | 35 | 22 | 0.629 | 0.088 |
| transfer | Qwen2.5-3B-Instruct | A1 | both members passed | located heads write | 23 | 11 | 0.478 | 0.661 |
| transfer | Qwen2.5-3B-Instruct | A1 | all twins | hidden, after the located heads | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-3B-Instruct | A1 | both members passed | hidden, after the located heads | 23 | 18 | 0.783 | 0.005 |
| transfer | Qwen2.5-3B-Instruct | A1 | all twins | hidden, last layer | 35 | 31 | 0.886 | 0.000 |
| transfer | Qwen2.5-3B-Instruct | A1 | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-3B-Instruct | B | all twins | located heads write | 35 | 22 | 0.629 | 0.088 |
| transfer | Qwen2.5-3B-Instruct | B | both members passed | located heads write | 23 | 13 | 0.565 | 0.339 |
| transfer | Qwen2.5-3B-Instruct | B | all twins | hidden, after the located heads | 35 | 28 | 0.800 | 0.000 |
| transfer | Qwen2.5-3B-Instruct | B | both members passed | hidden, after the located heads | 23 | 16 | 0.696 | 0.047 |
| transfer | Qwen2.5-3B-Instruct | B | all twins | hidden, last layer | 35 | 32 | 0.914 | 0.000 |
| transfer | Qwen2.5-3B-Instruct | B | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-7B | A1 | all twins | located heads write | 35 | 26 | 0.743 | 0.003 |
| transfer | Qwen2.5-7B | A1 | both members passed | located heads write | 23 | 15 | 0.652 | 0.105 |
| transfer | Qwen2.5-7B | A1 | all twins | hidden, after the located heads | 35 | 25 | 0.714 | 0.008 |
| transfer | Qwen2.5-7B | A1 | both members passed | hidden, after the located heads | 23 | 15 | 0.652 | 0.105 |
| transfer | Qwen2.5-7B | A1 | all twins | hidden, last layer | 35 | 26 | 0.743 | 0.003 |
| transfer | Qwen2.5-7B | A1 | both members passed | hidden, last layer | 23 | 15 | 0.652 | 0.105 |
| transfer | Qwen2.5-7B | B | all twins | located heads write | 35 | 25 | 0.714 | 0.008 |
| transfer | Qwen2.5-7B | B | both members passed | located heads write | 23 | 14 | 0.609 | 0.202 |
| transfer | Qwen2.5-7B | B | all twins | hidden, after the located heads | 35 | 32 | 0.914 | 0.000 |
| transfer | Qwen2.5-7B | B | both members passed | hidden, after the located heads | 23 | 20 | 0.870 | 0.000 |
| transfer | Qwen2.5-7B | B | all twins | hidden, last layer | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-7B | B | both members passed | hidden, last layer | 23 | 19 | 0.826 | 0.001 |
| transfer | Qwen2.5-7B-Instruct | A1 | all twins | located heads write | 35 | 33 | 0.943 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | A1 | both members passed | located heads write | 23 | 23 | 1.000 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | A1 | all twins | hidden, after the located heads | 35 | 30 | 0.857 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | A1 | both members passed | hidden, after the located heads | 23 | 18 | 0.783 | 0.005 |
| transfer | Qwen2.5-7B-Instruct | A1 | all twins | hidden, last layer | 35 | 30 | 0.857 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | A1 | both members passed | hidden, last layer | 23 | 18 | 0.783 | 0.005 |
| transfer | Qwen2.5-7B-Instruct | B | all twins | located heads write | 35 | 27 | 0.771 | 0.001 |
| transfer | Qwen2.5-7B-Instruct | B | both members passed | located heads write | 23 | 19 | 0.826 | 0.001 |
| transfer | Qwen2.5-7B-Instruct | B | all twins | hidden, after the located heads | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | B | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | B | all twins | hidden, last layer | 35 | 29 | 0.829 | 0.000 |
| transfer | Qwen2.5-7B-Instruct | B | both members passed | hidden, last layer | 23 | 21 | 0.913 | 0.000 |
| transfer | gemma-2b | A1 | all twins | located heads write | 35 | 30 | 0.857 | 0.000 |
| transfer | gemma-2b | A1 | both members passed | located heads write | 23 | 19 | 0.826 | 0.001 |
| transfer | gemma-2b | A1 | all twins | hidden, after the located heads | 35 | 31 | 0.886 | 0.000 |
| transfer | gemma-2b | A1 | both members passed | hidden, after the located heads | 23 | 21 | 0.913 | 0.000 |
| transfer | gemma-2b | A1 | all twins | hidden, last layer | 35 | 28 | 0.800 | 0.000 |
| transfer | gemma-2b | A1 | both members passed | hidden, last layer | 23 | 20 | 0.870 | 0.000 |
| transfer | gemma-2b | B | all twins | located heads write | 35 | 27 | 0.771 | 0.001 |
| transfer | gemma-2b | B | both members passed | located heads write | 23 | 18 | 0.783 | 0.005 |
| transfer | gemma-2b | B | all twins | hidden, after the located heads | 35 | 29 | 0.829 | 0.000 |
| transfer | gemma-2b | B | both members passed | hidden, after the located heads | 23 | 19 | 0.826 | 0.001 |
| transfer | gemma-2b | B | all twins | hidden, last layer | 35 | 30 | 0.857 | 0.000 |
| transfer | gemma-2b | B | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
| transfer | gemma-2b-it | A1 | all twins | located heads write | 35 | 32 | 0.914 | 0.000 |
| transfer | gemma-2b-it | A1 | both members passed | located heads write | 23 | 21 | 0.913 | 0.000 |
| transfer | gemma-2b-it | A1 | all twins | hidden, after the located heads | 35 | 32 | 0.914 | 0.000 |
| transfer | gemma-2b-it | A1 | both members passed | hidden, after the located heads | 23 | 23 | 1.000 | 0.000 |
| transfer | gemma-2b-it | A1 | all twins | hidden, last layer | 35 | 29 | 0.829 | 0.000 |
| transfer | gemma-2b-it | A1 | both members passed | hidden, last layer | 23 | 21 | 0.913 | 0.000 |
| transfer | gemma-2b-it | B | all twins | located heads write | 35 | 30 | 0.857 | 0.000 |
| transfer | gemma-2b-it | B | both members passed | located heads write | 23 | 20 | 0.870 | 0.000 |
| transfer | gemma-2b-it | B | all twins | hidden, after the located heads | 35 | 32 | 0.914 | 0.000 |
| transfer | gemma-2b-it | B | both members passed | hidden, after the located heads | 23 | 23 | 1.000 | 0.000 |
| transfer | gemma-2b-it | B | all twins | hidden, last layer | 35 | 31 | 0.886 | 0.000 |
| transfer | gemma-2b-it | B | both members passed | hidden, last layer | 23 | 22 | 0.957 | 0.000 |
