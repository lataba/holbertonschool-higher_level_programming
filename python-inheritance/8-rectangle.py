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


class Rectangle(BaseGeometry):
    """
    Rectangle class
    """

    def __init__(self, width, height):
        """instant of width and height"""
        if width > -1:
            self.__width = width
        if height > -1:
            self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
