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

read first_line < "$filename"
max=$(echo "$first_line" | awk -F'#matches: ' '{print $2}')

awk -F'#matches: ' -v max="$max" '
{
    value = $2
    sum += value
    count++
    if (value > max) max = value
}
END {
    printf "Mean: %.2f\n", sum / count
    printf "Max: %d\n", max
}
' "$filename"

