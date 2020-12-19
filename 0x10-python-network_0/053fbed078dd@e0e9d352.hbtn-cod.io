#!/bin/bash
# Take in a URL and display the size of that response in bytes.
curl -s "$1" | wc -c
