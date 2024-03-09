/**
* Banafshe Bamdad
* Sa Mar 9, 2024 22:33:43 CET
* 
* This script retrievs the intrinsic parameters of my RealSense D435i camera
* Compile: $ g++ -std=c++11 get_D435i_intrinsics.cpp -lrealsense2 -o get_D435i_intrinsics
* Usage: $ ./get_D435i_intrinsics
*
* fx: 425.7
* fy: 425.7
* cx: 428.042
* cy: 238.335
* k1: 0
* k2: 0
* p1: 0
* p2: 0
* k3: 0
*/
#include <iostream>
#include <librealsense2/rs.hpp> 

int main(int argc, char * argv[]) try {
    rs2::pipeline p;

    p.start();

    rs2::frameset frames = p.wait_for_frames();

    rs2::depth_frame depth = frames.get_depth_frame();

    rs2::sensor depth_sensor = p.get_active_profile().get_device().first<rs2::depth_sensor>();

    rs2_intrinsics intrinsics = depth.get_profile().as<rs2::video_stream_profile>().get_intrinsics();

    // Print intrinsics
    std::cout << "fx: " << intrinsics.fx << std::endl;
    std::cout << "fy: " << intrinsics.fy << std::endl;
    std::cout << "cx: " << intrinsics.ppx << std::endl;
    std::cout << "cy: " << intrinsics.ppy << std::endl;
    std::cout << "k1: " << intrinsics.coeffs[0] << std::endl;
    std::cout << "k2: " << intrinsics.coeffs[1] << std::endl;
    std::cout << "p1: " << intrinsics.coeffs[2] << std::endl;
    std::cout << "p2: " << intrinsics.coeffs[3] << std::endl;
    std::cout << "k3: " << intrinsics.coeffs[4] << std::endl;

    return EXIT_SUCCESS;
} catch (const rs2::error & e) {
    std::cerr << "RealSense error calling " << e.get_failed_function() << "(" << e.get_failed_args() << "):\n    " << e.what() << std::endl;
    return EXIT_FAILURE;
} catch (const std::exception & e) {
    std::cerr << e.what() << std::endl;
    return EXIT_FAILURE;
}

