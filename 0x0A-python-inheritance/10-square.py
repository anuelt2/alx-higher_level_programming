#!/usr/bin/python3
"""Define square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """Initializes a square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2
