#!/usr/bin/python3
"""
Script that takes URL and email, sends a POST request with the email,
displays body of response
"""
from sys import argv
import requests


if __name__ == "__main__":
    params = {"email": argv[2]}
    response = requests.post(argv[1], params)
    print(response.text)
