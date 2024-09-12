#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_of_args = len(argv) - 1
    if num_of_args == 1:
        print("{} argument:".format(num_of_args))
    elif num_of_args == 0:
        print("{} arguments.".format(num_of_args))
    else:
        print("{} arguments:".format(num_of_args))
    i = 1
    while i <= num_of_args:
        print("{}: {}".format(i, argv[i]))
        i += 1
