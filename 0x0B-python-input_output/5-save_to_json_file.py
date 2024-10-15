#!/usr/bin/python3
"""Module for save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file.
    Using a JSON representation.

    Args:
        my_obj: The Object.
        filename: Name of JSON text file.
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
