#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for part in keys:
        print("{}:".format(part), a_dictionary[part])
