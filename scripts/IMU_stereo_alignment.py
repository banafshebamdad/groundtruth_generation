import pandas as pd
import numpy as np

pd.set_option('display.float_format', '{:.6f}'.format)

# Load IMU data from CSV file
imu_data = pd.read_csv('/media/banafshe/Banafshe_2TB/ORB-SLAM3/18_Jun_2023_winti02_RPG_D435i_infra_frames/crowded_frames/imu/data-cp.csv')

# Load stereo image timestamps from text file
with open('/media/banafshe/Banafshe_2TB/ORB-SLAM3/18_Jun_2023_winti02_RPG_D435i_infra_frames/crowded_frames/crowded_timestamps-cp.txt', 'r') as f:
    stereo_timestamps = [float(line.strip()) for line in f]

# Preprocess data: Convert IMU timestamps to seconds
imu_data['#timestamp [ns]'] /= 1e9

# Initialize lists to store matched timestamps
matched_stereo_timestamps = []
matched_imu_timestamps = []

# Find the closest matching IMU data timestamp for each stereo image timestamp
for stereo_ts in stereo_timestamps:
    closest_imu_ts = imu_data['#timestamp [ns]'].iloc[(np.abs(imu_data['#timestamp [ns]'] - stereo_ts)).idxmin()]
    matched_stereo_timestamps.append(stereo_ts)
    matched_imu_timestamps.append(closest_imu_ts)

# Combine matched timestamps into a new DataFrame
synchronized_data = pd.DataFrame({'stereo_timestamp': matched_stereo_timestamps,
                                  'imu_timestamp': matched_imu_timestamps})

# Calculate the time difference between stereo and IMU timestamps
synchronized_data['time_diff'] = synchronized_data['stereo_timestamp'] - synchronized_data['imu_timestamp']

# Print the synchronized data
print(synchronized_data)

synchronized_data.to_csv('synchronized_data.csv', index=False)
