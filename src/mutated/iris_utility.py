import numpy as np

def round_down_to_1(cube):
    """
    Round down the data in the cube to a maximum of 1.
    If less than 1, stay the same
    Aware of the mask.
    """
    cube.data = np.ma.where(cube.data > 1, -1, cube.data)
    cube.attributes['history'] = 'round_down_to_1'
    return cube