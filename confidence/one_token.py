from typing import Dict, List

from text_bridge.probabilities import complete_with_probabilities

from confidence.common import set_text_bridge_config


def one_token_confidence(question: str, answer: str) -> float:
    """Return the confidence that the answer is correct.

    Use "one token detection" method.

    Args:
        question: the question
        answer: the answer

    Returns:
        the confidence that the answer is correct
    """
    set_text_bridge_config()
    text_with_token_probabilities = complete_with_probabilities(
        "one_token",
        question=question,
        answer=answer
    )
    probabilities = text_with_token_probabilities.probabilities[0]
    yes_tokens = ["true", "tr", " true"]
    no_tokens = ["false", "fa", "fal", " false"]
    correct_probability = joint_probability(probabilities, yes_tokens)
    incorrect_probability = joint_probability(probabilities, no_tokens)
    if correct_probability == 0 and incorrect_probability == 0:
        return 0.5
    return correct_probability / (correct_probability + incorrect_probability)


def joint_probability(
        probabilities: Dict[str, float],
        tokens: List[str]
) -> float:
    """Sum of probabilities of sampling the given tokens.

    Args:
        probabilities: the probabilities of sampling each token
        tokens: the tokens that interest us

    Returns:
        the sum of probabilities of sampling the given tokens
    """
    token_probabilities = (
        probabilities[token]
        for token in tokens
        if token in probabilities
    )
    return sum(token_probabilities)
