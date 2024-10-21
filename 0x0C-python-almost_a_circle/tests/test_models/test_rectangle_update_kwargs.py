#!/usr/bin/python3
"""Unittests for rectangle.py."""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleUpdateKwargs(unittest.TestCase):
    """A class representing test cases for the update method of
    Rectangle class, implementing *kwargs functionality.
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

    def test_update_kwargs_zero(self):
        """A method that tests update with no **kwargs."""
        self.r1.update()
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_kwargs_one(self):
        """A method that tests update with one **kwargs provided."""
        self.r1.update(id=17)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 10/10 - 10/10")

    def test_update_kwargs_two(self):
        """A method that tests update with two **kwargs provided."""
        self.r1.update(id=17, width=150)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 10/10 - 150/10")

    def test_update_kwargs_three(self):
        """A method that tests update with three **kwargs provided."""
        self.r1.update(id=17, height=150, width=25)
        self.assertEqual(str(self.r1), "[Rectangle] (17) 10/10 - 25/150")

    def test_update_kwargs_four(self):
        """A method that tests update with four **kwargs provided."""
        self.r1.update(height=17, id=150, x=25, width=20)
        self.assertEqual(str(self.r1), "[Rectangle] (150) 25/10 - 20/17")

    def test_update_kwargs_five(self):
        """A method that tests update with five **kwargs provided."""
        self.r1.update(height=17, y=150, x=25, width=20, id=40)
        self.assertEqual(str(self.r1), "[Rectangle] (40) 25/150 - 20/17")

    def test_update_kwargs_six_plus(self):
        """A method that tests update with minimum six **kwargs provided."""
        self.r1.update(width=17, height=150, extra=25, x=20, y=40, id=6)
        self.assertEqual(str(self.r1), "[Rectangle] (6) 20/40 - 17/150")

    def test_update_kwargs_id_is_none(self):
        """A method that tests update with id is None."""
        self.r1.update(id=None)
        (self.assertEqual(str(self.r1),
                          (f"[Rectangle] ({self.r1.id}) 10/10 - 10/10")))

    def test_update_kwargs_id_is_none_plus(self):
        """A method that tests update with id is None, with other parameters
        set.
        """
        self.r1.update(x=2, y=3, height=4, width=5, id=None)
        (self.assertEqual(str(self.r1),
                          (f"[Rectangle] ({self.r1.id}) 2/3 - 5/4")))

    def test_update_kwargs_with_two_calls(self):
        """A method that tests update with two calls of method."""
        self.r1.update(width=17, x=150, id=25, height=20, y=40, extra=6)
        self.r1.update(id=1, width=4, height=5, x=8, y=9)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 8/9 - 4/5")

    def test_update_kwargs_width_not_int(self):
        """A method that tests update with width not int."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r1.update(x=100, width="string")

    def test_update_kwargs_width_zero(self):
        """A method that tests update with width=0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.update(width=0)

    def test_update_kwargs_width_less_than_zero(self):
        """A method that tests update with width<0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r1.update(y=100, width=-17)

    def test_update_kwargs_height_not_int(self):
        """A method that tests update with height not int."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r1.update(y=100, id=3, height="string")

    def test_update_kwargs_height_zero(self):
        """A method that tests update with height=0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r1.update(height=0)

    def test_update_kwargs_height_less_than_zero(self):
        """A method that tests update with height<0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r1.update(height=-17)

    def test_update_kwargs_x_not_int(self):
        """A method that tests update with x not int."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r1.update(x="x")

    def test_update_kwargs_x_less_than_zero(self):
        """A method that tests update with x<0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r1.update(x=-2)

    def test_update_kwargs_y_not_int(self):
        """A method that tests update with y not int."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r1.update(y="y")

    def test_update_kwargs_y_less_than_zero(self):
        """A method that tests update with y<0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r1.update(y=-2)

    def test_update_args_kwargs(self):
        """A method that tests update providing both *args and **kwargs."""
        self.r1.update(1, 4, 5, y=8, x=9)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 4/5")

    def test_update_kwargs_keys_wrong(self):
        """A method that tests update providing wrong keys."""
        self.r1.update(pid=1, weight=5, v=8, u=9)
        self.assertEqual(str(self.r1), "[Rectangle] (1) 10/10 - 10/10")

    def test_update_kwargs_some_keys_wrong(self):
        """A method that tests update providing wrong keys."""
        self.r1.update(weight=1, id=4, x=5, v=8, u=9)
        self.assertEqual(str(self.r1), "[Rectangle] (4) 5/10 - 10/10")


if __name__ == "__main__":
    unittest.main()
