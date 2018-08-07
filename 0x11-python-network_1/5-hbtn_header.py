#!/usr/bin/python3
"""
Displays value of 'X-Request-Id' header
"""
import requests
import sys


def fetch_header(url):
    """
    Requests a specified URL and displays data concerning it
    """
    req = requests.get(url)
    print('{}'.format(req.headers.get('X-Request-Id')))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header(url)
