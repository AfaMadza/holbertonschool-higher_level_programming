#!/usr/bin/python3
"""
Sends request to SWAPI
"""
import sys
import requests


def request_swapi(url, s_string):
    """
    Takes in a string and sends a search request to the Star Wars API
    """
    payload = {'search': s_string}
    req = requests.get(url, params=payload).json()
    num = req.get('count')
    print('Number of results: {}'.format(num))
    if num > 0:
        search_res = req.get('results')
        for indiv in search_res:
            print(indiv.get('name'))

if __name__ == "__main__":
    s_string = sys.argv[1]
    url = 'https://swapi.co/api/people/'
    request_swapi(url, s_string)
