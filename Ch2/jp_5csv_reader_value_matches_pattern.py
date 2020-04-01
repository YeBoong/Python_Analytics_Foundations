#!/usr/bin/env python3
import sys
import re
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        
        header = next(filereader)
        filewriter.writerow(header)
        print(header)

        for row in filereader :
            invoice_num = row[1]
            if pattern.search(invoice_num):
                filewriter.writerow(row)
                print(row)