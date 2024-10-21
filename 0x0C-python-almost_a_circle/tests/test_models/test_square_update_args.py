#!/usr/bin/python3
"""Unittests for square.py."""

import unittest
from models.base import Base
from models.square import Square


class TestSquareUpdateArgs(unittest.TestCase):
    """A class representing test cases for the update method of
    Square class, implementing *args functionality.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        Base._Base__nb_objects = 0
        self.s1 = Square(10, 10, 10)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        del Base._Base__nb_objects
        del self.s1

    def test_update_args_zero(self):
        """A method that tests update with no *args."""
        self.s1.update()
        self.assertEqual(str(self.s1), "[Square] (1) 10/10 - 10")

    def test_update_args_one(self):
        """A method that tests update with one *args provided."""
        self.s1.update(17)
        self.assertEqual(str(self.s1), "[Square] (17) 10/10 - 10")

    def test_update_args_two(self):
        """A method that tests update with two *args provided."""
        self.s1.update(17, 150)
        self.assertEqual(str(self.s1), "[Square] (17) 10/10 - 150")

    def test_update_args_three(self):
        """A method that tests update with three *args provided."""
        self.s1.update(17, 150, 25)
        self.assertEqual(str(self.s1), "[Square] (17) 25/10 - 150")

    def test_update_args_four(self):
        """A method that tests update with four *args provided."""
        self.s1.update(17, 150, 25, 20)
        self.assertEqual(str(self.s1), "[Square] (17) 25/20 - 150")

    def test_update_args_four_plus(self):
        """A method that tests update with minimum five *args provided."""
        self.s1.update(17, 150, 25, 20, 40)
        self.assertEqual(str(self.s1), "[Square] (17) 25/20 - 150")

    def test_update_args_id_is_none(self):
        """A method that tests update with id is None."""
        self.s1.update(None)
        (self.assertEqual(str(self.s1),
                          (f"[Square] ({self.s1.id}) 10/10 - 10")))

    def test_update_args_id_is_none_plus(self):
        """A method that tests update with id is None, with other parameters
        set.
        """
        self.s1.update(None, 2, 3, 4, 5)
        (self.assertEqual(str(self.s1),
                          (f"[Square] ({self.s1.id}) 3/4 - 2")))

    def test_update_args_with_two_calls(self):
        """A method that tests update with two calls of method."""
        self.s1.update(17, 150, 25, 20, 40, 6)
        self.s1.update(1, 4, 5, 8, 9)
        self.assertEqual(str(self.s1), "[Square] (1) 5/8 - 4")

    def test_update_args_size_not_int(self):
        """A method that tests update with size not int."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.update(100, "string")

    def test_update_args_size_zero(self):
        """A method that tests update with size=0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.update(100, 0)

    def test_update_args_size_less_than_zero(self):
        """A method that tests update with size<0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.update(100, -17)

    def test_update_args_x_not_int(self):
        """A method that tests update with x not int."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.update(3, 7, "x")

    def test_update_args_x_less_than_zero(self):
        """A method that tests update with x<0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.s1.update(133, 5, -2)

    def test_update_args_y_not_int(self):
        """A method that tests update with y not int."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.update(3, 7, 5, "y")

    def test_update_args_y_less_than_zero(self):
        """A method that tests update with y<0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s1.update(33, 5, 15, -2)

    def test_update_args_size_before_x(self):
        """A method that tests update to check size set before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.update(1, "size", "x")

    def test_update_args_size_before_y(self):
        """A method that tests update to check size set before y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.update(1, "size", 2, "y")

    def test_update_args_x_before_y(self):
        """A method that tests update to check x set before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.update(15, 12, "x", "y")


if __name__ == "__main__":
    unittest.main()
