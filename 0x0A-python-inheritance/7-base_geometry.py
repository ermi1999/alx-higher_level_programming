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


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
