#!/bin/bash

#
# Banafshe Bamdad
# 1 Aug. 2023 13:45 CET
#
# This script gets the content of the desired start and the end line in a text file and returns the content of file between these two lines. The end line is excluded.
# e.g. usage:
# bash  banafshe_extract_lines.sh /media/banafshe/Banafshe_2TB/ORB-SLAM3/18_Jun_2023_winti02_RPG_D435i_infra_frames/timestamps.txt /media/banafshe/Banafshe_2TB/ORB-SLAM3/18_Jun_2023_winti02_RPG_D435i_infra_frames/crowded_timestamps.txt 1687072130 1687072189
#

if [ "$#" -ne 4 ]; then
    echo "Usage: $0 [/path/to/input/filename] [/path/to/output/file] [start tumestamp] [end timestamp]"
    exit 1
fi

input_file="$1"
output_file="$2"
start_ts="$3"
end_ts="$4"

if [ ! -f "$input_file" ]; then
    echo "Input file '$input_file' not found."
    exit 1
fi

extracted_lines=$(awk -v start="$start_ts" -v end="$end_ts" '
    # If the line contains the start string, set the flag to true
    $0 ~ start { found = 1 }
    # If the line contains the end string, set the flag to false
    $0 ~ end { found = 0 }
    # If the flag is true, print the line
    found { print }
' "$input_file")

# Print the extracted lines
echo "$extracted_lines" > "$output_file"

