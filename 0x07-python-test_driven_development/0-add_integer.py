#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """A function that adds 2 integers.

    Args:
        a: first integer.
        b: second integer, initialized to 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        Integer addition of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
