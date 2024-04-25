#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"
