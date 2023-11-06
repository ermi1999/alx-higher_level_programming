#!/usr/bin/python3
"""
This program validets an integer.
"""


class BaseGeometry:
    """
    Initializes a class called BaseGeometry.
    """
    def area(self):
        """
        Raises an exceprion when it is called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates an integer.
        Args:
            name: the name of the integer.
            value: the integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
