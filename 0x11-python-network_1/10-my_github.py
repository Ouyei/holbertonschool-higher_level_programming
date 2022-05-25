#!/usr/bin/python3
"""Takes my Github credentials (username and password)
and uses the Github API to display my Github id.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    req = requests.get('https://api.github.com/user',
                       auth=(username, password))
    print(req.json().get('id'))
