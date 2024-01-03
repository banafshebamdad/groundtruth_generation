#!/bin/bash

#
# Banafshe Bamdad
# Do Jul 20, 2023 07:46:15 CET
# 
# This script gets the path to the trajectory file created by Kimera-VIO in the following format:
# timestamp_kf,x,y,z,qw,qx,qy,qz
# Reads each line and makes a new file with the following format in each line:
# timestamp x y z qx qy qz qw
# The output of this script can be used in RPG_evaluate_trajectory tool
#
# Usage: bash convert_kimera_output.sh /path/to/kimera/traj/file /path/to/output/filename.txt
# e.g.
#   input_file="/home/banafshe/catkin_ws/src/Kimera-VIO-ROS/output_logs/Winti_HB_RPG_D435i/traj_pgo.csv"
#   output_file="kimera2rpg.txt"
#

if [ $# -nq 2 ]; then
    echo "Usage: $0 /path/to/kimera/traj/file /path/to/output"
    exit 1
fi
input_file="$1"
output_file="$2"

if [ ! -f "$input_file" ]; then
  echo "Input file not found: $input_file"
  exit 1
fi

IFS=","
while read -r timestamp x y z qx qy qz qw vx vy vz bgx bgy bgz bax bay baz; do
  echo "$timestamp $x $y $z $qx $qy $qz $qw" >> "$output_file"
done < "$input_file"

unset IFS

echo "Data has been written to $output_file. successfully"
