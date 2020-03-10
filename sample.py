import pytest

def FizzBuzz(x):
    if x % 3 and x % 5:
        return "FizzBuzz"






def test_answers():
    assert FizzBuzz(6) == "FizzBuzz"

