#!/usr/bin/python3
"""Defines a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the result of the division.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats.
        TypeError: If the div is not a number.
        ZeroDivisionError: If div is 0.
        TypeError: If each row of the matrix doesn't have the same size.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
