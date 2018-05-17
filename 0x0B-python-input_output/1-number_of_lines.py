#!/usr/bin/python3
"""
This module contains a function that returns the number
of lines in a text file.
"""


def number_of_lines(filename=""):
    """
    read_file - reads a file and prints to stdout
    Args:
        filename: file's name
    """
    line_no = 0
    with open(filename, mode='r', encoding ='utf-8') as f:
        for line in f:
            line_no += 1
        return line_no
