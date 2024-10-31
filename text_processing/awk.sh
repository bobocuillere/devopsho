#!/bin/bash

echo "--------------------Using the AWK method-------------------------"
awk '{
    # Convert to lowercase
    line = tolower($0)
    # Remove protocol and trailing dots
    gsub(/https?:\/\//, "", line)
    gsub(/\.$/, "", line)
    # Split by dots
    n = split(line, parts, ".")
    # Print the last two parts (domain and TLD)
    if (n >= 2) {
        print parts[n-1]"."parts[n]
    }
}' input.txt | sort -u
