#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and :
    The text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    my_list = [".", "?", ":"]

    for i in range(len(text)):
        if text[i - 1] in my_list and text[i] is " ":
            pass
        elif text[i] in my_list:
            print("{}\n".format(text[i]))
        else:
            print("{}".format(text[i]), end="")
