#!/usr/bin/bash
#a bash script for geting the size of a body from a url

curl -s "$1" | wc -c
