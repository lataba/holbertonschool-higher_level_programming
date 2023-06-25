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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
