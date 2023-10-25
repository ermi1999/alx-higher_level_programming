#!/usr/bin/python3
""" defines a Private instance attribute: size """


class Square:
    """
    defines a Private instance attribute size

    """
    def __init__(self, size=0, position=(0, 0)):
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

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int) or \
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        Returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Returns the size.
        """
        return self.__size

    @property
    def position(self):
        """
        Returns the size of position.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Sets the size.
        Args:
            size The size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        Sets the position
        Args:
            value a tuple value of the position
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
            return
        i = 0
        while i < self.__position[1]:
            print()
            i += 1
        i = 0
        while i < self.__size:
            print(" " * self.__position[0] + "#" * self.__size)
            i += 1
