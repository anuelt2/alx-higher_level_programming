#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleUpdateArgs(unittest.TestCase):
    """A class representing test cases for the update method of
    Rectangle class, implementing *args functionality.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        Base._Base__nb_objects = 0
        self.r1 = Rectangle(10, 10, 10, 10)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        del Base._Base__nb_objects
        del self.r1

    def test_update_args_zero(self):
        """A method that tests update with no *args."""
        self.r1.update()
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_args_one(self):
        """A method that tests update with one *args provided."""
        self.r1.update(17)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 10/10 - 10/10")

    def test_update_args_two(self):
        """A method that tests update with two *args provided."""
        self.r1.update(17, 150)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 10/10 - 150/10")

    def test_update_args_three(self):
        """A method that tests update with three *args provided."""
        self.r1.update(17, 150, 25)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 10/10 - 150/25")

    def test_update_args_four(self):
        """A method that tests update with four *args provided."""
        self.r1.update(17, 150, 25, 20)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 20/10 - 150/25")

    def test_update_args_five(self):
        """A method that tests update with five *args provided."""
        self.r1.update(17, 150, 25, 20, 40)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 20/40 - 150/25")

    def test_update_args_six_plus(self):
        """A method that tests update with minimum six *args provided."""
        self.r1.update(17, 150, 25, 20, 40, 6)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 20/40 - 150/25")

    def test_update_args_id_is_none(self):
        """A method that tests update with id is None."""
        self.r1.update(None)
        (self.assertEqual(str(self.r1),
                          (f"[Rectangle] ({self.r1.id}) 10/10 - 10/10")))

    def test_update_args_id_is_none_plus(self):
        """A method that tests update with id is None, with other parameters
        set.
        """
        self.r1.update(None, 2, 3, 4, 5)
        (self.assertEqual(str(self.r1),
                          (f"[Rectangle] ({self.r1.id}) 4/5 - 2/3")))

    def test_update_args_with_two_calls(self):
        """A method that tests update with two calls of method."""
        self.r1.update(17, 150, 25, 20, 40, 6)
        self.r1.update(1, 4, 5, 8, 9)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 8/9 - 4/5")

    def test_update_args_width_not_int(self):
        """A method that tests update with width not int."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(100, "string")

    def test_update_args_width_zero(self):
        """A method that tests update with width=0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.update(100, 0)

    def test_update_args_width_less_than_zero(self):
        """A method that tests update with width<0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.update(100, -17)

    def test_update_args_height_not_int(self):
        """A method that tests update with height not int."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r1.update(100, 3, "string")

    def test_update_args_height_zero(self):
        """A method that tests update with height=0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r1.update(100, 13, 0)

    def test_update_args_height_less_than_zero(self):
        """A method that tests update with height<0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r1.update(100, 133, -17)

    def test_update_args_x_not_int(self):
        """A method that tests update with x not int."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r1.update(100, 3, 7, "x")

    def test_update_args_x_less_than_zero(self):
        """A method that tests update with x<0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r1.update(100, 133, 5, -2)

    def test_update_args_y_not_int(self):
        """A method that tests update with y not int."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r1.update(100, 3, 7, 5, "y")

    def test_update_args_y_less_than_zero(self):
        """A method that tests update with y<0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r1.update(100, 133, 5, 15, -2)

    def test_update_args_width_before_height(self):
        """A method that tests update to check width set before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(100, "width", "height")

    def test_update_args_width_before_x(self):
        """A method that tests update to check width set before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(100, "width", 12, "x")

    def test_update_args_width_before_y(self):
        """A method that tests update to check width set before y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(100, "width", 12, 2, "y")

    def test_update_args_height_before_x(self):
        """A method that tests update to check height set before x."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r1.update(100, 15, "height", "x", 12)

    def test_update_args_height_before_y(self):
        """A method that tests update to check height set before y."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r1.update(100, 15, "height", 2, "y")

    def test_update_args_x_before_y(self):
        """A method that tests update to check x set before y."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r1.update(100, 15, 12, "x", "y")


if __name__ == "__main__":
    unittest.main()
