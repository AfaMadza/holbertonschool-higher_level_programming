#!/usr/bin/python3
"""Module docstring
This module creates a class Square that defines a square by:
(based on 3-square.py)
"""


class Square:
    """ Class docstring
    __init__: This class defines a square by: (based on 3-square.py).

    Args:
        size (int): size of square
    Attributes:
        size: (int): size of square
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ Getter property for size. Setter below"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Method docstring Returns: Area of square"""
        return self.__size * self.__size
