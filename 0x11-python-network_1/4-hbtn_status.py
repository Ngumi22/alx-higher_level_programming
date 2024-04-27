#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status using request"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    body_response = response.text

    print("Body response:")
    print("\t- type:", type(body_response))
    print("\t- content:", body_response)
