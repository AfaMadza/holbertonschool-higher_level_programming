#!/usr/bin/python3
"""Module docstring
This module creates a class Square that defines a square by:
(based on 1-square.py)
"""


class Square:
    """ Class docstring
    This class defines a square by: (based on 1-square.py).
    With size validation.
    Args:
        size (int): size of square
    """

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError('size must be an integer')
        elif __size < 0:
            raise ValueError('size must be >= 0')
        self.__size = __size
