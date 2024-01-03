# !!! ACHTUNG !!! The first line should not be empty
#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

if [ ! -f "$filename" ]; then
    echo "Error: File not found!"
    exit 1
fi

# Initialize max and min to the first value in the file
read first_line < "$filename"
first_value=$(echo "$first_line" | awk -F'#matches: ' '{print $2}')
max=$first_value
min=$first_value

echo $first_value
echo $max
echo $min

# Calculate mean, max, and min
awk -F'#matches: ' -v max="$max" -v min="$min" '
{
    sum += $2
    count++
    if ($2 > max) max = $2
    if ($2 < min) min = $2
}
END {
    printf "Mean: %.2f\n", sum / count
    printf "Max: %d\n", max
    printf "Min: %d\n", min
}
' "$filename"

