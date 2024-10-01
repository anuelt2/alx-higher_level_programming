#!/usr/bin/python3
"""Define a magic class class"""
import math


class MagicClass:
    """A class representing a magic class"""

    def __init__(self, radius=0):
        """Initialize a magic class, with radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns area of a circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns circumference of a circle"""
        return 2 * math.pi * self.__radius
