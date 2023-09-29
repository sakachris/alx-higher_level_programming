#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -sX PUT -d "user_id=1" 0.0.0.0:5000/catch_me
