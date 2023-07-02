#!/usr/bin/python3
"""
Unittest for ....
"""

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for the Base class.

    Args:
        unittest: The unittest module for creating test cases.
    """

    def test_init_with_id(self):
        """Test the constructor with an explicit ID"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_init_without_id(self):
        """Test the constructor without an explicit ID"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_private(self):
        """Teste nb_instances"""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_public_id(self):
        """Test that the "id" attribute is correctly set when provided"""
        b1 = Base(3)
        b1.id = 8
        self.assertEqual(b1.id, 8)

    def test_str_id(self):
        """Teste str id"""
        self.assertEqual("hello", Base("hello").id)

    def test_set_id(self):
        """Test set id"""
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for ..."""

    def test_to_json_string_empty(self):
        """Test that the to_json_string method returns "[]" for an empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_not_empty(self):
        """Test that the to_json_string method returns the correct JSON for a non-empty list"""
        json_string = Base.to_json_string(
            [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        )
        expected_json = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(json_string, expected_json)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for..."""

    def test_from_json_string_empty(self):
        """Test that the from_json_string method returns an empty list for an empty JSON"""
        list_objs = Base.from_json_string("[]")
        self.assertEqual(list_objs, [])


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for..."""

    def test_load_from_file_first_rectangle(self):
        """Teste load from file rectangle"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_rectangle_types(self):
        """Teste load from file rectangle"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))


if __name__ == "__main__":
    unittest.main()
