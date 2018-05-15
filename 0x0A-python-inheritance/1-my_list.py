#!/usr/bin/python3
"""
This module contains a class called
MyList that inherits from list
"""
class MyList(list):
    """
    myList - This class inherits from list
    Args:
        list: the list superclass
    """
    def print_sorted(self):
        """
        print_sorted - public instance method that prints
        a sorted list.
        Args:
            None
        Return: None
        """
        print(sorted(self))
