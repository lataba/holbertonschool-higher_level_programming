#!/usr/bin/python3
"""
Unittest for ....
"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class.

    Args:
        unittest: The unittest module for creating test cases.
    """

    def test_constructor_with_valid_arguments(self):
        """Test that the constructor sets the attributes correctly with valid arguments"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_width_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)

    def test_height_getter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

    def test_constructor_with_invalid_arguments(self):
        """Test that the constructor raises the expected exceptions with invalid arguments"""
        with self.assertRaises(TypeError):
            Square("5", 2, 3, 1)
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 1)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_area(self):
        """Test that the area method returns the correct area of the square"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)

    def test_str(self):
        """Test that the str method returns the correct string representation of the square"""
        s = Square(5, 2, 3, 1)
        expected_str = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_str)

    def test_update_with_args(self):
        """Test that the update method assigns the attributes correctly with positional arguments"""
        s = Square(5, 2, 3, 1)
        s.update(2, 8, 4, 6)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_update_with_kwargs(self):
        """Test that the update method assigns the attributes correctly with keyword arguments"""
        s = Square(5, 2, 3, 1)
        s.update(x=4, y=6, id=2, size=8)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.width, 8)
        self.assertEqual(s.height, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 6)

    def test_to_dictionary(self):
        """Test that the to_dictionary method returns the correct dictionary representation of the square"""
        s = Square(5, 2, 3, 1)
        expected_dict = {"id": 1, "size": 5, "x": 2, "y": 3}
        self.assertEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
