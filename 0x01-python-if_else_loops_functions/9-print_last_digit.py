#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        pos_num = -1 * number
    else:
        pos_num = number
    n = pos_num % 10
    print("{:d}".format(n), end="")
    return (n)
