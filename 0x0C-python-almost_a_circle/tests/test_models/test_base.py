#!/usr/bin/python3
"""Unittests for base.py."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class representing test cases for Base class."""

    def setUp(self):
        """Method that sets up the necessary environmentand
        objects for running each test.
        """
        # Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Method that cleans up the test environment after
        each test is executed.
        """
        # Base._Base__nb_objects = 0
        pass

    def test_id_is_not_none(self):
        """A method that tests for when id is not None."""
        base1 = Base(23)
        self.assertEqual(base1.id, 23)

    def test_id_is_none(self):
        """A method that tests for when id is None."""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_id_is_none_and_not_none(self):
        """A method that tests for when id is None and is not None."""
        base1 = Base()
        base2 = Base(12)
        base3 = Base(255)
        base4 = Base()
        base5 = Base()
        self.assertEqual(base1.id, base4.id - 1)
        self.assertEqual(base2.id, 12)
        self.assertEqual(base3.id, 255)
        self.assertEqual(base4.id, base5.id - 1)

    def test_nb_objects_increments_when_id_is_none(self):
        """A method that tests for __nb_objects increment when id is None."""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, base2.id - 1)
        self.assertEqual(base2.id, base3.id - 1)

    def test_id_is_public_instance_attribute(self):
        """A method that tests id is public instance attribute."""
        base1 = Base()
        base1.id = 123
        self.assertEqual(base1.id, 123)

    def test_nb_objects_is_private_class_attribute(self):
        """A method that tests nb_objects is private class attribute."""
        base1 = Base()
        with self.assertRaises(AttributeError):
            base1.__nb_objects

    def test_str_id(self):
        """A method that tests for when id is str."""
        base1 = Base("id")
        self.assertEqual(base1.id, "id")

    def test_float_id(self):
        """A method that tests for when id is float."""
        base1 = Base(9.3)
        self.assertEqual(base1.id, 9.3)

    def test_complex_id(self):
        """A method that tests for when id is a complex number."""
        base1 = Base(2+1j)
        self.assertEqual(base1.id, 2+1j)

    def test_inf_id(self):
        """A method that tests for when id is inf."""
        base1 = Base(float('inf'))
        self.assertEqual(base1.id, float('inf'))

    def test_NaN_id(self):
        """A method that tests for when id is NaN."""
        base1 = Base(float('NaN'))
        self.assertNotEqual(base1.id, float('NaN'))

    def test_two_class_args(self):
        """A method that tests for two args when creating class instance."""
        with self.assertRaises(TypeError):
            base1 = Base(1, 2)


if __name__ == "__main__":
    unittest.main()
