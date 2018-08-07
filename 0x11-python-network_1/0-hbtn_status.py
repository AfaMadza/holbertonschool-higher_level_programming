#!/usr/bin/python3
"""
Fetches a url
"""
import urllib.request


def fetch_url(url):
    """
    Requests a specified URL and displays data concerning it
    """
    with urllib.request.urlopen(url) as resp:
        html = resp.read()
    print('Body response:')
    print('\t- type: {}'.format(type(html)))
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf8')))


if __name__ == "__main__":
    fetch_url('https://intranet.hbtn.io/status')
