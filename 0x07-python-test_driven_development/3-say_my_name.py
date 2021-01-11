#!/usr/bin/python3
"""Function that prints your name"""


def say_my_name(first_name, last_name=""):
    """This function says your name
    it works with your first and last name or just your first name
    the first and last name must be strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if last_name is "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
