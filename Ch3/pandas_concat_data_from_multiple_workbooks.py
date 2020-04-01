#!/usr/bin/env python3
import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]

all_workbook = glob.glob(os.path.join(input_path, 'sales*.xls*'))
all_data_frame = []

for workbook in all_workbook:
    all_worksheet = pd.read_excel(workbook, sheet_name=None, index_col= None)
    for worksheet_name, data in all_worksheet.items():
        all_data_frame.append(data)
all_data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index = True)

writer = pd.ExcelWriter(output_file)
all_data_frame_concat.to_excel(writer, sheet_name = 'concat_data', index=False)
writer.save()