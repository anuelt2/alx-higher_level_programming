#!/usr/bin/python3
"""Define a basegeometry class"""


class BaseGeometry:
    """A class representing a base geometry"""

    def area(self):
        """Unimplemented public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as int"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
