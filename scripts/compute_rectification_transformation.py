#
# Banafshe bamdad
# Mon Aug 28 15:09
# I used the calibration parameters values from /media/banafshe/Banafshe_2TB/calibration/Kalibr/2023_08_03_ZHAW_D435i_calibration/ZHAW_D435i_calibration-camchain.yaml
#
import numpy as np

# Intrinsic and extrinsic calibration data
cam0_intrinsics = [447.3360644325708, 447.18160879946294, 420.387475094417, 236.18473422455554]  # fx, fy, cx, cy
cam1_intrinsics = [446.6530568481328, 447.3769225414639, 413.69626161024894, 234.91340249001303]

# from T_cn_cnm1 matrix
cam1_to_cam0_rotation = np.array([[0.9998848142598853, 0.0006777775661598811, 0.015162415046345619],
                                  [-0.0007273394600374542, 0.9999944103942778, 0.003263457905727369],
                                  [-0.015160118395867164, -0.00327411022468585, 0.999879718272379]])

# World frame = left camera frame, so camera left does not have any rotation or translation w.r.t itself as the world frame
R1 = np.identity(3)
R2 = cam1_to_cam0_rotation

K0 = np.array([[cam0_intrinsics[0], 0, cam0_intrinsics[2]],
               [0, cam0_intrinsics[1], cam0_intrinsics[3]],
               [0, 0, 1]])

K1 = np.array([[cam1_intrinsics[0], 0, cam1_intrinsics[2]],
               [0, cam1_intrinsics[1], cam1_intrinsics[3]],
               [0, 0, 1]])


# projection matrices (P = K * [R|t])
P0 = K0 @ np.hstack((np.identity(3), np.zeros((3, 1))))
P1 = K1 @ np.hstack((cam1_to_cam0_rotation, np.array([[0.05014804746801571], [9.738617861848383e-05], [-0.0012453524960823114]])))

# Print the computed parameters
print("Rectification Transformation:")
print("R1:\n", R1)
print("R2:\n", R2)

print("\nNew Projection Matrices:")
print("P0:\n", P0)
print("P1:\n", P1)

