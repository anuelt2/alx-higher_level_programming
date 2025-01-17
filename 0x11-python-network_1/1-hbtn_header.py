#!/usr/bin/python3
"""
Script that takes a URL, sends request, displays value of specified header
"""
from sys import argv
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
