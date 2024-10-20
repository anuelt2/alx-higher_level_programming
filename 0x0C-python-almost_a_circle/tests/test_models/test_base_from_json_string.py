#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseFromJsonString(unittest.TestCase):
    """A class representing test cases for the from_json_string
    static method of Base class.
    """

    def test_from_json_string_rectangle_type(self):
        """A method that tests type of Python object from deserialization
        of JSON string.
        """
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_string = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_one_rectangle(self):
        """A method that tests one rectangle from deserialization of
        JSON string.
        """
        list_input = [{'id': 89, 'width': 10, 'height': 4, 'x': 18, 'y': 12}]
        json_string = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """A method that tests two rectangles from deserialization of
        JSON string.
        """
        list_input = [
                {'id': 89, 'width': 10, 'height': 4, 'x': 18, 'y': 12},
                {'id': 6, 'width': 51, 'height': 22, 'x': 9, 'y': 2}
                ]
        json_string = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """A method that tests one square from deserialization of JSON string.
        """
        list_input = [{'id': 89, 'size': 10, 'x': 18, 'y': 12}]
        json_string = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_string)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """A method that tests two squares from deserialization of JSON string.
        """
        list_input = [
                {'id': 89, 'size': 10, 'x': 18, 'y': 12},
                {'id': 6, 'size': 51, 'x': 9, 'y': 2}
                ]
        json_string = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_string)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_json_string_is_none(self):
        """A method that tests from_json_string when json_string is None."""
        self.assertEqual(Rectangle.from_json_string(None), [])

    def test_from_json_string_json_string_is_empty(self):
        """A method that tests from_json_string when json_string is empty list.
        """
        self.assertEqual(Rectangle.from_json_string("[]"), [])

    def test_from_json_string_with_no_args(self):
        """A method that tests from_json_string with no arguments provided."""
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()

    def test_from_json_string_with_more_than_one_arg(self):
        """A method that tests from_json_string with more than one arg
        provided.
        """
        with self.assertRaises(TypeError):
            Rectangle.from_json_string()


if __name__ == "__main__":
    unittest.main()
