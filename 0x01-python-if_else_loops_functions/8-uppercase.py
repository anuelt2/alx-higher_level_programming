#!/usr/bin/python3
def uppercase(str):
    index = 0
    while index < len(str):
        char_ascii = ord(str[index])
        if char_ascii >= 97 and char_ascii <= 122:
            char_ascii = char_ascii - 32
            str = str[:index] + chr(char_ascii) + str[index + 1:]
        else:
            pass
        index += 1
    print("{}".format(str))
