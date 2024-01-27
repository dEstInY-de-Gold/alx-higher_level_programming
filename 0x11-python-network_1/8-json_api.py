#!/usr/bin/python3
'''Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) == 1:
        letter = ''
    else:
        letter = sys.argv[1]
    load = {'q': letter}
    req = requests.post('http://0.0.0.0:5000/search_user', data=load)

    try:
        resp = req.json()
        if resp == {}:
            print('No result')
        else:
            print('[{}] {}'.format(resp.get('id'), resp.get('name')))
    except ValueError:
        print('Not a valid JSON')
