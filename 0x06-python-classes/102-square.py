#!/usr/bin/python3
"""Define a sqaure class"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initializes a square, with a size"""
        self.__size = size

    """Getter for size private instance attribute"""
    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of a square based on current size"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define equal comparator for areas of sqaure"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define not-equal comparator for areas of sqaure"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Define greater than comparator for areas of sqaure"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define greater than or equal comparator for areas of sqaure"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Define less than comparator for areas of sqaure"""
        return self.area() < other.area()

    def __le__(self, other):
        """Define less than or equal comparator for areas of sqaure"""
        return self.area() <= other.area()
