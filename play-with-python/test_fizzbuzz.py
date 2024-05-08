
from fizzbuzz import fizzbuzz


def test_fizzbuzz_with_input_3_should_get_fizz():
    result = fizzbuzz(3)
    assert result == "Fizz"


def test_fizzbuzz_with_input_5_should_get_buzz():
    result = fizzbuzz(5)
    assert result == "buzz"
