#!/usr/bin/env python3
import pandas as pd
import sys
import glob
import os

#팬더스 모듈로 통합 문서 및 워크시트별 합계 및 평균 계산하기

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbooks = glob.glob(os.path.join(input_path, 'sales_*.xls*'))
data_frames = []
for workbook in all_workbooks:
    all_workbooks = pd.read_excel(workbook, sheet_name=None, index_col=None)
    workbook_total_sales = []
    workbook_number_of_sales = []
    worksheet_data_frames = []
    worksheets_data_frame = None
    workbook_data_frame = None
    for worksheet_name, data in all_workbooks.items():
        total_sales = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data.loc[:, 'Sale Amount']]).sum()
        number_of_sales = len(data.loc[:, 'Sale Amount'])
        average_sales = pd.DataFrame(total_sales/number_of_sales)