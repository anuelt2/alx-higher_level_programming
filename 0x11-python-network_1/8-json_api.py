#!/usr/bin/python3
"""
Script that takes a letter, sends a POST request to
http://0.0.0.0:5000/search_user with letter as parameter
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    params = {"q": q}
    response = requests.post(url, params)
    if "application/json" in response.headers.get("Content-Type"):
        json_data = response.json()
        if json_data:
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
