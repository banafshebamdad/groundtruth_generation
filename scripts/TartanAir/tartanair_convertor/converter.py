#
# Banafshe Bmdad
# Jan 19, 2024
#
# Usage
# set the parameters value in config.txt
#   DATASET_HOME: dataset home /path/to/rgb/depth/association.txt files
#   NPY_SOURCE: .npy source folder in original dataset
#   RGB_SOURCE: left_image folder in original dataset
#   NUM_OF_FRAMES: number of frames in sequence
# $ source /home/banafshe/global_env/bin/activate
# $ python converter.py /pth/to/config.txt
#
import os
import shutil
import numpy as np
from PIL import Image
import sys

def read_config(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    config = {}
    for line in lines:
        if not line.startswith("#") and line.strip():
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()

    return config

def copy_and_rename_files(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            base_name = os.path.basename(file).split('_')[0]
            extension = file.split('.')[-1]
            new_name = f"{base_name}.{extension}"
            print(new_name, "has been copied.")
            shutil.copy(file_path, os.path.join(destination_folder, new_name))

def convert_npy_to_tum_depth_images(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    npy_files = [file for file in os.listdir(input_folder) if file.endswith('.npy')]
    for npy_file in npy_files:
        depth_data = np.load(os.path.join(input_folder, npy_file))
        scaled_depth = (depth_data * 5000.0).astype(np.uint16)
        depth_image = Image.fromarray(scaled_depth, mode='I;16')
        depth_image.save(os.path.join(output_folder, os.path.splitext(npy_file)[0] + '.png'))
        print(npy_file, " has been converted")

def generate_associations_file(num_entries, output_file):
    with open(output_file, 'w') as file:
        for i in range(num_entries):
            num_str = f"{i:06d}"
            line = f"{num_str} rgb/{num_str}.png {num_str} depth/{num_str}.png\n"
            file.write(line)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python converter.py /path/to/the/config.txt")
        sys.exit(1)

    
    print("\nStep 1. Read config file ...\n")
    config_file_path = sys.argv[1]
    config = read_config(config_file_path)

    DATASET_HOME = config['DATASET_HOME']
    NPY_SOURCE = config['NPY_SOURCE']
    RGB_SOURCE = config['RGB_SOURCE']
    NUM_OF_FRAMES = int(config['NUM_OF_FRAMES'])

    RGB_PATH = os.path.join(DATASET_HOME, 'rgb')
    DEPTH_PATH = os.path.join(DATASET_HOME, 'depth')
    NPY_PATH = os.path.join(DATASET_HOME, 'npy')

    # Step 2. Create directories
    print("\nStep 2. Create dataset structure ...\n")
    for path in [RGB_PATH, DEPTH_PATH, NPY_PATH]:
        os.makedirs(path, exist_ok=True)

    # Step 3. Copy and rename RGB files
    print("\nStep 3. Copy RGB files. Please wait ...\n")
    copy_and_rename_files(RGB_SOURCE, RGB_PATH)

    # Step 4. Convert .npy files to depth images
    print("\nStep 4. convert .npy files to depth images ...\n")
    convert_npy_to_tum_depth_images(NPY_SOURCE, NPY_PATH)

    # Step 5. Copy and rename NPY files
    print("\nStep 5. Copy depth images ...\n")
    copy_and_rename_files(NPY_PATH, DEPTH_PATH)

    # Step 6. Generate associations file
    print("\nStep 6. Generate associations file ...\n")
    associations_file = os.path.join(DATASET_HOME, 'associations.txt')
    generate_associations_file(NUM_OF_FRAMES, associations_file)
    
    print("\n::: The dataset has been generated successfully. Check ", DATASET_HOME, "\n")

