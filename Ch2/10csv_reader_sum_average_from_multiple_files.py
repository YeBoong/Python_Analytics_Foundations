#!/usr/bin/env python3
import csv
import sys
import glob
import os

# 파일에서 데이터 값의 합계 및 평균 계산하기

input_path = sys.argv[1]
output_file = sys.argv[2]

csv_out_file = open(output_file, 'w', newline='')
filewriter = csv.writer(csv_out_file)

output_header = ['file name', 'total sales', 'average sales']
filewriter.writerow(output_header)
print(output_header)

for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        total_sales = 0.0
        number_of_sales = 0.0
        
        row_list = []
        for row in filereader:
            total_sales += float(str(row[3]).strip('$').replace(',', ''))
            number_of_sales += 1.0
        average = float(total_sales/number_of_sales)
        row_list.append(os.path.basename(input_file))
        row_list.append(total_sales)
        row_list.append('{0:.2f}'.format(average))
    filewriter.writerow(row_list)
    print(row_list)
csv_in_file.close()



