#!/usr/bin/python3
"""Script that takes in a URL, sends a
request to the URL and displays X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        print(url.getheader('X-Request-Id'))
