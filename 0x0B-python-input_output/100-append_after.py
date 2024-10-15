#!/usr/bin/python3
"""Module of append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line
    containing a specific string.

    Args:
        filename: Name of file.
        search_string: String to search.
        new_string: String to insert.
    """

    line_number = 0
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        for line in lines:
            line_number += 1
            if search_string in line:
                lines.insert(line_number, new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
