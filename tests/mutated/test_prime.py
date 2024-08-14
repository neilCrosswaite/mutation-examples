import pytest
from mutated.prime import is_prime

def test_is_prime():
    # chat-gpt
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(31)
    # assert is_prime(9999999900000001)


    # assert not is_prime(1)
    # assert not is_prime(4)
    # assert not is_prime(6)
    # assert not is_prime(8)
