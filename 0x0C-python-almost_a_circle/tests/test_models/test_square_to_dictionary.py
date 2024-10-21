#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.square import Square


class TestSquareToDictionary(unittest.TestCase):
    """A class representing test cases for the to_dictionary method of
    Square class.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        Base._Base__nb_objects = 0
        self.s1 = Square(10, 2, 8, 9)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        del Base._Base__nb_objects
        del self.s1

    def test_to_dictionary_expected_output(self):
        """A method that tests to_dictionary method for expected output."""
        sq_dict = {"id": 9, "y": 8, "size": 10, "x": 2}
        self.assertDictEqual(self.s1.to_dictionary(), sq_dict)

    def test_to_dictionary_return_object_no_id_change(self):
        """A method that tests to_dictionary does not return object with
        different identity than original.
        """
        s2 = Square(89, 4, 1, 12)
        s2.update(**self.s1.to_dictionary())
        self.assertNotEqual(self.s1, s2)

    def test_to_dictionary_with_args(self):
        """A method that tests to_dictionary with args provided."""
        with self.assertRaises(TypeError):
            self.s1.to_dictionary([])


if __name__ == "__main__":
    unittest.main()
