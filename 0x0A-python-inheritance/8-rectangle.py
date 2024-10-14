#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Define a rectangle class"""


class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
