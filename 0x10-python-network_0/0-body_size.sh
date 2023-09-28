#!/usr/bin/bash
# Bash script that takes in a URL and diplays size
curl -s -o /dev/null -w "%{size_download}" $1
