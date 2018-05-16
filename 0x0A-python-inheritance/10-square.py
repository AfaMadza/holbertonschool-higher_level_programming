#!/usr/bin/python3
"""
This module contains a class called
Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    BaseGeometry - An empty class
    Args:
        BaseGeometry: superclass
    """
    def __init__(self, width, height):
        """
        __init__ - instantiation for Rectangle
        Args:
            width: Rectangle width
            height: Rectangle height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area implementation"""
        return self.__width * self.__height

    def __str__(self):
        """
        __str__ - string magic method
        """
        return "[{}] {}/{}".format("Rectangle",
                                   self.__width, self.__height)


class Square(Rectangle):
    """Square - Inherits from Rectangle"""
    def __init__(self, size):
        """
        __init__ - instantiation for Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
