#!/bin/bash
# Send a DELETE request.
curl -si -X OPTIONS "$1" | grep Allow | cut -d " " -f 2-100
