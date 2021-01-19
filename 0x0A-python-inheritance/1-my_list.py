#!/usr/bin/python3
"""Class that inherits from list"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Prints the list sorted in assending order"""
        new_MyList = self[:]
        new_MyList.sort()
        print(new_MyList)
