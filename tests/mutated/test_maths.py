import pytest
from mutated.maths import add, subtract, is_within_range, is_prime

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
    assert not is_within_range(0, 1, 10)
    assert not is_within_range(11, 1, 10)
    assert is_within_range(1, 1, 10)

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(31)
