#!/usr/bin/python3
"""
This program raises an error when area is called.
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
