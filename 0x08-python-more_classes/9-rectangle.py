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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        __init__: Initializes Rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width Getter: returns width
        Setter below.
        """
        return self.__width

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
        Height Getter: returns height
        Setter below
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Public instance method
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Public instance method
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """
        __str__ magic method
        """
        new_string = ""
        if self.__width == 0 or self.__height == 0:
            return new_string
        for i in range(self.__height):
            for j in range(self.__width):
                new_string += str(self.print_symbol)
            if i < self.__height - 1:
                new_string += '\n'
        return new_string

    def __repr__(self):
        """
        __repr__ magic method
        """
        return "Rectangle(" + str(self.__width) + ", " +\
            str(self.__height) + ")"

    def __del__(self):
        """
        __del__ magic method
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        static method used to determine larger triangle
        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        square: returns an instance of a rectangle
        that is a square
        Args:
            cls: instance of square
            size: size of rectangle
        """
        return cls(size, size)
