#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import xldate_as_tuple, open_workbook
from xlwt import Workbook

# 특정 집합의 값을 포함하는 행의 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

important_p_date = ['01/24/2013', '01/31/2013']

p_date_index = 4

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []
    header = worksheet.row_values(0)
    data.append(header)
    for row_index in range(1,worksheet.nrows):
        row_list = []
        p_date = xldate_as_tuple(worksheet.cell_value(row_index, p_date_index), workbook.datemode)
        p_date = date(*p_date[0:3]).strftime('%m/%d/%Y')
        if p_date in important_p_date:
            for col_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index,col_index)
                cell_type = worksheet.cell_type(row_index,col_index)
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