#!/usr/bin/python3
"""Module for class_to_json function"""


def class_to_json(obj):
    """Returns dictionary description with simple data
    structure for JSON serialization of an object.

    Args:
        obj: Instance of a class

    Returns:
        Dictionary description of object.
    """

    return obj.__dict__
