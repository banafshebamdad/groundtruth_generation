#
# Banafshe Bamdad
# Di Jul 18, 2023 11:25:43 CET
#

import argparse
import os
import rosbag
import rospy
import sys

def retrieve_timestamps_and_frame_ids(bag_file: str, ros_topic: str="/camera/color/image_raw"):
    """
    Retrieves the timestamps and frame IDs corresponding to frames from a bag file.
    Inputs:
        bag_file: The path to the bag file.
    Returns:
        A list of tuples, where each tuple contains a timestamp and a frame ID.
    """

    bag = rosbag.Bag(bag_file, "r")
    timestamps_and_frame_ids = []

    frame_id = 0
    for topic, msg, _ in bag.read_messages():
        if topic == ros_topic:
            if hasattr(msg, 'header') and hasattr(msg.header, 'frame_id'):
                timestamp = msg.header.stamp.to_nsec()
                #frame_id = msg.header.frame_id
                timestamps_and_frame_ids.append((timestamp, frame_id))
                print(frame_id, " - ", timestamp)                
                frame_id += 1

    return timestamps_and_frame_ids

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bagfile', help='Path to the bag file.')
    parser.add_argument('-t', '--rostopic', help='ROS topic from which we want to retrieve the information.')

    args = parser.parse_args()
    bagfile = args.bagfile
    rostopic = args.rostopic

    if not (bagfile and rostopic):
        print('\nPlease provide both path to bag file and the ros topic as command-line arguments.\n')
        print('Usage:')
        print('\t$ python3 timestamp_frameid.py -b /path/to/filename.bag -t /ros/topic/name')
        print('e.g:')
        print('\t$ python3 timestamp_frameid.py -b /home/banafshe/data_collection/2023_06_18/winti02_RPG_D435i.bag -t /camera/infra1/image_rect_raw')
        sys.exit(1)

    if not os.path.exists(bagfile):
        print("\n{}: No such file or directory".format(bagfile))
        sys.exit(1)

    timestamps_and_frame_ids = retrieve_timestamps_and_frame_ids(bagfile)

