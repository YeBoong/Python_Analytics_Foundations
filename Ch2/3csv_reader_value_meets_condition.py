#!/usr/bin/env python3
import csv
import sys

# 특정 조건을 충족하는 행의 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)

        header = next(filereader)
        filewriter.writerow(header)
        print(header)

        for row in filereader:
            if row[0] == 'Supplier Z' or float(str(row[3]).strip('$').replace(',', '')) >= 600.00:
                filewriter.writerow(row)
                print(row)
