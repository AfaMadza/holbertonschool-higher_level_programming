#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary:
        new_dict = {key: value}
        a_dictionary.update(new_dict)
        return a_dictionary
    return None
