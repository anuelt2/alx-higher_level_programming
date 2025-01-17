#!/usr/bin/python3
"""
Script that takes URL and email, sends a POST request with the email,
displays body of response
"""
from sys import argv
import urllib.request
import urllib.parse


if __name__ == "__main__":
    params = {"email": argv[2]}
    params = urllib.parse.urlencode(params)
    params = params.encode('utf-8')

    with urllib.request.urlopen(argv[1], params) as response:
        body = response.read()
        body = body.decode('utf-8')
        print(body)
