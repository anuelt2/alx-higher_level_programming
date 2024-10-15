#!/usr/bin/python3
"""Module for to_json_string function"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: The object.

    Returns:
        JSON representation of object.
    """

    return json.dumps(my_obj)
