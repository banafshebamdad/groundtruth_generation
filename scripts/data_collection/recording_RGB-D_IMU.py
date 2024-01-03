import os
import pyrealsense2 as rs
import cv2
import time
import numpy as np

# Create output directories if they don't exist
color_dir = 'color_images'
depth_dir = 'depth_images'
imu_data_file = 'imu_data.txt'

os.makedirs(color_dir, exist_ok=True)
os.makedirs(depth_dir, exist_ok=True)

# Initialize the camera and pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 848, 480, rs.format.bgr8, 30)
config.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, 100)
config.enable_stream(rs.stream.gyro, rs.format.motion_xyz32f, 200)

pipeline.start(config)

try:
    imu_data = []
    while True:
        # Wait for the next set of frames from the camera
        frames = pipeline.wait_for_frames()

        # Get color and depth images
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if not color_frame or not depth_frame:
            continue

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

            # Save images
            timestamp_ms = int(time.time() * 1000)
            color_filename = os.path.join(color_dir, f'{timestamp_ms}_color.png')
            depth_filename = os.path.join(depth_dir, f'{timestamp_ms}_depth.png')

            color_image = np.asanyarray(color_frame.get_data())
            depth_image = np.asanyarray(depth_frame.get_data())

            cv2.imwrite(color_filename, color_image)
            cv2.imwrite(depth_filename, depth_image)

except KeyboardInterrupt:
    with open(imu_data_file, 'w') as imu_file:
        imu_file.write("#timestamp [ns],w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]\n")
        for imu_entry in imu_data:
            imu_file.write(','.join(map(str, imu_entry)) + '\n')
finally:
    pipeline.stop()

