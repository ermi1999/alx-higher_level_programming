#!/usr/bin/python3
"""
This program prints a square with a character #.
The number of times it will be printed is passed as an argument.
The argument have to be an integer.
"""


def print_square(size):
    """
    This function prints a square size times.
    Args:
        size: The number of times to be printed.
    Returns:
        nothing.
    Raises:
        TypeError: if size is not an integer or if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    i = 0
    while i < size:
        print("#" * size)
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
