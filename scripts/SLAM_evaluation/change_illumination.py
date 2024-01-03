#
# Banafshe Bamdad
# Mo Dez 18, 2023
# This script randomly selects 30% of the images to darken and applies a darker illumination change to them, 
# saving the modified images with the same names in a new folder. 
# The remaining 70% of the images are copied without any changes. 
#

import os
import random
from PIL import Image, ImageEnhance
import shutil

def apply_illumination_change(image_path, output_path, factor=0.7):
    original_image = Image.open(image_path)

    enhancer = ImageEnhance.Brightness(original_image)
    darkened_image = enhancer.enhance(factor)

    darkened_image.save(output_path)

def process_images(input_folder, output_folder, illumination_factor=0.7, percentage_to_darken=30):

    all_images = 0
    modified_images = 0

    os.makedirs(output_folder, exist_ok=True)

    image_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".png")]

    images_to_darken = random.sample(image_files, int(percentage_to_darken / 100 * len(image_files)))
    
    for filename in image_files:
        all_images += 1
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if filename in images_to_darken:
            print(filename)
            apply_illumination_change(input_path, output_path, illumination_factor)
            modified_images += 1
        else:
            shutil.copy(input_path, output_path)

    print("# of images: ", all_images, ", # of modified images: ", modified_images)

if __name__ == "__main__":
    #input_folder = "/media/banafshe/Banafshe_2TB/Datasets/TUM/Testing_and_Debugging/xyz/rgbd_dataset_freiburg1_xyz/rgb"
    input_folder ="/media/banafshe/Banafshe_2TB/Datasets/TUM/Testing_and_Debugging/xyz/rgbd_dataset_freiburg2_xyz/rgb" 
    #output_folder = "/media/banafshe/Banafshe_2TB/Datasets/TUM/Testing_and_Debugging/xyz/rgbd_dataset_freiburg1_xyz/rgb_30_darker_07"
    output_folder = "/media/banafshe/Banafshe_2TB/Datasets/TUM/Testing_and_Debugging/xyz/rgbd_dataset_freiburg2_xyz/rgb_30_darker_07"

    # the illumination factor (0.0 means completely dark, 1.0 means no change)
    illumination_factor = 0.7

    percentage_to_darken = 30

    process_images(input_folder, output_folder, illumination_factor, percentage_to_darken)


