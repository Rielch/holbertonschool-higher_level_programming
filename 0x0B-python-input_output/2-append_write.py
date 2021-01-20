#!/usr/bin/python3
"""Writes a string into a file"""


def append_write(filename="", text=""):
    """Writes a string into a file"""
    with open(filename, mode="a", encoding="utf-8") as wr_file:
        wr_file.write(text)
    return len(text)
