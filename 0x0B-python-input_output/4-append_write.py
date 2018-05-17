#!/usr/bin/python3
"""
This module contains a function that appends a string to a text
file (UTF8) and returns number of characters.
"""


def append_write(filename="", text=""):
    """
    append_write - appends a string to a text file
    Args:
        filename: file's name
        text: text to be written to file
    """
    with open(filename, mode='a', encoding ='utf-8') as f:
        return f.write(text)
