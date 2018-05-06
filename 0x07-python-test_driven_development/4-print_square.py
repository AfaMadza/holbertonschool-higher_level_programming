#!/usr/bin/python3
"""Module docstring
This module contains a function that prints a square
of specified dimensions by using the # character.
"""


def print_square(size):
    """Function docstring
    print_square: prints a square with the character #
    Args:
        size: length of square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
