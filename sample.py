import pytest

def FizzBuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 5 == 0:
            return "Buzz"

    elif x % 3 == 0:
        return "Fizz"

    




def test_answers():
    assert FizzBuzz(15) == "FizzBuzz"
    assert FizzBuzz(10) == "Buzz"
    assert FizzBuzz(6) == "Fizz"
    
