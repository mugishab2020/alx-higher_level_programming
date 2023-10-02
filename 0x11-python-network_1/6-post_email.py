#!/usr/bin/python3
"""script that takes in a URL and an email address, sends a POST"""
import requests
from sys import argv

if __name__ == "__main__":
    my_url = argv[1]
    email = argv[2]
    show = {"email": email}
    prints = requests.post(my_url, data=show)
    print(prints.text)
