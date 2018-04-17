#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero_tup = (0,)
    if len(tuple_a) < 1:
        tuple_a = zero_tup + zero_tup
    if len(tuple_a) == 1:
        tuple_a = tuple_a + zero_tup
    if len(tuple_b) < 1:
        tuple_b = zero_tup + zero_tup
    if len(tuple_b) == 1:
        tuple_b = tuple_b + zero_tup
    sum_tup = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
    return sum_tup
