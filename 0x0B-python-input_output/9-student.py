#!/usr/bin/python3
"""Creates a class Student"""


class Student:
    """Creates a class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializates the instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student instance"""
        return self.__dict__
