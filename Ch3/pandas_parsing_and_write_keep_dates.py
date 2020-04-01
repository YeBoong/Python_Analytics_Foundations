#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 날짜형식 할당

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

writer = pd.ExcelWriter(output_file)

data_frame.to_excel(writer, sheet_name='jan_2013_output', index=False)