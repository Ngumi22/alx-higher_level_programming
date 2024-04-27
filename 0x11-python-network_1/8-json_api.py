#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post(url, data={'q': q})

    if response.status_code == 200:
        try:
            json_data = response.json()
            if json_data:
                print("[{}] {}".format(json_data['id'], json_data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    else:
        print("Error:", response.status_code)
