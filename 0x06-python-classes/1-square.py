#!/usr/bin/python3
""" defines a Private instance attribute: size """


class Square:
    """
    defines a Private instance attribute size

    """
    def __init__(self, size):
        """
        Initializes a Square object with a given size.
        Args:
            size The size of the square.
        """
        self.__size = size
