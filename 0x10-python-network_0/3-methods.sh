#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -s "$1" --head | grep 'Allow:' | cut -d":" -f2 | awk '{$1=$1;print}'
