#!/usr/bin/python3
"""
This module contains the definition
of a class called Rectangle
"""


class Rectangle:
    """Class Rectangle
    Simply defines the Rectangle class.
    Args: None
    """
    def __init__(self, width=0, height=0):
        """
        __init__: Initializes Rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Width Getter: returns width
        Setter below
        """
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Height Getter: gets height
        Setter below
        """
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        new_string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new_string += '#'
            if i < self.__height - 1:
                new_string += '\n'
        return new_string
