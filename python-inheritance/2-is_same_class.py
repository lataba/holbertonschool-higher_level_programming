#!/usr/bin/python3
"""
Defines a function that indicates if an object is an instance
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is an instance of a class
    """
    if isinstance(obj, a_class):
        return True

    return False
