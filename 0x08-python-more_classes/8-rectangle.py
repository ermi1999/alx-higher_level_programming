#!/usr/bin/python3
"""
This program defines a class called Rectangle.
"""


class Rectangle():
    """
    Defines a class called rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initializes private property width and height.
        Args:
            width: an integer.
            height: an integer.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        getter for width.
        """
        return self.__width

    @property
    def height(self):
        """
        getter for height.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter for width.
        Args:
            value: the value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter for height.
        Args:
            value: The value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns the perimeter of length and width.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Returns a string representation of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbols = ""
        for i in range(self.__height):
            symbols += str(self.print_symbol) * self.__width
            symbols += "\n"
        return symbols.rstrip()

    def __call__(self):
        """
        Returns a string representation of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbols = ""
        for i in range(self.__height):
            symbols += str(self.print_symbol) * self.__width
            symbols += "\n"
        return symbols.rstrip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        delets the rectangle.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        Args:
            rect_1: an instance of Rectangle.
            rect_1: an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
