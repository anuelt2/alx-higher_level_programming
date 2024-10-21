#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import remove


class TestBaseLoadFromFileCsv(unittest.TestCase):
    """A class representing test cases for the load_from_file_csv class
    method of Base class.
    """

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        try:
            remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        """A method that tests deserialization of CSV string representation
        of rectangle from file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 7, 5)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))

    def test_load_from_file_csv_second_rectangle(self):
        """A method that tests deserialization of CSV string representation
        of rectangle from file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 7, 5)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(list_rectangles_output[1]), str(r2))

    def test_load_from_file_csv_rectangles_types(self):
        """A method that tests that the objects in the list from the file
        are all of type Rectangle.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4, 7, 5)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in list_rectangles))

    def test_load_from_file_csv_first_square(self):
        """A method that tests deserialization of CSV string representation
        of square from file.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 7, 5)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(list_squares_output[0]), str(s1))

    def test_load_from_file_csv_second_square(self):
        """A method that tests deserialization of CSV string representation
        of square from file.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 7, 5)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(list_squares_output[1]), str(s2))

    def test_load_from_file_csv_squares_types(self):
        """A method that tests that the objects in the list from the file
        are all of type Square.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(2, 7, 5)
        Square.save_to_file_csv([s1, s2])
        list_squares = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in list_squares))

    def test_load_from_file_csv_file_not_exist(self):
        """A method that tests load_from_file_csv when file does not exist."""
        no_file = Square.load_from_file_csv()
        self.assertEqual(no_file, [])

    def test_load_from_file_csv_with_more_than_one_arg(self):
        """A method that tests load_from_file_csv with more than one arg
        provided.
        """
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv([], [])


if __name__ == "__main__":
    unittest.main()
