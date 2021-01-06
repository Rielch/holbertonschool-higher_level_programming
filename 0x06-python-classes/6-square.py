#!/usr/bin/python3
"""class Square: creates a Square class"""


class Square:
    """Creates the class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Define size and position of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position[0]) is not int or type(position[1]) is not int or type(position) is not touple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0 or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square in stdout"""
        if self.__size == 0:
            print("", end="\n")
        else:
            for a in range(self.__position[1]):
                print("", end="\n")
            for i in range(self.__size):
                for b in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("", end="\n")

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @property
    def position(self):
        """Returns the position of the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """Modifies the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Modifies the position of the square"""
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
