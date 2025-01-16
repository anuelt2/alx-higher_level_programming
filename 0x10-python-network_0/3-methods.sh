#!/bin/bash
# Script takes URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep -i Allow | awk '{$1=""; sub(/^ /, ""); print $0}'
