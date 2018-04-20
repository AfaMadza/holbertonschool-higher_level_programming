#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = {key: value}
    b_dictionary = dict(a_dictionary)
    for i in list(a_dictionary):
        if key in a_dictionary:
            del(a_dictionary[key])
            a_dictionary.update(new_dict)
        a_dictionary.update(new_dict)
    return a_dictionary
