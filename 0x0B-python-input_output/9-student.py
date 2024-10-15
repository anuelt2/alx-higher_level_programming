#!/usr/bin/python3
"""Define a student class"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student, with first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
