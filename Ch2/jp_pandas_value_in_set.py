#!/usr/bin/env python3
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

important_dates = ['1/20/14', '1/31/14']

data_frame = pd.read_csv(input_file)
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates)]
data_frame_value_in_set.to_csv(output_file)
print(data_frame_value_in_set)