#!/bin/bash
# Script takes URL, sends GET request with header variable and value
curl -sH "X-School-User-Id: 98" "$1"
