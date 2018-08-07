#!/usr/bin/python3
"""
Sends request to a URL and displays Body
"""
import sys
import requests



def error_request(url):
    """
    Takes in URL as parameter, sends a request and displays Body
    """
    req = requests.get(url)
    if req.status_code >= 400:
        print('Error code: {}'.format(req.status_code))
    else:
        print('{}'.format(req.text))


if __name__ == "__main__":
    url = sys.argv[1]
    error_request(url)
