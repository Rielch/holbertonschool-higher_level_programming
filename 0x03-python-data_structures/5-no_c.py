#!/usr/bin/python3
def no_c(my_string):
    mystr = my_string.translate({ord('c'): None})
    mystr = mystr.translate({ord('C'): None})
    return mystr
