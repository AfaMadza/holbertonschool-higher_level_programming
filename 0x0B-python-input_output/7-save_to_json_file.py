#!/usr/bin/python3
"""
This module contains a function that returns the Python
data structure representation of a JSON string.
"""


def save_to_json_file(my_obj, filename):
    import json
    """
    save_to_json_file - saves JSON obj to file
    Args:
        my_obj: object to be saved
        filename: file's name
    """
    with open(filename, mode='w', encoding ='utf-8') as f:
        f.write(json.dumps(my_obj))
