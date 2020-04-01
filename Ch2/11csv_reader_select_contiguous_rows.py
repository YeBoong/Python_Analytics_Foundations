#!/usr/bin/env python3
import csv
import sys

# 연속된 행 선택하기

input_file = sys.argv[1]
output_file = sys.argv[2]

row_count = 0

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row in filereader:
            if row_count >=3 and row_count <= 15:
                filewriter.writerow([value.strip() for value in row])
                print([value.strip() for value in row])
            row_count += 1