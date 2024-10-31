#!/bin/bash

echo "----------------Using the SED and GREP method-----------------------------"
grep -oE '((http|https)://)?[^/ ]+' input.txt | \
sed -E 's/https?:\/\///I; s/\.$//; s/.*@//' | \
tr '[:upper:]' '[:lower:]' | \
awk -F. '{ 
    if (NF>=2) 
        print $(NF-1)"."$NF 
}' | sort -u
