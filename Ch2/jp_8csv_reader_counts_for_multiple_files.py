#!/usr/bin/env python3
import sys
import glob
import csv
import os

input_path = sys.argv[1]

file_counter = 0

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    file_counter += 1
    with open(input_file, 'r', newline = '') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        row_count = 1
        col_count = len(header)
        for row in filereader:
            row_count += 1
        print("{0!s} : \t{1:d} rows \t{2:d} columns \n".format(os.path.basename(input_file), row_count, col_count))

print("file_count : {}".format(file_counter))
            