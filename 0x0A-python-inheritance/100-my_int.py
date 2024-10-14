#!/usr/bin/python3
"""Define MyInt class"""


class MyInt(int):
    """A class representing myint"""

    def __eq__(self, other):
        """Change == to !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Change != to =="""
        return super().__eq__(other)
