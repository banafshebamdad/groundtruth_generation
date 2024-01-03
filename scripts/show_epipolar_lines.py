#
# Banafshe Bamdad
# Di Aug 22, 2023 09:09 CET
# This script shows epipolar line in two stereo images and print if two images are rectified or not
#
# !!! Achtung !!!
# This script does not work
#

import cv2
import numpy as np

def validate_rectification_and_draw_lines(left_img, right_img, camera_matrix_left, camera_matrix_right, distortion_coeff_left, distortion_coeff_right, fundamental_matrix):
    img_left = cv2.imread(left_img)
    img_right = cv2.imread(right_img)

    img_left_rectified = cv2.undistort(img_left, camera_matrix_left, distortion_coeff_left)
    img_right_rectified = cv2.undistort(img_right, camera_matrix_right, distortion_coeff_right)

    point = np.array([[100, 100, 1]])

    lines = cv2.computeCorrespondEpilines(point, 1, fundamental_matrix)
    lines = lines.reshape(-1, 3)

    img_right_with_lines = img_right_rectified.copy()
    for line in lines:
        a, b, c = line
        x0, y0 = map(int, [0, -c / b])
        x1, y1 = map(int, [img_right_rectified.shape[1], -(a * img_right_rectified.shape[1] + c) / b])
        cv2.line(img_right_with_lines, (x0, y0), (x1, y1), (0, 255, 0), 1)

    cv2.imshow("Left Rectified Image", img_left_rectified)
    cv2.imshow("Right Rectified Image with Epipolar Lines", img_right_with_lines)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


left_image_path = "/media/banafshe/Banafshe_2TB/ORB-SLAM3/11_Aug_2023_Zurich_HB_ZHAW_D435i/stereo_imu/shopville/barely_dynamic_ZurichHB_manually_2023_08_21/infra1/data/1691737904618810654.png"
right_image_path = "/media/banafshe/Banafshe_2TB/ORB-SLAM3/11_Aug_2023_Zurich_HB_ZHAW_D435i/stereo_imu/shopville/barely_dynamic_ZurichHB_manually_2023_08_21/infra2/data/1691737904618810654.png"

# Camera calibration data
fx_left = 447.336
fy_left = 447.181
cx_left = 420.387
cy_left = 236.184

fx_right = 446.653
fy_right = 447.376
cx_right = 413.696
cy_right = 234.913

k1_left = 0.051129
k2_left = -0.024424
p1_left = -0.003890
p2_left = -0.007353
k3_left = 0.0

k1_right = 0.054395
k2_right = -0.029805
p1_right = -0.005150
p2_right = -0.009516
k3_right = 0.0

camera_matrix_left = np.array([[fx_left, 0, cx_left], [0, fy_left, cy_left], [0, 0, 1]])
camera_matrix_right = np.array([[fx_right, 0, cx_right], [0, fy_right, cy_right], [0, 0, 1]])
distortion_coeff_left = np.array([k1_left, k2_left, p1_left, p2_left, k3_left])
distortion_coeff_right = np.array([k1_right, k2_right, p1_right, p2_right, k3_right])

points_left = np.array([[100, 100]])
points_right = np.array([[100, 100]])

fundamental_matrix, _ = cv2.findFundamentalMat(points_left, points_right)

validate_rectification_and_draw_lines(left_image_path, right_image_path, camera_matrix_left, camera_matrix_right, distortion_coeff_left, distortion_coeff_right, fundamental_matrix)








