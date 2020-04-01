#!/usr/bin/env python3
import csv
import sys

# 헤더 추가하기

input_file = sys.argv[1]
output_file = sys.argv[2]

header_list = ['Supplier Name','Invoice Number','Part Number','Cost','Purchase Date']

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)

        filewriter.writerow(header_list)
        print(header_list)
        for row in filereader:
            filewriter.writerow(row)
            print(row)