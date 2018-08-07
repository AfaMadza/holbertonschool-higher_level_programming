#!/usr/bin/python3
"""
Displays value of 'X-Request-Id' header
"""
import urllib.request
import sys


def fetch_header(url):
    """
    Requests a specified URL and displays data concerning it
    """
    with urllib.request.urlopen(url) as resp:
        header = resp.info()
    print('{}'.format(header.get('X-Request-Id')))

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_header(url)
