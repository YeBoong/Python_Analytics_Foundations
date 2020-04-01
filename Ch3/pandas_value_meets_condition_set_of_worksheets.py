#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 워크시트 집합에 걸쳐서 특정 행 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

my_sheets = [0, 1]
output_list = []

data_frame = pd.read_excel(input_file, sheet_name = my_sheets, index_col=None)

for worksheet_name, data in data_frame.items():
    output_list.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 1900])

filtered_value = pd.concat(output_list, axis=0, ignore_index = True)

writer = pd.ExcelWriter(output_file)
filtered_value.to_excel(writer, sheet_name = 'Output', index = False)
writer.save()