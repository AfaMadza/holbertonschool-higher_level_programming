#!/usr/bin/python3
"""
Send POST request with a given parameter
"""
import sys
import requests


def post_request(url, email):
    """
    Sends post request to URL with email as parameter
    """
    post_fields = {'email': email}
    req = requests.post(url, data=post_fields)
    print('{}'.format(req.text))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_request(url, email)
