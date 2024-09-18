#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    for idx in range(len(roman_string)):
        if (roman_string[idx] == 'I' or roman_string[idx] == 'V'
                or roman_string[idx] == 'X' or roman_string[idx] == 'L'
                or roman_string[idx] == 'C' or roman_string[idx] == 'D'
                or roman_string[idx] == 'M'):
            continue
        else:
            return 0
    for idx in range(len(roman_string)):
        if roman_string[idx] == 'V' and roman_string[idx + 1] == 'V':
            return 0
        elif roman_string[idx] == 'L' and roman_string[idx + 1] == 'L':
            return 0
        elif roman_string[idx] == 'D' and roman_string[idx + 1] == 'D':
            return 0
        if idx + 3 < len(roman_string):
            if (roman_string[idx] == 'I' and roman_string[idx + 1] == 'I'
                    and roman_string[idx + 2] == 'I'
                    and roman_string[idx + 3] == 'I'):
                return 0
            if (roman_string[idx] == 'X' and roman_string[idx + 1] == 'X'
                    and roman_string[idx + 2] == 'X'
                    and roman_string[idx + 3] == 'X'):
                return 0
            if (roman_string[idx] == 'C' and roman_string[idx + 1] == 'C'
                    and roman_string[idx + 2] == 'C'
                    and roman_string[idx + 3] == 'C'):
                return 0
            if (roman_string[idx] == 'M' and roman_string[idx + 1] == 'M'
                    and roman_string[idx + 2] == 'M'
                    and roman_string[idx + 3] == 'M'):
                return 0
    rom_num = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    int_num = [1, 5, 10, 50, 100, 500, 1000]
    rom_num_values = dict(zip(rom_num, int_num))
    char_to_num = [rom_num_values.get(char) for char in roman_string]
    length = len(char_to_num)
    number = 0
    for i in range(length - 1):
        if char_to_num[i] < char_to_num[i + 1]:
            number += char_to_num[i + 1] - char_to_num[i]
            i = i + 1
        else:
            number += char_to_num[i]
    if char_to_num[length - 1] <= char_to_num[length - 2]:
        number += char_to_num[length - 1]
    return number
