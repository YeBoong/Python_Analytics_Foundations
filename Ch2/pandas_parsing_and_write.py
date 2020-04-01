#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈을 이용하여 CSV 파일 처리

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame.to_csv(output_file, index=False)
print(data_frame)
