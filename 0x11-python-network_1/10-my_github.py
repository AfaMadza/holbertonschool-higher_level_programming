#!/usr/bin/python3
"""
Uses github credentials to display id
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def request_git_id(url, unm, pw):
    """
    Takes your Github credentials (username and password) and uses
    the Github API to display your id
    """
    req = requests.get(url, auth=HTTPBasicAuth(unm, pw))
    json = req.json()
    print('{}'.format(json.get('id')))


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    unm = sys.argv[1]
    pw = sys.argv[2]
    request_git_id(url, unm, pw)
