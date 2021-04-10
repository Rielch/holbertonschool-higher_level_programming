#!/usr/bin/python3
"""Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        dic = {'q': ''}
    else:
        dic = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=dic)

    try:
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            json_id = json.get('id')
            json_name = json.get('name')
            print("[{}] {}".format(json_id, json_name))
    except ValueError:
        print("Not a valid JSON")
