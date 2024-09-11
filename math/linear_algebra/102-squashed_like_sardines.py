#!/usr/bin/env python3
"""
Squashed Like Sardines
"""


import numpy as np


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Returns None if the matrices cannot be concatenated.
    """
    mat1 = np.array(mat1)
    mat2 = np.array(mat2)
    
    try:
        result = np.concatenate((mat1, mat2), axis=axis)
        return result.tolist()
    except ValueError:
        return None

