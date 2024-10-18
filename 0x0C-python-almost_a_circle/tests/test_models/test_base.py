#!/usr/bin/python3
"""Unittest for Base class."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class representing test cases for Base class."""

    def setUp(self):
        """"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """"""
        del Base._Base__nb_objects

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
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 12)
        self.assertEqual(base3.id, 255)
        self.assertEqual(base4.id, 2)
        self.assertEqual(base5.id, 3)

    def test_nb_objects_increments_when_id_is_none(self):
        """A method that tests for __nb_objects increment when id is None."""
        base1 = Base()
        self.assertEqual(base1._Base__nb_objects, 1)
        base2 = Base()
        self.assertEqual(base2._Base__nb_objects, 2)
        base3 = Base()
        self.assertEqual(base3._Base__nb_objects, 3)

    def test_nb_objects_reset_after_each_test(self):
        """A method that tests reset of __nb_objects between tests. """
        base5 = Base()
        self.assertEqual(base5._Base__nb_objects, 1)

    def test_nb_objects_status_when_id_is_not_none(self):
        """A method that tests for __nb_objects status when id is not None."""
        base1 = Base(123)
        self.assertEqual(base1._Base__nb_objects, 0)
        base2 = Base(246)
        self.assertEqual(base2._Base__nb_objects, 0)
        base3 = Base(357)
        self.assertEqual(base3._Base__nb_objects, 0)
