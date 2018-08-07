#!/usr/bin/python3
"""
Send POST request with a given parameter
"""
from urllib.request import Request
import urllib.request
from urllib.parse import urlencode
import sys


def post_request(url, email):
    """
    Sends post request to URL with email as parameter
    """
    post_fields = {'email': email}
    request = Request(url, urlencode(post_fields).encode('ascii'))
    with urllib.request.urlopen(request) as resp:
        html = resp.read()
    print('{}'.format(html.decode('utf8')))

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_request(url, email)
