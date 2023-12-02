#!/usr/bin/python3
"""Unittests 4 max_int"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordr = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordr), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordr = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordr), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beg = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beg), 4)

    def test_empty_list(self):
        """Test an empty list."""
        emp = []
        self.assertEqual(max_integer(emp), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_ele = [7]
        self.assertEqual(max_integer(one_ele), 7)

    def test_floats(self):
        """Test a list of floats."""
        flo = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(flo), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_nd_flo = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_nd_flo), 15.5)

    def test_string(self):
        """Test a string."""
        strg = "Brennan"
        self.assertEqual(max_integer(strg), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strgs = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strgs), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
