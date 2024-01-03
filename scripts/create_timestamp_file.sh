#
# Banafshe Bamdad
# Di Sep 19, 08.19 CET
#
# This script lists the filenames without extensions in a specific directory and save them to a text file.
# Usage: create_timestamp_file.sh /path/to/the/frames/directory 
#!/bin/bash

directory="$1"
script_path=$PWD

echo 
output_file="create_timestamp_file_output.txt"

cd "$directory" || exit

for file in *; do
  if [ -f "$file" ]; then
    filename_without_extension="${file%.*}"
    echo $filename_without_extension 
    echo "$filename_without_extension" >> "$script_path/$output_file"
  fi
done

echo "File names without extensions have been saved to $script_path/$output_file"

