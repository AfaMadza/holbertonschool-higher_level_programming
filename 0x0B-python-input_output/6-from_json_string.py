#!/usr/bin/python3
"""
This module contains a function that returns the Python
data structure representation of a JSON string.
"""


def from_json_string(my_str):
    import json
    """
    to_json_string - returns Python data structure of JSON obj
    Args:
        my_str: object to be converted
    """
    return json.loads(my_str)
