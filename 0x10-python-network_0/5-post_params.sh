#!/bin/bash
# Sends GET request and displays response body
curl -s $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
