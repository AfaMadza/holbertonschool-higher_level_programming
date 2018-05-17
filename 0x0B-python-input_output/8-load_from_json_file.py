#!/usr/bin/python3
"""
This module contains a function that creates an object
from a JSON file
"""
import json
import os


def load_from_json_file(filename):
    """
    load_from_json_file - creates object from JSON file
    Args:
        filename: file's name
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        my_obj = json.loads(f.read())
        return my_obj
