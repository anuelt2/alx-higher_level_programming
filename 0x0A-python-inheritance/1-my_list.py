#!/usr/bin/python3
"""Define a mylist class"""


class MyList(list):
    """A class that gets list inheritance"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))