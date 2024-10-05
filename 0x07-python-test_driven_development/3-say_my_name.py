#!/usr/bin/python3
"""Module for say_my_name function"""


def say_my_name(first_name, last_name=""):
    """A function that prints a given name.

    Args:
        first_name: First name.
        last_name: Last name.

    Raises:
        TypeError: If first_name, last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
