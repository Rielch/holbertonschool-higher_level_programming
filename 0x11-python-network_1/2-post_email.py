#!/usr/bin/python3
"""Script that takes in a URL and an email and sends a POST"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], data) as post:
        http = post.read()
        print(http.decode('utf-8'))
