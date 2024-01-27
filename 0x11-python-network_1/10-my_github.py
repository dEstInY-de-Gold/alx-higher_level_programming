#!/usr/bin/python3
'''Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
'''
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    uname = sys.argv[1]
    upass = sys.argv[2]

    tkn = HTTPBasicAuth(uname, upass)
    req = requests.get('https://api.github.com/user', auth=tkn)
    print(req.json().get('id'))
