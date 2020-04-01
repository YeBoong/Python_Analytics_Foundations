#!/usr/bin/env python3
import csv
import sys

# 열의 인덱스 값을 사용하여 특정 열을 선택하는 방법

input_file = sys.argv[1]
output_file = sys.argv[2]

my_col = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)

        for row in filereader:
            row_list = []
            for index in my_col:
                row_list.append(row[index])
            filewriter.writerow(row_list)
            print(row_list)
