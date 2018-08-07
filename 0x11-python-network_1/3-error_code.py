#!/usr/bin/python3
"""
Sends request to a URL and displays Body
"""
import sys
import urllib.request


def error_request(url):
    """
    Takes in URL as parameter, sends a request and displays Body
    """
    try:
        request = urllib.request.Request(url)
        with urllib.request.urlopen(request) as resp:
            html = resp.read()
        print('{}'.format(html.decode('utf8')))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))


if __name__ == "__main__":
    url = sys.argv[1]
    error_request(url)
