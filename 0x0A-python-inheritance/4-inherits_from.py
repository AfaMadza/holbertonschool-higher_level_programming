#!/usr/bin/python3
"""
This module contains a function that returns True if the
object is an instance (directly or indirectly)
of the specified class.
"""
def inherits_from(obj, a_class):
    """
    is_same_class - return true if class is subclass, false otherwise
    Args:
        obj: object to be evaluated
        a_class: class to be evaluated against
    Return: True or False for success or failure
    """
    if not type(obj) == a_class and issubclass(type(obj), a_class):
        return True
    return False
