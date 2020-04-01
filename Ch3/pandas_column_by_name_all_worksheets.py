#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 모든 워크시트에서 특정 열 선택하기
# customer name, sale amount 
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name = None, index_col = None)

output_list = []

for worksheet_name, data in data_frame.items():
    output_list.append(data.loc[:, ['Customer Name', 'Sale Amount']])

filtered = pd.concat(output_list, axis=0, ignore_index = True)

writer = pd.ExcelWriter(output_file)
filtered.to_excel(writer, sheet_name='important_col', index=False)
writer.save()