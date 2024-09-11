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
    def convert_to_2d(matrix):
        if isinstance(matrix[0], (int, float)):
            return [matrix]
        return matrix

    mat1 = convert_to_2d(mat1)
    mat2 = convert_to_2d(mat2)

    # Check dimensions
    def get_dimensions(matrix):
        dimensions = []
        while isinstance(matrix, list):
            dimensions.append(len(matrix))
            matrix = matrix[0] if matrix else []
        return dimensions

    def can_concatenate(dim1, dim2, axis):
        if axis >= len(dim1) or axis >= len(dim2):
            return False
        if dim1[axis] != dim2[axis]:
            return False
        return True

    dim1 = get_dimensions(mat1)
    dim2 = get_dimensions(mat2)

    if not can_concatenate(dim1, dim2, axis):
        return None

    # Concatenate matrices
    if axis == 0:
        return mat1 + mat2
    elif axis == 1:
        # Check if the number of rows is the same
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    elif axis == 2:
        # Handle 3D matrices: concatenate along the third axis
        if len(mat1) != len(mat2):
            return None
        if any(len(mat1[i]) != len(mat2[i]) for i in range(len(mat1))):
            return None
        return [[m1 + m2 for m1, m2 in zip(mat1_layer, mat2_layer)]
                for mat1_layer, mat2_layer in zip(mat1, mat2)]
    else:
        # Unsupported axis
        return None

