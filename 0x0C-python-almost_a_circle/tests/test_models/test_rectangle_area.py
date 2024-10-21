#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleArea(unittest.TestCase):
    """A class representing test cases for the area method of
    Rectangle class.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 7, 2, 8, 9)
        self.r2 = Rectangle(99999999999999, 999999999999, 2, 8, 9)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        del Base._Base__nb_objects
        del self.r1

    def test_area_normal(self):
        """A method that that tests area with normal parameters"""
        self.assertEqual(self.r1.area(), 70)

    def test_area_large(self):
        """A method that that tests area with large parameters"""
        self.assertEqual(self.r2.area(), 99999999999899000000000001)

    def test_area_change_rectangle_parameters(self):
        """A method that that tests area when rectangle is assigned new
        parameters.
        """
        self.r1.width = 20
        self.r1.height = 21
        self.assertEqual(self.r1.area(), 420)

    def test_area_with_args(self):
        """A method that tests area with args provided."""
        with self.assertRaises(TypeError):
            self.r1.area(17)


if __name__ == "__main__":
    unittest.main()
