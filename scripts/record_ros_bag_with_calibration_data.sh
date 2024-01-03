#!/bin/bash

#
# Banafshe bamdad
# Di Aug 22, 2023 10:59
#
#

LEFT_CAMERA_K="[447.3360644325708, 0.0, 420.387475094417, 0.0, 447.18160879946294, 236.18473422455554, 0.0, 0.0, 1.0]"
LEFT_CAMERA_D="[0.0511292236271853, -0.02442462059567389, -0.0038908118701216103, -0.007353566077430776]"

RIGHT_CAMERA_K="[446.6530568481328, 0.0, 413.69626161024894, 0.0, 447.3769225414639, 234.91340249001303, 0.0, 0.0, 1.0]"
RIGHT_CAMERA_D="[0.054395481001679465, -0.029805301218825016, -0.005150987710169745, -0.00951600574540279]"

rosparam set /camera/infra1/distortion_model "pinhole"
rosparam set /camera/infra1/D "${LEFT_CAMERA_D}"
rosparam set /camera/infra1/K "${LEFT_CAMERA_K}"
rosparam set /camera/infra1/R "[0.99988481, 0.00067778, 0.01516242, -0.00072734, 0.99999441, 0.00326346, -0.01516012, -0.00327411, 0.99987972]"
rosparam set /camera/infra1/P "[447.3360644325708, 0, 420.387475094417, -0.05014805, 0, 447.18160879946294, 236.18473422455554, -0.00009739, 0, 0, 1, 0]"


rosparam set /camera/infra2/distortion_model "pinhole"
rosparam set /camera/infra2/D "${RIGHT_CAMERA_D}"
rosparam set /camera/infra2/K "${RIGHT_CAMERA_K}"
rosparam set /camera/infra2/R "[0.99988481, 0.00067778, 0.01516242, -0.00072734, 0.99999441, 0.00326346, -0.01516012, -0.00327411, 0.99987972]"
rosparam set /camera/infra2/P "[446.6530568481328, 0, 413.69626161024894, -0.05014805, 0, 447.3769225414639, 234.91340249001303, -0.00009739, 0, 0, 1, 0]"

rosbag record -O my_bag  /camera/accel/imu_info /camera/color/camera_info /camera/color/image_raw /camera/depth/camera_info /camera/depth/image_rect_raw /camera/gyro/imu_info /camera/imu /camera/infra1/camera_info /camera/infra1/image_rect_raw /camera/infra2/camera_info /camera/infra2/image_rect_raw


# LEFT_CAMERA_K="[focal_length_x, 0.0, principal_point_x, 0.0, focal_length_y, principal_point_y, 0.0, 0.0, 1.0]"
# LEFT_CAMERA_D="[distortion_coefficients]" = "[k1, k2, p1, p2, k3]"
# Extract /camera/infra1/R and /camera/infra2/R from Baseline (cam0 to cam1) in kalibr file = "[R11, R12, R13, R21, R22, R23, R31, R32, R33]"
# [[ R11  R12  R13  Tx ]
# [ R21  R22  R23  Ty ]
# [ R31  R32  R33  Tz ]
# [  0    0    0   1  ]]
# R matrix should be like the below:
# [[ R11  R12  R13 ]
# [ R21  R22  R23 ]
# [ R31  R32  R33 ]]

# /camera/infra1/P, same Tx and Ty values from Baseline (cam0 to cam1) for both cameras. = "[fx, 0, cx, Tx, 0, fy, cy, Ty, 0, 0, 1, 0]"
# [[ fx'  0  cx'  Tx ]
# [  0  fy' cy'  Ty ]
# [  0   0   1   0  ]]


