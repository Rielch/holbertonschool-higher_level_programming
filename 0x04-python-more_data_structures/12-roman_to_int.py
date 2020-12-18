#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str and roman_string:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman_string) - 1):
            if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                result -= roman[roman_string[i]]
            else:
                result += roman[roman_string[i]]
        result += roman[roman_string[len(roman_string) - 1]]
        return result
    else:
        return 0
