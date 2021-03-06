#!/usr/bin/python3
"""
This module contains a function that prints a series of strings.
In this case, a first and last name are printed following the
string "My name is"
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name: prints "Say my name" followed by a name
    Args:
        first_name: first name
        last_name: last name"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
