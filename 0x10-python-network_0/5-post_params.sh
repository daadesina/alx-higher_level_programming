#!/bin/bash
#Takes in a URL
curl -s -X post -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
