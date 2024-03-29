from text_bridge.basic import complete

from confidence.common import set_text_bridge_config


def simple_confidence(question: str, answer: str) -> float:
    """Return the confidence that the answer is correct.

    Use a simple method.

    Args:
        question: the question
        answer: the answer

    Returns:
        the confidence that the answer is correct
    """
    set_text_bridge_config()
    text = complete("simple", question=question, answer=answer)
    text = text[:2]
    if text.isdigit():
        return int(text) / 100
    return 0.5
