#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

# 팬더스 모듈로 여러 파일 데이터 합치기

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frame = []

for file in all_files:
    data_frame = pd.read_csv(file, index_col=None)
    all_data_frame.append(data_frame)
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index = True)
data_frame_concat.to_csv(output_file)
print(data_frame_concat)