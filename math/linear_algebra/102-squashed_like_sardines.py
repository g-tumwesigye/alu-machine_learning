def cat_matrices(mat1, mat2, axis=0):
    # Validating shape compatibility (axis 0)
    if axis == 0:
        # same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        # row axis
        return [row for row in mat1] + [row for row in mat2]
    
    # Validating shape compatibility (axis 1)
    elif axis == 1:
        # same number of rows
        if len(mat1) != len(mat2):
            return None
        # Concatenate along the column axis
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    
   
