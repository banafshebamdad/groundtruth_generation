#
# Banafshe Bamdad
# First modification at Di Jul 18, 2023 09:48:59 CET
# Usage: python3 visualize_trajectory.py -g /path/to/ground-truth.txt -e /path/to/estimated.txt
#

import argparse
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_trajectory_from_file(filename, title):
    # Read the trajectory data from the file
    Tx = []
    Ty = []
    Tz = []
    Rx = []
    Ry = []
    Rz = []

    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            data = line.split()
            ts = float(data[0])
            tx = float(data[1])
            ty = float(data[2])
            tz = float(data[3])
            rx = float(data[4])
            ry = float(data[5])
            rz = float(data[6])
            rw = float(data[7])
            
            line = file.readline()
            
            Tx.append(tx)
            Ty.append(ty)
            Tz.append(tz)
            Rx.append(rx)
            Ry.append(ry)
            Rz.append(rz)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the trajectory
    ax.plot(Tx, Ty, Tz, '-b', label='Trajectory')
    ax.scatter(Tx[0], Ty[0], Tz[0], c='g', marker='o', label='Start')
    ax.scatter(Tx[-1], Ty[-1], Tz[-1], c='r', marker='o', label='End')
    
    print("\n::: {} :::\nstart: \t{}\nend: \t{}".format(title, (Tx[0], Ty[0], Tz[0]), (Tx[-1], Ty[-1], Tz[-1])))

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--groundtruth', help='Path to txt file containing poses in correct scale.')
    parser.add_argument('-e', '--estimated', help='Path to the file containing estimated poses.')

    args = parser.parse_args()
    gt = args.groundtruth
    est = args.estimated
    
    if not (gt and est):
        print('\nPlease provide both ground-truth and estimated files as command-line arguments.\n')
        print('Usage: ')
        print('\t$ python3 visualize_trajectory.py -g /path/to/ground-truth.txt -e /path/to/estimated.txt')
        print('e.g.')
        print('\t$ python3 visualize_trajectory.py -g /media/banafshe/Banafshe_2TB/ground_truth/colmap_workspace/my_evaluation/352-438/stamped_groundtruth.txt -e /media/banafshe/Banafshe_2TB/ground_truth/colmap_workspace/my_evaluation/352-438/stamped_traj_estimate.txt\n')
        
        sys.exit(1)
    
    # Example usage
    visualize_trajectory_from_file(gt, "ground-truth")
    visualize_trajectory_from_file(est, "estimated")

