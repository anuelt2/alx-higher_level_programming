#!/bin/bash
# Script that send request to URL, displays only status code of response
curl -o /dev/null -sw "%{http_code}" "$1"
