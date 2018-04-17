#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    count = 0
    while count < idx:
        count += 1
    my_list[count] = element
    return my_list
