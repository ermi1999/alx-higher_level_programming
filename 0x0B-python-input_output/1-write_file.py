#!/usr/bin/python3
"""
This program writes a string into a text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    This function writes a string into a text file.
    Args:
        filename: The name of the file to be created.
        text: the text to be written.
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
