#!/usr/bin/bash
# Get byte size of url content
curl -s '$1' | wc -c
