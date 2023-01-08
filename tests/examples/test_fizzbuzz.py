import pytest

from template_python.examples import fizzbuzz


@pytest.mark.parametrize(
    "input_item,output",
    [(1, 1), (2, 2), (3, "Fizz"), (4, 4), (5, "Buzz"), (15, "FizzBuzz")],
)
def test_fizzbuzz(input_item: int, output: int | str) -> None:
    assert fizzbuzz.fizzbuzz_list()[input_item] == output
