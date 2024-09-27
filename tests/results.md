How to read the results:

Bucket - this is the bucket of probabilities that the given answer is correct (not a hallucination).

Average - this is the percentage (divided by 100) of the answers that were 
correct in the given bucket. Ideally, it should be in the middle of the 
probability bucket (for example, it should be 0.25 for 0.2-0.3 bucket).

Samples - the number of samples in which the algorithm has decided probability that falls to the given bucket.

# Simple method

Simple method is asking the LLM to output the confidence as a number.

Simple method is NOT one token method and is included here only for comparison.

| Bucket       | Average | Samples |
|--------------|---------|---------|
| 0.0-0.1      | 0.37    | 1258    |
| 0.1-0.2      | -       | 0       |
| 0.2-0.3      | -       | 0       |
| 0.3-0.4      | -       | 0       |
| 0.4-0.5      | -       | 0       |
| 0.5-0.6      | 0.0     | 3       |
| 0.6-0.7      | -       | 0       |
| 0.7-0.8      | 0.1     | 48      |
| 0.8-0.9      | 0.07    | 43      |
| 0.9-1.0      | 0.8     | 648     |

# One token method

One token method is the method introduced in this repository.

| Bucket       | Average | Samples |
|--------------|---------|---------|
| 0.0-0.1      | 0.01    | 80      |
| 0.1-0.2      | 0.02    | 134     |
| 0.2-0.3      | 0.03    | 149     |
| 0.3-0.4      | 0.13    | 152     |
| 0.4-0.5      | 0.16    | 164     |
| 0.5-0.6      | 0.2     | 158     |
| 0.6-0.7      | 0.45    | 139     |
| 0.7-0.8      | 0.48    | 186     |
| 0.8-0.9      | 0.77    | 244     |
| 0.9-1.0      | 0.97    | 594     |

# Conclusions

Conclusions (might depend on the prompt and/or the model and/or the softmax 
temperature):
1. Simple method of just asking the LLM to output the confidence works a little bit, but not very well.
2. Simple method is too confident, almost always giving probability from 0% to 10% or from 70% to 100%.
3. One token method works well.
4. One token method has a slight bias towards answering that the answer is correct (not a hallucination), except when it answers with confidence from 90% to 100% that the answer is correct (then it's not biased).

Additional info:
1. The bias can be the result of the prompt (with a different prompt, there might be no bias or a different bias).
2. The bias can be probably solved by adjusting the confidence, with the 
   knowledge of the bias.