import numpy as np
import pytest
from mutated.numpy_utility import multiply_arr_by

def test_multiply_arr_by():
    # me
    arr = np.ones(5)
    num = 2
    result = multiply_arr_by(arr, num)
    assert np.all(result == 2)