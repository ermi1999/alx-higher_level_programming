#!/usr/bin/python3
""" defines a Private instance attribute: size """


class Square:
    """
    defines a Private instance attribute size

    """
    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.
        Args:
            size The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        Returns the current square area
        """
        return self.__size
