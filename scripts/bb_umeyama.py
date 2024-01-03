
#
# Banafshe Bamdad
# Sa Jul 15, 2023 12:45:45 CET 
# This script gets path to two files, first trajectory genrated by COLMAP and reformat by stamped_traj_estimate_from_colmap_traj.sh script, second trajectory generated w.r.t Charuco marker using banafshe_detect_board_charuco.cpp. I tthen compte rotation matrix, translation vector, and scale using Umeyama's method.
#
# Usage: python3 bb_umeyama.py -s /path/to/COLMAP/poses -t /path/to/charuco/marker/poses
# e.g. python3 bb_umeyama.py -s /media/banafshe/Banafshe_2TB/ground_truth/colmap_workspace/my_evaluation/352-438/stamped_groundtruth.txt -t  /media/banafshe/Banafshe_2TB/ground_truth/colmap_workspace/my_evaluation/352-438/stamped_traj_estimate.txt
#

import argparse
import os
import numpy as np
import sys
from scipy.linalg import orthogonal_procrustes

#
# Banafshe Bamdad
# Sa Jul 15, 2023 11:17:37 CET
# Input
#   data_file: path to a text file containing poses info: timestamp Tx Ty Tz Qx Qy Qz Qw 
#
def pose_2_array(data_file: str):
    
    trajectory = np.empty((0, 3))
     
    with open(data_file, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
    
        pose_line = line.strip().split()
        translation_components = np.array([np.float64(pose_line[1]), np.float64(pose_line[2]), np.float64(pose_line[3])])
        trajectory = np.vstack((trajectory, translation_components))
        
    return trajectory
#
# 
#
def umeyama_alignment(source_points, target_points):
	# Convert points to homogeneous coordinates
	source_homogeneous = np.hstack((source_points, np.ones((source_points.shape[0], 1))))
	target_homogeneous = np.hstack((target_points, np.ones((target_points.shape[0], 1))))

	# Center the points by subtracting their means
	source_centered = source_homogeneous - np.mean(source_homogeneous, axis=0)
	target_centered = target_homogeneous - np.mean(target_homogeneous, axis=0)

	# Compute the covariance matrix
	covariance_matrix = np.dot(np.transpose(source_centered), target_centered)

	# Perform Singular Value Decomposition
	U, _, Vt = np.linalg.svd(covariance_matrix)

	# Calculate the optimal rotation matrix
	optimal_rotation = np.dot(Vt.T, U.T)

	# Calculate the optimal scale factor
	det = np.linalg.det(optimal_rotation)
	scale_factor = np.prod(np.sign(det)) * np.sum(_) / np.sum(np.square(source_centered))

	# Calculate the optimal translation vector
	optimal_translation = np.mean(target_homogeneous, axis=0) - scale_factor * np.dot(np.mean(source_homogeneous, axis=0), optimal_rotation.T)

	# Create the transformation matrix
	transformation_matrix = np.eye(4)
	transformation_matrix[:3, :3] = optimal_rotation[:3, :3]
	transformation_matrix[:3, 3] = optimal_translation[:3]
    
	print("Optimal Rotation:")
	print(optimal_rotation)
	print("\nOoptimal Translation:")
	print(optimal_translation)

	return transformation_matrix, scale_factor

# Example usage
source_points = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
target_points = np.array([[10, 10, 10], [20, 20, 20], [30, 30, 30]])

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', help='Path to the source file')
parser.add_argument('-t', '--target', help='path to the target file')

args = parser.parse_args()
source_file = args.source
target_file = args.target

if not (source_file and target_file):
    print("Please provide both source and target file paths as command-line arguments.")
    print("Usage: python3 bb_umeyama.py -s /path/to/source/file -t /path/to/target/file")
    sys.exit(1)

if not os.path.exists(source_file):
    print("{0} does not exist.".format(source_file))
    sys.exit(1)

if not os.path.exists(target_file):
    print("{0} does not exist.".format(target_file))
    sys.exit(1)

source_points = pose_2_array(source_file)
target_points = pose_2_array(target_file)

# Align the source points to the target points
transformation_matrix, scale_factor = umeyama_alignment(source_points, target_points)

# Print the transformation matrix and scale factor
print("Transformation matrix (SE(3)):")
print(transformation_matrix)
print("\nScale factor:")
print(scale_factor)

