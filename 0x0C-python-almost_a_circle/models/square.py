#!/usr/bin/python3
"""
This module contains the Square Class
"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """
    Declaring the Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ - instantiation of Square Class
        Args:
            size: size
            x: x
            y: y
            id: id
        """
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """
        Public method
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """
        Public method
        """
        attr = ['id', 'size', 'x', 'y']
        if args and len(args) >= 1:
            for i in range(len(args)):
                print(args[i])
                setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """str magic method"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """
        Getter for size.
        Setter below
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value
