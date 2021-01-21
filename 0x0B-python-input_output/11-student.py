#!/usr/bin/python3
"""Creates a class Student"""


class Student:
    """Creates a class Student"""
    def __init__(self, first_name, last_name, age):
        """Initializates the instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance"""
        i = 0
        new_dict = {}
        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    i += 1
            if i == 0:
                for element in attrs:
                    if element in self.__dict__:
                        new_dict[element] = self.__dict__[element]
                return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the instance"""
        for key in json:
            setattr(self, key, json[key])
