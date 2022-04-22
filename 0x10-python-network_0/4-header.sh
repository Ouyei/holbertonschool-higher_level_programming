#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. Also, a header variable X-HolbertonSchool-User-Id must be sent with the value 98.
curl -sH "X-HolbertonSchool-User-Id:98" "$1"
