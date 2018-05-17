#!/usr/bin/python3
"""
This module contains a function that returns the dictionary
description for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    class_to_json - see module description
    Args:
        obj: instance of a Class
    """
    return (obj.__dict__)
