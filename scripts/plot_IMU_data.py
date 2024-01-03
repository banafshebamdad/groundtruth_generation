# 
# Banafshe bamdad
# 4 Aug. 2023 10:47 CET
#
# Usage: replace the full path of csv file containing imu data in the line started with "imu_data = pd.read_csv("
# $ python3 plot_IMU_data.py
# You need to install the following packages:
# $ sudo apt install python3-pip
# $ pip3 install pandas
# $ pip3 install matplotlib
#

import pandas as pd
import matplotlib.pyplot as plt

# Load IMU data from CSV file
imu_data = pd.read_csv('/media/banafshe/Banafshe_2TB/ORB-SLAM3/18_Jun_2023_winti02_RPG_D435i_infra_frames/crowded_frames/imu/data.csv')

# Extract timestamp and convert to seconds
imu_data['#timestamp [ns]'] /= 1e9

# w_RS_S_x [rad s^-1],w_RS_S_y [rad s^-1],w_RS_S_z [rad s^-1],a_RS_S_x [m s^-2],a_RS_S_y [m s^-2],a_RS_S_z [m s^-2]
# Plot angular velocities in x, y, and z axes over time
plt.figure(figsize=(10, 6))
plt.plot(imu_data['#timestamp [ns]'], imu_data['w_RS_S_x [rad s^-1]'], label='Angular Velocity X')
plt.plot(imu_data['#timestamp [ns]'], imu_data['w_RS_S_y [rad s^-1]'], label='Angular Velocity Y')
plt.plot(imu_data['#timestamp [ns]'], imu_data['w_RS_S_z [rad s^-1]'], label='Angular Velocity Z')
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('IMU Angular Velocities')
plt.legend()
plt.grid(True)
plt.show()

# Plot accelerations in x, y, and z axes over time
plt.figure(figsize=(10, 6))
plt.plot(imu_data['#timestamp [ns]'], imu_data['a_RS_S_x [m s^-2]'], label='Acceleration X')
plt.plot(imu_data['#timestamp [ns]'], imu_data['a_RS_S_y [m s^-2]'], label='Acceleration Y')
plt.plot(imu_data['#timestamp [ns]'], imu_data['a_RS_S_z [m s^-2]'], label='Acceleration Z')
plt.xlabel('Time (seconds)')
plt.ylabel('Acceleration (m/s^2)')
plt.title('IMU Accelerations')
plt.legend()
plt.grid(True)
plt.show()

