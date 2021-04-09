#!/usr/bin/python3
""" Function that returns the peak of a list"""


def find_peak(list_of_integers):
        """Function that finds the peak in a list"""

        if len(list_of_integers) == 0 or list_of_integers is None:
            return None
        elif len(list_of_integers) == 1:
            return list_of_integers[0]
        elif len(list_of_integers) == 2:
            return max(list_of_integers)
        else:
            mid = int(len(list_of_integers) // 2)

            if list_of_integers[mid] >= list_of_integers[mid - 1] and\
               list_of_integers[mid] >= list_of_integers[mid + 1]:
                return list_of_integers[mid]
            if list_of_integers[mid + 1] > list_of_integers[mid]:
                return find_peak(list_of_integers[mid + 1:])
            if list_of_integers[mid - 1] > list_of_integers[mid]:
                return find_peak(list_of_integers[:mid - 1])
