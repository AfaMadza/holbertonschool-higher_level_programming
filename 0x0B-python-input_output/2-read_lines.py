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
    line_no = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            if nb_lines <= 0 or nb_lines > f.seek(0, 2):
                print(line, end='')
            else:
                line_no += 1
                if line_no <= nb_lines:
                    print(line, end='')
