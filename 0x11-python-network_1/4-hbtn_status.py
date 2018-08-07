#!/usr/bin/python3
"""
Fetches a url
"""
import requests


def fetch_url(url):
    """
    Requests a specified URL and displays data concerning it
    """
    req = requests.get(url)
    html = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))

if __name__ == "__main__":
    fetch_url('https://intranet.hbtn.io/status')
