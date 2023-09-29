#!/usr/bin/python3
"""using urllib to send a request"""

from sys import argv
from urllib import request
from urllib import error
if __name__ == "__main__":
    my_url = argv[1]
    try:
        with request.urlopen(my_url) as answer:
            print(answer.read().decode('utf-8'))

    except error.HTTPError:
        print("Error code: {}".format(error.HTTPError.code))
