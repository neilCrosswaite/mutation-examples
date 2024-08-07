from mutated import iris_utility
from iris import cube
import numpy as np

def test_round_down_to_1():
    """ Test round_down_to_1 function """
    masked_array = np.ma.masked_array([0.5, 0.6, 1, 1, 1.1, 1.2], mask=[1, 0, 1, 0, 1, 0])
    input_cube = cube.Cube(masked_array)
    result = iris_utility.round_down_to_1(input_cube)
    print(result.data.data)
    print(result.data.mask)
    assert np.all(result.data == np.ma.masked_array([0.5, 0.6, 1, 1, 1, 1], mask=[1, 0, 1, 0, 1, 0]))

def test_round_down_to_1_bad():
    """ Test round_down_to_1 function """
    masked_array = np.ma.masked_array([0.5, 0.6, 1, 1, 1.1, 1.2], mask=[1, 0, 1, 0, 1, 0])
    input_cube = cube.Cube(masked_array)
    result = iris_utility.round_down_to_1_bad(input_cube)
    print(result.data.data)
    print(result.data.mask)
    assert np.all(result.data == np.ma.masked_array([0.5, 0.6, 1, 1, 1, 1], mask=[1, 0, 1, 0, 1, 0]))