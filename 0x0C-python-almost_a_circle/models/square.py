#!/usr/bin/python3
"""Module that defines Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class representing a square, that inherits from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square, with size, x, y, id.

        Args:
            size: Size of square.
            x: x-coordinate.
            y: y- coordinate.
            id: Unique id for each square instance.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Custom __str__ method. Returns string representation of Square."""
        return ("[Square] (" + str(self.id) + ") " + str(self.x) + "/"
                + str(self.y) + " - " + str(self.width))
