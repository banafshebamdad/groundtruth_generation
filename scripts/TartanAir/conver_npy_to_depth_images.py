#
# Banafshe Bamdad
# Di jan 16, 2024
#
# This script gets the path to a folder containing .npy files and convert all of them into .png file with the following format (depth file in TUN RGB-D) 
# scaled by a factor of 5000, i.e., a pixel value of 5000 in the depth image corresponds to a distance of 1 meter from the camera, 10000 to 2 meter distance, etc. 
# A pixel value of 0 means missing value/no data. The depth maps are stored as 640x480 16-bit monochrome images in PNG format
# Save the depth image in the output folder with the same filename and '.png' extension
# I use this script to convert .npy depth files in TartanAir dataset ino depth file
# Usage:
# Specify the input and output folders in input_folder and output_folder vaiables
# $ python conver_npy_to_depth_images.py
#
import os
import numpy as np
from PIL import Image

def convert_npy_to_tum_depth_images(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    npy_files = [file for file in os.listdir(input_folder) if file.endswith('.npy')]

    for npy_file in npy_files:
        depth_data = np.load(os.path.join(input_folder, npy_file))

        scaled_depth = (depth_data * 5000.0).astype(np.uint16)

        depth_image = Image.fromarray(scaled_depth, mode='I;16')

        depth_image.save(os.path.join(output_folder, os.path.splitext(npy_file)[0] + '.png'))

if __name__ == "__main__":
    # Specify the input and output folders
    #input_folder = "/media/banafshe/Banafshe_2TB/Datasets/TartanAir/training_data/hospital/Hard/hospital/hospital/Hard/P037/depth_left"
    #output_folder = "/media/banafshe/Banafshe_2TB/Datasets/TartanAir/my_test_sequences/hospital_hard/P037/npy"

    input_folder = "/media/banafshe/Banafshe_2TB/Datasets/TartanAir/training_data/hospital/Hard/hospital/hospital/Hard/P038/depth_left"
    output_folder = "/media/banafshe/Banafshe_2TB/Datasets/TartanAir/my_test_sequences/hospital_hard/P038/npy"

    convert_npy_to_tum_depth_images(input_folder, output_folder)

