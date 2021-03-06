#!/usr/bin/python3
"""class Square: creates a Square class"""


class Square:
    """Creates the class Square"""
    def __init__(self, size=0):
        """Define size of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square in stdout"""
        if self.__size == 0:
            print("", end="\n")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("", end="\n")

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Modifies the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
