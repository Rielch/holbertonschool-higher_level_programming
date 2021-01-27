#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from the class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectanglle class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
            raise TypeError("height must be an integer")
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
        print(("\n" * self.__y) + (((" " * self.__x) + ("#" * self.__width) +
                                    "\n")) * self.__height, end="")

    def __str__(self):
        """Return the Rectangle instance characterristics"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                     self.__y, self.__width,
                                                     self.__height)

    def update(self, *args, **kwargs):
        """Updates the values of the Rectangle instance"""
        if len(args) is 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def to_dictionary(self):
        """Returns a dictionary representation of the Rectangle instance"""
        return {'x': self.x, 'y': self.y, 'height': self.height,
                'width': self.width, 'id': self.id}
