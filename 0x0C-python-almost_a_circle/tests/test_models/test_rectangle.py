#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """A class representing test cases for Rectangle class."""

    def test_rectangle_type_base(self):
        """A method that tests for Rectangle type."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_rectangle_no_args(self):
        """A method that tests for rectangle instance with no args."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_one_arg(self):
        """A method that tests for rectangle instance with one arg."""
        with self.assertRaises(TypeError):
            Rectangle(57)

    def test_rectangle_two_args(self):
        """A method that tests for rectangle instance with two args."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_three_args(self):
        """A method that tests for rectangle instance with three args."""
        r1 = Rectangle(10, 2, 17)
        r2 = Rectangle(2, 10, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_four_args(self):
        """A method that tests for rectangle instance with four args."""
        r1 = Rectangle(10, 2, 17, 3)
        r2 = Rectangle(2, 10, 5, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rectangle_five_args(self):
        """A method that tests for rectangle instance with five args."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        r2 = Rectangle(2, 10, 5, 4, 15)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, 15)

    def test_rectangle_six_args_plus(self):
        """A method that tests for rectangle instance with six args plus."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 17, 3, 12, 7)

    def test_rectangle_width_is_private(self):
        """A method that checks for width as private attribute."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        with self.assertRaises(AttributeError):
            r1.__width

    def test_rectangle_height_is_private(self):
        """A method that checks for height as private attribute."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        with self.assertRaises(AttributeError):
            r1.__height

    def test_rectangle_x_is_private(self):
        """A method that checks for x as private attribute."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        with self.assertRaises(AttributeError):
            r1.__x

    def test_rectangle_y_is_private(self):
        """A method that checks for y as private attribute."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        with self.assertRaises(AttributeError):
            r1.__y

    def test_rectangle_width_getter(self):
        """A method that tests for width getter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        self.assertEqual(r1.width, 10)

    def test_rectangle_width_setter(self):
        """A method that tests for width setter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        r1.width = 76
        self.assertEqual(r1.width, 76)
        with self.assertRaises(TypeError):
            Rectangle("string", 7)
        with self.assertRaises(ValueError):
            Rectangle(0, 7)
        with self.assertRaises(TypeError):
            Rectangle(7.7, 7)

    def test_rectangle_height_getter(self):
        """A method that tests for height getter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        self.assertEqual(r1.height, 2)

    def test_rectangle_height_setter(self):
        """A method that tests for height setter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        r1.height = 76
        self.assertEqual(r1.height, 76)
        with self.assertRaises(TypeError):
            Rectangle(7, "string")
        with self.assertRaises(ValueError):
            Rectangle(7, 0)
        with self.assertRaises(TypeError):
            Rectangle(7, 7.7)

    def test_rectangle_x_getter(self):
        """A method that tests for x getter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        self.assertEqual(r1.x, 17)

    def test_rectangle_x_setter(self):
        """A method that tests for x setter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        r1.x = 176
        self.assertEqual(r1.x, 176)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, "string")
        with self.assertRaises(ValueError):
            Rectangle(7, 7, -7)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, 7.7)

    def test_rectangle_y_getter(self):
        """A method that tests for y getter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        self.assertEqual(r1.y, 3)

    def test_rectangle_y_setter(self):
        """A method that tests for y setter implementation for rectangle."""
        r1 = Rectangle(10, 2, 17, 3, 12)
        r1.y = 6
        self.assertEqual(r1.y, 6)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, 7, "string")
        with self.assertRaises(ValueError):
            Rectangle(7, 7, 7, -7)
        with self.assertRaises(TypeError):
            Rectangle(7, 7, 7, 7.7)


if __name__ == "__main__":
    unittest.main()
