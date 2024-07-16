#!/usr/bin/python3
"""
Rotate a 2D Matrix interview prep
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    for i in range(int(len(matrix) / 2)):
        for j in range(i, (len(matrix) - i - 1)):
            x = (len(matrix) - 1 - j)
            temp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[(len(matrix) - i - 1)][x]
            matrix[(len(matrix) - i - 1)][x] = matrix[j][(len(matrix) - i - 1)]
            matrix[j][(len(matrix) - i - 1)] = temp
