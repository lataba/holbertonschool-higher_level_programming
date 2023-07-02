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

    def test_public_id(self):
        """Test that the "id" attribute is correctly set when provided"""
        b1 = Base(3)
        b1.id = 8
        self.assertEqual(b1.id, 8)

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

    def test_from_json_string_empty(self):
        """Test that the from_json_string method returns an empty list for an empty JSON"""
        list_objs = Base.from_json_string("[]")
        self.assertEqual(list_objs, [])


if __name__ == "__main__":
    unittest.main()
