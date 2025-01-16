#!/bin/bash
# Script sends JSON POST request to URL, displays body of response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
