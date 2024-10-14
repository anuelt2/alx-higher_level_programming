#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is an instance of
    a class that inherited(directly or not) from the specified class.

    Args:
        obj: The object.
        a_class: The class.

    Returns:
        True or False
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
