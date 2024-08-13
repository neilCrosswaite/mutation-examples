import numpy as np

def multiply_by_pattern(arr):
    """
    Takes a NumPy array and multiplies it by a repeating pattern [0, 1].
    
    Parameters:
    arr (numpy.ndarray): Input array of numbers.

    Returns:
    numpy.ndarray: Array where elements are multiplied by the pattern [0, 1].
    """
    pattern = np.array([0, 1])
    return arr * np.tile(pattern, len(arr) // len(pattern) + 1)[:len(arr)]