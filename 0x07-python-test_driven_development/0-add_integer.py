#!/usr/bin/python3
""" Adds two integers or floats
    It needs two integers as an argument.
    The second argument is optional.
    if there is no second argument 98 gets passed automatically
    and returns the addition of the two integers.
"""


def add_integer(a, b=98):
    """
    Adds Two integers and Returns the result
    Args:
        a: the first number to be added.
        b: the second number to be added.
    Returns:
        int: The addition of the two numbers.
    Raises:
        TypeError: if a or b is not an integer or a float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
