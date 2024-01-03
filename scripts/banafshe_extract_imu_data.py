#! /usr/bin/python3

import rospy
from sensor_msgs.msg import Imu
import cv2
import subprocess
import sys
import os

def get_imu(msg):
    time = msg.header.stamp
    try:
        # Get the Imu 
        w_RS_S_x = msg.angular_velocity.x
        w_RS_S_y = msg.angular_velocity.y
        w_RS_S_z = msg.angular_velocity.z
        a_RS_S_x = msg.linear_acceleration.x
        a_RS_S_y = msg.linear_acceleration.y
        a_RS_S_z = msg.linear_acceleration.z

        data_line = str(time) + "," + str(w_RS_S_x) + "," + str(w_RS_S_y) + "," + str(w_RS_S_z) + "," + str(a_RS_S_x) + "," + str(a_RS_S_y) + "," + str(a_RS_S_z) + "\n"

        print(data_line)

        imu_data.write(data_line)
    except:
        rospy.logerr("Exception encountered on cam0.")


def run_bash_cmd(command:str):
    process = subprocess.Popen(command.split())
    output, error = process.communicate()


def main():
    global imu_data
    rospy.init_node('imu_data_extractor', anonymous=True)

    imu_data = open("imu_data.csv", "w")
    imu_data.write("#timestamp [ns],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]\n")

    rospy.loginfo("\nIMU data will be saved to imu_data.csv file in currect directory.\n\nNow,  Run 'rosbag play ROSBAG_NAME.bag' in a new terminal.\n\nTerminate this script with Ctrl+C after rosbag is finished playing.")

    print("\nCopy imu_data.csv to your desired path after rosbag is finished playing ...\n")
    
    # Subscribe to the imu streams.
    
    rospy.Subscriber("/camera/imu", Imu, get_imu)
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
