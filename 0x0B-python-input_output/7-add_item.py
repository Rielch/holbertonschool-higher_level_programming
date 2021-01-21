#!/usr/bin/python3
"""Add all arguments to a python list and then saves it into a file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


my_list = argv[:]
my_list.pop(0)
try:
    my_list = load_from_json_file("add_item.json") + my_list
except:
    pass
save_to_json_file(my_list, "add_item.json")
