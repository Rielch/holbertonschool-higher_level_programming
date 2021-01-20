#!/usr/bin/python3
"""Function to add an attribute to an object"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible"""

    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
