# Text Processing Scripts

This repository contains scripts for processing text files to extract domain names. The scripts use different methods to achieve the same goal. Below are the details of each script and how to use them.

## Scripts

### 1. SED and GREP Method (`sed.sh`)

This script uses a combination of `grep`, `sed`, `tr`, and `awk` to extract domain names from a text file.

#### Usage

1. Ensure the script has execute permissions:
    ```bash
    chmod +x sed.sh
    ```

2. Run the script:
    ```bash
    ./sed.sh
    ```

#### Script Details

```shell
#!/bin/bash

echo "----------------Using the SED and GREP method-----------------------------"
grep -oE '((http|https)://)?[^/ ]+' input.txt | \
sed -E 's/https?:\/\///I; s/\.$//; s/.*@//' | \
tr '[:upper:]' '[:lower:]' | \
awk -F. '{ 
    if (NF>=2) 
        print $(NF-1)"."$NF 
}' | sort -u
```

### 2. AWK Method (`awk.sh`)

This script uses `awk` to process the text file and extract domain names.

#### Usage

1. Ensure the script has execute permissions:
    ```bash
    chmod +x awk.sh
    ```

2. Run the script:
    ```bash
    ./awk.sh
    ```

#### Script Details

```shell
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
```

## Input File

Both scripts process a file named `input.txt`. Below is an example of the content of `input.txt`:

```plaintext
http://tiktok.com
https://ads.faceBook.com.
https://sub.ads.faCebook.com
api.tiktok.com
Google.com.
aws.amazon.com
```

## Output

Both scripts will produce a sorted list of unique domain names in the format `domain.tld`. For the example `input.txt`, the output will be:

```plaintext
amazon.com
facebook.com
google.com
tiktok.com
```
