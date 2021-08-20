#!/usr/bin/python3
"""Returns the last 10 commits in a repository"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{}/{}/commits?per_page=10'
                     .format(sys.argv[2], sys.argv[1]))
    http = r.json()
    for element in http:
        print('{}: {}'.format(element['sha'],
                              element['commit']['author']['name']))
