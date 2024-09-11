#!/usr/bin/env python3
"""
Squashed Like Sardines
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Returns None if the matrices cannot be concatenated.
    """

    # Convert 1D vectors to 2D matrices
    if len(mat1) == 1 and isinstance(mat1[0], (int, float)):
        mat1 = [mat1]
    if len(mat2) == 1 and isinstance(mat2[0], (int, float)):
        mat2 = [mat2]

    if axis == 0:
        # Check if the number of columns is the same
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2

    elif axis == 1:
        # Check if the number of rows is the same
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]

    else:
        # Unsupported axis
        return None
