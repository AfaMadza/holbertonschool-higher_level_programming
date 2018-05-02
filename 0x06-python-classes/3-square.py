#!/usr/bin/python3
"""Module docstring
This module creates a class Square that defines a square by:
(based on 2-square.py)
"""


class Square:
    """ Class docstring
    __init__: This class defines a square by: (based on 2-square.py).

    Args:
        size (int): size of square
    Attributes:
        size: (int): size of square
    """

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError('size must be an integer')
        elif __size < 0:
            raise ValueError('size must be >= 0')
        self.__size = __size

    def area(self):
        """Method docstring Returns: Area of square"""
        self.area = self.__size * self.__size
        return self.area
