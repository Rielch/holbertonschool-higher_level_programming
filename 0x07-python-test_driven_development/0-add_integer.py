#!/usr/bin/python3
"""Adds two integers or floats"""


def add_integer(a, b=98):
    """Adds two integers or floats
    If the function only recieves one number the second will be 98
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
