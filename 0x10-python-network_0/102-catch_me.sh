#!/bin/bash
# Script makes request to URL with message You got me! in body of response
curl -LX PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_2
