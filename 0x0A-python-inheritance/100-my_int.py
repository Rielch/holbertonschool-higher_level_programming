#!/usr/bin/python3
"""Creates a class MyInt that inherites from int that inverts == and !="""


class MyInt(int):
    """Class that inherites from int but inverts == and !="""
    def __init__(self, value):
        """Initializates a MyInt class"""
        self.value = value
    def __new__(cls, value):
        """Creates a new int object"""
        return int.__new__(cls, value)
    def __eq__(self, other):
        """defines equality"""
        return self.value != other
    def __ne__(self, other):
        """defines inequality"""
        return self.value == other
