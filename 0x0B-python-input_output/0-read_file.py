#!/usr/bin/python3
"""Reads a text file and prints it to standard output"""


def read_file(filename=""):
    """Reads a text file and prints it to standard output"""

    with open(filename, encoding="utf-8") as rd_file:
        for line in rd_file:
            print(line, end="")
