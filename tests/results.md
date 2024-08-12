How to read the results:

Bucket - this is the bucket of probabilities that the given answer is correct (not a hallucination).
Average - this is the percentage (divided by 100) of the answers that were correct in the given bucket.
Samples - the number of samples in which the algorithm has decided probability that falls to the given bucket.

Simple:

Bucket 0.0-0.1, average: 0.37, samples: 1258
Bucket 0.1-0.2 - empty, samples: 0
Bucket 0.2-0.3 - empty, samples: 0
Bucket 0.3-0.4 - empty, samples: 0
Bucket 0.4-0.5 - empty, samples: 0
Bucket 0.5-0.6, average: 0.0, samples: 3
Bucket 0.6-0.7 - empty, samples: 0
Bucket 0.7-0.8, average: 0.1, samples: 48
Bucket 0.8-0.9, average: 0.07, samples: 43
Bucket 0.9-1.0, average: 0.8, samples: 648


One token:

Bucket 0.0-0.1, average: 0.01, samples: 80
Bucket 0.1-0.2, average: 0.02, samples: 134
Bucket 0.2-0.3, average: 0.03, samples: 149
Bucket 0.3-0.4, average: 0.13, samples: 152
Bucket 0.4-0.5, average: 0.16, samples: 164
Bucket 0.5-0.6, average: 0.2, samples: 158
Bucket 0.6-0.7, average: 0.45, samples: 139
Bucket 0.7-0.8, average: 0.48, samples: 186
Bucket 0.8-0.9, average: 0.77, samples: 244
Bucket 0.9-1.0, average: 0.97, samples: 594


Conclusions (might depend on the prompt):
1. Simple method of just asking the LLM to output the confidence works a little bit, but not very well.
2. Simple method is too confident, almost always giving probability from 0% to 10% or from 70% to 100%.
3. One token method works well.
4. One token method has a slight bias towards answering that the answer is correct (not a hallucination), except when it answers with confidence from 90% to 100% that the answer is correct (then it's not biased).

Additional info:
1. The bias can be the result of the prompt (with a different prompt, there might be no bias or a different bias).
2. The bias can be probably solved by adjusting the confidence.