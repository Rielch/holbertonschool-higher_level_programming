#!/usr/bin/python3
"""Creates a Square class that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square class"""
    def __init__(self, size):
        """initializates the object Square"""
        if self.integer_validator("size", size) is None:
            self.__size = size
            Rectangle.__init__(self, size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2
