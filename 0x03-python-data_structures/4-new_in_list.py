#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    count = 0
    while count < idx:
        count += 1
    list_copy = my_list[:]
    list_copy[count] = element
    return list_copy
