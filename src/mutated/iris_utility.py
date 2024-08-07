import numpy as np

def round_down_to_1(cube):
    """
    Round down the data in the cube to a maximum of 1.
    If less than 1, stay the same
    Aware of the mask.
    """
    cube.data = np.ma.where(cube.data > 1, 1, cube.data)
    return cube

def round_down_to_1_bad(cube):
    """
    Round down the data in the cube to a maximum of 1.
    If less than 1, stay the same
    Aware of the mask.
    """
    above_one = np.where((cube.core_data() > 1), True, False)
    cube.core_data()[above_one] = 1
    return cube

