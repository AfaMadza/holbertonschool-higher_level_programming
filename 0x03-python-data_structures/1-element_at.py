#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return None
    count = 0
    while count < idx:
        count = count + 1
    return my_list[count]