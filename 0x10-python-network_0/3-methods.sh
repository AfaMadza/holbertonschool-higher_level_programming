#!/bin/bash
# Displays methods a server will accept
curl -l $1 -Is | grep -Fi Allow | cut -d' ' -f 2-
