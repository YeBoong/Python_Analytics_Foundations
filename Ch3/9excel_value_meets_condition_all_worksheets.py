#!/usr/bin/env python3
import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# 모든 워크시트에서 특정 행 필터링 하기
# Sale Amount >= 2000.00

input_file = sys.argv[1]
output_file = sys.argv[2]

sale_amount_index = 3

first_worksheet = True

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sale_amount_gt2000')

with open_workbook(input_file) as workbook:
    data = []
    for worksheet in workbook.sheets():
        if first_worksheet:
            header = worksheet.row_values(0)
            data.append(header)
            first_worksheet = False
        for row_index in range(1, worksheet.nrows):
            row_list = []
            sale_amount = worksheet.cell_value(row_index, sale_amount_index)
            if sale_amount >= 2000.00:
                for col_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, col_index)
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