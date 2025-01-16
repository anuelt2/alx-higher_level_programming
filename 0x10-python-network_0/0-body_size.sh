#!/bin/bash
# Script that takes and sends request to URL, displays size of body of response
curl -sI "$1" | grep -i Content-Length
