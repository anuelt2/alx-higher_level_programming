#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.square import Square


class TestSquareUpdateKwargs(unittest.TestCase):
    """A class representing test cases for the update method of
    Square class, implementing **kwargs functionality.
    """

    def setUp(self):
        """Method that sets up the necessary environment
        and objects for running each test.
        """
        # Base._Base__nb_objects = 0
        self.s1 = Square(10, 10, 10, 10)

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        # del Base._Base__nb_objects
        del self.s1

    def test_update_kwargs_zero(self):
        """A method that tests update with no **kwargs."""
        self.s1.update()
        self.assertEqual(str(self.s1), "[Square] (10) 10/10 - 10")

    def test_update_kwargs_one(self):
        """A method that tests update with one **kwargs provided."""
        self.s1.update(id=17)
        self.assertEqual(str(self.s1), "[Square] (17) 10/10 - 10")

    def test_update_kwargs_two(self):
        """A method that tests update with two **kwargs provided."""
        self.s1.update(id=17, size=150)
        self.assertEqual(str(self.s1), "[Square] (17) 10/10 - 150")

    def test_update_kwargs_three(self):
        """A method that tests update with three **kwargs provided."""
        self.s1.update(id=17, x=150, y=25)
        self.assertEqual(str(self.s1), "[Square] (17) 150/25 - 10")

    def test_update_kwargs_four(self):
        """A method that tests update with four **kwargs provided."""
        self.s1.update(size=17, id=150, x=25, y=20)
        self.assertEqual(str(self.s1), "[Square] (150) 25/20 - 17")

    def test_update_kwargs_four_plus(self):
        """A method that tests update with minimum five **kwargs provided."""
        self.s1.update(size=17, y=150, x=25, weight=20, id=40)
        self.assertEqual(str(self.s1), "[Square] (40) 25/150 - 17")

    def test_update_kwargs_id_is_none(self):
        """A method that tests update with id is None."""
        self.s1.update(id=None)
        (self.assertEqual(str(self.s1),
                          (f"[Square] ({self.s1.id}) 10/10 - 10")))

    def test_update_kwargs_id_is_none_plus(self):
        """A method that tests update with id is None, with other parameters
        set.
        """
        self.s1.update(x=2, y=3, size=4, id=None)
        (self.assertEqual(str(self.s1),
                          (f"[Square] ({self.s1.id}) 2/3 - 4")))

    def test_update_kwargs_with_two_calls(self):
        """A method that tests update with two calls of method."""
        self.s1.update(x=150, id=25, size=20, y=40, extra=6)
        self.s1.update(id=1, size=4, x=8, y=9)
        self.assertEqual(str(self.s1), "[Square] (1) 8/9 - 4")

    def test_update_kwargs_size_not_int(self):
        """A method that tests update with size not int."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.update(x=100, size="string")

    def test_update_kwargs_size_zero(self):
        """A method that tests update with size=0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.update(size=0)

    def test_update_kwargs_size_less_than_zero(self):
        """A method that tests update with size<0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s1.update(y=100, size=-17)

    def test_update_kwargs_x_not_int(self):
        """A method that tests update with x not int."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.update(x="x")

    def test_update_kwargs_x_less_than_zero(self):
        """A method that tests update with x<0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.s1.update(x=-2)

    def test_update_kwargs_y_not_int(self):
        """A method that tests update with y not int."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.update(y="y")

    def test_update_kwargs_y_less_than_zero(self):
        """A method that tests update with y<0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s1.update(y=-2)

    def test_update_args_kwargs(self):
        """A method that tests update providing both *args and **kwargs."""
        self.s1.update(1, 5, y=8, x=9)
        self.assertEqual(str(self.s1), "[Square] (1) 10/10 - 5")

    def test_update_kwargs_keys_wrong(self):
        """A method that tests update providing wrong keys."""
        self.s1.update(pid=1, weight=5, v=8, u=9)
        self.assertEqual(str(self.s1), "[Square] (10) 10/10 - 10")

    def test_update_kwargs_some_keys_wrong(self):
        """A method that tests update providing wrong keys."""
        self.s1.update(weight=1, id=4, x=5, v=8, u=9)
        self.assertEqual(str(self.s1), "[Square] (4) 5/10 - 10")

    def test_update_kwargs_width_setter(self):
        """A method that tests implementation of width setter for Square."""
        self.s1.update(size=1, id=4, x=5)
        self.assertEqual(self.s1.width, 1)

    def test_update_kwargs_height_setter(self):
        """A method that tests implementation of height setter for Square."""
        self.s1.update(size=11, id=4, y=5)
        self.assertEqual(self.s1.height, 11)


if __name__ == "__main__":
    unittest.main()
