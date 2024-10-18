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
        if not isinstance(width, int):
            raise TypError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    """height private instance attribute."""
    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height attribute."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    """x private instance attribute."""
    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x attribute."""
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    """y private instance attribute."""
    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y."""
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints to stdout the Rectangle instance with # character."""
        for h in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Custom __str__ method. Returns string representation
        of Rectangle.
        """
        return ("[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/"
                + str(self.__y) + " - " + str(self.__width) + "/" +
                str(self.__height))
