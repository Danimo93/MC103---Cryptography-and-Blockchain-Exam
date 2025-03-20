#!/bin/bash
while read pass; do
    echo "Trying password: $pass"
    echo "$pass" | gpg --batch --yes --passphrase-fd 0 --decrypt msg.txt.asc 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Password found: $pass"
        break
    fi
done < mylist.txt
