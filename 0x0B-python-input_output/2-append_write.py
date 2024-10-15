#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file.
    Returns the number of characters added.

    Args:
        filename: Name of text file.
        text: String to be appended.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
