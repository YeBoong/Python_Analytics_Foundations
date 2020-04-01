#!/usr/bin/env python3
import csv
import glob
import os
import sys

# 여러 파일의 데이터 합치기

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                    print(row)
                    first_file = False
            else:
                header = next(filereader)
                for row in filereader:
                    filewriter.writerow(row)
                    print(row)
            