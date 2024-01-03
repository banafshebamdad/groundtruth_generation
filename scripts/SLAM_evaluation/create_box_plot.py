#
# Banafshe Bamdad
# Mo Dez 18, 2023
# This scripes read number of matches in consequitive frames from 4 trials and create a Box plot
# .csv files have only one column containing the number of matches in each row
#

import pandas as pd
import matplotlib.pyplot as plt

""" 
# Set 1
file1 = "/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/freiburg1_xyz/2023-12-18/1200F_SF1.2_L8/Banafshe_num_matches.csv"
file2 = "/home/banafshe/SUPERSLAM3/my_logs/freiburg1_xyz/2023-12-18/original/Banafshe_num_matches.csv"
file3 = "/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/freiburg2_xyz/2023-12-18/1200F_SF1.2_L8/Banafshe_num_matches.csv"
file4 = "/home/banafshe/SUPERSLAM3/my_logs/freiburg2_xyz/2023-12-18/original/Banafshe_num_matches.csv"

file5 = "/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/freiburg1_xyz/2023-12-18/1200F_SF1.2_L8_darker/Banafshe_num_matches.csv"
file6 = "/home/banafshe/SUPERSLAM3/my_logs/freiburg1_xyz/2023-12-18/darker/Banafshe_num_matches.csv"
file7 = "/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/freiburg2_xyz/2023-12-18/1200F_SF1.2_L8_darker/Banafshe_num_matches.csv"
file8 = "/home/banafshe/SUPERSLAM3/my_logs/freiburg2_xyz/2023-12-18/darker/Banafshe_num_matches.csv"

file9 = "/media/banafshe/62b47ac0-37ed-41e8-b72b-48b8247b3fe7/home/banafshe/ORB_SLAM3/my_logs/freiburg1_xyz/2023-12-18/1200F_SF1.2_L8_blurry/Banafshe_num_matches.csv"
file10 = "/home/banafshe/SUPERSLAM3/my_logs/freiburg1_xyz/2023-12-18/blurry/Banafshe_num_matches.csv"
"""

# Set 2
file1 = "/home/banafshe/Desktop/junk/reyhi/ORB/200.csv"
file2 = "/home/banafshe/Desktop/junk/reyhi/SELM/200.csv"
file3 = "/home/banafshe/Desktop/junk/reyhi/ORB/500.csv"
file4 = "/home/banafshe/Desktop/junk/reyhi/SELM/500.csv"
file5 = "/home/banafshe/Desktop/junk/reyhi/ORB/750.csv"
file6 = "/home/banafshe/Desktop/junk/reyhi/SELM/750.csv"
file7 = "/home/banafshe/Desktop/junk/reyhi/ORB/900.csv"
file8 = "/home/banafshe/Desktop/junk/reyhi/SELM/900.csv"
file9 = "/home/banafshe/Desktop/junk/reyhi/ORB/1000.csv"
file10 = "/home/banafshe/Desktop/junk/reyhi/SELM/1000.csv"
file11 = "/home/banafshe/Desktop/junk/reyhi/ORB/1200.csv"
file12 = "/home/banafshe/Desktop/junk/reyhi/SELM/1200.csv"

df1 = pd.read_csv(file1, header=None, names=['Number of Matches'])
df2 = pd.read_csv(file2, header=None, names=['Number of Matches'])
df3 = pd.read_csv(file3, header=None, names=['Number of Matches'])
df4 = pd.read_csv(file4, header=None, names=['Number of Matches'])
df5 = pd.read_csv(file5, header=None, names=['Number of Matches'])
df6 = pd.read_csv(file6, header=None, names=['Number of Matches'])
df7 = pd.read_csv(file7, header=None, names=['Number of Matches'])
df8 = pd.read_csv(file8, header=None, names=['Number of Matches'])
df9 = pd.read_csv(file9, header=None, names=['Number of Matches'])
df10 = pd.read_csv(file10, header=None, names=['Number of Matches'])

df11 = pd.read_csv(file11, header=None, names=['Number of Matches'])
df12 = pd.read_csv(file12, header=None, names=['Number of Matches'])

data_to_plot = [df1['Number of Matches'], df2['Number of Matches'], df3['Number of Matches'], df4['Number of Matches'], df5['Number of Matches'], df6['Number of Matches'], df7['Number of Matches'], df8['Number of Matches'], df9['Number of Matches'], df10['Number of Matches'], df11['Number of Matches'], df12['Number of Matches']]

plt.figure(figsize=(10, 7))

# Set 1
# boxplot = plt.boxplot(data_to_plot, labels=['f1-ORB', 'f1_SELM', 'f2_ORB', 'f2_SELM', 'f1_drk_ORB', 'f1_drk_SELM', 'f2_drk_ORB', 'f2_drk_SELM', 'f1_bly_ORB', 'f1_blry_SELM'])

# Set 2
boxplot = plt.boxplot(data_to_plot, labels=['ORB 200', 'SELM 200', 'ORB 500', 'SELM 500', 'ORB 750', 'SELM 750', 'ORB 900', 'SELM 900', 'ORB 1000', 'SELM 1000', 'ORB 1200', 'SELM 1200'])

plt.xticks(rotation=90, fontsize=7)


plt.title('Number of matches in the freiburg1_xyz_blurry sequence with varying numbers of features per frame.')
plt.xlabel('')
plt.ylabel('Number of Matches')

plt.savefig('orb_selm_freiburg1_xyz_blurry_varying_nFeaturesy.png')

plt.show()


