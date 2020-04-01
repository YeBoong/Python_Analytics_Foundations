#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 패턴을 활용한 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
data_frame_value_matches_pattern = data_frame[data_frame['Customer Name'].str.startswith('J')]

writer = pd.ExcelWriter(output_file)

data_frame_value_matches_pattern.to_excel(writer, sheet_name = 'jan_output_2013', index=False)
writer.save()