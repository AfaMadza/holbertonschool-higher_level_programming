#!/usr/bin/python3
"""Module docstring"""


def add_integer(a, b=98):
    """Function docstring
    add_integer: adds 2 integers
    Args:
        a (int, float): first number
        b (int, float): second number
    Return (int): a + b"""
    if a is None:
        raise TypeError('a must be an integer')
    if b is None:
        raise TypeError('b must be an integer')
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
