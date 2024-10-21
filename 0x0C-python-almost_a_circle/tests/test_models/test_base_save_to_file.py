#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import remove


class TestBaseSaveToFile(unittest.TestCase):
    """A class representing test cases for the save_to_file
    class method of Base class.
    """

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        try:
            remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            remove("Square.json")
        except FileNotFoundError:
            pass
        try:
            remove("Base.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_one_rectangle(self):
        """A method that tests writing JSON string representation of one
        rectangle instance to a file.
        """
        r1 = [Rectangle(10, 7, 2, 8, 5)]
        Rectangle.save_to_file(r1)
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        """A method that tests writing JSON string representation of two
        rectangle instances to a file.
        """
        r1 = Rectangle(10, 7, 2, 8, 4)
        r2 = Rectangle(10, 4, 5, 3, 9)
        list_objs = [r1, r2]
        Rectangle.save_to_file(list_objs)
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 106)

    def test_save_to_file_one_square(self):
        """A method that tests writing JSON string representation of one
        square instance to a file.
        """
        s1 = [Square(10, 2, 8, 5)]
        Square.save_to_file(s1)
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        """A method that tests writing JSON string representation of two
        square instances to a file.
        """
        s1 = Square(10, 2, 8, 3)
        s2 = Square(10, 5, 3, 2)
        list_objs = [s1, s2]
        Square.save_to_file(list_objs)
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) == 78)

    def test_save_to_file_filename_must_be_class_name(self):
        """A method that tests filename of JSON file."""
        br = [Rectangle(100, 17, 2, 8, 2)]
        Base.save_to_file(br)
        with open("Base.json", 'r') as f:
            self.assertTrue(len(f.read()) == 55)

    def test_save_to_file_overwrite_if_file_already_exists(self):
        """A method that tests file overwrite of JSON file if already exists.
        """
        r1 = [Rectangle(100, 17, 2, 8, 3)]
        Rectangle.save_to_file(r1)
        r1 = [Rectangle(12, 7, 2, 8, 7)]
        Rectangle.save_to_file(r1)
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_list_objs_is_none(self):
        """A method that tests save_to_file when list of objects is None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list_objs_is_empty(self):
        """A method that tests save_to_file when list of objects is empty."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_no_args(self):
        """A method that tests save_to_file with no arguments provided."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_with_more_than_one_arg(self):
        """A method that tests save_to_file with more than one arg provided."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


if __name__ == "__main__":
    unittest.main()
