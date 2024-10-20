#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseCreate(unittest.TestCase):
    """A class representing test cases for the create
    class method of Base class.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 7, 2, 8, 9)
        self.s1 = Square(10, 2, 8, 9)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        del Base._Base__nb_objects
        del self.r1
        del self.s1

    def test_create_rectangle_from_default_parameters(self):
        """A method that tests for rectangle instance given
        default parameters.
        """
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(self.r1), "[Rectangle] (9) 2/8 - 10/7")

    def test_create_rectangle_from_create_method_return_object(self):
        """A method that tests for rectangle instance from dictionary
        created from previous rectangle instance.
        """
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), "[Rectangle] (9) 2/8 - 10/7")

    def test_create_rectangle_object1_is_not_object2(self):
        """A method that tests for rectangle instance object is not
        another rectangle instance object even with same parameters.
        """
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(self.r1, r2)

    def test_create_rectangle_object1_not_equal_object2(self):
        """A method that tests for rectangle instance object is not equal
        to another rectangle instance object even with same parameters.
        """
        r1_dictionary = self.r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(self.r1, r2)

    def test_create_square_from_default_parameters(self):
        """A method that tests for square instance given
        default parameters.
        """
        s1_dictionary = self.s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(self.s1), "[Square] (9) 2/8 - 10")

    def test_create_square_from_create_method_return_object(self):
        """A method that tests for square instance from dictionary
        created from previous square instance.
        """
        s1_dictionary = self.s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (9) 2/8 - 10")

    def test_create_square_object1_is_not_object2(self):
        """A method that tests for square instance object is not
        another square instance object even with same parameters.
        """
        s1_dictionary = self.s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(self.s1, s2)

    def test_create_square_object1_not_equal_object2(self):
        """A method that tests for square instance object is not equal
        to another square instance object even with same parameters.
        """
        s1_dictionary = self.s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(self.s1, s2)


if __name__ == "__main__":
    unittest.main()
