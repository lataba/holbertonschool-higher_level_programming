#!/usr/bin/python3
"""
Defines a function that cheks the inherited
"""


def inherits_from(obj, a_class):
    """
    function that returns True if an object is an inherited instance of a class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
