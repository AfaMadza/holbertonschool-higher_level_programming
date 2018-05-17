#!/usr/bin/python3
"""
This module contains a function that returns the JSON
representation of an object
"""


def to_json_string(my_obj):
    import json
    """
    to_json_string - returns JSON representation of an object
    Args:
        my_obj: object to be converted
    """
    return json.dumps(my_obj)
