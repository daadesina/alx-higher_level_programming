#!/usr/bin/python3

"""A module of matrix"""


def matrix_divided(matrix, div):
    """A function of matrix"""

    row = len(matrix)
    col = len(matrix[0])

    new_mat = [[0 for i in range(col)] for j in range(row)]

    for i in range(row - 1):
        if len(matrix[i]) == len(matrix[i + 1]):
            pass
        else:
            raise TypeError('Each row of the matrix must have the same size')


    
    for i in range(row):
        for j in range(col):
            if isinstance(matrix[i][j], int):
                new_mat[i][j] = round((matrix[i][j] / div), 2)
            elif isinstance(matrix[i][j], float):
                new_mat[i][j] = round((matrix[i][j] / div), 2)
            else:
                raise TypeError('matrix must be a matrix of integers/floats')
    



    return (new_mat)
