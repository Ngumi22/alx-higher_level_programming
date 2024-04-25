#!/bin/bash
# takes in a URL, sends a POST request to the passed URL
curl -s -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
