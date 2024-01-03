#!/bin/bash

#
# Banafshe bamdad
# Mi Aug 2, 2023 CET 12:30
#
# This scripts reads the name of the files files in a folder, 
# and writes the data to a CSV file with the file names in the second column and the corresponding timestamps in the first column.
# 
# The output will be written into data.csv file.
# You need to move this file to your desired path.
#
# $1: input_folder. path to the folder containing images
# Usage: bash banafshe_create_data_from_frames_name.sh /path/to/the/folder/with/images
#

#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/18_Jun_2023_winti02_RPG_D435i_infra_frames/crowded_frames/cam1/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/challenging_conditions/08_Aug_2023_ZHAW_D435i_infra_frames/blur/infra1/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/challenging_conditions/08_Aug_2023_ZHAW_D435i_infra_frames/blur/infra2/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/challenging_conditions/08_Aug_2023_ZHAW_D435i_infra_frames/loop/infra1/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/challenging_conditions/08_Aug_2023_ZHAW_D435i_infra_frames/loop/infra2/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/challenging_conditions/08_Aug_2023_ZHAW_D435i_infra_frames/occlusion/infra1/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/challenging_conditions/08_Aug_2023_ZHAW_D435i_infra_frames/occlusion/infra2/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/11_Aug_2023_Zurich_HB_ZHAW_D435i/stereo_imu/shopville/shopville_stereo_stereo_imu_loop_ZurichHB/infra2/data"
#input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/11_Aug_2023_Zurich_HB_ZHAW_D435i/stereo_imu/shopville/barely_dynamic_ZurichHB_manually_generated/infra2/data"
input_folder="/media/banafshe/Banafshe_2TB/ORB-SLAM3/11_Aug_2023_Zurich_HB_ZHAW_D435i/stereo_imu/shopville/barely_dynamic_ZurichHB_manually_2023_08_21/infra2/data"
#input_folder=$1
output_csv="data.csv"

convert_to_nanoseconds() {
  #timestamp_seconds=$1
  #echo "$((timestamp_seconds * 1000000000))"
  echo "$1"
}

# Header for the CSV file
echo "#timestamp [ns],filename" > "$output_csv"

for file in "$input_folder"/*; do
  filename=$(basename "$file")

  timestamp_seconds="${filename%.*}"

  timestamp_nanoseconds=$(convert_to_nanoseconds "$timestamp_seconds")

  echo "$timestamp_nanoseconds,$filename" >> "$output_csv"

  echo "$timestamp_nanoseconds , $filename"
done

echo "Conversion completed. CSV file created: $output_csv"
echo
echo "Copy data.csv to your desired path."
