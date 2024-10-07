#!/usr/bin/python3
"""Define a rectangle class"""


class Rectangle():
    """A class representing a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with width and height"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    """width private instance attribute"""
    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """height private instance attribute"""
    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join([str(self.print_symbol) * self.__width
                           for _ in range(self.__height)]))

    def __repr__(self):
        """Returns str representation of rectangle to recreate new instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Called when instance of rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new rectangle instance with width == height == size"""
        return cls(width=size, height=size)
