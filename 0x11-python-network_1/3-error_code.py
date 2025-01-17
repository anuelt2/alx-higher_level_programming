#!/usr/bin/python3
"""Script takes URL, sends request and displays body of response"""
from sys import argv
import urllib.request
import urllib.error


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(f"{body.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
