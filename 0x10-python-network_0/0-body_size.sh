#!/bin/bash
# Finds the Content-Length of a given website
curl -Is $1 | grep Content-Length | cut -d ' ' -f2
