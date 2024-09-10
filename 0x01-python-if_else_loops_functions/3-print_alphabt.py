#!/usr/bin/python3
for asci in range(97, 123):
    if asci == 101 or asci == 113:
        continue
    else:
        print("{}".format(chr(asci)), end="")
