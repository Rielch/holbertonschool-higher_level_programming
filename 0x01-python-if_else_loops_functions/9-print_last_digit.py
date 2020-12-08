#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if number < 0 and last != 0:
        last = (last - 10) * -1
    print("{:d}".format(last), end='')
    return last
