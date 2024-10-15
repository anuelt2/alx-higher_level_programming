#!/usr/bin/python3
"""Define a student class"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student, with first_name, last_name, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if (isinstance(attrs, list)
                and all(isinstance(attr, str) for attr in attrs)):
            attr_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    attr_dict[key] = value
            return attr_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
