#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 특정 집합의 값을 포함하는 행의 필터링

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates=['1/20/14', '1/30/14']

data_frame = pd.read_csv(input_file)
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]

data_frame_value_in_set.to_csv(output_file, index=False)
print(data_frame_value_in_set)