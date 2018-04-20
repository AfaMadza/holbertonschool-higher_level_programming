#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    roman_num = 0
    std_not = {'I': 1, 'V': 5, 'X': 10,
               'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub_not = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    for x in sub_not.keys():
        if x in roman_string:
            roman_num += sub_not[x]
            roman_string = roman_string.replace(x, "")
    for x in roman_string:
            roman_num += std_not[x]
    return roman_num
