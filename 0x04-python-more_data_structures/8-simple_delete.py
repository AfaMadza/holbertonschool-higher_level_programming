#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    b_dictionary = dict(a_dictionary)
    for i in list(a_dictionary):
        if key in a_dictionary:
            del(a_dictionary[key])
    return a_dictionary
