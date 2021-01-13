#!/usr/bin/python3
"""Class with no class or object attributes"""


class LockedClass:
    """Locked class without class or object attributes"""

    __slots__ = ['first_name']

    def __init__(self):
        """initializates the class empty"""
        pass
