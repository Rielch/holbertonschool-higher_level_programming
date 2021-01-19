#!/usr/bin/python3
"""Creates a Rectangle class that inherites from the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a rectangle, width and height must be integers greater than 0"""
    def __init__(self, width, height):
        """Initializates the rectangle"""
        if self.integer_validator("width", width) is None:
            self.__width = width
        if self.integer_validator("height", height) is None:
            self.__height = height

    def area(self):
        """Returns the area of the Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string to print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
