#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 특정 집합의 값을 포함하는 행의 필터링
# Purchase Date 값이 01/24/2013 혹은 01/31/2013 인 행만 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

important_p_date = ['01/24/2013', '01/31/2013']

data_frame = pd.read_excel(input_file, sheet_name='january_2013')
data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_p_date)]

writer = pd.ExcelWriter(output_file)

data_frame_value_in_set.to_excel(writer, sheet_name = 'jan_2013_output', index = False)
writer.save()