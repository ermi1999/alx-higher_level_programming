#!/usr/bin/python3
"""
This program prints a person name given as an argument.
last name is optional.
first name must be a string otherwise it raises an error
last name must be a string otherwise it raises an error
"""


def say_my_name(first_name, last_name=""):
    """
    this function prints a string given as an argument.
    Args:
        first_name: the first name to be printed.
        last_name: (optional) the last name to be printed
    Returns:
        Nothing.
    Raises:
        TypeError: if first name or last name doesn't exist.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
