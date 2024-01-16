#
# Banafshe Bamdad
# Di Jan 16, 2024
#
# This script reads each line from the associations.txt file,
# extracts the RGB and depth file names, and then copies the corresponding files to the my_rgb and my_depth directories.
# I use this script to create a subset of sequences in the TUM RGB-D dataset.
# To use this script, first remove unwanted lines from associations.txt, and then run this script.
# The script should be placed in the sequence folder where associations.txt, rgb/, and depth/ directories exist.
#
#!/bin/bash

mkdir -p my_rgb
mkdir -p my_depth

while read -r line; do
    rgb_col=$(echo "$line" | awk '{print $2}')
    depth_col=$(echo "$line" | awk '{print $4}')

    cp "$rgb_col" my_rgb/
    cp "$depth_col" my_depth/
done < associations.txt

