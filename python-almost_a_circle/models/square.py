#!/usr/bin/python3
"""
Defines Square class inherited from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square define"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set and get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    @property
    def width(self):
        """set and get the width of the square"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set and get the height of the square"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set and get the x position"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set and get the y position"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the square"""
        return self.__height * self.__width

    def display(self):
        """prints in stdout the square instance"""
        if self.__height == 0 or self.__width == 0:
            print("")
            return

        if self.__y > 0:
            print("\n" * (self.__y - 1))

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.__x, self.__y, self.__width
        )

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.__x = args[2]
            if len(args) == 4:
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
