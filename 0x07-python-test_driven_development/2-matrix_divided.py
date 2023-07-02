#!/usr/bin/python3
"""

    Matrix division

"""


def matrix_divided(matrix, div):
    """
    Dividing each element of matrix by an integer/float
    """
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    len0 = len(matrix[0]) if matrix else None
    if not len0:
        raise TypeError(err_msg)
    if all(len(m_row) == len0 for m_row in matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")
    if all(isinstance(m_row, list) for m_row in matrix) is False:
        raise TypeError(err_msg)
    if all(isinstance(e, (int, float)) for rw in matrix for e in rw) is False:
        raise TypeError(err_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
