#!/usr/bin/python3
"""
This module contains the Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
    Declaring the Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ - instantiation of Rectqangle Class
        Args:
            width: width
            height: height
            x: x
            y: y
            id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """
        Public method
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

    def update(self, *args, **kwargs):
        """
        Public method
        """
        attr = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) >= 1:
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """str magic method"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height)

    def display(self):
        """
        Public method
        """
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def area(self):
        """
        Public method
        """
        return self.__height * self.__width

    @property
    def width(self):
        """
        Getter for width.
        Setter below
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter for height.
        Setter below
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        Getter for x.
        Setter below
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        Getter for y.
        Setter below
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
