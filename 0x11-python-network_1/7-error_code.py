#!/usr/bin/python3
"""using requests module to fetch and show error code"""

import sys
import requests


if __name__ == "__main__":
    my_url = sys.argv[1]
    response = requests.get(my_url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
