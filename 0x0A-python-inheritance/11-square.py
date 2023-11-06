#!/usr/bin/python3
"""
This program intializes the class square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class intializes the object square.
    Args:
        Rectangle: The class that the object inherits from.
    """
    def __init__(self, size):
        """
        This function initializes size.
        Args:
            size: The size.
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        This function returns the area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        This function Returns a string.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
