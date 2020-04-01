#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

# CSV 모듈을 사용하여 CSV 파일 읽기

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        for row in filereader:
            filewriter.writerow(row)
            print(row)