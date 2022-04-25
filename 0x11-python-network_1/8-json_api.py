#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to `http://0.0.0.0:5000/search_user` with the
letter as a parameter and with `requests` module.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        a_dict = {'q': ''}
    elif len(sys.argv) > 1:
        a_dict = {'q': sys.argv[1]}

    try:
        req = requests.post('http://0.0.0.0:5000/search_user', a_dict)
        if req.json():
            print('[{}] {}'.format(req.json().get('id'),
                                   req.json().get('name')))
        else:
            print('No result')

    except ValueError:
        print("Not a valid JSON")
