#!/usr/bin/python3
"""Module for load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file".

    Args:
        filename: Name of "JSON file".
    """

    with open(filename) as f:
        return json.load(f)
