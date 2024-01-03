#!/bin/bash

# 
# Banafshe Bamdad
# Mi Jul 19, 2023 13:50:24 CET
#

if [ $# -ne 2 ]; then
    echo "Usage: $0 /path/to/source/folder /path/to/target/folder"
    exit 1
fi

source_dir="$1"
target_dir="$2"

mkdir -p "$target_dir"

find "$source_dir" -maxdepth 1 -type f -iname "*.jpg" | while read -r file; do
    filename=$(basename "$file")

    timestamp="${filename%.jpg}"

    if [[ "$timestamp" -ge 1687071905259163086 ]] && [[ "$timestamp" -le 1687071910694010268 ]]; then
        cp "$file" "$target_dir"
        echo "$file is copied."
    fi
done

echo "Files copied to target directory: $target_dir"
