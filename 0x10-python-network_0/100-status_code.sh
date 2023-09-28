#!/bin/bash
# Bash script that display status code
curl -so /dev/null -w "%{http_code}" "$1"
