#!/usr/bin/python3
"""Unittest for max_integer function([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """A class representing test cases for max_integer function"""

    def test_positive_integers_list(self):
        """A method that tests a list of positive integers"""
        my_list = list(range(10))
        self.assertEqual(max_integer(my_list), 9)

    def test_negative_integers_list(self):
        """A method that tests a list of negative integers"""
        my_list = list(range(-5, 0))
        self.assertEqual(max_integer(my_list), -1)

    def test_positive_negative_integers_list(self):
        """A method that tests a list of positive and negative integers"""
        my_list = [1, 7, 5, -2, 4, 11, 10]
        self.assertEqual(max_integer(my_list), 11)

    def test_one_integer_list(self):
        """A method that tests a list of one integer element"""
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        """A method that tests an empty list"""
        self.assertIsNone(max_integer([]))

    def test_repeated_numbers_list(self):
        """A method that tests a list with repeated numbers"""
        my_list = [1, 1, 3, 5, 2, 4, 5]
        self.assertEqual(max_integer(my_list), 5)

    def test_list_with_int_and_string(self):
        """A method that tests a list with strings"""
        my_list = [1, 5, 7, "hello", 2]
        with self.assertRaises(TypeError):
            max_integer(my_list)

    def test_list_with_all_strings(self):
        """A method that tests a list with all strings"""
        my_list = ["one", "hello", "2"]
        self.assertEqual(max_integer(my_list), "one")

    def test_list_with_float(self):
        """A method that tests a list with floats"""
        my_list = [1, 1.2, 3, 5, 2, 4, 5.5]
        self.assertEqual(max_integer(my_list), 5.5)

    def test_all_floats_list(self):
        """A method that tests a list of all floats"""
        my_list = [1.1, 2.2, 3.3, 4.4]
        self.assertEqual(max_integer(my_list), 4.4)

    def test_all_identical_list(self):
        """A method that tests a list of all identical integers"""
        my_list = [7, 7, 7, 7, 7]
        self.assertEqual(max_integer(my_list), 7)

    def test_large_list(self):
        """A method that tests a large list"""
        my_list = list(range(1000))
        self.assertEqual(max_integer(my_list), 999)

    def test_list_with_zero(self):
        """A method that tests a list with 0 value"""
        my_list = [5, 2, 8, 0, 3]
        self.assertEqual(max_integer(my_list), 8)

    def test_list_with_none(self):
        """A method that tests a list with None value"""
        my_list = [1, 2, None, 5]
        with self.assertRaises(TypeError):
            max_integer(my_list)

    def test_list_with_all_none_values(self):
        """A method that tests a list with None value"""
        my_list = [None, None, None, None]
        with self.assertRaises(TypeError):
            max_integer(my_list)
