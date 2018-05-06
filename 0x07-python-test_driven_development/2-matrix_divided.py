#!/usr/bin/python3
"""Module docstring
This module contains a function called matrix_divided
It divides a matrix by a given number, or raises and error
upon failure.
"""


def matrix_divided(matrix, div):
    """Function docstring
    matrix_divided: this function divides a matrix by div
    Args:
        matrix: numerator
        div: denominator"""
    TE = TypeError
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError('Each row of the matrix must have the same size')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    try:
        new_matrix = [[round(i/div, 2) for i in j] for j in matrix]
    except:
        raise TE('matrix must be a matrix (list of lists) of integers/floats')
    return new_matrix
