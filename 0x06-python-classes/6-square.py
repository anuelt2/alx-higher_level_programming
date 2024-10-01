#!/usr/bin/python3
"""Define a sqaure class"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square, with size and position"""
        self.__size = size
        self.__position = position

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

    """Getter for position private instance attribute"""
    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if ((not isinstance(value, tuple))
                or (len(value) != 2)
                or (not (all(isinstance(i, int))
                         and i >= 0 for i in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns area of a square based on current size"""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
