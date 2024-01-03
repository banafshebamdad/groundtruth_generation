#!/bin/bash

# reads the names of files from a text file, adds the ".png" file extension to each name, and then copies the files from one directory to another. 

#
# Banafshe Bamdad
# 1 Aug. 2023 14:10 CET
#

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 [file_list.txt] [source_directory] [destination_directory]"
    exit 1
fi

file_list="$1"
source_dir="$2"
destination_dir="$3"

if [ ! -f "$file_list" ]; then
    echo "File list '$file_list' not found."
    exit 1
fi

if [ ! -d "$source_dir" ]; then
    echo "Source directory '$source_dir' not found."
    exit 1
fi

if [ ! -d "$destination_dir" ]; then
    echo "Destination directory '$destination_dir' not found."
    exit 1
fi

# Read each line from the file list and copy the files with ".png" extension
while read -r filename; do
    if [ -f "$source_dir/$filename.png" ]; then
        cp "$source_dir/$filename.png" "$destination_dir/${filename}.png"
        echo "Copied: $filename -> ${filename}.png"
    else
        echo "File not found: $filename"
    fi
done < "$file_list"

