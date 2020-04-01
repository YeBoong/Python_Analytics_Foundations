#!/usr/bin/env python3
import sys
import glob
import os

# 텍스트 파일 읽기 (과거 방식)
#input_file = sys.argv[1]
#print("Output #139 : ")
#filereader = open(input_file, 'r')
#for row in filereader:
#    print(row.strip())
#filereader.close()

# 텍스트 파일 읽기 (새로운 방식)
## with open(읽을 데이트 파일, 모드 선택, newline = '')
## newline 옵션 : 읽은 데이터 파일의 각 라인 뒤에 빈 라인이 추가되는 문제를 해결하기 위한 옵션
#input_file = sys.argv[1]
#print("Output #140 : ")
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print(row.strip())



# glob을 이용해 다수의 텍스트 파일 읽기
#print("Output #141 : ")
#input_path = sys.argv[1]
#for input_file in glob.glob(os.path.join(input_path, '*.txt')):
#    with open(input_file, 'r', newline = '') as filereader:
#        for row in filereader:
#            print(row.strip())


# 텍스트 파일 쓰기
# 파일 작성하기
# 하나의 텍스트 파일 작성하기
#my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#max_index = len(my_letters)
#output_file = sys.argv[1]
#filewriter = open(output_file, 'w')
#for index_value in range(len(my_letters)):
#    if index_value < (max_index -1):
#        filewriter.write(my_letters[index_value] + '\t')
#    else:
#        filewriter.write(my_letters[index_value] + '\n')
#filewriter.close()
#print("Output #142 : Output written to file")



# CSV 파일 쓰기
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = sys.argv[1]
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1) :
        filewriter.write(str(my_numbers[index_value])+',')
    else :
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output #143 : Output appended to file")