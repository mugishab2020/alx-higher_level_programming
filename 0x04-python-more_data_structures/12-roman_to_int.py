#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    main_roman = {'I': 1, 'V': 5, 'L': 50, 'X': 10, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for a in reversed(roman_string):
        value = main_roman.get(a, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
