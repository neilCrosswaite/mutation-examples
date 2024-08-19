import pytest
from mutated.prime import is_prime

def test_is_prime():
    # chat-gpt
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(31)
