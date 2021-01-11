#!/usr/bin/python3
"""Prints a square using #"""


def print_square(size):
    """Prints a square using #
    the size must be an integer
    and larger than 0
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is float:
        size = int(size)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
