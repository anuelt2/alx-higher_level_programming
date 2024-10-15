#!/usr/bin/python3
"""Module for write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file.
    Returns number of characters written.

    Args:
        filename: Name of text file.
        text: String to be written to file.

    Returns:
        Number of characters written.
    """

    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
