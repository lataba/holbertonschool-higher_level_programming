#!/usr/bin/python3
"""
Unittest for ....
"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class.

    Args:
        unittest: The unittest module for creating test cases.
    """

    def test_constructor_with_valid_arguments(self):
        """Test that the constructor sets the attributes correctly with valid arguments"""
        r = Rectangle(10, 20, 2, 3, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_constructor_with_invalid_arguments(self):
        """Test that the constructor raises the expected exceptions with invalid arguments"""
        with self.assertRaises(TypeError):
            Rectangle("10", 20, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 2, 3, 1)

    def test_area(self):
        """Test that the area method returns the correct area of the rectangle"""
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_str(self):
        """Test that the str method returns the correct string representation of the rectangle"""
        r = Rectangle(5, 10, 2, 3, 1)
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_str)

    def test_update_with_args(self):
        """Test that the update method assigns the attributes correctly with positional arguments"""
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(2, 8, 12, 4, 6)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)

    def test_update_with_kwargs(self):
        """Test that the update method assigns the attributes correctly with keyword arguments"""
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(x=4, y=6, id=2, width=8, height=12)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 6)

    def test_to_dictionary(self):
        """Test that the to_dictionary method returns the correct dictionary representation of the rectangle"""
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {"x": 2, "y": 3, "id": 1, "height": 10, "width": 5}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
