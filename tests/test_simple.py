from confidence.simple import simple_confidence
from tests.common import error_test, buckets_test


def test_simple_error():
    """Error test for "Simple" method.

    Error test means summing up the absolute difference between the
    confidence and the expected confidence (0 or 1) for each sample.

    For example, if the returned confidence that answer is correct is
    0.4, and the answer is incorrect (is a hallucination), then the
    error is 0.4.
    """
    error_test(simple_confidence, "Simple")


def test_simple_buckets():
    """Bucket test for "Simple" method.

    Bucket test means putting the samples into buckets depending on the
    confidence and then measuring the average correctness in each bucket.
    """
    buckets_test(simple_confidence)
