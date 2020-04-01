#!/usr/bin/env python3
import pandas as pd
import sys

# 팬더스 모듈로 연속된 행 선택하기

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header= None)  # header = None으로 자동으로 0행을 헤더로 지정하는 것을 막음.

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0] # 헤더 지정
data_frame = data_frame.reindex(data_frame.index.drop(3)) # 3행은 헤더이므로 헤더 다음 행부터 인덱스를 다시 계산.
data_frame.to_csv(output_file, index=False)
print(data_frame)
