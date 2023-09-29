#!/usr/bin/python3
""" finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers
    """
    if type(list_of_integers) is not list:
        return (None)

    list_len = len(list_of_integers)

    if list_len == 0:
        return (None)

    return (max(list_of_integers))
