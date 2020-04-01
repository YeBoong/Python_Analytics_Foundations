#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline = '') as filereader:
    with open(output_file, 'w', newline = '') as filewriter :
        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        print(header_list)
        
        # 구분자.join(map(변환하고자 하는 데이터 타입, 적용할 리스트))
        # : 리스트의 모든 요소들을 변환하고자 하는 데이터 타입으로 변환시켜 요소 사이마다 구분자를 넣어 하나로 연결.
        filewriter.write(','.join(map(str, header_list))+'\n')
        
        for row in filereader :
            row = row.strip()
            row_list = row.split()
            print(row_list)
            filewriter.write(','.join(map(str, row_list))+'\n')
        