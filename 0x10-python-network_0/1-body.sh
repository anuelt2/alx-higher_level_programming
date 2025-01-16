#!/bin/bash
# Script takes in URL, sends GET request, displays body of response
curl -Lsw "%{http_code}" "$1" | grep -q 200 && curl -sL "$1"
