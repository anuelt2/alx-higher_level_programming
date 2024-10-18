#!/usr/bin/python3
"""Module that defines Base class."""


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
