#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
'''
from urllib.request import Request, urlopen
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    except Exception as error:
        print(error)
