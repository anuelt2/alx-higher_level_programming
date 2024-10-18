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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of object to a file."""
        with open(f"{cls.__name__}.json", 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                str_json = Base.to_json_string(list_dict)
                f.write(str_json)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation."""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)
