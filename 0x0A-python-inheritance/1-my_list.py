#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """A class that is a subclass to list"""
    def print_sorted(self):
        """Prints a sorted list in ascending order"""
        print(sorted(self))
