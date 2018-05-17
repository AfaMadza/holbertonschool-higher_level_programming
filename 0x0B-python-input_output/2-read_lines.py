#!/usr/bin/python3
"""
This module contains a function that reads n lines of a text
file (UTF8) and prints it to stdout.
"""


def read_lines(filename="", nb_lines=0):
    """
    read_lines - reads n lines and prints to stdout
    Args:
        filename: file's name
    """
    if nb_lines < 0:
        nb_lines = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line_no, line in enumerate(f):
            if nb_lines and nb_lines == line_no:
                break
            print(line, end='')
