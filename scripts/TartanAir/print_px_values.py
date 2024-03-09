#
# Banafshe Bamdad
# Di Jan 16, 2024
#
# This script prints the px values of a given image, specified in image_path, as well as maximum and minimum pixel values
# Usage: Specify the path to the image in image_path
# $ python print_px_values.py
#
from PIL import Image

def print_pixel_values(image_path):
    image = Image.open(image_path)

    pixel_values = list(image.getdata())

    print("Pixel values:")
    for i in range(0, len(pixel_values), image.width):
        row = pixel_values[i:i + image.width]
        print(row)

    max_value = max(pixel_values)
    min_value = min(pixel_values)
    print("\nMax Pixel Value:", max_value)
    print("Min Pixel Value:", min_value)

if __name__ == "__main__":
    image_path = "old.png"

    print_pixel_values(image_path)

