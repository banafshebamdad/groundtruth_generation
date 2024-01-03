#
# Banafshe Bamdad
# This script captures and saves simultaneously color, depth, infrared stereo images, and IMU data from the RealSense D435i camera. 
# The left and right stereo images will be saved in two separate folders
# Req.
#    pip3 install pyrealsense2
#
import os
import pyrealsense2 as rs
import cv2
import time
import numpy as np

# Create output directories if they don't exist
left_stereo_dir = 'left_stereo_images'
right_stereo_dir = 'right_stereo_images'
imu_data_file = 'imu_data.txt'

os.makedirs(left_stereo_dir, exist_ok=True)
os.makedirs(right_stereo_dir, exist_ok=True)

# Initialize the camera and pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 848, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.infrared, 1, 848, 480, rs.format.y8, 30)
config.enable_stream(rs.stream.infrared, 2, 848, 480, rs.format.y8, 30)
config.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, 100)
config.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)

pipeline.start(config)

try:
    imu_data = []
    while True:
        # Wait for the next set of frames from the camera
        frames = pipeline.wait_for_frames()

        # Get stereo infrared images
        infrared_frame_left = frames.get_infrared_frame(1)
        infrared_frame_right = frames.get_infrared_frame(2)

        if not infrared_frame_left or not infrared_frame_right:
            continue

        # Get stereo color and depth images
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        # Get IMU data (accelerometer and gyroscope)
        accel_frame = frames.first_or_default(rs.stream.accel)
        gyro_frame = frames.first_or_default(rs.stream.gyro)
        if accel_frame and gyro_frame:
            accel_data = accel_frame.as_motion_frame().get_motion_data()
            gyro_data = gyro_frame.as_motion_frame().get_motion_data()
            timestamp_ns = accel_frame.timestamp

            imu_data.append((timestamp_ns,
                             gyro_data.x, gyro_data.y, gyro_data.z,
                             accel_data.x, accel_data.y, accel_data.z))

            # Save stereo images
            timestamp_ms = int(time.time() * 1000)
            left_filename = os.path.join(left_stereo_dir, f'{timestamp_ms}_left.png')
            right_filename = os.path.join(right_stereo_dir, f'{timestamp_ms}_right.png')

            infrared_image_left = np.asanyarray(infrared_frame_left.get_data())
            infrared_image_right = np.asanyarray(infrared_frame_right.get_data())

            cv2.imwrite(left_filename, infrared_image_left)
            cv2.imwrite(right_filename, infrared_image_right)

except KeyboardInterrupt:
    with open(imu_data_file, 'w') as imu_file:
        imu_file.write("#timestamp [ns],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]\n")
        for imu_entry in imu_data:
            imu_file.write(','.join(map(str, imu_entry)) + '\n')
finally:
    pipeline.stop()
