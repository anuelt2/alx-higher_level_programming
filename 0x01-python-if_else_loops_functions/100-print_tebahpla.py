#!/usr/bin/python3
for alpha_lower, alpha_upper in zip(range(122, 96, -2), range(89, 64, -2)):
    print("{}{}".format(chr(alpha_lower), chr(alpha_upper)), end="")
