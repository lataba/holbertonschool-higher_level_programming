#!/usr/bin/python3
"""
Defines a function that returns a Pascal's triangle
"""


def pascal_triangle(n):
    """Pascal's triangle function"""
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        triangle = pascal_triangle(n - 1)
        last_row = triangle[-1]
        new_row = (
            [1]
            + [last_row[i - 1] + last_row[i] for i in range(1, len(last_row))]
            + [1]
        )
        triangle.append(new_row)
        return triangle
