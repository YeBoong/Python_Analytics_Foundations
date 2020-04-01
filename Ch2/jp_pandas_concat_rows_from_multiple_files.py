#!/usr/bin/env python3
import sys
import pandas as pd
import glob
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

all_df = []

for input_file in glob.glob(os.path.join(input_path,'sales_*')):
    data_frame = pd.read_csv(input_file)
    all_df.append(data_frame)
data_frame_concat = pd.concat(all_df, axis=0, ignore_index = True)
print(data_frame_concat)