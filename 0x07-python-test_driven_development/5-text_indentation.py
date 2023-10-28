#!/usr/bin/python3
"""
This program prints a string given to it as an argument.
It prints two new lines after each ., ? and :
the argument have to be a string.
"""


def text_indentation(text):
    """
    This function prints a string given to it as an argument.
    and adds two new lines on every ., ? and : it encounters.
    Args:
        text: The string to be printed
    Returns:
        nothing.
    Raises:
        TypeError: if the text is not an integer
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        if result and result[-1] == "\n" and char == " ":
            continue
        result += char
        if char == "." or char == "?" or char == ":":
            result += '\n\n'
    print(result, end='')

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
