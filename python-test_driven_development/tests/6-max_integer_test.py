#!/usr/bin/python3
"""
Unittests for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([])
        self.assertIsNone(result, None)
        self.assertIsNone(max_integer([None]), None)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_empty_list(self):
        """Test with an empty string"""
        result = max_integer("")
        self.assertIsNone(result, None)

    def test_positive_numbers(self):
        """Test with positive numbers"""
        result = max_integer([1, 2, 3, 5, 4])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        result = max_integer([-1, 0, 1, 2, 3])
        self.assertEqual(result, 3)

    def test_floats(self):
        """Test a list of floats."""
        result = max_integer([1.53, 6.33, -9.123, 15.2, 6.0])
        self.assertEqual(result, 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        result = max_integer([1.53, 15.5, -9, 15, 6])
        self.assertEqual(result, 15.5)

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)

    def test_single_number(self):
        """Test with a single number"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_string(self):
        """Test a string."""
        result = max_integer("Laura")
        self.assertEqual(result, 'u')

    def test_list_of_strings(self):
        """Test a list of strings."""
        result = max_integer(["aaa", "bbb", "ccc"])
        self.assertEqual(result, "ccc")

    def test_list_of_lists(self):
        self.assertEqual(max_integer([[5, 8.2], [3.7, -4]]), [5, 8.2])


if __name__ == '__main__':
    unittest.main()
