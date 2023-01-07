import pytest

from template_python.examples import fibonacci


@pytest.mark.parametrize(
    "input_n,output_n",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (14, 377),
        (15, 610),
    ],
)
def test_fibonacci(input_n: int, output_n: int) -> None:
    assert fibonacci.f(input_n) == output_n
