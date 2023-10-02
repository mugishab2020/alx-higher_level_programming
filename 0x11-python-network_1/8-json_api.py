#!/usr/bin/python3
"""Using sys and requests module to send a post request"""

from sysy import argv
import requests


if __name__ == "__main__":
    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        parsed_response = response.json()
        if parsed_response == {}:
            print("No result")
        else:
            print("[{}] {}".format(parsed_response.get(
                "id"), parsed_response.get("name")))
    except ValueError:
        print("Not a valid JSON")
