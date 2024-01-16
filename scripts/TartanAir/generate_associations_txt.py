#
# Banafshe Bamdad
# Di Jan 16, 2024
# The script generates lines with 6-digit numbers starting from 000000 and increments them up to the specified number of entries. 
# The output is written to the associations.txt file in the current working directory.
# I use this script to generate associations.txt file similar to TUM RGB-D.
# I use the file numbers as timestamps for this file.
# Usage:
# Specify the number of entries and the output file in num_entries and output_file, respectively.
# num_entries is the number of RGB and depth images 
#

def generate_associations_file(num_entries, output_file):
    with open(output_file, 'w') as file:
        for i in range(num_entries):
            num_str = f"{i:06d}"

            line = f"{num_str} rgb/{num_str}.png {num_str} depth/{num_str}.png\n"
            file.write(line)

if __name__ == "__main__":
    # Specify the number of entries and the output file
    num_entries = 403  
    output_file = "/media/banafshe/Banafshe_2TB/Datasets/TartanAir/my_test_sequences/hospital_hard/P037/associations.txt"

    generate_associations_file(num_entries, output_file)

