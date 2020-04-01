#!/usr/bin/env python3
import glob
import sys
import os
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
#통합 문서 및 워크시트별 합계 및 평균 계산하기

input_path = sys.argv[1]
output_file = sys.argv[2]

all_data = []
header = ['workbook', 'worksheet', 'worksheet_total', 'worksheet_average', 'workbook_total', 'workbook_average']
all_data.append(header)
sale_index = 3

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('workbooks_sum_average')

for input_file in glob.glob(os.path.join(input_path, 'sales*_xls*')):
    with open_workbook(input_file) as workbook:
        list_of_total = []
        list_of_number = []
        workbook_output = []
        for worksheet in workbook.sheets():
            total_sales = 0
            number_of_sales = 0
            worksheet_list = []
            worksheet_list.append(os.path.basename())
            worksheet_list.append(worksheet.name)
            for row_index in range(1, worksheet.nrows):
                try:
                    total_sales += float(str(worksheet.cell_value(row_index,sale_index)).strip('$').replace(',', ''))
                    number_of_sales += 1
                except:
                    total_sales += 0.
                    number_of_sales += 0.
            average_sales = '%.2f' % float(total_sales/number_of_sales)
            worksheet_list.append(total_sales)
            worksheet_list.append(float(average_sales))
            list_of_total.append(total_sales)
            list_of_number.append(float(number_of_sales))
            workbook_output.append(worksheet_list)
        workbook_total = sum(list_of_total)
        workbook_average = sum(list_of_total) / sum(list_of_number)

        for list_element in workbook_output:
            list_element.append(workbook_total)
            list_element.append(workbook_average)
        all_data.extend(workbook_output)

for list_index, output_list in enumerate(all_data):
    for element_index, element in enumerate(output_list):
        output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)