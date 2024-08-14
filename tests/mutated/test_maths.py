import pytest
from mutated.maths import add, is_within_range, multiply, divide

def test_add():
    # me
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_within_range():
    # me
    assert is_within_range(5, 1, 10)
    assert not is_within_range(0, 1, 10)
    assert not is_within_range(11, 1, 10)

def test_multiply():
    # co-pilot
    assert multiply(1, 2) == 2
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1
    assert multiply(0, 1) == 0

def test_divide():
    # co-pilot
    assert divide(2, 1) == 2
    assert divide(-1, 1) == -1
    assert divide(-1, -1) == 1

    # Test divide by zero and error message regex
    with pytest.raises(ValueError):
        divide(1, 0)