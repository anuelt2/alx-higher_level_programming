#!/usr/bin/python3
"""Module for find_peak function"""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers

    Args:
        list_of_integers: List of unsorted integers
    """
    if not list_of_integers:
        return None
    high = len(list_of_integers) - 1
    low = 0
    while low < high:
        mid = int((low + high) / 2)
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
