#!/usr/bin/env python3
import sys
from xlrd import open_workbook

# 엑셀 통합 문서 내부 살펴보기
# 워크북의 워크시트 수, 이름, 시트 별 행 수, 열 수
input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of sheets : ', workbook.nsheets)
for worksheet in workbook.sheets():
    print("worksheet name:",worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)
