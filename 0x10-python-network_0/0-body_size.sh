#!/bin/bash
# Using curl to get the response body and measure its size in bytes
curl -s "$url" | wc -c
