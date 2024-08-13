import numpy as np
import pytest
from mutated.numpy_utility import multiply_by_pattern

def test_even_length_array():
    arr = np.array([1, 2, 3, 4, 6, 7])
    result = multiply_by_pattern(arr)
    expected = np.array([0, 2, 0, 4, 0, 7])
    np.testing.assert_array_equal(result, expected)