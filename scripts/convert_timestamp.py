#
# Banafshe bamdad
#
# Do. Jul 20 12:29 CET
#
# convert timestamp in this format "1.6870719052899407e+18" to this format "1687071905221604109".

def scientific_to_integer(timestamp_scientific):
    try:
        # Convert the scientific notation string to a float
        timestamp_float = float(timestamp_scientific)

        # Convert the float to an integer after removing the decimal point
        timestamp_integer = int(timestamp_float)

        return timestamp_integer
    except ValueError:
        # Return None if the conversion fails
        return None


def convert_timestamp_file(input_file, output_file):
    with open(input_file, 'r') as f_in:
        lines = f_in.readlines()

    converted_lines = []
    for line in lines:
        columns = line.split()
        if len(columns) > 0:
            timestamp_scientific = columns[0]
            converted_timestamp = scientific_to_integer(timestamp_scientific)

            if converted_timestamp is not None:
                # Replace the first column with the converted timestamp
                columns[0] = str(converted_timestamp)
                converted_line = ' '.join(columns)
                converted_lines.append(converted_line)

    with open(output_file, 'w') as f_out:
        f_out.write('\n'.join(converted_lines))


# Example usage:
input_file = "/home/banafshe/Desktop/demonstration/trial2/rpg_on_kimera/stamped_groundtruth.txt"
output_file = "/home/banafshe/Desktop/demonstration/trial2/rpg_on_kimera/new_ts.txt"
convert_timestamp_file(input_file, output_file)

