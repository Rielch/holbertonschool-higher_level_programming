#!/usr/bin/python3
"""Reads a text file and prints it to standard output"""
import os


def read_file(filename=""):
    """Reads a text file and prints it to standard output"""

    with open(filename, encoding="utf-8") as rd_file:
        print(rd_file.read())
