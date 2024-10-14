#!/usr/bin/python3
"""Define a mylist class"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
