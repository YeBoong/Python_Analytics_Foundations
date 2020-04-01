#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 모든 워크시트에서 특정 행 필터링하기
# Sale Amount >= 2000.00

input_file = sys.argv[1]
output_file = sys.argv[2]

output_list = []

data_frame = pd.read_excel(input_file, sheet_name=None, index_col = None)

for worksheet_name, data in data_frame.items():
    output_list.append(data[data['Sale Amount'].replace('$', '').replace(',', '').astype(float) > 2000.00])

filtered_rows = pd.concat(output_list, axis=0, ignore_index = True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name = 'sale_amount_gt2000', index=False)
writer.save()