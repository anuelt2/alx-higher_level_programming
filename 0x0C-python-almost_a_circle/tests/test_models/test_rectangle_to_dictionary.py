#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleToDictionary(unittest.TestCase):
    """A class representing test cases for the to_dictionary method of
    Rectangle class.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        # Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 7, 2, 8, 9)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        # del Base._Base__nb_objects
        del self.r1

    def test_to_dictionary_expected_output(self):
        """A method that tests to_dictionary method for expected output."""
        rec_dict = {"id": 9, "y": 8, "height": 7, "width": 10, "x": 2}
        self.assertDictEqual(self.r1.to_dictionary(), rec_dict)

    def test_to_dictionary_return_object_no_id_change(self):
        """A method that tests to_dictionary does not return object with
        different identity than original.
        """
        r2 = Rectangle(89, 10, 4, 1, 12)
        r2.update(**self.r1.to_dictionary())
        self.assertNotEqual(self.r1, r2)

    def test_to_dictionary_with_args(self):
        """A method that tests to_dictionary with args provided."""
        with self.assertRaises(TypeError):
            self.r1.to_dictionary([])


if __name__ == "__main__":
    unittest.main()
