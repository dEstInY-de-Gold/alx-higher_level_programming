#!/usr/bin/bash

# Check if the user provided a URL as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL provided by the user
url="$1"

# Use curl to send a GET request and store the output in a variable
response=$(curl -sI "$url")

# Extract the Content-Length header value from the response headers
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Use curl again to get the response body and measure its size in bytes
body_size=$(curl -s "$url" | wc -c)

# Display the content length in bytes
echo "$body_size"
