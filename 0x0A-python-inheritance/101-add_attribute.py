#!/usr/bin/python3
"""Module for add_attribute function"""


def add_attribute(obj, attribute, value):
    """A function that adds attribute to object
    if possible.

    Args:
        obj: Object to which attribute will be added
        attribute: Name of attribute to be added
        value: Value of attribute to be added

    Raises:
        TypeError: If object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
