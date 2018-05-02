#!/usr/bin/python3
"""Module docstring

This module creates a class Square that defines a square by:
(based on 4-square.py)

"""


class Square:

    """ Class docstring

    __init__: This class defines a square by: (based on 4-square.py).

    Args:
        size (int): size of square
        position (tuple): position where # will be printed
    Attributes:
        size: (int): size of square
        position (tuple): position where # will be printed
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter property for position. Position setter below."""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and\
           isinstance(value[0], int) and isinstance(value[1], int)\
           and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Method docstring

        Args: None

        Returns: Area of square """
        return self.__size * self.__size

    def my_print(self):
        """Method docstring Prints # according to position and size """

        if self.__size == 0:
            print()
        else:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("{:s}".format('#'), end="")
                print()
