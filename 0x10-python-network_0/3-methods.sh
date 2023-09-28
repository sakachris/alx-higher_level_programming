#!/bin/bash
# Bash script that takes in a URL and diplays size
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
