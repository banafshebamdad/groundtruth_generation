#
# Usage $ bash remove_duplicates.sh /home/banafshe/SUPERSLAM3/my_logs/Banafshe_num_matches.log
#

#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

if [ ! -f "$filename" ]; then
    echo "Error: File not found!"
    exit 1
fi

awk '!seen[$0]++' "$filename" > "${filename}.tmp" && mv "${filename}.tmp" "$filename"

echo "Duplicate lines removed from $filename."

