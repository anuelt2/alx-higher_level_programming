#!/usr/bin/python3
"""Script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body reponse:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
