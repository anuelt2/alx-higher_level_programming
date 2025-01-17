#!/usr/bin/python3
"""
Script that takes 2 arguments and lists 10 commits
from the latest, of a GitHub repository
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        for commit in json_data[:10]:
            sha = commit.get("sha")
            author_name = (commit.get("commit", {})
                           .get("author", {}).get("name", {}))
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")
