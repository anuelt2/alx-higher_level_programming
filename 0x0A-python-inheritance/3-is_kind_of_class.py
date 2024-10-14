#!/usr/bin/python3
"""Module for is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object is an instance
    of tha class, or of a class that inherits from the class.

    Args:
        obj: The object.
        a_class: The class.

    Returns:
        True or False
    """

    return isinstance(obj, a_class)
