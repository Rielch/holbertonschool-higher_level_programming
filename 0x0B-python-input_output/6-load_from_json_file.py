#!/usr/bin/python3
"""Function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as my_json:
        return json.load(my_json)
