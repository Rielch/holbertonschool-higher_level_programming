#!/usr/bin/python3
"""Writes a string into a file"""


def write_file(filename="", text=""):
    """Writes a string into a file"""
    with open(filename, mode="w", encoding="utf-8") as wr_file:
        wr_file.write(text)
    return len(text)
