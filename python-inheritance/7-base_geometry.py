#!/usr/bin/python3
"""
Defines a new class BaseGeometry
"""


class BaseGeometry:
    """
    Defines a new class BaseGeometry
    """

    def area(self):
        """definition of method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """definition of validation method"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
