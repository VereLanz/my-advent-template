# This file can be copied for each day to make test driven development even easier!
import pytest

from my_advent.day_template import a, b

EXAMPLE_INPUT = [
    0,
]


@pytest.skip
def test_example_a():
    example_result = 0
    assert a(EXAMPLE_INPUT) == example_result


@pytest.skip
def test_example_b():
    example_result = 0
    assert b(EXAMPLE_INPUT) == example_result
