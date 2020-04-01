#!/usr/bin/env python3
import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline = '') as csv_in_file :
    with open(output_file, 'w', newline = '') as csv_out_file :
        # csv.reader() / csv.writer()의 delimiter 옵션
        # : 행 구분자. 기본값은 쉼표(,) 이므로 쉼표일 경우 굳이 쓰지 않아도 된다.
        filereader = csv.reader(csv_in_file, delimiter = ',')
        filewriter = csv.writer(csv_out_file, delimiter = ',')
        for row in filereader : 
            filewriter.writerow(row)
            print(row)