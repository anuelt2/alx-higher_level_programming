#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print("{:d}".format(" ".join("{}".format(num) for num in row)))
