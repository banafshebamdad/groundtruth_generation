#
# Banafshe Bamdad
# Mo Jan 22, 2024
#
# The file should be in the following format: FrameId: 1215	#MPs: 3980, which is tab-separated
# This script keeps the first occurrence of each #MPs (the data in the second column), and remove subsequent duplicates.
#!/bin/bash

input_file=$1

awk -F'\t' '!seen[$2]++' $input_file > "$input_file"_no_duplicate.csv

# '!seen[$2]++' is an awk idiom that uses an associative array to keep track of which keyframe counts have been seen.
# The '!' negates the condition, so it's true only the first time a particular keyframe count is encountered.

