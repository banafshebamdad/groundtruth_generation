#
# !!! Achtung !!!
# Use the convert_images_kevin_robb.py script instead of this one. I modified that script to fullfill my needs.
# Banafshe Bamdad
# Mi Jul 19, 2023 10:00:32 CET
#
# Usage e.g. $ python3 extract_frames_from_bag.py -b /home/banafshe/data_collection/2023_06_18/winti02_RPG_D435i.bag -o /home/banafshe/Desktop/demonstration/colmap_ws/frames_by_cv -t /camera/color/image_raw
#
import argparse
import cv2
import os
import rosbag
from cv_bridge import CvBridge

def save_images(bagfile, outdir, rostopic):
    bag = rosbag.Bag(bagfile, "r")
    bridge = CvBridge()
    frame_number = 0

    for topic, msg, t in bag.read_messages(topics=[rostopic]):
        try:
            cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            print(f"Error converting ROS image message: {e}")
            continue

        #frame_filename = os.path.join(outdir, f"frame{frame_number:06d}.jpg")
        frame_filename = os.path.join(outdir, f"{t}.jpg")
        cv2.imwrite(frame_filename, cv_image)
        print(frame_number)
        frame_number += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bagfile', help='Path to the bag file.')
    parser.add_argument('-o', '--outdir', help='Path to the directory in which images will be saved.')
    parser.add_argument('-t', '--rostopic', help='ROS topic from which images should be extracted.')

    args = parser.parse_args()

    bagfile = args.bagfile
    outdir = args.outdir
    rostopic = args.rostopic

    if not (bagfile and outdir and rostopic):
        print("\nUsage: python3 extract_frames_from_bag.py -b /path/to/bag/file -o /path/to/output/directory -t /ros/topic\n")
        exit(1)

    save_images(bagfile, outdir, rostopic)

