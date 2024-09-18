#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    int_num = [1, 5, 10, 50, 100, 500, 1000]
    rom_num_values = dict(zip(rom_num, int_num))
    char_to_num = [rom_num_values.get(char) for char in roman_string]
    length = len(char_to_num)
    number = 0
    for i in range(length - 1):
        if char_to_num[i] < char_to_num[i + 1]:
            number -= char_to_num[i]
        else:
            number += char_to_num[i]
    number += char_to_num[length - 1]
    return number
