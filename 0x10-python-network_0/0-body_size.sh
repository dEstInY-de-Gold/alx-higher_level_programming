#!/usr/bin/bash
#a bash script for saving response from a server

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to URL and save response to variable
response=$(curl -sI "$1")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i 'content-length:' | awk '{print $2}')

# Display the content length in bytes
echo "Content length: $content_length bytes"
