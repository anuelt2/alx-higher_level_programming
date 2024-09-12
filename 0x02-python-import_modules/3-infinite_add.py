#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num_of_args = len(argv) - 1
    i = 1
    sum_of_args = 0
    while i <= num_of_args:
        sum_of_args += int(argv[i])
        i += 1
    print(sum_of_args)
