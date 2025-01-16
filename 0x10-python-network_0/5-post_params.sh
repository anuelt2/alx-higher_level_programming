#!/bin/bash
# Script takes URL, sends POST request, displays body of response
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
