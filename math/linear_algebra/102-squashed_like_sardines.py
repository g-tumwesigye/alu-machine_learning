#!/usr/bin/env python3
"""
Squashed Like Sardines
"""

def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.
    Returns None if the matrices cannot be concatenated.
    """
    # Function to get the dimensions of the matrix
    def get_dimensions(matrix):
        dimensions = []
        while isinstance(matrix, list):
            dimensions.append(len(matrix))
            matrix = matrix[0] if matrix else []
        return dimensions

    def can_concatenate(dim1, dim2, axis):
        """
        Check if two matrices with dimensions dim1 and dim2 can be concatenated along the given axis.
        """
        if axis >= len(dim1) or axis >= len(dim2):
            return False
        if dim1[axis] != dim2[axis]:
            return False
        return True

    # Convert 1D vectors to 2D matrices
    if isinstance(mat1[0], (int, float)):
        mat1 = [mat1]
    if isinstance(mat2[0], (int, float)):
        mat2 = [mat2]

    # Get dimensions of both matrices
    dim1 = get_dimensions(mat1)
    dim2 = get_dimensions(mat2)

    # Check if dimensions are compatible for concatenation along the specified axis
    if not can_concatenate(dim1, dim2, axis):
        return None

    # Concatenate matrices
    if axis == 0:
        return mat1 + mat2
    elif axis == 1:
        # Ensure both matrices have the same number of rows
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
