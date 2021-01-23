#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from the class Base"""

    def __init__(self, width, height, x=0, y=0, id = None):
        """Initialization of Rectanglle class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("heigth must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the value of the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Changes the value of the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of the private attribute heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """Changes the value of the private attribute height"""
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the value of the private attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Changes the value of the private attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the value of the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Changes the value of the private attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance in stdout"""
        print((("#" * self.__width) + "\n") * self.__height, end="")

    def __str__(self):
        """Return the Rectangle instance characterristics"""
        return "[Rectangle] ({}) {}/{} {}/{}".format(self.id, self.__x,
                                                     self.__y, self.__width,
                                                     self.__height)
