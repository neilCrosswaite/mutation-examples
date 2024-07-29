import pytest
from mutated.maths import add, subtract, is_within_range

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0
    assert subtract(-1, -1) == 0

def test_within_range():
    assert is_within_range(5, 1, 10)

def test_below_range():
    assert not is_within_range(0, 1, 10)

def test_above_range():
    assert not is_within_range(11, 1, 10)