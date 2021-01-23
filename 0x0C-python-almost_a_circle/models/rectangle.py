#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from the class Base"""

    def __init__(self, width, height, x, y, id = None):
        
