#!/usr/bin/python3
"""Defines a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializates an instance of the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the Square instance characteristcs"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Change the size value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the values of the size instance"""
        if len(args) is 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """Returns the dictionary representation for the instance of Square"""
        return {"x": self.x, "y": self.y, "size": self.size, "id": self.id}
