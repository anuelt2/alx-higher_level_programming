#!/usr/bin/python3
"""Module for from_json_string function"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str: JSON string.

    Returns:
        Python data structure object.
    """

    return json.loads(my_str)
