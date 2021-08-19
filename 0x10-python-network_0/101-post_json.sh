#!/bin/bash
#Sends a POST request with the contents of a file
curl -H 'Content-Type: application/json' -d @"$2" "$1"
