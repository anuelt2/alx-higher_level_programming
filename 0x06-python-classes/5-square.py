#!/usr/bin/python3
"""Define a square class"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializes a square with a size"""
        self.__size = size

    """Getter for size private instance attribute"""
    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of a square based on current size"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
