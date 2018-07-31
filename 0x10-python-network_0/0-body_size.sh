#!/bin/bash
# Finds the Content-Length of a given website
curl $1 -Is | grep -Fi Content-Length | cut -d' ' - f2
