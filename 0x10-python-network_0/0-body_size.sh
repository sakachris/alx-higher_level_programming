#!/bin/bash
# Bash script that takes in a URL and diplays size
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
