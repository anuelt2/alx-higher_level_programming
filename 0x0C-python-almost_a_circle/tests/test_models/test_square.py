#!/usr/bin/python3
"""Unittests for square.py."""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """A class representing test cases for Square class."""

    def test_square_type_base(self):
        """A method that tests for Square type."""
        self.assertIsInstance(Square(1), Base)

    def test_square_no_args(self):
        """A method that tests for square instance with no args."""
        with self.assertRaises(TypeError):
            Square()

    def test_square_one_arg(self):
        """A method that tests for square instance with one arg."""
        r1 = Square(10)
        r2 = Square(2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_square_two_args(self):
        """A method that tests for square instance with two args."""
        r1 = Square(10, 2)
        r2 = Square(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_square_three_args(self):
        """A method that tests for square instance with three args."""
        r1 = Square(10, 2, 17)
        r2 = Square(2, 10, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_square_four_args(self):
        """A method that tests for square instance with four args."""
        r1 = Square(10, 2, 17, 3)
        r2 = Square(2, 10, 5, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_square_five_args_plus(self):
        """A method that tests for square instance with five args plus."""
        with self.assertRaises(TypeError):
            Square(10, 2, 17, 3, 12, 7)

    def test_square_size_is_private(self):
        """A method that checks for size as private attribute."""
        r1 = Square(10, 2, 17, 3)
        with self.assertRaises(AttributeError):
            r1.__size

    def test_square_x_is_private(self):
        """A method that checks for x as private attribute."""
        r1 = Square(10, 17, 3, 12)
        with self.assertRaises(AttributeError):
            r1.__x

    def test_square_y_is_private(self):
        """A method that checks for y as private attribute."""
        r1 = Square(10, 17, 3, 12)
        with self.assertRaises(AttributeError):
            r1.__y

    def test_square_size_getter(self):
        """A method that tests for size getter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        self.assertEqual(r1.size, 10)

    def test_square_size_setter(self):
        """A method that tests for size setter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        r1.size = 76
        self.assertEqual(r1.size, 76)
        with self.assertRaises(TypeError):
            Square("string", 7)
        with self.assertRaises(ValueError):
            Square(0, 7)
        with self.assertRaises(TypeError):
            Square(7.7, 7)

    def test_square_width_getter(self):
        """A method that tests for width getter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        r1.size = 23
        self.assertEqual(r1.width, 23)

    def test_square_height_getter(self):
        """A method that tests for height getter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        r1.size = 56
        self.assertEqual(r1.height, 56)

    def test_square_x_getter(self):
        """A method that tests for x getter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        self.assertEqual(r1.x, 2)

    def test_square_x_setter(self):
        """A method that tests for x setter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        r1.x = 176
        self.assertEqual(r1.x, 176)
        with self.assertRaises(TypeError):
            Square(7, "string")
        with self.assertRaises(ValueError):
            Square(7, -7)
        with self.assertRaises(TypeError):
            Square(7, 7.7)

    def test_square_y_getter(self):
        """A method that tests for y getter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        self.assertEqual(r1.y, 17)

    def test_square_y_setter(self):
        """A method that tests for y setter implementation for square."""
        r1 = Square(10, 2, 17, 3)
        r1.y = 6
        self.assertEqual(r1.y, 6)
        with self.assertRaises(TypeError):
            Square(7, 7, "string")
        with self.assertRaises(ValueError):
            Square(7, 7, -7)
        with self.assertRaises(TypeError):
            Square(7, 7, 7.7)


if __name__ == "__main__":
    unittest.main()
