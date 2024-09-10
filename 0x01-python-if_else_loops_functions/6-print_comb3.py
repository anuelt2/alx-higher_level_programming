#!/usr/bin/python3
for first_digit in range(0, 10):
    for second_digit in range(0, 10):
        if first_digit == second_digit or first_digit > second_digit:
            continue
        print("{}".format(first_digit), end="")
        if second_digit == 9 and first_digit == second_digit - 1:
            print("{}".format(second_digit))
        else:
            print("{}".format(second_digit), end=", ")
