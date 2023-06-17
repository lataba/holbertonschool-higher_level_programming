#!/usr/bin/python3
"""
Defines a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Definition of the function
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b