#!/usr/bin/python3
"""
Unittests for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Test with an empty list"""
        result = max_integer([], None)
        self.assertIsNone(result)

    def test_positive_numbers(self):
        """Test with positive numbers"""
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        result = max_integer([-5, -4, -3, -2, -1])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        result = max_integer([-1, 0, 1, 2, 3])
        self.assertEqual(result, 3)

    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        result = max_integer([2, 2, 2, 2])
        self.assertEqual(result, 2)

    def test_single_number(self):
        """Test with a single number"""
        result = max_integer([7])
        self.assertEqual(result, 7)

    def test_large_list(self):
        """Test with a large list of numbers"""
        result = max_integer(list(range(1, 1000001)))
        self.assertEqual(result, 1000000)


if __name__ == '__main__':
    unittest.main()
