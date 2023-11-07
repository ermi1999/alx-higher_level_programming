#!/usr/bin/python3
"""
This program writes a string into a text file by appending it.
"""


def append_write(filename="", text=""):
    """
    This function writes a string into a text file by appending it.
    Args:
        filename: the name of the file.
        text: the text to be written.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
