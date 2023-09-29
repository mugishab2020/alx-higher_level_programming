#!/usr/bin/python3
""" fetching the url statis using urllib"""
from urllib import request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as answer:
        responce = answer.read()
        print("Body response:")
        print("\t- type: {}".format(type(responce)))
        print("\t- content: {}".format(responce))
        print("\t- utf8 content: {}".format(responce.decode("utf-8")))
