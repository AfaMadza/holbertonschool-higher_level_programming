#!/usr/bin/python3
"""
This module contains a function that returns the list
of available attributes and methods of an object.
"""


def lookup(obj):
    """
    lookup - returns the list of available attributes and methods
    of an object.
    Args:
        obj: object to be evaluated
    Return: list object
    """
    return dir(obj)
