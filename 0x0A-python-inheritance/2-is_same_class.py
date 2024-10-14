#!/usr/bin/python3
"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """A function that returns True if the object
    is exactly an instance of the specified class.

    Args:
        obj: The object.
        a_class: The class.

    Returns:
        True or False
    """

    return type(obj) is a_class
