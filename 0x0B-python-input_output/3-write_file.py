#!/usr/bin/python3
"""
This module contains a function that writes a string to a text
file (UTF8) and returns number of characters.
"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file
    Args:
        filename: file's name
        text: text to be written to file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
