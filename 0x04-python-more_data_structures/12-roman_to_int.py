#!/usr/bin/python3
def roman_to_int(roman_string):
    from functools import reduce
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list([])
    for i in roman_string:
        for j in roman_num:
            if i == j:
                roman_list.append(roman_num[j])
    func = lambda x, y: x+y if (x >= y) else y-x
    return(reduce(func, roman_list))
