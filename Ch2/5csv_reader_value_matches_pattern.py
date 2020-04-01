#!/usr/bin/env python3
import csv
import sys
import re

# 패턴/정규 표현식을 활용한 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_group>^001_*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)

        header = next(filereader)
        filewriter.writerow(header)
        print(header)

        for row in filereader:
            if pattern.search(row[1]):
                filewriter.writerow(row)
                print(row)