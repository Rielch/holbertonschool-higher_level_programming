#!/usr/bin/python3
"""Defines the Base class"""


class Base:
    """A base class for the models package"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
