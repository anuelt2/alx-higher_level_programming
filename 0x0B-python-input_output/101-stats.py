#!/usr/bin/python3
"""Module for a script that reads stdin
line by line and computes metrics
"""
from sys import stdin


file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


def print_metrics(file_size, status_codes):
    """Prints statistics since the commencement of inputs.

    Args:
        file_size: The accumulated file size from metrics.
        status_codes: A dictionary of key/value pairs of staus codes
        appearances.
    """

    print(f"File size: {file_size}")
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print(f"{key}: {status_codes[key]}")


try:
    input_count = 0
    for line in stdin:
        input_count += 1
        parts = line.split()
        try:
            file_size += int(parts[-1])
        except (ValueError, IndexError):
            continue
        try:
            status_code = parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except IndexError:
            continue
        if input_count % 10 == 0:
            print_metrics(file_size, status_codes)
except KeyboardInterrupt:
    print_metrics(file_size, status_codes)
    raise

print_metrics(file_size, status_codes)
