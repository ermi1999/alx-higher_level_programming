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

    def __lt__(self, self1):
        """
        Implements the less than operator.
        """
        if isinstance(self1, Square):
            return self.__size < self1.__size
        raise TypeError("Unsupported operand")

    def __le__(self, self1):
        """
        Implements the less than or equal to operator.
        """
        if isinstance(self1, Square):
            return self.__size <= self1.__size
        raise TypeError("Unsupported operand")

    def __eq__(self, self1):
        """
        Implements the equal to operator.
        """
        if isinstance(self1, Square):
            return self.__size == self1.__size
        return False

    def __ne__(self, self1):
        """
        Implements the not equal to  operator.
        """
        return not self.__eq__(self1)

    def __gt__(self, self1):
        """
        Implements the greater than operator.
        """
        if isinstance(self1, Square):
            return self.__size > self1.__size
        raise TypeError("Unsupported operand")

    def __lt__(self, self1):
        """
        Implements the greater than or equal to operator.
        """
        if isinstance(self1, Square):
            return self.__size >= self1.__size
        raise TypeError("Unsupported operand")

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
