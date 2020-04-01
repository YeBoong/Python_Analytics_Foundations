#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 열의 인덱스 값을 사용하여 특정 열 선택하기
# Customer Name과 Purchase Date

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

writer = pd.ExcelWriter(output_file)

data_frame_column_by_index.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()