#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body_response = response.read().decode('utf-8')
        print(body_response)
