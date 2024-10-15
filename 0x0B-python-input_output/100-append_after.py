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

    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    line_list = []

    for line in lines:
        line_list.append(line)
        if search_string in line:
            line_list.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
