#!/usr/bin/python3
"""Script that fetches https://intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as holb:
        http = holb.read()
        body = http.decode()

        print("Body response:")
        print("\t- type: {}".format(type(http)))
        print("\t- content: {}".format(http))
        print("\t- utf8 content: {}".format(body))
