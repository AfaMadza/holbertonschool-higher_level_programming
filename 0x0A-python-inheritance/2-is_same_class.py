#!/usr/bin/python3
"""
This module contains a function that returns True if the
object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    is_same_class - return true if class is same, false otherwise
    Args:
        obj: object to be evaluated
        a_class: class to be evaluated against
    Return: True or False for success or failure
    """
    if type(obj) == a_class:
        return True
    return False
