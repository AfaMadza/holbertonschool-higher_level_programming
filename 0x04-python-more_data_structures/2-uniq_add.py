#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_sum = 0;
    new_list = list(set(my_list))
    for i in range(len(new_list)):
            my_sum += new_list[i]
    return my_sum
