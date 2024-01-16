#
# Banafshe Bamdad
# Di Jan 16, 2024 
# This script print the value of a .npy file as well as the min and max value.
# I use this script to compare the value of depth information in tartanAir dataset with depth info. in TUM RGB-D dataset.
# Usage: 
# Specify the path to the .npy file in npy_file_path
# $ python print_npy_values.py
#

import numpy as np

def print_npy_values(npy_file_path):
    data = np.load(npy_file_path)

    flattened_data = data.flatten()

    print("All values:")
    for value in flattened_data:
        print(value)

    max_value = np.max(data)
    min_value = np.min(data)
    print("\nMax Value:", max_value)
    print("Min Value:", min_value)

if __name__ == "__main__":
    # Specify the path to the .npy file
    npy_file_path = "000000_left_depth.npy" 

    print_npy_values(npy_file_path)

