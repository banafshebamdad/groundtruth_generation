#
# usage: $ bash compute_mean.sh /file/name/in/the/following/format  "FrameId: 44     #matches: 609" 
# !!! ACHTUNG !!! The first line should not be empty
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

mean=$(awk -F'#matches: ' '{sum += $2; count++} END {print sum / count}' "$filename")

echo "Mean number after #matches: $mean"

