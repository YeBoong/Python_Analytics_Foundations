#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import xldate_as_tuple, open_workbook
from xlwt import Workbook

# 열 헤더를 사용하여 특정 열 선택하기
# Customer ID, Purchase Date

input_file = sys.argv[1]
output_file = sys.argv[2]

important_col_name = ['Customer ID', 'Purchase Date']

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_output_2013')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = important_col_name
    data.append(header)
    for row_index in range(1,worksheet.nrows):
        row_list = []
        for col_index in range(worksheet.ncols):
            if worksheet.cell_value(0, col_index) in important_col_name:
                cell_value = worksheet.cell_value(row_index,col_index)
                cell_type = worksheet.cell_type(row_index, col_index)
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)
        if row_list:
            data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
