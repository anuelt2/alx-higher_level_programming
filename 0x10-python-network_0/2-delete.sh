#!/bin/bash
# Script sends DELETE request to URL passed as argument, displays response body
curl -sX DELETE "$1"
