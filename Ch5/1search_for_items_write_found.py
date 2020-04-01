#!/usr/bin/env python3
import glob
import sys
import os
import csv
from xlrd import open_workbook, xldate_as_tuple
from datetime import datetime, date

item_numbers_file = sys.argv[1]
path_to_folder = sys.argv[2]
output_file = sys.argv[3]

item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='', encoding='UTF8') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])

filewriter = csv.writer(open(output_file, 'a', newline=''))

file_counter = 0
line_counter = 0
count_of_item_number = 0
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):
    file_counter += 1
    if input_file.split('.')[1] == 'csv':
        with open(input_file, 'r', newline='', encoding='UTF8') as csv_in_folder:
            filereader = csv.reader(csv_in_folder)
            header = next(filereader)
            for row in filereader:
                row_of_output = []
                for col in range(len(header)):
                    if col < 3:
                        cell_value = str(row[col]).strip()
                        row_of_output.append(cell_value)
                    elif col == 3:
                        cell_value = str(row[col]).strip('$').replace(',', '').split('.')[0].strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(row[col]).strip()
                        row_of_output.append(cell_value)
                    row_of_output.append(os.path.basename(input_file))
                if row[0] in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_number += 1
                line_counter += 1
    elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
        workbook = open_workbook(input_file)
        for worksheet in workbook.sheets():
            try:
                header = worksheet.row_values(0)
            except IndexError:
                pass
            for row in range(1, worksheet.nrows):
                row_of_output = []
                for col in range(len(header)):
                    if col < 3:
                        cell_value = str(worksheet.cell_value(row,col)).strip()
                        row_of_output.append(cell_value)
                    elif col == 3:
                        cell_value = str(worksheet.cell_value(row,col)).strip('$').replace(',', '').split('.')[0].strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(worksheet.cell_value(row,col)).strip()
                        row_of_output.append(cell_value)
                    row_of_output.append(os.path.basename(input_file))
                if worksheet.cell_value(row,0) in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_number += 1
                line_counter += 1
print('Number of files : {}'.format(file_counter))
print('Number of lines : {}'.format(line_counter))
print('Number of item numbers : {}'.format(count_of_item_number))
                        