#!/usr/bin/env python3
import glob
import os
import sys
from xlrd import open_workbook

# 통합 문서의 개수 및 각 통합 문서의 행과 열 개수 세기
input_dir = sys.argv[1]

workbook_counter = 0

for input_file in glob.glob(os.path.join(input_dir,'sales*.xls*')):
    workbook_counter += 1
    print("workbook : " + os.path.basename(input_file))
    with open_workbook(input_file) as workbook:
        print("Number of worksheets : ", workbook.nsheets)
        for worksheet in workbook.sheets():
            print("worksheet name : {0:s} \tRows : {1:d}\t \tColumns : {2:d}".format(worksheet.name, worksheet.nrows, worksheet.ncols))

print("Number of Excel workbooks : ", workbook_counter)