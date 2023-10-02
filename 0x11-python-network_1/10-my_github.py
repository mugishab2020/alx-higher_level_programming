#!/usr/bin/python3
"""using the GitHub API to siplay my id"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    authorization = HTTPBasicAuth(username, password)
    my_url = "https://api.github.com/user"
    response = requests.get(my_url, auth=authorization)
    print(response.json().get("id"))
