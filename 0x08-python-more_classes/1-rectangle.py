#!/usr/bin/python3
"""Creates a class Rectangle"""


class Rectangle:
    """Creates and defines a rectangle
    The rectangle has width and height
    """

    def __init__(self, width=0, height=0):
        """Initializates the rectangle
        width and height must be integers larger or equal than 0
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Returns the width value"""

        return self.__width

    @width.setter
    def width(self, value):
        """Modifies the width value
        The value has to be an integer and larger or equal than 0
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Modifies the height value
        The value has to be an int and larger or equal than 0
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
