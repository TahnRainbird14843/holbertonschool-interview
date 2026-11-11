#!/usr/bin/python3

"""
this is documented
"""


def rotate_2d_matrix(matrix):
    """rotate the matrix"""
    n = len(matrix)
    for j in range(n // 2):
        for i in range(n // 2 + n % 2):
            tmp = matrix[j][i]
            matrix[j][i] = matrix[n - i - 1][j]
            matrix[n - i - 1][j] = matrix[n - j - 1][n - i - 1]
            matrix[n - j - 1][n - i - 1] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = tmp


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()
