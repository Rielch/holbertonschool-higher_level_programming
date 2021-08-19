#!/bin/bash
#Sends a request to a URL and prints only the status code
curl -s -w "%{http_code}" "$1" -o /dev/null
