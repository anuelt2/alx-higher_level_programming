#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import remove


class TestBaseSaveToFileCsv(unittest.TestCase):
    """A class representing test cases for the save_to_file_csv
    class method of Base class.
    """
    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        Base._Base__nb_objects = 0

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
        try:
            remove("Base.csv")
        except FileNotFoundError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        """A method that tests writing CSV string representation of one
        rectangle instance to a file.
        """
        r1 = [Rectangle(10, 7, 2, 8)]
        Rectangle.save_to_file_csv(r1)
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), "1,10,7,2,8\n")

    def test_save_to_file_csv_two_rectangles(self):
        """A method that tests writing CSV string representation of two
        rectangle instances to a file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(10, 4, 5, 3)
        list_objs = [r1, r2]
        Rectangle.save_to_file_csv(list_objs)
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), "1,10,7,2,8\n2,10,4,5,3\n")

    def test_save_to_file_csv_one_square(self):
        """A method that tests writing CSV string representation of one
        square instance to a file.
        """
        s1 = [Square(10, 2, 8)]
        Square.save_to_file_csv(s1)
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), "1,10,2,8\n")

    def test_save_to_file_csv_two_squares(self):
        """A method that tests writing CSV string representation of two
        square instances to a file.
        """
        s1 = Square(10, 2, 8)
        s2 = Square(10, 5, 3)
        list_objs = [s1, s2]
        Square.save_to_file_csv(list_objs)
        with open("Square.csv", 'r') as f:
            self.assertEqual(f.read(), "1,10,2,8\n2,10,5,3\n")

    def test_save_to_file_csv_filename_must_be_class_name(self):
        """A method that tests filename of CSV file."""
        br = [Square(100, 2, 8)]
        Base.save_to_file_csv(br)
        with open("Base.csv", 'r') as f:
            self.assertEqual(f.read(), "1,100,2,8\n")

    def test_save_to_file_csv_overwrite_if_file_already_exists(self):
        """A method that tests file overwrite of CSV file if already exists.
        """
        r1 = [Rectangle(100, 17, 2, 8)]
        Rectangle.save_to_file_csv(r1)
        r1 = [Rectangle(12, 7, 2, 8)]
        Rectangle.save_to_file_csv(r1)
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), "2,12,7,2,8\n")

    def test_save_to_file_csv_list_objs_is_none(self):
        """A method that tests save_to_file_csv when list of objects is None.
        """
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_csv_list_objs_is_empty(self):
        """A method that tests save_to_file_csv when list of objects is empty.
        """
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", 'r') as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_csv_with_no_args(self):
        """A method that tests save_to_file_csv with no arguments provided."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_with_more_than_one_arg(self):
        """A method that tests save_to_file_csv with more than one arg
        provided.
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


if __name__ == "__main__":
    unittest.main()
