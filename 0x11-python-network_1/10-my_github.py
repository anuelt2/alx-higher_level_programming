#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses GitHub API to display id
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (argv[1], argv[2])
    response = requests.get(url, auth=auth)
    json_data = response.json()
    print(f"{json_data.get('id')}")
