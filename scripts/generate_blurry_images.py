#
# $ source /home/banafshe/global_env/bin/activate
# $ python generate_blurry_images.py

import os
import cv2

def apply_gaussian_blur(input_folder, output_folder, patch_size=13, sigma=2.15):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        img = cv2.imread(image_path)

        blurred_img = cv2.GaussianBlur(img, (patch_size, patch_size), sigma)

        output_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_path, blurred_img)

if __name__ == "__main__":
    input_folder = "/media/banafshe/Banafshe_2TB/Datasets/TUM/Testing_and_Debugging/xyz/rgbd_dataset_freiburg1_xyz/rgb"
    output_folder = "/media/banafshe/Banafshe_2TB/Datasets/TUM/Testing_and_Debugging/xyz/rgbd_dataset_freiburg1_xyz/blurry_rgb"

    apply_gaussian_blur(input_folder, output_folder)

