#!/bin/bash
#Makes a request
curl -sX PUT -L -d "user_id=98" --header "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
