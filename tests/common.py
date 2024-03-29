from json import load
from logging import getLogger
from os.path import dirname, join
from typing import List, Dict, Callable

# The start of the samples in the dataset
START = 0

# The end of the samples in the dataset
END = 100


def error_test(tested_function: Callable[[str, str], float], name: str):
    """Error test for a method.

    Args:
        tested_function: the method to test
        name: the name of the method
    """
    samples = read_from_file("halueval.json")
    samples = samples[START:END]
    error_sum = 0
    for key, sample in enumerate(samples):
        getLogger("tests.test_confidence").info(f"Sample {key}")
        question = sample["knowledge"] + "\n\n" + sample["question"]
        answer = sample["right_answer"]
        error = error_on_sample(tested_function, question, answer, 1)
        error_sum += error
        answer = sample["hallucinated_answer"]
        error = error_on_sample(tested_function, question, answer, 0)
        error_sum += error
    getLogger("tests.test_confidence").info(f"{name} Error sum: {error_sum}")
    assert error_sum < 100


def read_from_file(relative_file_path: str) -> List[Dict[str, str]]:
    """Read a list of dictionaries from a file.

    Args:
        relative_file_path: the path to the file

    Returns:
        the list of dictionaries
    """
    file_path = join(dirname(__file__), relative_file_path)
    with open(file_path, "r") as file:
        return load(file)


def error_on_sample(
        tested_function: Callable[[str, str], float],
        question: str,
        answer: str,
        expected_confidence: int
) -> float:
    """Return the error on a sample.

    Args:
        tested_function: the method to test
        question: the question
        answer: the answer
        expected_confidence: the expected confidence (0 or 1)

    Returns:
        the absolute difference between the confidence and the expected
        confidence
    """
    getLogger("tests.test_confidence").info(f"Question: {question}")
    getLogger("tests.test_confidence").info(f"Answer: {answer}")
    getLogger("tests.test_confidence").info(
        f"Correct: {bool(expected_confidence)}"
    )
    confidence_ = tested_function(question, answer)
    getLogger("tests.test_confidence").info(
        "Confidence: " + str(confidence_)
    )
    result = abs(confidence_ - expected_confidence)
    getLogger("tests.test_confidence").info(f"Error: {result}")
    return result


def buckets_test(tested_function: Callable[[str, str], float]):
    """Bucket test for a method.

    Args:
        tested_function: the method to test
    """
    samples = read_from_file("halueval.json")
    samples = samples[START:END]
    buckets_ = buckets(samples, tested_function)
    bucket_averages_ = bucket_averages(buckets_)
    for key, average in enumerate(bucket_averages_):
        assert abs(average - (key / 10 + 0.05)) < 0.5


def buckets(
        samples: List[Dict[str, str]],
        tested_function: Callable[[str, str], float]
) -> List[List[int]]:
    """Classifies the samples into buckets depending on the confidence.

    It puts the expected confidence (0 or 1) into the bucket.

    Args:
        samples: the samples
        tested_function: the method to test

    Returns:
        the buckets of correctness
    """
    buckets_ = [[] for _ in range(10)]
    for key, sample in enumerate(samples):
        getLogger("tests.test_confidence").info(f"Sample {key}")
        question = sample["knowledge"] + "\n\n" + sample["question"]
        answer = sample["right_answer"]
        confidence_ = tested_function(question, answer)
        bucket_key = int(confidence_ * 10) if confidence_ < 1 else 9
        buckets_[bucket_key].append(1)
        answer = sample["hallucinated_answer"]
        confidence_ = tested_function(question, answer)
        bucket_key = int(confidence_ * 10) if confidence_ < 1 else 9
        buckets_[bucket_key].append(0)
    return buckets_


def bucket_averages(buckets_: List[List[int]]) -> List[float]:
    """Return the average correctness in each bucket.

    Args:
        buckets_: the buckets

    Returns:
        the average correctness in each bucket
    """
    bucket_averages_ = []
    for key in range(10):
        samples = len(buckets_[key])
        start = round(key / 10, 1)
        end = round(start + 0.1, 1)
        range_ = f"{start}-{end}"
        if samples > 0:
            bucket = buckets_[key]
            average = round(sum(bucket) / samples, 2)
        else:
            getLogger("tests.test_confidence").info(
                f"Bucket {range_} - empty"
            )
            continue
        bucket_averages_.append(average)
        getLogger("tests.test_confidence").info(
            f"Bucket {range_}, average: {average}, samples: {samples}"
        )
    return bucket_averages_
