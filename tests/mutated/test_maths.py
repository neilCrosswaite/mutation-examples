import pytest
from mutated.maths import add, is_within_range

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_within_range():
    assert is_within_range(5, 1, 10)
    assert not is_within_range(0, 1, 10)

    # assert is_within_range(5, 5, 5)

