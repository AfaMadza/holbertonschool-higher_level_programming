#!/usr/bin/python3
"""
This module contains a function that creates an object
from a JSON file
"""
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


def main():
    """
    main - see module description
    Args:
        None
    """
    try:
        my_list = load_from_json_file('./add_item.json')
    except:
        my_list = []
    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, './add_item.json')

if __name__ == '__main__':
    main()
