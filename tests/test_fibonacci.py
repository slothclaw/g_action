import pytest
from math_functions.fibonacci import fibonacci


def test_singular_fibonacci():
    assert fibonacci(1) == 1

def test_negative_fibonacci():
    with pytest.raises(ValueError):
        fibonacci(0)

def test_positive_fibonacci():
    assert fibonacci(9) == 34
