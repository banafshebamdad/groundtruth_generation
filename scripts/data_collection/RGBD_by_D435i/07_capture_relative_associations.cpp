/**
 * Banafshe Bamdad
 * Fr Mar 8 16:42:09 ECT
 *
 * RealSense Frame Capture with Associations
 * 
 * This script captures RGB and depth frames from an Intel RealSense camera and saves them
 * to specified directories. It requires a destination folder as a command-line argument,
 * within which 'rgb' and 'depth' subdirectories are created.
 * Image files are named after their capture timestamp.
 * 
 * An 'associations.txt' file is also generated in the destination folder, listing timestamps
 * and relative paths of corresponding RGB and depth images in a space-separated format. 
 * 
 * Usage:
 *     <executable> <destination folder path>
 * 
 * The script captures frames continuously until interrupted by Ctrl+C. Depth values are scaled
 * by a factor of 5000, where a pixel value of 5000 represents 1 meter from the camera.
 * A pixel value of 0 indicates no data.
 * 
 * Requirements:
 * - Intel RealSense SDK 2.0
 * - OpenCV library
 * - C++17 compiler support for filesystem operations
 *
 * Related Links
 * https://dev.intelrealsense.com/docs/projection-in-intel-realsense-sdk-20
 * https://cvg.cit.tum.de/data/datasets/rgbd-dataset/file_formats
 */


#include <librealsense2/rs.hpp> 
#include <opencv2/opencv.hpp>   
#include <iostream>
#include <signal.h>
#include <chrono>
#include <fstream>              
#include <filesystem>           // C++17 Standard header for filesystem operations

volatile sig_atomic_t stop;

void signal_handler(int signal) {
    stop = 1;
}

void create_directory(const std::string& path) {
    std::filesystem::create_directories(path);
}

int main(int argc, char * argv[]) try
{
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <destination folder path>" << std::endl;
        return EXIT_FAILURE;
    }

    signal(SIGINT, signal_handler);

    std::string dest_folder = argv[1];
    create_directory(dest_folder); 

    std::string rgb_dir = dest_folder + "/rgb";
    std::string depth_dir = dest_folder + "/depth";
    create_directory(rgb_dir);
    create_directory(depth_dir);

    std::ofstream assoc_file(dest_folder + "/associations.txt");

    rs2::pipeline p;

    rs2::config cfg;
    cfg.enable_stream(RS2_STREAM_COLOR, 640, 480, RS2_FORMAT_BGR8, 30);
    cfg.enable_stream(RS2_STREAM_DEPTH, 640, 480, RS2_FORMAT_Z16, 30);
    p.start(cfg);

    while (!stop && assoc_file) {
        auto frames = p.wait_for_frames(); // Wait for the next set of frames from the camera

        // Get each frame
        auto color_frame = frames.get_color_frame();
        auto depth_frame = frames.get_depth_frame();

        // Convert frames to OpenCV matrices
        auto color_mat = cv::Mat(cv::Size(640, 480), CV_8UC3, (void*)color_frame.get_data(), cv::Mat::AUTO_STEP);
        cv::Mat depth_mat(cv::Size(640, 480), CV_16UC1, (void*)depth_frame.get_data(), cv::Mat::AUTO_STEP);

        depth_mat.convertTo(depth_mat, CV_16U, 5.0);

        // Generate timestamp in seconds (as a floating point number)
        auto now = std::chrono::system_clock::now();
        auto now_ms = std::chrono::time_point_cast<std::chrono::milliseconds>(now);
        auto epoch = now_ms.time_since_epoch();
        auto value = std::chrono::duration_cast<std::chrono::milliseconds>(epoch);
        double timestamp = value.count() / 1000.0;

        std::string color_filename = std::to_string(timestamp) + ".png";
        std::string depth_filename = std::to_string(timestamp) + ".png";

        cv::imwrite(rgb_dir + "/" + color_filename, color_mat);
        cv::imwrite(depth_dir + "/" + depth_filename, depth_mat);

        assoc_file << std::fixed << std::setprecision(5) << timestamp << " rgb/" << timestamp << ".png " << timestamp << " depth/" << timestamp << ".png" << std::endl;

        std::cout << "Saved " << color_filename << " and " << depth_filename << " with associations." << std::endl;
    }

    assoc_file.close();

    return EXIT_SUCCESS;
}
catch (const rs2::error & e)
{
    std::cerr << "RealSense error calling " << e.get_failed_function() << "(" << e.get_failed_args() << "):\n    " << e.what() << std::endl;
    return EXIT_FAILURE;
}
catch (const std::exception& e)
{
    std::cerr << e.what() << std::endl;
    return EXIT_FAILURE;
}

