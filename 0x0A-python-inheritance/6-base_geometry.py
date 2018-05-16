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
