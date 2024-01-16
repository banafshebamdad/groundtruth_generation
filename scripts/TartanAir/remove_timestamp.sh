#
#
#

#!/bin/bash

input_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/hospital/hard/P037/CameraTrajectory.txt"
output_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/hospital/hard/P037/pose_est.txt"

# Remove the timestamp in the first column 
awk '{$1=""; print $0}' "$input_file" | sed 's/^[[:space:]]*//' > "$output_file"
