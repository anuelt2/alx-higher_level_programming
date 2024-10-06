#!/usr/bin/python3
"""Module for print_square function."""


def print_square(size):
    """A function that prints a square with the # character.

    Args:
        size: Length of the square.

    Raises:
        TypeError: If size is not int.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        for p in range(size):
            print("#", end="")
        print()
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
