#!/bin/bash
# Script takes URL and displays all HTTP methods the server will accept
curl -isX OPTIONS "$1" | grep -i Allow | awk '{$1=""; sub(/^ /, ""); print $0}'
