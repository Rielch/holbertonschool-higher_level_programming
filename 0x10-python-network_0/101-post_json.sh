#!/bin/bash
#Sends a POST request with the contents of a file
curl -s -H 'Content-Type: application/json' -X POST "$1" -d @"$2"
