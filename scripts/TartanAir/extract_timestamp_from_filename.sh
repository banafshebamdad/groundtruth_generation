#
# Banafshe Bamdad
# Di Jan 16, 2024
# 
# This script reads files from a source folder, extracts the first part of the name before '_', keeps the extension, and then saves the file with the new name in a destination folder
# I use this script to prepare TartanAir RGB and depth files in the TUM RGB-D format.
#
# Usage:
# Specify source and destination folder path in source_folder and destination_folder variables
# $ bash extract_timestamp_from_filename.sh

#!/bin/bash

#source_folder="/media/banafshe/Banafshe_2TB/Datasets/TartanAir/training_data/hospital/Hard/hospital/hospital/Hard/P037/image_left"
#destination_folder="/media/banafshe/Banafshe_2TB/Datasets/TartanAir/my_test_sequences/hospital_hard/P037/rgb"

source_folder="/media/banafshe/Banafshe_2TB/Datasets/TartanAir/my_test_sequences/hospital_hard/P037/npy"
destination_folder="/media/banafshe/Banafshe_2TB/Datasets/TartanAir/my_test_sequences/hospital_hard/P037/depth"

mkdir -p "$destination_folder"

for file in "$source_folder"/*; do
    if [ -f "$file" ]; then
        base_name=$(basename "$file" | cut -d'_' -f1)

        extension="${file##*.}"

        new_name="${base_name}.${extension}"

        cp "$file" "$destination_folder/$new_name"
    fi
done

