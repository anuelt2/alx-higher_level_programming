#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: List of lists of ints, floats.
        div: Matrix int, float divisor.

    Raises:
        TypeError: If matrix is not list of lists of int, float.
        TypeError: If sublists of matrix are not all same size.
        TypeError: If div is not int, float.
        ZeroDivisionError: If div is 0.

    Returns:
        New matrix of divided elements.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)" +
                            " of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                " of integers/floats")

    return [[round((num / div), 2) for num in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
