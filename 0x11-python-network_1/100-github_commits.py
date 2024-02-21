#!/usr/bin/python3
'''Please list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
'''
import sys
import requests

if __name__ == '__main__':
    repo_name = sys.argv[1]
    uname = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo_name, uname)

    req = requests.get(url)
    commits = req.json()
    try:
        for item in range(10):
            print('{}: {}'.format(commits[item].get('sha'),
                    commits[item].get('commit').get('author').get('name')))
    except IndexError:
        pass
