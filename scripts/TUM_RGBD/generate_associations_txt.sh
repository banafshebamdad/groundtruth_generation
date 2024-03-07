#
# Banafshe Bamdad
# Do Mar. 07, 2024
# This script gets a path to a dataset sequneces in the TUM RGB-D format and generates an associations.txt file. 
# It is compatible with the TUM RGB-D, Bonn, and ICL-NUIm datasets
# 
# !!! ACHTUNG ACHTUNG !!!
#	!!! bofore running this script, check the path to the associate.py script.(the value of path_associate_py) !!!
# 	!!! Activate an appropriate ptthon virtual environment 
# !!!
#
# Usage: bash generate_associations_txt.sh /patjh/to/dataset/sequences
# e.g. 
#	$ source /home/banafshe/global_env/bin/activate
# 	$ bash generate_associations_txt.sh /media/banafshe/Banafshe_2TB/Datasets/Bonn/rgbd_bonn_dataset
#
#!/bin/bash

PARENT_DIR=$1

# Change it! path to the associate.py script
path_associate_py="/media/banafshe/Banafshe_2TB/Datasets/TUM"

cd $path_associate_py

for dir in "$PARENT_DIR"/*; do
  if [ -d "$dir" ]; then 
    echo "Running command on $dir"
    COMMAND="python associate.py $dir/rgb.txt $dir/depth.txt > $dir/associations.txt"
    bash -c "$COMMAND"
  fi
done

