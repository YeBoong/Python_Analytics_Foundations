#!/usr/bin/env python3
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

important_cols = ['Invoice Number', 'Purchase Date']
my_col_index = []

with open(input_file, 'r', newline = '') as csv_in_file:
    with open(output_file, 'w', newline = '') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        
        for index_value in range(len(header)):
            if header[index_value] in important_cols:
                my_col_index.append(index_value)
        filewriter.writerow(important_cols)
        print(important_cols)
        for row_list in filereader:
            row_list_output = []
            for index_value in range(len(row_list)):
                if index_value in my_col_index:
                    row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)
            print(row_list_output)
                    