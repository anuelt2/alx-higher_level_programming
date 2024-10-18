#!/usr/bin/python3
"""Module that defines Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle, that inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle, with width, height, x, y, id.

        Args:
            width: Width of rectangle.
            height: Height of rectangle.
            x:
            y:
            id: Unique id for each rectangle instance.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """width private instance attribute."""
    @property
    def width(self):
        """Getter for width atrribute."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width attribute."""
        self.__width = width

    """height private instance attribute."""
    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height attribute."""
        self.__height = height

    """x private instance attribute."""
    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x attribute."""
        self.__x = x

    """y private instance attribute."""
    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y."""
        self.__y = y
