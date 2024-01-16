#
# Banafshe Bamdad
# Di Jan 16, 2024
#
# This script gets a text file and adds an incrementally added six-digit number at the beginning of each line. 
# The output is redirected to a new file.
# I use this script to append the name of the RGB and depth images in ground-truth file. I assume these numbers as timestamps.
# Usage:
# specify path to ground-truth file in input_file and the name of the output file in the output_file variable.
# $ bash append_timestamp.sh
#

#!/bin/bash

input_file="pose_left.txt"

output_file="output_with_numbers.txt"

counter=0

awk -v counter="$counter" '{ printf "%06d %s\n", counter++, $0 }' "$input_file" > "$output_file"

