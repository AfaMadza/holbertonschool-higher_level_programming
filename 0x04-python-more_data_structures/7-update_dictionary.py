#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        new_dict = {key: value}
        a_dictionary.update(new_dict)
        return a_dictionary
    else:
        return None
