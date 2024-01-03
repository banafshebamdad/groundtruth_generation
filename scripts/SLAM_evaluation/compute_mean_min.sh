#
# Usage $ bash compute_mean_min.sh  /file/name/in/the/following/format  "FrameId: 44     #matches: 609"
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

read first_line < "$filename"

echo $first_line
min=$(echo "$first_line" | awk -F'#matches: ' '{print $2}')

awk -F'#matches: ' -v min="$min" '
{
    value = $2
    sum += value
    count++
    if (value < min) min = value
}
END {
    printf "Mean: %.2f\n", sum / count
    printf "Min: %d\n", min
}
' "$filename"

