#!/usr/bin/python3
"""
This program Initializes a class that is inherited from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initializes a class that is inherited from BaseGeometry.
    Args:
        BaseGeometry: The class that is inherited from.
    """
    def __init__(self, width, height):
        """
        This function initializes width and height.
        Args:
            width: The width
            height: The height.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
