#!/bin/bash

#
# Banafshe Bamdad
#
# Fr Jul 14, 2023 13:08:51 CET
#
# This script reads images.txt (an output from COLMAP) file and generates a new text file with one line per image,
# containing the rpg_evaluate_trajectory desired fields in the specified order.
# This script extracts the frame id from the name of the frame and adds it as a timestamp in the first column.
# It checks if input_file is in the list of command parameters and uses it as input_file to extract the data, otherwise it uses the images.txt in the current directory.
# It checks if output_file is in the list of command parameters and uses it as output_file to save the required data, otherwise it names it stamped_traj_estimate.txt and saves it in the current directory.
#
# Usage: stamped_traj_estimate_from_colmap_traj.sh [/path/to/the/input/file] [/path/to/the/output/file]
# e.g. $ bash stamped_traj_estimate_from_colmap_traj.sh my_images.txt test.txt
#

# -Z: check if $1 is empty or has a length of zero
if [ -z "$1" ]; then
   input_file="images.txt"
else
   input_file="$1"
fi

if [ ! -f "$input_file" ]; then
   echo "File $input_file does not exist."
fi

if [ -z "$2" ]; then
   output_file="stamped_groundtruth.txt"
else
   output_file="$2"
fi

while read -r line1 && read -r line2; do
   
   # Internal Field Separator: a variable containing seperator in $line1
   # <<<: Here String: redirects the content of $line1 (a string) as input to the read command.
   IFS=', ' read -r IMAGE_ID QW QX QY QZ TX TY TZ CAMERA_ID NAME <<< "$line1"

   # Extract the frame ID. This Id will be used as timestmap.
   frame_id="${NAME/frame0/}"
   frame_id="${frame_id/frame/}"
   frame_id="${frame_id/.jpg/}"
 
   output_line="$frame_id $TX $TY $TZ $QX $QY $QZ $QW"

   echo "$output_line" >> "$output_file"
done < "$input_file"
