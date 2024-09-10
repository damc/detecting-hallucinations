from confidence.one_token import one_token_confidence
from tests.common import error_test, buckets_test


def test_one_token_error():
    """Error test for "One token" method.

    Error test means summing up the absolute difference between the
    confidence and the expected confidence (0 or 1) for each sample.

    For example, if the returned confidence that answer is correct is
    0.4, and the answer is incorrect (is a hallucination), then the
    error is 0.4 because |0.4 - 0| = 0.4.
    """
    error_test(one_token_confidence, "One Token")


def test_one_token_buckets():
    """Bucket test for "One token" method.

    Bucket test means putting the samples into buckets depending on the
    confidence and then measuring the average correctness in each bucket.
    """
    buckets_test(one_token_confidence)
