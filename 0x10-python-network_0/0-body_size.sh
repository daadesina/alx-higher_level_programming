#!/bin/bash
#Takes a url
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
