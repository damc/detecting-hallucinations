import logging
import pytest
from sys import stdout


@pytest.fixture(scope='session', autouse=True)
def set_up_logging():
    """Set up logging for the tests.

    Feel free to uncomment the commented lines to see more detailed logs.
    """
    logging.basicConfig(level=logging.WARNING, stream=stdout)
    logging.getLogger("tests.test_confidence").setLevel(logging.DEBUG)
    logging.getLogger("confidence.confidence").setLevel(logging.DEBUG)
    # logging.getLogger("text_bridge.basic").setLevel(logging.DEBUG)
    yield
