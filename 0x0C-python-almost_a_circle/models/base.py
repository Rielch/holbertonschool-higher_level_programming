#!/usr/bin/python3
"""Defines the Base class"""
import json


class Base:
    """A base class for the models package"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializates the Base instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Transformas a dictionary representation to a JSON string"""
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string to a file"""
        with open(cls.__name__ + ".json", mode="w", encoding="utf-8") as save:
            element_list = []
            if list_objs is not None:
                for element in list_objs:
                    element_list.append(cls.to_dictionary(element))
            save.write(cls.to_json_string(element_list))
