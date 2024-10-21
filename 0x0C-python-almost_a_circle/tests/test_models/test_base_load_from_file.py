#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import remove


class TestBaseLoadFromFile(unittest.TestCase):
    """A class representing test cases for the load_from_file class
    method of Base class.
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

    def test_load_from_file_first_rectangle(self):
        """A method that tests deserialization of JSON string representation
        of rectangle from file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 7, 5)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))

    def test_load_from_file_second_rectangle(self):
        """A method that tests deserialization of JSON string representation
        of rectangle from file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 7, 5)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[1]), str(r2))

    def test_load_from_file_rectangles_types(self):
        """A method that tests that the objects in the list from the file
        are all of type Rectangle.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 7, 5)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in list_rectangles))

    def test_load_from_file_first_square(self):
        """A method that tests deserialization of JSON string representation
        of square from file.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 7, 5)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))

    def test_load_from_file_second_square(self):
        """A method that tests deserialization of JSON string representation
        of square from file.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 7, 5)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[1]), str(s2))

    def test_load_from_file_squares_types(self):
        """A method that tests that the objects in the list from the file
        are all of type Square.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 7, 5)
        Square.save_to_file([s1, s2])
        list_squares = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in list_squares))

    def test_load_from_file_file_not_exist(self):
        """A method that tests load_from_file when file does not exist."""
        no_file = Square.load_from_file()
        self.assertEqual(no_file, [])

    def test_load_from_file_with_more_than_one_arg(self):
        """A method that tests load_from_file with more than one arg
        provided.
        """
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], [])


if __name__ == "__main__":
    unittest.main()
