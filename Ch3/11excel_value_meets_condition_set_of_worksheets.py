#!/usr/bin/env python3
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
# 워크시트 집합에 걸쳐서 특정 행 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

my_sheets = [0, 1]
sale_amount_index = 3

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('Output')

fir_worksheet = True

with open_workbook(input_file) as workbook:
    data = []
    for sheet_index in range(workbook.nsheets):
        if sheet_index in my_sheets:
            worksheet = workbook.sheet_by_index(sheet_index)
            if fir_worksheet:
                header = worksheet.row_values(0)
                data.append(header)
                fir_worksheet = False
            for row_index in range(1,worksheet.nrows):
                row_list = []
                for col_index in range(worksheet.ncols):
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