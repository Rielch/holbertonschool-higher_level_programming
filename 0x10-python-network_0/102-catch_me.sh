#!/bin/bash
#Makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with You got me!
curl -d user_id=98 -H 'HolbertonSchool' -L -X PUT 0.0.0.0:5000/catch_me
