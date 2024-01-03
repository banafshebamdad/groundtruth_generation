#!/bin/bash

# 
# Banafshe Bamdad
# Di. Aug. 15, 2023 07:58 CET
#
# $1: bag_path: /path/to/bag/file
# $2: desired_ds_path: /desired/path/for/dataset
# $3: dataset_name: the extracted data will be saved in a directory with this name in desired_ds_path.
# $4: config_type: realsense_infra
# $5: bag_name: name of the bag file.bag
#
# usage: bash generate_dataset.sh /path/to/bag/file /desired/path/for/dataset dataset_name realsense_infra bag_name.bag

#
# Step 1. Extract infra stereo images
#

echo -e "#"
echo -e "# Step 1. Extract infra stereo images"
echo -e "#"
read -p "Press Enter to continue..."

echo -e "Please run the 'roscore' command in a separate terminal and press Enter here when done."
read -p "Press Enter to continue..."

scripts_dir="/media/banafshe/Banafshe_2TB/ground_truth/scripts" # !!! Achtung!!! Change this path if required
bag_path="$1"
desired_ds_path="$2"
dataset_name=$3
config_type=$4
bag_name=$5
cur_dir=$PWD

echo -e "Please run the following two commands in two separate terminal and follow the instraction. Press Enter here when done."
echo -e ""
echo -e "python3 $scripts_dir/convert_images_kevin_robb_infra_imu.py $dataset_name $config_type"
echo -e ""
echo -e "rosbag play $bag_path/$bag_name"
echo -e ""
read -p "Press Enter to continue..."

mv -v "$HOME/$dataset_name" "$desired_ds_path"
echo -e "Check if $HOME/$dataset_name is moved to $desired_ds_path correctly."
echo -e ""
read -p "Press Enter to continue..."

#
# Step 2. Extract IMU data
#

echo -e "#"
echo -e "# Step 2. Extract IMU data"
echo -e "#"
read -p "Press Enter to continue..."

echo -e "Please make sure that 'roscore' command is running in a separate terminal and press Enter here when done."
read -p "Press Enter to continue..."

echo -e "Please run the following two commands in two separate terminal and follow the instraction. Press Enter here when done."
echo -e ""
echo -e "cd $scripts_dir; python3 banafshe_extract_imu_data.py"
echo -e ""
echo -e "rosbag play $bag_path/$bag_name"
echo -e ""
read -p "Press Enter to continue..."

mkdir -p $desired_ds_path/$dataset_name/imu
mv $scripts_dir/imu_data.csv $desired_ds_path/$dataset_name/imu/data.csv
echo -e ""
echo -e "Check if $scripts_dir/imu_data.csv is moved to $desired_ds_path/$dataset_name/imu/data.csv correctly."
echo -e ""
read -p "Press Enter to continue..."


#
# Spep 3. Generating data.csv files for images
#

echo -e "#"
echo -e "# Spep 3. Generating data.csv files for images"
echo -e "#"

echo -e "Please run the following command in a separate terminal. Press Enter here when done."
echo -e ""
#echo -e "cd $scripts_dir; bash banafshe_create_data_from_frames_name.sh $desired_ds_path/$dataset_name/infra1/data"
cd $scripts_dir
./banafshe_create_data_from_frames_name.sh $desired_ds_path/$dataset_name/infra1/data
echo -e ""
read -p "Press Enter to continue..."
echo -e ""
mv "$scripts_dir/data.csv" "$desired_ds_path/$dataset_name/infra1"
echo -e "Check if $scripts_dir/data.csv is moved to $desired_ds_path/$dataset_name/infra1 correctly."
echo -e ""
read -p "Press Enter to continue..."
echo -e ""

echo -e "Please run the following command in a separate terminal. Press Enter here when done."
echo -e ""
# echo -e "cd $scripts_dir; bash banafshe_create_data_from_frames_name.sh $desired_ds_path/$dataset_name/infra2/data"
cd $scripts_dir
./banafshe_create_data_from_frames_name.sh $desired_ds_path/$dataset_name/infra2/data
echo -e ""
read -p "Press Enter to continue..."
echo -e ""
mv "$scripts_dir/data.csv" "$desired_ds_path/$dataset_name/infra2"
echo -e "Check if $scripts_dir/data.csv is moved to $desired_ds_path/$dataset_name/infra2 correctly."
echo -e ""
read -p "Press Enter to continue..."

#
# Step 4. Copy default sensors configuration files
#
cp $cur_dir/rectified_param.yaml $desired_ds_path/$dataset_name
cp $cur_dir/imu_sensor.yaml $desired_ds_path/$dataset_name/imu/sensor.yaml
cp $cur_dir/infra1_sensor.yaml $desired_ds_path/$dataset_name/infra1/sensor.yaml
cp $cur_dir/infra2_sensor.yaml $desired_ds_path/$dataset_name/infra2/sensor.yaml

echo -e "Check if the following files are copied correctly."
echo -e ""
ls $desired_ds_path/$dataset_name/rectified_param.yaml
ls $desired_ds_path/$dataset_name/imu/sensor.yaml
ls $desired_ds_path/$dataset_name/infra1/sensor.yaml
ls $desired_ds_path/$dataset_name/infra2/sensor.yaml
echo ""
echo -e "Boro knosh bash!"
echo -e ""
