#
#
#

#!/bin/bash

#input_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/hospital/hard/P037/CameraTrajectory.txt"
#input_file="/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/TartanAir/no_loop_closure/Hospital/hard/P037/CameraTrajectory.txt"
#input_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/no_loop_closure/hospital/hard/P037/run02_ORB_Relocalization/CameraTrajectory.txt"
#input_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/no_loop_closure/hospital/hard/P038/run01/CameraTrajectory.txt"
input_file="/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/TartanAir/no_loop_closure/Hospital/hard/P037/run01_1200F/CameraTrajectory.txt"

#output_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/hospital/hard/P037/pose_est.txt"
#output_file="/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/TartanAir/no_loop_closure/Hospital/hard/P037/pose_est.txt"
#output_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/no_loop_closure/hospital/hard/P037/run02_ORB_Relocalization/pose_est.txt"
#output_file="/home/banafshe/SUPERSLAM3/my_logs/TartanAir/no_loop_closure/hospital/hard/P038/run01/pose_est.txt"
output_file="/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/TartanAir/no_loop_closure/Hospital/hard/P037/run01_1200F/pose_est.txt"

# Remove the timestamp in the first column 
awk '{$1=""; print $0}' "$input_file" | sed 's/^[[:space:]]*//' > "$output_file"
