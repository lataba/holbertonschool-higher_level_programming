#!/usr/bin/python3
"""
Defines a new class Square that inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)
