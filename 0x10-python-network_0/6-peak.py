#!/usr/bin/python3
"""
This module contains a function to find a peak in an array
"""


def find_peak(list_of_integers):
    """
    Finds a peak in an array and returns the number or none
    """
    i = 0
    loi = list_of_integers
    if not loi:
        return None
    if len(loi) == 1:
        return loi[0]
    mid = int(len(loi) / 2)
    if len(loi) >= 3:
        prv = int((len(loi) / 2) - 1)
        nxt = int((len(loi) / 2) + 1)
    if loi[prv] < loi[mid] and loi[mid] > loi[nxt]:
        return loi[mid]
    else:
        while (loi[i] < loi[i + 1]):
            i += 1
    return loi[i]


if __name__ == "__main__":
    find_peak(list_of_integers)
