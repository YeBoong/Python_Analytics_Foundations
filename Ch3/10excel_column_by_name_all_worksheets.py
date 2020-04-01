#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

# 모든 워크시트에서 특정 열 선택하기
# customer name, sale amount 열만 선택

input_file = sys.argv[1]
output_file = sys.argv[2]

important_header = ['Customer Name', 'Sale Amount']
header_index_list = []
first_worksheet = True

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('important_col')

with open_workbook(input_file) as workbook:
    data = []
    for worksheet in workbook.sheets():
        if first_worksheet:
            data.append(important_header)
            header = worksheet.row_values(0)
            for col_index in range(len(header)):
                if header[col_index] in important_header:
                    header_index_list.append(col_index)
            first_worksheet = False
        for row_index in range(1,worksheet.nrows):
            row_list = []
            for col_index in header_index_list:
                row_list.append(worksheet.cell_value(row_index, col_index))
            if row_list:
                data.append(row_list)
    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
