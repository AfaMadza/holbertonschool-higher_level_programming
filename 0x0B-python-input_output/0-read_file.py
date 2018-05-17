#!/usr/bin/python3
"""
This module contains a function that reads a text file
(UTF*) and prints it to stdout.
"""


def read_file(filename=""):
    """
    read_file - reads a file and prints to stdout
    Args:
        filename: file's name
    """
    with open(filename, mode='r', encoding ='utf-8') as f:
        for line in f:
            print(line, end='')
