#!/usr/bin/python3
"""
Send POST request with a given parameter
"""
import sys
import requests


def post_request(url, q):
    """
    Sends post request to URL with letter as parameter
    """
    post_fields = {'q': q}
    req = requests.post(url, data=post_fields)
    if req.headers.get('content-type') == 'application/json':
        json = req.json()
        if len(json) > 0:
            print('[{}] {}'.format(json.get('id'), json.get('name')))

        else:
            print('No result')
    else:
        print('Not a valid JSON')


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        q = sys.argv[1]
    except:
        q = ""
    post_request(url, q)
