#!/usr/bin/python3
"""
Defines a matrix division function
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    for row in matrix:
        for element in row:
            if (not isinstance(element, float)
                    and not isinstance(element, int)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    for row in matrix:
        if not (len(row) == len(matrix[0])):
            raise TypeError("Each row of the matrix must "
                            "have the same size")

    if (not isinstance(div, float)
            and not isinstance(div, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
