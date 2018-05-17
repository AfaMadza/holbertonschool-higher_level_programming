#!/usr/bin/python3
"""
This module contains a function that returns a list
of lists of integers representing the Pascal's triangle
of n
"""


def pascal_triangle(n):
    """
    pascal_triangle - see module description
    Args:
        n: number of rows
    """
    seed_list = [1]
    list_cont = []
    flag = 1
    for i in range(n - 1):
        if flag == 1:
            print(seed_list)
            flag = 0
        res_list = []
        res_list.append(seed_list[0])
        for i in range(len(seed_list) - 1):
            res_list.append(seed_list[i] + seed_list[i + 1])
        res_list.append(seed_list[-1])
        seed_list = list(res_list)
        list_cont.append(res_list)
    return list_cont
