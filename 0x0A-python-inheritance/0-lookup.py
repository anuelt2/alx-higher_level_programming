#!/usr/bin/python3
"""Module for lookup function"""


def lookup(obj):
    """A function that returns the list of available
    attributes and methods of an object.

    Args:
        obj: The object of focus.

    Returns:
        List of attributes and objects
    """

    return dir(obj)
