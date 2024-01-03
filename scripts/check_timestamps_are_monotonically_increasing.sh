#!/bin/bash
#
# This script chack if Timestamps are in correct order and monotonically increasing.
#
# usage:bash check_timestamps_are_monotonically_increasing.sh /path/to/time/stamp.txt
# Input file containing timestamps (one per line)
input_file="$1"

# Read timestamps into an array
readarray -t timestamps < "$input_file"

# Check if timestamps are in ascending order
is_monotonic=true
prev_timestamp=${timestamps[0]}
for timestamp in "${timestamps[@]:1}"; do
    if (( timestamp <= prev_timestamp )); then
        is_monotonic=false
        break
    fi
    prev_timestamp=$timestamp
done

if $is_monotonic; then
    echo "Timestamps are in correct order and monotonically increasing."
else
    echo "Timestamps are not in correct order or not monotonically increasing."
fi

