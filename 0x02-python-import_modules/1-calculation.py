#!/usr/bin/python3
import calculator_1
if __name__ == "__main__":
    a = 10
    b = 5
    calculator_1.add(a, b)
    calculator_1.sub(a, b)
    calculator_1.mul(a, b)
    calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
