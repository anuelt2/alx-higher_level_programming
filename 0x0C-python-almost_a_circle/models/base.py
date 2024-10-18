#!/usr/bin/python3
"""Module that defines Base class."""
import json


class Base:
    """A class representing a base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a base, with id.

        Args:
            id: Unique id for new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries."""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
