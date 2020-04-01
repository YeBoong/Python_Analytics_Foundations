#!/usr/bin/env python3
import pandas as pd
import sys
import glob
import os

# 팬더스 모듈로 파일에서 데이터 값의 합계 및 평균 계산하기

input_path = sys.argv[1]
output_file = sys.argv[2]

all_files = glob.glob(os.path.join(input_path,'sales_*'))
all_data_frame = []

header_list = ['file name', 'total sales', 'average sales']

for input_file in all_files:
    data_frame = pd.read_csv(input_file)
    total_sale = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
    average_sale = pd.DataFrame([float(str(value).strip('$').replace(',', '')) for value in data_frame.loc[:, 'Sale Amount']]).mean()
    average_sale_convert = '{0:.2f}'.format(float(average_sale))
    data = {'file name' : os.path.basename(input_file),
            'total sales' : total_sale,
            'average sales' : average_sale_convert}
    
    all_data_frame.append(pd.DataFrame(data, columns = header_list))
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index = True)
data_frame_concat.to_csv(output_file, index = False)
print(data_frame_concat)