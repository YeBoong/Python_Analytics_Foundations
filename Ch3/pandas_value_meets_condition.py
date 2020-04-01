#!/usr/bin/env python3
import sys
import pandas as pd

# 팬더스 모듈로 특정 조건을 충족하는 행 필터링
input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)

data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype(float) > 1400.0]

data_frame_value_meets_condition.to_excel(writer, sheet_name='jan_2013_output', index=False)
writer.save()