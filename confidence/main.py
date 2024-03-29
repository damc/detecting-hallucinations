from __future__ import annotations

from logging import basicConfig, WARNING, DEBUG, INFO, getLogger
from sys import stdout

from .one_token import one_token_confidence

# Debug mode.
DEBUG_MODE = True


def run():
    """Run the program."""
    set_logging_config()
    question = input("Enter a question: ")
    answer = input("Enter an answer: ")
    confidence_ = one_token_confidence(question, answer)
    print(f"Confidence: {confidence_}")


def set_logging_config():
    """Set logging configuration."""
    basicConfig(level=WARNING, stream=stdout)
    getLogger("confidence.confidence").setLevel(DEBUG if DEBUG_MODE else INFO)
    # getLogger("text_bridge.basic").setLevel(DEBUG if DEBUG_MODE else INFO)
