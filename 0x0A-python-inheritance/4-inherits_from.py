#!/usr/bin/python3
"""Checks if the object is an instance of a class that inherited
(directly or indirectly) of the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instanceof a class that inherited
    (directly or indirectly) from a_class, otherwise return False
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
