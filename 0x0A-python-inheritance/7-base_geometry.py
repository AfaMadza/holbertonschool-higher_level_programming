#!/usr/bin/python3
"""
This module contains a class called
MyList that inherits from list
"""


class BaseGeometry:
    """
    BaseGeometry - An empty class
    Args:
        None
    """
    pass

    def area(self):
        """
        area - public instance method that raises an exception
        with a specified message.
        Args:
            None
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        integer_validator -  public instance method that validates value
        Args:
            name: string used as name
            value: value to be validated
        Return: None
        """
        if not isinstance(name, str):
            raise TypeError(name +' must be a string')
        if type(value) != int:
            raise TypeError(name +' must be an integer')
        if value <= 0:
            raise ValueError(name +' must be greater than 0')
