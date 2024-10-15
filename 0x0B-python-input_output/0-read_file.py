#!/usr/bin/python3
"""Module for read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename: Name of text file.
    """

    with open(filename, encoding='utf-8') as f:
        print(f.read())
