"One token" method is a method for detecting hallucinations (specifically, getting the confidence of a model that the answer is correct) in the content generated by large language models.

I haven't shared this idea with too many people so far, and I might be wrong about something, but the empirical evidence generated by this project suggests that it works (see "conclusions" for more information).

I described that method here:
https://damc4.substack.com/p/hallucination-detector-solution-to?r=12s5s6&utm_campaign=post&utm_medium=web

In this repository, I empirically test that method by comparing it with simply asking the model to output the confidence.

The project uses TextBridge package https://pypi.org/project/text-bridge/

# Conclusions

Conclusions (might depend on the prompt):
1. Simple method of just asking the LLM to output the confidence works a little bit, but not very well.
2. Simple method is too confident, almost always giving probability from 0% to 10% or from 70% to 100%.
3. One token method works well.
4. One token method has a slight bias towards answering that the answer is correct (not a hallucination), except when it answers with confidence from 90% to 100% that the answer is correct (then it's not biased).

Additional info:
1. The bias can be the result of the prompt (with a different prompt, there might be no bias or a different bias).
2. The bias can be probably solved by adjusting the confidence.