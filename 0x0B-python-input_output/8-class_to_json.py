#!/usr/bin/python3
"""Returns the dictionary descriptionwith simple data
structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary descriptionwith simple data
    structure for JSON serialization of an object
    """
    return obj.__dict__
