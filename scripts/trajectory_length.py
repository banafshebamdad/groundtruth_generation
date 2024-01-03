#
# Banafshe Bamdad
# Mo Jul 17, 2023 09:45:18 CET
#
# This script computes the length of a trajectory. To do so, it gives a file containing poses in the following format and calculate the sum of distances between consecutive poses
# timestamp Tx Ty Tz Qx Qy Qz Qw
# usage e.g.: 
#   python3 trajectory_length.py /media/banafshe/Banafshe_2TB/ground_truth/colmap_workspace/my_evaluation/352-438/stamped_groundtruth.txt
#
import sys
import math

def compute_trajectory_length(filename):
    with open(filename, 'r') as file:
        poses = file.readlines()

    trajectory_length = 0.0
    prev_pose = None

    for pose_str in poses:
        pose = pose_str.split()

        # Extract position coordinates (Tx, Ty, Tz) and convert to float
        tx, ty, tz = map(float, pose[1:4])

        if prev_pose is not None:
            # Convert previous position coordinates to float
            prev_tx, prev_ty, prev_tz = map(float, prev_pose[1:4])

            # Compute Euclidean distance between consecutive poses
            distance = math.sqrt((tx - prev_tx)**2 + (ty - prev_ty)**2 + (tz - prev_tz)**2)
            trajectory_length += distance

        prev_pose = pose

    return trajectory_length

# Check if the file name is provided as a command line argument
if len(sys.argv) < 2:
    print("Please provide the file name as a command line argument.")
else:
    filename = sys.argv[1]
    length = compute_trajectory_length(filename)
    print(f"Trajectory length: {length}")

