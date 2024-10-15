#!/usr/bin/python3
"""Module for a script that reads stdin
line by line and computes metrics
"""
from sys import stdin


file_size = two_h = three_h = five_h = 0
four_h = four_one = four_three = four_four = four_five = 0

while True:
    keys = ['200', '301', '400', '401', '403', '404', '405', '500']
    values = [two_h, three_h, four_h, four_one, four_three, four_four,
              four_five, five_h]
    status_code_dict = dict(zip(keys, values))

    try:
        for i in range(10):
            line = input()
            parts = line.split()
            file_size += int(parts[-1])
            status_code = int(parts[-2])
            if status_code == 200:
                two_h += 1
            if status_code == 301:
                three_h += 1
            if status_code == 400:
                four_h += 1
            if status_code == 401:
                four_one += 1
            if status_code == 403:
                four_three += 1
            if status_code == 404:
                four_four += 1
            if status_code == 405:
                four_five += 1
            if status_code == 500:
                five_h += 1
    except KeyboardInterrupt:
        print(f"File size: {file_size}")
        for key, value in status_code_dict.items():
            if value > 0:
                print(f"{key}: {value}")
    else:
        print(f"File size: {file_size}")
        for key, value in status_code_dict.items():
            if value > 0:
                print(f"{key}: {value}")
