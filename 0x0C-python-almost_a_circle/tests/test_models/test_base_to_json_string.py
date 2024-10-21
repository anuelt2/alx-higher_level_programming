#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseToJsonString(unittest.TestCase):
    """A class representing test cases for the to_json_string
    static method of Base class.
    """

    def test_to_json_string_rectangle_type(self):
        """A method that tests type of json string representation
        of a rectangle instance.
        """
        r1 = Rectangle(10, 7, 2, 8)
        self.assertEqual(type(Base.to_json_string([r1.to_dictionary()])), str)

    def test_to_json_string_rectangle_one_dict(self):
        """A method that tests output of json string representation
        of one rectangle instance.
        """
        r1 = Rectangle(10, 7, 2, 8, 5)
        self.assertTrue(len(Base.to_json_string([r1.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        """A method that tests output of json string representation
        of two rectangle instances.
        """
        r1 = Rectangle(10, 7, 2, 8, 4)
        r2 = Rectangle(10, 4, 5, 3, 7)
        list_dict = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dict)) == 106)

    def test_to_json_string_square_type(self):
        """A method that tests type of json string representation
        of a square instance.
        """
        s1 = Square(10, 2, 8)
        self.assertEqual(type(Base.to_json_string([s1.to_dictionary()])), str)

    def test_to_json_string_square_one_dict(self):
        """A method that tests output of json string representation
        of one square instance.
        """
        s1 = Square(10, 2, 8, 8)
        self.assertTrue(len(Base.to_json_string([s1.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        """A method that tests output of json string representation
        of two square instances.
        """
        s1 = Square(10, 2, 8, 2)
        s2 = Square(10, 5, 3, 7)
        list_dict = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dict)) == 78)

    def test_to_json_string_list_dict_is_none(self):
        """A method that tests to_json_string method when list of dictionaries
        is None.
        """
        self.assertTrue(Base.to_json_string(None), "[]")

    def test_to_json_string_list_dict_is_empty(self):
        """A method that tests to_json_string method when list of dictionaries
        is empty.
        """
        self.assertTrue(Base.to_json_string([]), "[]")

    def test_to_json_string_no_args(self):
        """A method that tests to_json_string method when no arguments given.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_args(self):
        """A method that tests to_json_string method when more than one
        argument given.
        """
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])


if __name__ == "__main__":
    unittest.main()
